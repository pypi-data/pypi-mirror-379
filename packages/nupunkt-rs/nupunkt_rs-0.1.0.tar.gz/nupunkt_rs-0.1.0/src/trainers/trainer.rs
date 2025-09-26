use crate::core::{
    ScoringConfig, ORTHO_BEG_LC, ORTHO_BEG_UC, ORTHO_MID_LC, ORTHO_MID_UC, ORTHO_UNK_LC,
    ORTHO_UNK_UC,
};
use crate::parameters::PunktParameters;
use crate::statistics::{
    calculate_abbreviation_score, AbbreviationScorer, CollocationScorer, SentenceStarterScorer,
};
use crate::tokens::PunktToken;
use crate::utils::{pair_iter, FreqDist, TextPreprocessor};
/// Punkt trainer for learning sentence boundary detection parameters
use anyhow::{Context, Result};
use pyo3::prelude::*;
use std::sync::Arc;

/// Punkt trainer for learning from text
pub struct PunktTrainer {
    /// Scoring configuration
    config: ScoringConfig,

    /// Parameters being trained
    params: PunktParameters,

    /// Type frequency distribution
    type_fdist: FreqDist<String>,

    /// Collocation frequency distribution
    collocation_fdist: FreqDist<(String, String)>,

    /// Sentence starter frequency distribution
    sent_starter_fdist: FreqDist<String>,

    /// Number of tokens with periods
    num_period_toks: usize,

    /// Number of sentence breaks
    sentbreak_count: usize,

    /// Text preprocessor
    preprocessor: TextPreprocessor,

    /// Common abbreviations to preserve
    common_abbrevs: Vec<String>,
}

impl PunktTrainer {
    /// Create a new trainer
    pub fn new() -> Self {
        Self::with_config(ScoringConfig::default())
    }

    /// Create a trainer with custom configuration
    pub fn with_config(config: ScoringConfig) -> Self {
        Self {
            config,
            params: PunktParameters::new(),
            type_fdist: FreqDist::new(),
            collocation_fdist: FreqDist::new(),
            sent_starter_fdist: FreqDist::new(),
            num_period_toks: 0,
            sentbreak_count: 0,
            preprocessor: TextPreprocessor::default(),
            common_abbrevs: vec!["...".to_string()], // Include ellipsis
        }
    }

    /// Load abbreviations from a JSON file
    pub fn load_abbreviations_from_json(&mut self, path: &str) -> Result<usize> {
        let contents = std::fs::read_to_string(path)
            .with_context(|| format!("Failed to read file: {}", path))?;
        let abbreviations: Vec<String> =
            serde_json::from_str(&contents).context("Failed to parse JSON")?;

        let count = abbreviations.len();
        let source = path.to_string();

        for abbrev in abbreviations {
            // Use add_provided_abbreviation to mark these as ground truth
            self.params
                .add_provided_abbreviation(abbrev, source.clone());
        }

        Ok(count)
    }

    /// Add abbreviations directly (marked as provided)
    pub fn add_abbreviations(&mut self, abbreviations: Vec<String>) {
        for abbrev in abbreviations {
            // Mark these as provided from "direct" source
            self.params.add_provided_abbreviation(abbrev, "direct");
        }
    }

    /// Train on text and return the learned parameters
    pub fn train(&mut self, text: &str, verbose: bool) -> Result<PunktParameters> {
        if verbose {
            println!("Starting training on {} characters...", text.len());
        }

        // Tokenize the text
        let tokens = self.word_tokenize_with_context(text);

        if verbose {
            println!("Found {} tokens", tokens.len());
        }

        // First pass: collect frequency distributions
        self.collect_frequencies(&tokens, verbose);

        // Find abbreviations using scoring
        self.find_abbreviations(verbose);

        // Annotate tokens with sentence breaks
        let annotated = self.annotate_tokens(tokens);

        // Collect orthographic data
        self.collect_ortho_data(&annotated);

        // Find collocations and sentence starters
        self.find_collocations_and_starters(&annotated, verbose);

        // Freeze parameters for inference
        self.params.freeze();

        if verbose {
            println!("Training complete!");
            println!("  Abbreviations: {}", self.params.abbrev_types.len());
            println!("  Collocations: {}", self.params.collocations.len());
            println!("  Sentence starters: {}", self.params.sent_starters.len());
        }

        Ok(self.params.clone())
    }

    /// Train incrementally on chunks of text (for streaming)
    pub fn train_incremental(&mut self, text: &str, verbose: bool) -> Result<()> {
        // Tokenize the text chunk
        let tokens = self.word_tokenize_with_context(text);

        if verbose && self.sentbreak_count % 10000 == 0 {
            println!("Processing... {} sentences so far", self.sentbreak_count);
        }

        // Collect frequency distributions for this chunk
        self.collect_frequencies(&tokens, false);

        // Annotate tokens with sentence breaks
        let annotated = self.annotate_tokens(tokens);

        // Collect orthographic data
        self.collect_ortho_data(&annotated);

        // Collect data for collocations and starters (but don't finalize yet)
        for i in 0..annotated.len() {
            let token = &annotated[i];

            // Track sentence breaks
            if token.sentbreak {
                self.sentbreak_count += 1;
            }

            // Track collocations but avoid spurious learning from abbreviations
            if i > 0 {
                let prev = &annotated[i - 1];
                if prev.period_final && !prev.sentbreak {
                    // Only learn as collocation if there's evidence OTHER than being an abbreviation
                    // This prevents spurious collocations from abbreviation-prevented breaks
                    let has_other_evidence =
                        token.first_lower() || (prev.parastart && token.first_upper());

                    if has_other_evidence || !prev.abbr {
                        let prev_type = prev.type_no_period();
                        let curr_type = token.type_no_sentperiod();
                        let pair = (prev_type.to_string(), curr_type.to_string());
                        self.collocation_fdist.add_count(pair, 1);
                    }
                }
            }

            // Track sentence starters
            if token.sentbreak || token.parastart {
                let type_no_sentperiod = token.type_no_sentperiod();
                self.sent_starter_fdist.add(type_no_sentperiod.to_string());
            }
        }

        Ok(())
    }

    /// Finalize training after all chunks have been processed
    pub fn finalize_training(&mut self, verbose: bool) -> Result<PunktParameters> {
        use crate::statistics::dunning_log_likelihood;

        // Find abbreviations using scoring
        self.find_abbreviations(verbose);

        // Process collected collocations using the same CollocationScorer as single-pass
        let total = self.type_fdist.total();
        let min_freq = (self.config.min_colloc_rate * total as f64) as usize;
        let colloc_scorer = crate::statistics::CollocationScorer::new(
            self.config.collocation_threshold,
            min_freq.max(1),
        );

        for ((first, second), count) in self.collocation_fdist.most_common() {
            // Get token counts, including period variants
            let first_count =
                self.type_fdist.get(first) + self.type_fdist.get(&format!("{}.", first));
            let second_count =
                self.type_fdist.get(second) + self.type_fdist.get(&format!("{}.", second));

            // Use the same scorer logic as single-pass training
            if colloc_scorer.is_collocation(first_count, second_count, count, total) {
                self.params.add_collocation(first, second);
            }
        }

        // Process sentence starters with quality filters
        for (token_type, count) in self.sent_starter_fdist.most_common() {
            let total = self.type_fdist.total();

            // Filter by minimum rate (not absolute count)
            let rate = count as f64 / total as f64;
            if rate < self.config.min_starter_rate {
                continue;
            }

            // Quality filter: require alphabetic characters
            if self.config.require_alpha_starters {
                if !token_type.chars().any(|c| c.is_alphabetic()) {
                    continue;
                }

                // Skip pure punctuation or symbols
                if token_type.chars().all(|c| !c.is_alphanumeric()) {
                    continue;
                }

                // Skip if it's just numbers
                if token_type.starts_with("##number##") {
                    continue;
                }
            }

            let type_count = self.type_fdist.get(token_type);

            if type_count > 0 && self.sentbreak_count > 0 {
                let score = dunning_log_likelihood(count + type_count, count, type_count, total);

                if score > self.config.sent_starter_threshold {
                    self.params.add_sent_starter(token_type);
                }
            }
        }

        // Freeze parameters for inference
        self.params.freeze();

        if verbose {
            println!("Training complete!");
            println!("  Abbreviations: {}", self.params.abbrev_types.len());
            println!("  Collocations: {}", self.params.collocations.len());
            println!("  Sentence starters: {}", self.params.sent_starters.len());
        }

        Ok(self.params.clone())
    }

    /// Tokenize text with paragraph and line context
    fn word_tokenize_with_context(&self, text: &str) -> Vec<PunktToken> {
        let mut tokens = Vec::new();
        let mut parastart = true;

        // Process the entire text to preserve spacing
        let lines: Vec<&str> = text.lines().collect();

        for (line_idx, line) in lines.iter().enumerate() {
            let mut linestart = true;

            // Get tokens with spacing information
            let words_with_spacing = self.preprocessor.word_tokenize_with_spacing(line);

            for (word_idx, (word, spaces_after, _, byte_pos)) in
                words_with_spacing.iter().enumerate()
            {
                let mut token = PunktToken::new(word.clone(), parastart, linestart);
                
                // Store byte position (relative to line, but that's OK for training)
                token.byte_position = Some(*byte_pos);

                // Check for ellipsis
                if token.is_ellipsis() {
                    token.ellipsis = true;
                }

                // Set spacing information
                // Check if this is the last word in the line
                if word_idx == words_with_spacing.len() - 1 && line_idx < lines.len() - 1 {
                    // Last word in line (but not last line) - has newline after
                    token.has_newline_after = true;
                    token.spaces_after = 0;

                    // Check if next line is empty (paragraph break)
                    if line_idx + 1 < lines.len() && lines[line_idx + 1].trim().is_empty() {
                        // Extra strong signal for paragraph break
                        token.spaces_after = 2; // Treat as double space
                    }
                } else {
                    token.spaces_after = *spaces_after;
                    token.has_newline_after = false;
                }

                tokens.push(token);
                parastart = false;
                linestart = false;
            }

            // Empty line indicates paragraph break
            if line.trim().is_empty() {
                parastart = true;
            }
        }

        tokens
    }

    /// Collect frequency distributions
    fn collect_frequencies(&mut self, tokens: &[PunktToken], verbose: bool) {
        if verbose {
            println!("Collecting frequency distributions...");
        }

        // Track total tokens
        self.params.total_tokens = tokens.len() as u32;

        for i in 0..tokens.len() {
            let token = &tokens[i];
            self.type_fdist.add(token.token_type.clone());

            // Collect token statistics
            let type_no_period = token.type_no_period();

            if token.period_final {
                self.num_period_toks += 1;
                self.params.total_period_tokens += 1;

                // Update token stats for tokens with periods
                self.params.update_token_stats(&type_no_period, |stats| {
                    stats.count_with_period += 1;
                });
            } else {
                // Update token stats for tokens without periods
                self.params.update_token_stats(&type_no_period, |stats| {
                    stats.count_without_period += 1;
                });
            }

            // Track collocations with next token
            if token.period_final && i + 1 < tokens.len() {
                let next_token = &tokens[i + 1];
                let next_type = next_token.type_no_sentperiod();

                self.params.update_token_stats(&type_no_period, |stats| {
                    *stats
                        .collocation_counts
                        .entry(next_type.clone())
                        .or_insert(0) += 1;
                });
            }
        }

        // Add common abbreviations
        for abbrev in &self.common_abbrevs {
            self.params.add_abbreviation(abbrev.clone());
        }
    }

    /// Find abbreviations using statistical scoring
    fn find_abbreviations(&mut self, verbose: bool) {
        if verbose {
            println!("Finding abbreviations...");
        }

        let scorer = AbbreviationScorer::new(
            self.config.abbrev_threshold,
            self.config.abbrev_boost,
            self.config.abbrev_consistency,
        );

        let total = self.type_fdist.total();

        // Check each token type that appears with a period
        for (token_type, _) in self.type_fdist.most_common() {
            // Skip if too long or is a number
            if token_type.len() > self.config.max_abbrev_length
                || token_type.starts_with("##number##")
            {
                continue;
            }

            // Check if it could be an abbreviation
            if token_type.ends_with('.') {
                let candidate = &token_type[..token_type.len() - 1];

                // Skip if candidate is too long (abbreviations are typically short)
                // Also skip if it's all lowercase and longer than 3 chars (likely a regular word)
                if candidate.len() > 10
                    || (candidate.len() > 3 && candidate.chars().all(|c| c.is_lowercase()))
                {
                    continue;
                }

                // Skip if candidate contains no letters (e.g., numbers only)
                if !candidate.chars().any(|c| c.is_alphabetic()) {
                    continue;
                }

                let count_with = self.type_fdist.get(token_type);
                let count_without = self.type_fdist.get(&candidate.to_string());

                // Additional check: abbreviations should appear with period more often than without
                // This helps filter out sentence-ending words
                if count_without > count_with * 2 {
                    continue;
                }

                if scorer.is_abbreviation(
                    candidate,
                    count_with,
                    count_without,
                    self.num_period_toks,
                    total,
                ) {
                    // Calculate score for learned abbreviation
                    let score = calculate_abbreviation_score(
                        candidate,
                        count_with,
                        count_without,
                        self.num_period_toks,
                        total,
                    );

                    // Add as learned (not provided) abbreviation
                    self.params.add_learned_abbreviation(
                        candidate.to_string(),
                        score,
                        count_with,
                        count_without,
                    );
                }
            }
        }
    }

    /// Annotate tokens with sentence break information
    /// Uses the SAME decision logic as inference to avoid training-inference divergence
    fn annotate_tokens(&mut self, mut tokens: Vec<PunktToken>) -> Vec<PunktToken> {
        use crate::decision::SentenceBoundaryDecider;
        use crate::tokenizers::sentence::InferenceConfig;

        // Use the same decision logic as inference
        // For training, use a balanced PR setting (0.5)
        let training_config = InferenceConfig {
            precision_recall_balance: 0.5, // Balanced for training
        };

        let decider = SentenceBoundaryDecider::new(&self.params, &training_config);
        let len = tokens.len();

        for i in 0..len {
            // Mark abbreviations for consistency
            if tokens[i].period_final {
                let type_no_period = tokens[i].type_no_period();
                if self.params.is_abbreviation(&type_no_period) {
                    tokens[i].abbr = true;
                }
            }

            // Skip ellipsis
            if tokens[i].ellipsis {
                tokens[i].sentbreak = false;
                continue;
            }

            // Get next token if available
            let next_token = if i + 1 < len {
                Some(&tokens[i + 1])
            } else {
                None
            };

            // Use the unified decider - SAME AS INFERENCE
            let decision = decider.decide(&tokens[i], next_token);
            tokens[i].sentbreak = decision.should_break;

            if decision.should_break {
                self.sentbreak_count += 1;
            }
        }

        tokens
    }

    /// Collect orthographic context data
    fn collect_ortho_data(&mut self, tokens: &[PunktToken]) {
        let mut context = "initial";

        for token in tokens {
            if token.parastart && context != "unknown" {
                context = "initial";
            }

            let ortho_key = token.type_no_sentperiod();
            let flag = match (context, token.first_upper(), token.first_lower()) {
                ("initial", true, _) => ORTHO_BEG_UC,
                ("initial", _, true) => ORTHO_BEG_LC,
                ("internal", true, _) => ORTHO_MID_UC,
                ("internal", _, true) => ORTHO_MID_LC,
                ("unknown", true, _) => ORTHO_UNK_UC,
                ("unknown", _, true) => ORTHO_UNK_LC,
                _ => 0,
            };

            if flag > 0 {
                self.params.add_ortho_context(ortho_key, flag);
            }

            // Track sentence starters
            if context == "initial" && token.is_non_punct() {
                let type_no_period = token.type_no_period();
                self.params.update_token_stats(&type_no_period, |stats| {
                    stats.count_as_starter += 1;
                });
            }

            // Update context based on sentence breaks
            if token.sentbreak {
                context = "initial";
            } else if !token.parastart && token.is_non_punct() {
                context = "internal";
            }
        }
    }

    /// Find collocations and sentence starters
    fn find_collocations_and_starters(&mut self, tokens: &[PunktToken], verbose: bool) {
        if verbose {
            println!("Finding collocations and sentence starters...");
        }

        // Collect collocation and starter candidates
        for (token1, next) in pair_iter(tokens.iter()) {
            if let Some(token2) = next {
                if !token1.period_final {
                    continue;
                }

                // Potential collocation - but ONLY if not breaking due to abbreviation alone
                // We should only learn collocations from genuine linguistic patterns,
                // not from abbreviation-prevented breaks (which would create spurious collocations)
                if token1.period_final && !token1.sentbreak {
                    // Only learn as collocation if there's evidence OTHER than being an abbreviation
                    // For example: next token is lowercase, or it's a known pattern
                    let has_other_evidence =
                        token2.first_lower() || (token1.parastart && token2.first_upper());

                    if has_other_evidence || !token1.abbr {
                        // This is a genuine collocation pattern, not just an abbreviation artifact
                        let type1 = token1.type_no_period();
                        let type2 = token2.type_no_sentperiod();
                        self.collocation_fdist.add((type1, type2));
                    }
                }

                // Potential sentence starter
                if token1.sentbreak {
                    self.sent_starter_fdist.add(token2.token_type.clone());
                }
            }
        }

        // Score and add collocations
        // Convert rate to approx count for old scorer (temporary compatibility)
        let min_freq = (self.config.min_colloc_rate * self.type_fdist.total() as f64) as usize;
        let colloc_scorer =
            CollocationScorer::new(self.config.collocation_threshold, min_freq.max(1));

        let total = self.type_fdist.total();

        for ((type1, type2), count) in self.collocation_fdist.most_common() {
            let count1 = self.type_fdist.get(type1) + self.type_fdist.get(&format!("{}.", type1));
            let count2 = self.type_fdist.get(type2) + self.type_fdist.get(&format!("{}.", type2));

            if colloc_scorer.is_collocation(count1, count2, count, total) {
                self.params.add_collocation(type1, type2);
            }
        }

        // Score and add sentence starters
        // Convert rate to approx count for old scorer (temporary compatibility)
        let min_freq = (self.config.min_starter_rate * self.type_fdist.total() as f64) as usize;
        let starter_scorer =
            SentenceStarterScorer::new(self.config.sent_starter_threshold, min_freq.max(1));

        for (starter, count) in self.sent_starter_fdist.most_common() {
            let type_count = self.type_fdist.get(starter);

            if starter_scorer.is_sentence_starter(self.sentbreak_count, type_count, count, total) {
                self.params.add_sent_starter(starter);
            }
        }
    }
}

impl Default for PunktTrainer {
    fn default() -> Self {
        Self::new()
    }
}

/// Python wrapper for ScoringConfig
#[pyclass(name = "ScoringConfig")]
#[derive(Clone)]
pub struct PyScoringConfig {
    pub inner: ScoringConfig,
}

#[pymethods]
impl PyScoringConfig {
    /// Create a new scoring configuration
    #[new]
    #[pyo3(signature = (
        abbrev_threshold=0.1,
        abbrev_boost=1.5,
        collocation_threshold=5.0,
        sent_starter_threshold=25.0,
        min_colloc_rate=0.00001,
        max_abbrev_length=9,
        abbrev_consistency=0.25,
        min_starter_rate=0.00005,
        require_alpha_starters=true
    ))]
    #[allow(clippy::too_many_arguments)]
    fn new(
        abbrev_threshold: f64,
        abbrev_boost: f64,
        collocation_threshold: f64,
        sent_starter_threshold: f64,
        min_colloc_rate: f64,
        max_abbrev_length: usize,
        abbrev_consistency: f64,
        min_starter_rate: f64,
        require_alpha_starters: bool,
    ) -> Self {
        Self {
            inner: ScoringConfig {
                abbrev_threshold,
                abbrev_boost,
                collocation_threshold,
                sent_starter_threshold,
                min_colloc_rate,
                max_abbrev_length,
                abbrev_consistency,
                min_starter_rate,
                require_alpha_starters,
            },
        }
    }

    #[getter]
    fn abbrev_threshold(&self) -> f64 {
        self.inner.abbrev_threshold
    }

    #[setter]
    fn set_abbrev_threshold(&mut self, val: f64) {
        self.inner.abbrev_threshold = val;
    }

    #[getter]
    fn collocation_threshold(&self) -> f64 {
        self.inner.collocation_threshold
    }

    #[setter]
    fn set_collocation_threshold(&mut self, val: f64) {
        self.inner.collocation_threshold = val;
    }

    #[getter]
    fn sent_starter_threshold(&self) -> f64 {
        self.inner.sent_starter_threshold
    }

    #[setter]
    fn set_sent_starter_threshold(&mut self, val: f64) {
        self.inner.sent_starter_threshold = val;
    }

    #[getter]
    fn abbrev_consistency(&self) -> f64 {
        self.inner.abbrev_consistency
    }

    #[setter]
    fn set_abbrev_consistency(&mut self, val: f64) {
        self.inner.abbrev_consistency = val;
    }

    fn __repr__(&self) -> String {
        format!(
            "ScoringConfig(abbrev_threshold={}, collocation_threshold={}, sent_starter_threshold={}, consistency={})",
            self.inner.abbrev_threshold,
            self.inner.collocation_threshold,
            self.inner.sent_starter_threshold,
            self.inner.abbrev_consistency
        )
    }
}

/// Python wrapper for PunktTrainer
#[pyclass(name = "Trainer")]
pub struct PyTrainer {
    inner: PunktTrainer,
}

#[pymethods]
impl PyTrainer {
    /// Create a new trainer with optional config
    #[new]
    #[pyo3(signature = (config=None))]
    fn new(config: Option<&PyScoringConfig>) -> Self {
        let inner = if let Some(config) = config {
            PunktTrainer::with_config(config.inner.clone())
        } else {
            PunktTrainer::new()
        };
        Self { inner }
    }

    /// Load abbreviations from a JSON file
    fn load_abbreviations_from_json(&mut self, path: &str) -> PyResult<usize> {
        self.inner
            .load_abbreviations_from_json(path)
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyIOError, _>(e.to_string()))
    }

    /// Train on text and return parameters
    fn train(
        &mut self,
        text: &str,
        verbose: Option<bool>,
    ) -> PyResult<crate::parameters::PyParameters> {
        let verbose = verbose.unwrap_or(false);

        self.inner
            .train(text, verbose)
            .map(|params| crate::parameters::PyParameters {
                inner: Arc::new(params),
            })
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_provided_abbreviations_dont_break() {
        let mut trainer = PunktTrainer::new();

        // Add "v" as a provided abbreviation
        trainer.params.add_provided_abbreviation("v", "test");

        // Create test text with "v."
        let text = "Smith v. Jones established precedent.";

        // Train on the text
        let params = trainer.train(text, false).unwrap();

        // Check that "v" is still an abbreviation
        assert!(params.is_abbreviation("v"));
        assert!(params.is_provided_abbreviation("v"));

        // Check that "Jones" is NOT learned as a sentence starter
        // (it would be if v. broke the sentence)
        assert!(!params.is_sent_starter("Jones"));
    }

    #[test]
    fn test_annotation_respects_provided_abbreviations() {
        let mut trainer = PunktTrainer::new();

        // Add provided abbreviations
        trainer.params.add_provided_abbreviation("Mr", "test");
        trainer.params.add_provided_abbreviation("Dr", "test");

        // Process text through training pipeline
        let text = "Mr. Smith met Dr. Jones.";
        trainer.train_incremental(text, false).unwrap();

        // Check that provided abbreviations are preserved
        assert!(trainer.params.is_provided_abbreviation("Mr"));
        assert!(trainer.params.is_provided_abbreviation("Dr"));

        // Check that Smith/Jones weren't learned as sentence starters
        assert!(!trainer.params.is_sent_starter("Smith"));
        assert!(!trainer.params.is_sent_starter("Jones"));
    }

    #[test]
    fn test_learned_abbreviations_can_be_overridden() {
        let mut trainer = PunktTrainer::new();

        // Add a learned abbreviation
        trainer.params.add_learned_abbreviation("Inc", 10.0, 20, 5);

        // Now add as provided (overriding)
        trainer.params.add_provided_abbreviation("Inc", "override");

        // Train with text where "Inc." appears
        let text = "Acme Inc.\nNext sentence here.";
        trainer.train_incremental(text, false).unwrap();

        // Should still be provided
        assert!(trainer.params.is_provided_abbreviation("Inc"));
    }

    #[test]
    fn test_load_abbreviations_marks_as_provided() {
        use std::fs;
        
        let mut trainer = PunktTrainer::new();

        // Create temp file with abbreviations
        let json = r#"["Mr.", "Dr.", "v.", "U.S."]"#;
        let mut temp_path = std::env::temp_dir();
        temp_path.push(format!("test_abbrevs_{}.json", std::process::id()));
        fs::write(&temp_path, json).unwrap();

        // Load abbreviations
        let count = trainer.load_abbreviations_from_json(temp_path.to_str().unwrap()).unwrap();
        assert_eq!(count, 4);

        // Check they're all marked as provided
        assert!(trainer.params.is_provided_abbreviation("Mr"));
        assert!(trainer.params.is_provided_abbreviation("Dr"));
        assert!(trainer.params.is_provided_abbreviation("v"));
        assert!(trainer.params.is_provided_abbreviation("U.S"));
        
        // Clean up
        let _ = fs::remove_file(&temp_path);
    }

    #[test]
    fn test_training_preserves_provided_abbreviations() {
        let mut trainer = PunktTrainer::new();

        // Add provided abbreviation
        trainer.params.add_provided_abbreviation("v", "legal");

        // Train on corpus with "v."
        let corpus = "Daubert v. Merrell established rules. Smith v. Jones followed.";
        let params = trainer.train(corpus, false).unwrap();

        // Check v is still provided after training
        assert!(params.is_provided_abbreviation("v"));

        // Check neither Merrell nor Jones became sentence starters
        assert!(!params.is_sent_starter("Merrell"));
        assert!(!params.is_sent_starter("Jones"));
    }
}
