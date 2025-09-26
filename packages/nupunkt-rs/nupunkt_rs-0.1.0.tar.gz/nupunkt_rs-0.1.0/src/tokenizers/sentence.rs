/// Sentence tokenizer using the Punkt algorithm
use crate::analysis::{AnalysisStatistics, TextAnalysis};
use crate::core::SentenceTokenizer;
use crate::parameters::PunktParameters;
use crate::tokens::PunktToken;
use crate::utils::TextPreprocessor;
use pyo3::prelude::*;
use std::sync::Arc;

/// Configuration for inference-time adjustments
#[derive(Debug, Clone)]
pub struct InferenceConfig {
    /// Precision/recall balance (0.0 to 1.0)
    /// - 0.0 = Maximum recall (breaks at most possible boundaries)
    /// - 0.5 = Balanced (default)
    /// - 1.0 = Maximum precision (breaks only at very clear boundaries)
    pub precision_recall_balance: f64,
}

impl Default for InferenceConfig {
    fn default() -> Self {
        Self {
            precision_recall_balance: 0.5, // Balanced by default
        }
    }
}

/// Punkt sentence tokenizer
#[derive(Clone)]
pub struct PunktSentenceTokenizer {
    /// Model parameters
    params: Arc<PunktParameters>,

    /// Text preprocessor
    preprocessor: TextPreprocessor,

    /// Inference configuration
    inference_config: InferenceConfig,

    /// Debug mode flag
    debug_mode: bool,
}

impl PunktSentenceTokenizer {
    /// Create a new tokenizer with parameters
    pub fn from_parameters(params: Arc<PunktParameters>) -> Self {
        Self {
            params,
            preprocessor: TextPreprocessor::default(),
            inference_config: InferenceConfig::default(),
            debug_mode: false,
        }
    }

    /// Create a tokenizer with default parameters
    pub fn new() -> Self {
        Self::from_parameters(Arc::new(PunktParameters::new()))
    }

    /// Set the precision/recall balance
    /// 0.0 = maximum recall (break often)
    /// 1.0 = maximum precision (break rarely)
    pub fn set_precision_recall_balance(&mut self, balance: f64) {
        self.inference_config.precision_recall_balance = balance.clamp(0.0, 1.0);
    }

    /// Convenience method for maximum recall mode
    pub fn set_max_recall(&mut self) {
        self.inference_config.precision_recall_balance = 0.0;
    }

    /// Convenience method for maximum precision mode
    pub fn set_max_precision(&mut self) {
        self.inference_config.precision_recall_balance = 1.0;
    }

    /// Convenience method for balanced mode
    pub fn set_balanced(&mut self) {
        self.inference_config.precision_recall_balance = 0.5;
    }

    /// Get the current inference configuration
    pub fn inference_config(&self) -> &InferenceConfig {
        &self.inference_config
    }

    /// Set the inference configuration
    pub fn set_inference_config(&mut self, config: InferenceConfig) {
        self.inference_config = config;
    }

    /// Enable or disable debug mode
    pub fn set_debug_mode(&mut self, enabled: bool) {
        self.debug_mode = enabled;
    }

    /// Check if debug mode is enabled
    pub fn is_debug_mode(&self) -> bool {
        self.debug_mode
    }

    /// Tokenize text into tokens with context
    fn tokenize_words(&self, text: &str) -> Vec<PunktToken> {
        let mut tokens = Vec::new();
        let mut parastart = true;

        // Process the entire text to preserve spacing
        let lines: Vec<&str> = text.lines().collect();
        
        // Pre-calculate line byte offsets to avoid O(n²) complexity
        let mut line_byte_offsets = Vec::with_capacity(lines.len());
        let mut cumulative_offset = 0;
        for (i, line) in lines.iter().enumerate() {
            line_byte_offsets.push(cumulative_offset);
            cumulative_offset += line.len();
            if i < lines.len() - 1 {
                cumulative_offset += 1; // Add 1 for newline
            }
        }

        for (line_idx, line) in lines.iter().enumerate() {
            let mut linestart = true;

            // Get tokens with spacing information
            let words_with_spacing = self.preprocessor.word_tokenize_with_spacing(line);

            for (word_idx, (word, spaces_after, _, byte_pos)) in
                words_with_spacing.iter().enumerate()
            {
                let mut token = PunktToken::new(word.clone(), parastart, linestart);

                // Use pre-calculated line offset
                let line_byte_offset = line_byte_offsets[line_idx];
                let full_byte_pos = line_byte_offset + byte_pos;
                token.byte_position = Some(full_byte_pos);
                // Skip char_position calculation - it's too expensive and not currently used
                // token.char_position = Some(text[..full_byte_pos].chars().count());

                // Mark abbreviations
                if token.period_final {
                    let type_no_period = token.type_no_period();
                    if self.params.is_abbreviation(&type_no_period) {
                        token.abbr = true;
                    }
                }

                // Mark ellipsis
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

            if line.trim().is_empty() {
                parastart = true;
            }
        }

        tokens
    }

    /// Annotate tokens with sentence boundaries using unified decider
    fn annotate_sentence_boundaries(&self, tokens: Vec<PunktToken>) -> Vec<PunktToken> {
        self.annotate_sentence_boundaries_with_config(tokens, &self.inference_config)
    }

    /// Annotate tokens with sentence boundaries using provided config
    fn annotate_sentence_boundaries_with_config(
        &self,
        mut tokens: Vec<PunktToken>,
        config: &InferenceConfig,
    ) -> Vec<PunktToken> {
        use crate::decision::SentenceBoundaryDecider;

        let decider = SentenceBoundaryDecider::new(&self.params, config);
        let len = tokens.len();

        for i in 0..len {
            // Skip tokens that already have abbr flag set (e.g., ellipsis)
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

            // Use the unified decider
            let decision = decider.decide(&tokens[i], next_token);

            tokens[i].sentbreak = decision.should_break;

            // Debug output if enabled
            if self.debug_mode && tokens[i].period_final {
                eprintln!(
                    "DEBUG: Token '{}' - Decision: {}, Confidence: {:.2}, Reason: {}",
                    tokens[i].tok,
                    if decision.should_break {
                        "BREAK"
                    } else {
                        "NO_BREAK"
                    },
                    decision.confidence,
                    decision.primary_reason
                );

                if self.debug_mode {
                    for factor in &decision.factors {
                        eprintln!(
                            "  Factor: {:?}, Weight: {:.2}, {}",
                            factor.factor_type, factor.weight, factor.description
                        );
                    }
                }
            }
        }

        tokens
    }

    /// Extract sentences from annotated tokens
    fn extract_sentences(&self, tokens: Vec<PunktToken>) -> Vec<String> {
        let mut sentences = Vec::new();
        let mut current = Vec::new();

        for token in tokens {
            current.push(token.tok.clone());

            if token.sentbreak && !current.is_empty() {
                sentences.push(current.join(" "));
                current.clear();
            }
        }

        // Add remaining tokens as final sentence
        if !current.is_empty() {
            sentences.push(current.join(" "));
        }

        sentences
    }

    /// Tokenize with analysis - returns both sentences and detailed analysis
    pub fn tokenize_with_analysis(&self, text: &str) -> (Vec<String>, TextAnalysis) {
        let analysis = self.analyze_tokens(text);
        let sentences = analysis.sentences.clone();
        (sentences, analysis)
    }

    /// Get statistics about the model
    pub fn get_statistics(&self) -> String {
        let mut stats = String::new();

        stats.push_str("Punkt Model Statistics\n");
        stats.push_str("======================\n\n");

        stats.push_str(&format!(
            "Abbreviations: {}\n",
            self.params.abbrev_types.len()
        ));
        if !self.params.abbrev_types.is_empty() {
            // Extract and sort just the abbreviation strings (keys)
            let mut abbrevs: Vec<String> = self.params.abbrev_types.keys().cloned().collect();
            abbrevs.sort();
            let sample: Vec<_> = abbrevs.iter().take(10).map(|s| s.as_str()).collect();
            stats.push_str(&format!("  Sample: {}\n", sample.join(", ")));
            if abbrevs.len() > 10 {
                stats.push_str(&format!("  ... and {} more\n", abbrevs.len() - 10));
            }

            // Count provided vs learned
            let provided_count = self
                .params
                .abbrev_types
                .values()
                .filter(|t| t.is_provided())
                .count();
            let learned_count = abbrevs.len() - provided_count;
            stats.push_str(&format!(
                "  Provided: {}, Learned: {}\n",
                provided_count, learned_count
            ));
        }

        stats.push_str(&format!(
            "\nCollocations: {}\n",
            self.params.collocations.len()
        ));
        if !self.params.collocations.is_empty() {
            let mut collocs: Vec<_> = self
                .params
                .collocations
                .iter()
                .map(|(a, b)| format!("{} + {}", a, b))
                .collect();
            collocs.sort();
            let sample: Vec<_> = collocs.iter().take(5).map(|s| s.as_str()).collect();
            stats.push_str(&format!("  Sample: {}\n", sample.join(", ")));
            if collocs.len() > 5 {
                stats.push_str(&format!("  ... and {} more\n", collocs.len() - 5));
            }
        }

        stats.push_str(&format!(
            "\nSentence starters: {}\n",
            self.params.sent_starters.len()
        ));
        if !self.params.sent_starters.is_empty() {
            let mut starters: Vec<_> = self.params.sent_starters.iter().collect();
            starters.sort();
            let sample: Vec<_> = starters.iter().take(10).map(|s| s.as_str()).collect();
            stats.push_str(&format!("  Sample: {}\n", sample.join(", ")));
            if starters.len() > 10 {
                stats.push_str(&format!("  ... and {} more\n", starters.len() - 10));
            }
        }

        stats.push_str(&format!(
            "\nOrthographic contexts: {}\n",
            self.params.ortho_context.len()
        ));

        stats.push_str("\nInference Configuration:\n");
        stats.push_str(&format!(
            "  Precision/recall balance: {:.2}",
            self.inference_config.precision_recall_balance
        ));

        // Add descriptive label
        let mode = if self.inference_config.precision_recall_balance < 0.3 {
            " (high recall)"
        } else if self.inference_config.precision_recall_balance > 0.7 {
            " (high precision)"
        } else {
            " (balanced)"
        };
        stats.push_str(mode);
        stats.push('\n');
        stats.push_str(&format!("  Debug mode: {}\n", self.debug_mode));

        stats
    }

    /// Explain the decision at a specific position in the text
    pub fn explain_decision(&self, text: &str, position: usize) -> Option<String> {
        let analysis = self.analyze_tokens(text);

        // Find the token at or near this position
        for token_analysis in &analysis.tokens {
            if position >= token_analysis.position
                && position < token_analysis.position + token_analysis.length
            {
                // Found the token at this position
                let mut explanation = String::new();

                explanation.push_str(&format!(
                    "Token: '{}' at position {}\n",
                    token_analysis.text, token_analysis.position
                ));
                explanation.push_str(&format!("Decision: {:?}\n", token_analysis.decision));
                explanation.push_str(&format!("Confidence: {:.2}\n", token_analysis.confidence));
                explanation.push_str(&format!(
                    "Primary reason: {}\n\n",
                    token_analysis.primary_reason
                ));

                if token_analysis.has_period {
                    explanation.push_str("Analysis:\n");
                    if token_analysis.in_abbrev_list {
                        explanation.push_str("  - In abbreviation list: YES\n");
                    } else {
                        explanation.push_str("  - In abbreviation list: NO\n");
                    }

                    if let Some(score) = token_analysis.abbrev_score {
                        explanation.push_str(&format!("  - Abbreviation score: {:.2}\n", score));
                    }

                    if token_analysis.is_collocation {
                        explanation.push_str("  - Forms collocation: YES\n");
                    }

                    if let Some(capital) = token_analysis.next_is_capital {
                        explanation.push_str(&format!(
                            "  - Next word capitalized: {}\n",
                            if capital { "YES" } else { "NO" }
                        ));
                    }

                    if !token_analysis.factors.is_empty() {
                        explanation.push_str("\nDecision factors:\n");
                        for factor in &token_analysis.factors {
                            let impact = if factor.weight > 0.0 {
                                "breaks"
                            } else {
                                "continues"
                            };
                            explanation.push_str(&format!(
                                "  - {:?} (weight: {:.2}, {}): {}\n",
                                factor.factor_type,
                                factor.weight.abs(),
                                impact,
                                factor.description
                            ));
                        }
                    }
                }

                return Some(explanation);
            }
        }

        None
    }

    /// Analyze tokens and return detailed scoring information
    /// This observes the actual tokenization decisions rather than making parallel ones
    pub fn analyze_tokens(&self, text: &str) -> TextAnalysis {
        use crate::analysis::{BreakDecision, TokenAnalysis};
        use crate::decision::SentenceBoundaryDecider;

        if text.is_empty() {
            return TextAnalysis {
                tokens: Vec::new(),
                sentences: Vec::new(),
                break_positions: Vec::new(),
                statistics: AnalysisStatistics {
                    total_tokens: 0,
                    total_breaks: 0,
                    abbreviations_found: 0,
                    collocations_found: 0,
                    average_confidence: 0.0,
                    low_confidence_decisions: 0,
                },
            };
        }

        // Use the actual tokenization process
        let tokens = self.tokenize_words(text);
        let decider = SentenceBoundaryDecider::new(&self.params, &self.inference_config);

        let mut token_analyses = Vec::new();
        let mut break_positions = Vec::new();
        let mut sentences = Vec::new();
        let mut current_sentence = Vec::new();

        // Statistics
        let mut total_breaks = 0;
        let mut abbreviations_found = 0;
        let mut collocations_found = 0;
        let mut total_confidence = 0.0;
        let mut low_confidence_decisions = 0;
        let mut decision_count = 0;

        // Process each token using the same logic as tokenize()
        for i in 0..tokens.len() {
            let token = &tokens[i];
            let next_token = if i + 1 < tokens.len() {
                Some(&tokens[i + 1])
            } else {
                None
            };

            // Calculate character position from byte position for TokenAnalysis
            // This is needed for user-facing analysis but not for internal tokenization
            let token_pos = if let Some(byte_pos) = token.byte_position {
                // Only calculate char position when needed for analysis
                text[..byte_pos].chars().count()
            } else {
                0
            };

            // Get the actual decision from the unified decider
            let decision = decider.decide(token, next_token);

            // Convert to TokenAnalysis
            let type_no_period = token.type_no_period();
            let mut analysis = TokenAnalysis {
                text: token.tok.clone(),
                position: token_pos,
                length: token.tok.len(),
                has_period: token.period_final,
                abbrev_score: None,
                in_abbrev_list: self.params.is_abbreviation(&type_no_period),
                collocation_score: None,
                is_collocation: false,
                next_is_capital: next_token.map(|t| t.first_upper()),
                decision: if decision.should_break {
                    BreakDecision::Break
                } else if token.period_final {
                    BreakDecision::NoBreak
                } else {
                    BreakDecision::Continue
                },
                confidence: decision.confidence,
                primary_reason: decision.primary_reason.clone(),
                factors: decision.factors.clone(),
            };

            // Add scoring information if available
            if let Some(stats) = self.params.get_token_stats(&type_no_period) {
                if stats.count_with_period > 0 || stats.count_without_period > 0 {
                    use crate::statistics::dunning_log_likelihood;
                    let score = dunning_log_likelihood(
                        (stats.count_with_period + stats.count_without_period) as usize,
                        self.params.total_period_tokens as usize,
                        stats.count_with_period as usize,
                        self.params.total_tokens as usize,
                    );
                    analysis.abbrev_score = Some(score);
                }
            }

            // Check for collocation
            if let Some(next) = next_token {
                let next_type = next.type_no_sentperiod();
                analysis.is_collocation = self.params.is_collocation(&type_no_period, &next_type);
            }

            // Update statistics
            if analysis.in_abbrev_list {
                abbreviations_found += 1;
            }
            if analysis.is_collocation {
                collocations_found += 1;
            }
            if analysis.has_period {
                decision_count += 1;
                total_confidence += analysis.confidence;
                if analysis.confidence < 0.3 {
                    low_confidence_decisions += 1;
                }
            }

            // Track sentence breaks
            current_sentence.push(token.tok.clone());
            if decision.should_break {
                total_breaks += 1;
                break_positions.push(token_pos + token.tok.len());
                sentences.push(current_sentence.join(" "));
                current_sentence.clear();
            }

            token_analyses.push(analysis);
        }

        // Add remaining sentence
        if !current_sentence.is_empty() {
            sentences.push(current_sentence.join(" "));
        }

        // Calculate average confidence
        let average_confidence = if decision_count > 0 {
            total_confidence / decision_count as f64
        } else {
            0.0
        };

        TextAnalysis {
            tokens: token_analyses,
            sentences,
            break_positions,
            statistics: AnalysisStatistics {
                total_tokens: tokens.len(),
                total_breaks,
                abbreviations_found,
                collocations_found,
                average_confidence,
                low_confidence_decisions,
            },
        }
    }

    /// Internal method: tokenize with a specific inference config
    pub fn tokenize_with_config(&self, text: &str, config: &InferenceConfig) -> Vec<String> {
        if text.is_empty() {
            return Vec::new();
        }

        let tokens = self.tokenize_words(text);
        let annotated = self.annotate_sentence_boundaries_with_config(tokens, config);
        self.extract_sentences(annotated)
    }

    /// Internal method: tokenize_spans with a specific inference config
    pub fn tokenize_spans_with_config(
        &self,
        text: &str,
        config: &InferenceConfig,
    ) -> Vec<(usize, usize)> {
        if text.is_empty() {
            return Vec::new();
        }

        let tokens = self.tokenize_words(text);
        let annotated = self.annotate_sentence_boundaries_with_config(tokens, config);

        let mut spans = Vec::new();
        let mut start = 0;

        // Use stored byte positions instead of searching
        for (i, token) in annotated.iter().enumerate() {
            if token.sentbreak {
                // Get the end position from the stored byte position
                if let Some(token_start) = token.byte_position {
                    let token_end = token_start + token.tok.len();
                    spans.push((start, token_end));
                    
                    // Find the start of the next sentence
                    if i + 1 < annotated.len() {
                        if let Some(next_pos) = annotated[i + 1].byte_position {
                            start = next_pos;
                        } else {
                            // Fallback: skip whitespace after current token
                            start = token_end;
                            while start < text.len() && text.as_bytes()[start].is_ascii_whitespace() {
                                start += 1;
                            }
                        }
                    } else {
                        // This was the last token, mark that we've covered everything
                        start = text.len();
                    }
                }
            }
        }

        // Add final span if there's remaining text and the last token wasn't a sentence break
        if start < text.len() && !annotated.is_empty() && !annotated.last().unwrap().sentbreak {
            spans.push((start, text.len()));
        }

        spans
    }
}

impl Default for PunktSentenceTokenizer {
    fn default() -> Self {
        Self::new()
    }
}

impl PunktSentenceTokenizer {
    /// Tokenize text into paragraphs, where each paragraph is a vector of sentences
    pub fn tokenize_paragraphs(&self, text: &str) -> Vec<Vec<String>> {
        if text.is_empty() {
            return Vec::new();
        }

        let tokens = self.tokenize_words(text);
        let annotated = self.annotate_sentence_boundaries(tokens);
        self.extract_paragraphs(annotated)
    }

    /// Tokenize text into paragraphs as strings (sentences joined with spaces)
    pub fn tokenize_paragraphs_flat(&self, text: &str) -> Vec<String> {
        self.tokenize_paragraphs(text)
            .into_iter()
            .map(|sentences| sentences.join(" "))
            .collect()
    }

    /// Extract paragraphs from annotated tokens
    fn extract_paragraphs(&self, tokens: Vec<PunktToken>) -> Vec<Vec<String>> {
        let mut paragraphs = Vec::new();
        let mut current_paragraph = Vec::new();
        let mut current_sentence = Vec::new();

        for (i, token) in tokens.iter().enumerate() {
            current_sentence.push(token.tok.clone());

            if token.sentbreak && !current_sentence.is_empty() {
                // Complete the current sentence
                current_paragraph.push(current_sentence.join(" "));
                current_sentence.clear();

                // Check if this is also a paragraph break
                // A paragraph break is indicated by:
                // 1. The current token has double spaces and newline after
                // 2. The next token (if exists) starts a paragraph
                let is_para_break = (token.spaces_after >= 2 && token.has_newline_after)
                    || (i + 1 < tokens.len() && tokens[i + 1].parastart);

                if is_para_break && !current_paragraph.is_empty() {
                    paragraphs.push(current_paragraph.clone());
                    current_paragraph.clear();
                }
            }
        }

        // Add remaining sentence
        if !current_sentence.is_empty() {
            current_paragraph.push(current_sentence.join(" "));
        }

        // Add remaining paragraph
        if !current_paragraph.is_empty() {
            paragraphs.push(current_paragraph);
        }

        paragraphs
    }
}

impl SentenceTokenizer for PunktSentenceTokenizer {
    fn tokenize(&self, text: &str) -> Vec<String> {
        if text.is_empty() {
            return Vec::new();
        }

        let tokens = self.tokenize_words(text);
        let annotated = self.annotate_sentence_boundaries(tokens);
        self.extract_sentences(annotated)
    }

    fn tokenize_spans(&self, text: &str) -> Vec<(usize, usize)> {
        if text.is_empty() {
            return Vec::new();
        }

        let tokens = self.tokenize_words(text);
        let annotated = self.annotate_sentence_boundaries(tokens);

        let mut spans = Vec::new();
        let mut start = 0;

        // Use stored byte positions instead of searching
        for (i, token) in annotated.iter().enumerate() {
            if token.sentbreak {
                // Get the end position from the stored byte position
                if let Some(token_start) = token.byte_position {
                    let token_end = token_start + token.tok.len();
                    spans.push((start, token_end));
                    
                    // Find the start of the next sentence
                    if i + 1 < annotated.len() {
                        if let Some(next_pos) = annotated[i + 1].byte_position {
                            start = next_pos;
                        } else {
                            // Fallback: skip whitespace after current token
                            start = token_end;
                            while start < text.len() && text.as_bytes()[start].is_ascii_whitespace() {
                                start += 1;
                            }
                        }
                    } else {
                        // This was the last token, mark that we've covered everything
                        start = text.len();
                    }
                }
            }
        }

        // Add final span if there's remaining text and the last token wasn't a sentence break
        if start < text.len() && !annotated.is_empty() && !annotated.last().unwrap().sentbreak {
            spans.push((start, text.len()));
        }

        spans
    }

    fn is_sentence_boundary(&self, text: &str, pos: usize) -> bool {
        // Simple check: is there a sentence-ending punctuation at this position?
        if pos >= text.len() {
            return false;
        }

        text.chars()
            .nth(pos)
            .is_some_and(|c| c == '.' || c == '!' || c == '?')
    }
}

/// Python wrapper for InferenceConfig
#[pyclass(name = "InferenceConfig")]
#[derive(Clone)]
pub struct PyInferenceConfig {
    pub inner: InferenceConfig,
}

#[pymethods]
impl PyInferenceConfig {
    #[new]
    #[pyo3(signature = (precision_recall_balance=0.5))]
    fn new(precision_recall_balance: f64) -> Self {
        Self {
            inner: InferenceConfig {
                precision_recall_balance: precision_recall_balance.clamp(0.0, 1.0),
            },
        }
    }

    #[getter]
    fn precision_recall_balance(&self) -> f64 {
        self.inner.precision_recall_balance
    }

    #[setter]
    fn set_precision_recall_balance(&mut self, val: f64) {
        self.inner.precision_recall_balance = val.clamp(0.0, 1.0);
    }

    /// Create config for maximum recall (breaks often)
    #[staticmethod]
    fn max_recall() -> Self {
        Self {
            inner: InferenceConfig {
                precision_recall_balance: 0.0,
            },
        }
    }

    /// Create config for maximum precision (breaks rarely)
    #[staticmethod]
    fn max_precision() -> Self {
        Self {
            inner: InferenceConfig {
                precision_recall_balance: 1.0,
            },
        }
    }

    /// Create config for balanced mode
    #[staticmethod]
    fn balanced() -> Self {
        Self {
            inner: InferenceConfig {
                precision_recall_balance: 0.5,
            },
        }
    }

    fn __repr__(&self) -> String {
        let mode = if self.inner.precision_recall_balance < 0.3 {
            "high_recall"
        } else if self.inner.precision_recall_balance > 0.7 {
            "high_precision"
        } else {
            "balanced"
        };

        format!(
            "InferenceConfig(precision_recall_balance={:.2}, mode={})",
            self.inner.precision_recall_balance, mode
        )
    }
}

/// Python wrapper for sentence tokenizer
#[pyclass(name = "SentenceTokenizer")]
pub struct PySentenceTokenizer {
    pub inner: PunktSentenceTokenizer,
}

#[pymethods]
impl PySentenceTokenizer {
    /// Create a new tokenizer
    #[new]
    fn new(params: Option<&crate::parameters::PyParameters>) -> Self {
        let tokenizer = if let Some(params) = params {
            PunktSentenceTokenizer::from_parameters(params.inner.clone())
        } else {
            PunktSentenceTokenizer::new()
        };

        Self { inner: tokenizer }
    }

    /// Tokenize text into sentences
    ///
    /// Args:
    ///     text: The text to tokenize
    ///     precision_recall_balance: Optional override for precision/recall balance (0.0-1.0)
    ///         - 0.0 = Maximum recall (breaks at most possible boundaries)
    ///         - 0.5 = Balanced (default)
    ///         - 1.0 = Maximum precision (breaks only at very clear boundaries)
    #[pyo3(signature = (text, precision_recall_balance=None))]
    fn tokenize(&self, text: &str, precision_recall_balance: Option<f64>) -> Vec<String> {
        if let Some(pr_balance) = precision_recall_balance {
            // Create temporary config with provided balance
            let config = InferenceConfig {
                precision_recall_balance: pr_balance.clamp(0.0, 1.0),
            };
            self.inner.tokenize_with_config(text, &config)
        } else {
            // Use stored config
            self.inner.tokenize(text)
        }
    }

    /// Get sentence boundaries as character spans
    ///
    /// Args:
    ///     text: The text to tokenize
    ///     precision_recall_balance: Optional override for precision/recall balance (0.0-1.0)
    #[pyo3(signature = (text, precision_recall_balance=None))]
    fn tokenize_spans(
        &self,
        text: &str,
        precision_recall_balance: Option<f64>,
    ) -> Vec<(usize, usize)> {
        if let Some(pr_balance) = precision_recall_balance {
            // Create temporary config with provided balance
            let config = InferenceConfig {
                precision_recall_balance: pr_balance.clamp(0.0, 1.0),
            };
            self.inner.tokenize_spans_with_config(text, &config)
        } else {
            // Use stored config
            self.inner.tokenize_spans(text)
        }
    }

    /// Check if a position is a sentence boundary
    fn is_sentence_boundary(&self, text: &str, pos: usize) -> bool {
        self.inner.is_sentence_boundary(text, pos)
    }

    /// Analyze tokens and return detailed scoring information
    fn analyze_tokens(&self, text: &str) -> crate::analysis::PyTextAnalysis {
        let analysis = self.inner.analyze_tokens(text);
        crate::analysis::PyTextAnalysis { inner: analysis }
    }

    /// Tokenize with analysis - returns both sentences and detailed analysis
    fn tokenize_with_analysis(&self, text: &str) -> (Vec<String>, crate::analysis::PyTextAnalysis) {
        let (sentences, analysis) = self.inner.tokenize_with_analysis(text);
        (
            sentences,
            crate::analysis::PyTextAnalysis { inner: analysis },
        )
    }

    /// Explain the decision at a specific position in the text
    fn explain_decision(&self, text: &str, position: usize) -> Option<String> {
        self.inner.explain_decision(text, position)
    }

    /// Set the precision/recall balance (0.0=recall, 1.0=precision)
    fn set_precision_recall_balance(&mut self, balance: f64) {
        self.inner.set_precision_recall_balance(balance);
    }

    /// Set to maximum recall mode (breaks at most boundaries)
    fn set_max_recall(&mut self) {
        self.inner.set_max_recall();
    }

    /// Set to maximum precision mode (breaks only at clear boundaries)
    fn set_max_precision(&mut self) {
        self.inner.set_max_precision();
    }

    /// Set to balanced mode
    fn set_balanced(&mut self) {
        self.inner.set_balanced();
    }

    /// Get the current inference configuration
    fn get_inference_config(&self) -> PyInferenceConfig {
        PyInferenceConfig {
            inner: self.inner.inference_config.clone(),
        }
    }

    /// Set the inference configuration
    fn set_inference_config(&mut self, config: &PyInferenceConfig) {
        self.inner.set_inference_config(config.inner.clone());
    }

    /// Enable or disable debug mode
    fn set_debug_mode(&mut self, enabled: bool) {
        self.inner.set_debug_mode(enabled);
    }

    /// Check if debug mode is enabled
    #[getter]
    fn debug_mode(&self) -> bool {
        self.inner.is_debug_mode()
    }

    /// Get statistics about the model
    fn get_statistics(&self) -> String {
        self.inner.get_statistics()
    }

    /// Tokenize multiple documents in a single call (reduces overhead)
    ///
    /// Args:
    ///     texts: List of texts to tokenize
    ///     precision_recall_balance: Optional override for precision/recall balance (0.0-1.0)
    #[pyo3(signature = (texts, precision_recall_balance=None))]
    fn tokenize_batch(
        &self,
        texts: Vec<String>,
        precision_recall_balance: Option<f64>,
    ) -> Vec<Vec<String>> {
        if let Some(pr_balance) = precision_recall_balance {
            let config = InferenceConfig {
                precision_recall_balance: pr_balance.clamp(0.0, 1.0),
            };
            texts
                .iter()
                .map(|text| self.inner.tokenize_with_config(text, &config))
                .collect()
        } else {
            texts.iter().map(|text| self.inner.tokenize(text)).collect()
        }
    }

    /// Count sentences without returning the actual strings (faster)
    ///
    /// Args:
    ///     text: The text to analyze
    ///     precision_recall_balance: Optional override for precision/recall balance (0.0-1.0)
    #[pyo3(signature = (text, precision_recall_balance=None))]
    fn count_sentences(&self, text: &str, precision_recall_balance: Option<f64>) -> usize {
        if let Some(pr_balance) = precision_recall_balance {
            let config = InferenceConfig {
                precision_recall_balance: pr_balance.clamp(0.0, 1.0),
            };
            self.inner.tokenize_with_config(text, &config).len()
        } else {
            self.inner.tokenize(text).len()
        }
    }

    /// Count sentences for multiple documents
    ///
    /// Args:
    ///     texts: List of texts to analyze
    ///     precision_recall_balance: Optional override for precision/recall balance (0.0-1.0)
    #[pyo3(signature = (texts, precision_recall_balance=None))]
    fn count_sentences_batch(
        &self,
        texts: Vec<String>,
        precision_recall_balance: Option<f64>,
    ) -> Vec<usize> {
        if let Some(pr_balance) = precision_recall_balance {
            let config = InferenceConfig {
                precision_recall_balance: pr_balance.clamp(0.0, 1.0),
            };
            texts
                .iter()
                .map(|text| self.inner.tokenize_with_config(text, &config).len())
                .collect()
        } else {
            texts
                .iter()
                .map(|text| self.inner.tokenize(text).len())
                .collect()
        }
    }

    /// Tokenize text into paragraphs
    ///
    /// Returns a list of paragraphs, where each paragraph is a list of sentences.
    ///
    /// Args:
    ///     text: The text to tokenize into paragraphs
    ///     precision_recall_balance: Optional override for precision/recall balance (0.0-1.0)
    ///
    /// Returns:
    ///     List of paragraphs, where each paragraph is a list of sentences
    #[pyo3(signature = (text, precision_recall_balance=None))]
    fn tokenize_paragraphs(&self, text: &str, precision_recall_balance: Option<f64>) -> Vec<Vec<String>> {
        if let Some(pr_balance) = precision_recall_balance {
            // Create temporary tokenizer with provided balance
            let mut temp_tokenizer = self.inner.clone();
            temp_tokenizer.set_precision_recall_balance(pr_balance);
            temp_tokenizer.tokenize_paragraphs(text)
        } else {
            self.inner.tokenize_paragraphs(text)
        }
    }

    /// Tokenize text into paragraphs as flat strings
    ///
    /// Returns a list of paragraphs as strings (sentences joined with spaces).
    ///
    /// Args:
    ///     text: The text to tokenize into paragraphs
    ///     precision_recall_balance: Optional override for precision/recall balance (0.0-1.0)
    ///
    /// Returns:
    ///     List of paragraphs as strings
    #[pyo3(signature = (text, precision_recall_balance=None))]
    fn tokenize_paragraphs_flat(&self, text: &str, precision_recall_balance: Option<f64>) -> Vec<String> {
        if let Some(pr_balance) = precision_recall_balance {
            // Create temporary tokenizer with provided balance
            let mut temp_tokenizer = self.inner.clone();
            temp_tokenizer.set_precision_recall_balance(pr_balance);
            temp_tokenizer.tokenize_paragraphs_flat(text)
        } else {
            self.inner.tokenize_paragraphs_flat(text)
        }
    }
}
