/// Parameters for the Punkt algorithm
use ahash::AHashSet;
use anyhow::{Context, Result};
use lru::LruCache;
use pyo3::prelude::*;
use serde::{Deserialize, Serialize};
use std::cell::RefCell;
use std::collections::{HashMap, HashSet};
use std::num::NonZeroUsize;
use std::sync::Arc;

// Thread-local cache for abbreviation lookups
// Caches the last 512 abbreviation checks to avoid repeated HashMap lookups
thread_local! {
    static ABBREV_CACHE: RefCell<LruCache<String, bool>> = 
        RefCell::new(LruCache::new(NonZeroUsize::new(512).unwrap()));
    
    static ABBREV_TYPE_CACHE: RefCell<LruCache<String, Option<AbbreviationType>>> = 
        RefCell::new(LruCache::new(NonZeroUsize::new(512).unwrap()));
}

/// Distinguishes between provided (ground truth) and learned abbreviations
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum AbbreviationType {
    /// Provided via external file - these are GROUND TRUTH
    /// They should NEVER cause sentence breaks during training
    Provided {
        source: String,  // e.g., "legal_abbreviations.json"
        added_at: usize, // Token position when added (for debugging)
    },

    /// Learned from statistical analysis during training
    /// These are hypotheses that can be overridden by other signals
    Learned {
        score: f64,            // Dunning log-likelihood score
        with_period: usize,    // Times seen with period
        without_period: usize, // Times seen without period
        confidence: f64,       // Computed confidence 0.0-1.0
    },
}

impl AbbreviationType {
    /// Is this a provided (ground truth) abbreviation?
    pub fn is_provided(&self) -> bool {
        matches!(self, AbbreviationType::Provided { .. })
    }

    /// Get confidence level (1.0 for provided, variable for learned)
    pub fn confidence(&self) -> f64 {
        match self {
            AbbreviationType::Provided { .. } => 1.0,
            AbbreviationType::Learned { confidence, .. } => *confidence,
        }
    }

    /// Get weight using provided decision weights
    pub fn get_weight(&self, pr: f64, weights: &DecisionWeights) -> f64 {
        match self {
            AbbreviationType::Provided { .. } => weights.provided_abbrev_weight(pr),
            AbbreviationType::Learned { confidence, .. } => {
                weights.learned_abbrev_weight(pr) * confidence
            }
        }
    }

    /// Debug description
    pub fn describe(&self) -> String {
        match self {
            AbbreviationType::Provided { source, .. } => {
                format!("Provided from {}", source)
            }
            AbbreviationType::Learned {
                score,
                confidence,
                with_period,
                without_period,
            } => {
                format!(
                    "Learned (score={:.1}, conf={:.2}, with={}, without={})",
                    score, confidence, with_period, without_period
                )
            }
        }
    }
}

/// Default decision weights for sentence boundary detection.
///
/// NOTE: These are NOT learned from data but are hand-tuned defaults.
/// Future versions may implement weight learning/optimization.
/// Models can override these defaults by storing custom weights.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DecisionWeights {
    /// Weight for provided abbreviations at different PR values
    /// Index by PR * 10 (so PR=0.5 -> index 5)
    pub provided_abbrev_weights: Vec<f64>,

    /// Weight for learned abbreviations at different PR values  
    pub learned_abbrev_weights: Vec<f64>,

    /// Weight for capitalization at different PR values
    pub capital_weights: Vec<f64>,

    /// Weight for collocations at different PR values
    pub colloc_weights: Vec<f64>,

    /// Weight for sentence starters at different PR values
    pub starter_weights: Vec<f64>,

    /// Weight for lowercase next token at different PR values
    pub lowercase_next_weights: Vec<f64>,

    /// Multiplier for sentence starter ratio weight at different PR values
    pub starter_ratio_multipliers: Vec<f64>,

    /// Weight for positive orthographic evidence at different PR values
    pub ortho_positive_weights: Vec<f64>,

    /// Weight for negative orthographic evidence at different PR values
    pub ortho_negative_weights: Vec<f64>,

    /// Threshold for breaking at different PR values
    pub break_thresholds: Vec<f64>,
}

impl Default for DecisionWeights {
    fn default() -> Self {
        // Hand-tuned default weights calibrated for legal text
        // These are NOT learned but manually optimized through testing
        Self {
            // 11 values for PR from 0.0 to 1.0 in 0.1 increments
            // Calibrated so PR=0.5 behaves like old PR=0.3 for legal text
            // At PR=0.5: -0.63 (balanced protection for legal abbreviations)
            // Strengthened to ensure provided abbreviations are protected even with capitalization
            provided_abbrev_weights: vec![
                -0.70, -0.72, -0.74, -0.76, -0.78, -0.80, -0.82, -0.84, -0.86, -0.88, -0.90,
            ],
            learned_abbrev_weights: vec![
                -0.1, -0.15, -0.2, -0.25, -0.3, -0.35, -0.4, -0.45, -0.5, -0.55, -0.6,
            ],
            // Reduced capital weights to prevent breaking after abbreviations
            capital_weights: vec![
                0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36, 0.38, 0.40,
            ],
            colloc_weights: vec![
                -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.75, -0.8, -0.85, -0.9, -0.95,
            ],
            starter_weights: vec![0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1],
            // Lowercase next token weights: -0.05 - 0.2 * pr
            // At PR=0.0: -0.05, At PR=1.0: -0.25
            lowercase_next_weights: vec![
                -0.05, -0.07, -0.09, -0.11, -0.13, -0.15, -0.17, -0.19, -0.21, -0.23, -0.25,
            ],
            // Sentence starter ratio multipliers: 0.4 * (1.0 - 0.3 * pr)
            // At PR=0.0: 0.4, At PR=1.0: 0.28
            starter_ratio_multipliers: vec![
                0.400, 0.388, 0.376, 0.364, 0.352, 0.340, 0.328, 0.316, 0.304, 0.292, 0.280,
            ],
            // Orthographic positive weights: 0.3 * (1.0 - 0.3 * pr)
            // At PR=0.0: 0.3, At PR=1.0: 0.21
            ortho_positive_weights: vec![
                0.300, 0.291, 0.282, 0.273, 0.264, 0.255, 0.246, 0.237, 0.228, 0.219, 0.210,
            ],
            // Orthographic negative weights: -0.2 - 0.15 * pr
            // At PR=0.0: -0.2, At PR=1.0: -0.35
            ortho_negative_weights: vec![
                -0.20, -0.215, -0.23, -0.245, -0.26, -0.275, -0.29, -0.305, -0.32, -0.335, -0.35,
            ],
            // Aggressive thresholds optimized for legal text
            // At PR=0.0: -0.60 (break very easily - target: 10-12 sentences)
            // Calibrated so PR=0.5 produces 9-11 sentences for legal text
            // At PR=0.0: -0.30 (very aggressive breaking)
            // At PR=0.5: -0.10 (balanced - allows some abbreviations to break)
            // At PR=1.0: 0.10 (conservative)
            // Must be monotonically increasing
            break_thresholds: vec![
                -0.30, -0.26, -0.22, -0.18, -0.14, -0.10, -0.06, -0.02, 0.02, 0.06, 0.10,
            ],
        }
    }
}

impl DecisionWeights {
    /// Get weight for a given PR value (0.0 to 1.0)
    #[inline(always)]
    pub fn get_weight(&self, weights: &[f64], pr: f64) -> f64 {
        let pr = pr.clamp(0.0, 1.0);
        let index = (pr * 10.0).round() as usize;
        let index = index.min(weights.len() - 1);
        weights[index]
    }

    /// Get provided abbreviation weight for PR
    #[inline]
    pub fn provided_abbrev_weight(&self, pr: f64) -> f64 {
        self.get_weight(&self.provided_abbrev_weights, pr)
    }

    /// Get learned abbreviation weight for PR
    #[inline]
    pub fn learned_abbrev_weight(&self, pr: f64) -> f64 {
        self.get_weight(&self.learned_abbrev_weights, pr)
    }

    /// Get capitalization weight for PR
    #[inline]
    pub fn capital_weight(&self, pr: f64) -> f64 {
        self.get_weight(&self.capital_weights, pr)
    }

    /// Get collocation weight for PR
    #[inline]
    pub fn colloc_weight(&self, pr: f64) -> f64 {
        self.get_weight(&self.colloc_weights, pr)
    }

    /// Get sentence starter weight for PR
    #[inline]
    pub fn starter_weight(&self, pr: f64) -> f64 {
        self.get_weight(&self.starter_weights, pr)
    }

    /// Get lowercase next token weight for PR
    #[inline]
    pub fn lowercase_next_weight(&self, pr: f64) -> f64 {
        self.get_weight(&self.lowercase_next_weights, pr)
    }

    /// Get sentence starter ratio multiplier for PR
    #[inline]
    pub fn starter_ratio_multiplier(&self, pr: f64) -> f64 {
        self.get_weight(&self.starter_ratio_multipliers, pr)
    }

    /// Get orthographic positive weight for PR
    #[inline]
    pub fn ortho_positive_weight(&self, pr: f64) -> f64 {
        self.get_weight(&self.ortho_positive_weights, pr)
    }

    /// Get orthographic negative weight for PR
    #[inline]
    pub fn ortho_negative_weight(&self, pr: f64) -> f64 {
        self.get_weight(&self.ortho_negative_weights, pr)
    }

    /// Get break threshold for PR
    #[inline]
    pub fn break_threshold(&self, pr: f64) -> f64 {
        self.get_weight(&self.break_thresholds, pr)
    }
}

/// Statistics for individual tokens
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TokenStats {
    /// Count of times token appears with period
    pub count_with_period: u32,
    /// Count of times token appears without period
    pub count_without_period: u32,
    /// Count of times token starts a sentence
    pub count_as_starter: u32,
    /// Collocation counts with following tokens
    pub collocation_counts: HashMap<String, u32>,
}

impl Default for TokenStats {
    fn default() -> Self {
        Self::new()
    }
}

impl TokenStats {
    pub fn new() -> Self {
        Self {
            count_with_period: 0,
            count_without_period: 0,
            count_as_starter: 0,
            collocation_counts: HashMap::new(),
        }
    }
}

/// Punkt parameters containing learned data for sentence boundary detection
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PunktParameters {
    /// Abbreviations with their source information (provided vs learned)
    pub abbrev_types: HashMap<String, AbbreviationType>,

    /// Set of collocations (word pairs that span sentence boundaries)
    pub collocations: HashSet<(String, String)>,

    /// Set of sentence starters
    pub sent_starters: HashSet<String>,

    /// Orthographic context for each token type
    pub ortho_context: HashMap<String, u32>,

    /// Token statistics for scoring
    pub token_stats: HashMap<String, TokenStats>,

    /// Total count of tokens with periods
    pub total_period_tokens: u32,

    /// Total count of all tokens
    pub total_tokens: u32,

    /// Decision weights for sentence boundary detection
    /// These default to hand-tuned values but can be overridden by models
    #[serde(default)]
    pub decision_weights: DecisionWeights,

    /// Frozen sets for faster lookups (not serialized)
    #[serde(skip)]
    frozen_abbrev_types: Option<Arc<AHashSet<String>>>,

    #[serde(skip)]
    frozen_collocations: Option<Arc<AHashSet<(String, String)>>>,

    #[serde(skip)]
    frozen_sent_starters: Option<Arc<AHashSet<String>>>,
}

impl PunktParameters {
    /// Create new empty parameters
    pub fn new() -> Self {
        Self {
            abbrev_types: HashMap::new(),
            collocations: HashSet::new(),
            sent_starters: HashSet::new(),
            ortho_context: HashMap::new(),
            token_stats: HashMap::new(),
            total_period_tokens: 0,
            total_tokens: 0,
            decision_weights: DecisionWeights::default(),
            frozen_abbrev_types: None,
            frozen_collocations: None,
            frozen_sent_starters: None,
        }
    }

    /// Add a provided abbreviation (from external source)
    pub fn add_provided_abbreviation(
        &mut self,
        abbrev: impl Into<String>,
        source: impl Into<String>,
    ) {
        let abbrev_str = abbrev.into();
        // Remove trailing period if present
        let clean = if abbrev_str.ends_with('.') {
            abbrev_str[..abbrev_str.len() - 1].to_string()
        } else {
            abbrev_str
        };

        // CRITICAL: Convert to lowercase to match token_type (which is always lowercase)
        let clean = clean.to_lowercase();

        self.abbrev_types.insert(
            clean.clone(),
            AbbreviationType::Provided {
                source: source.into(),
                added_at: self.total_tokens as usize,
            },
        );
        self.frozen_abbrev_types = None; // Invalidate frozen set
    }

    /// Add a learned abbreviation (from statistical analysis)
    pub fn add_learned_abbreviation(
        &mut self,
        abbrev: impl Into<String>,
        score: f64,
        with_period: usize,
        without_period: usize,
    ) {
        let abbrev_str = abbrev.into();
        // CRITICAL: Convert to lowercase to match token_type
        let abbrev_str = abbrev_str.to_lowercase();

        // Don't override provided abbreviations
        if let Some(existing) = self.abbrev_types.get(&abbrev_str) {
            if existing.is_provided() {
                return; // Never override provided with learned
            }
        }

        // Calculate confidence based on evidence
        let total = with_period + without_period;
        let ratio = if total > 0 {
            with_period as f64 / total as f64
        } else {
            0.0
        };
        let confidence = if total < 10 {
            ratio * 0.5 // Low confidence for rare tokens
        } else if ratio > 0.9 {
            0.9 + (score / 100.0).min(0.1) // High confidence for consistent usage
        } else {
            ratio * 0.7 // Medium confidence otherwise
        };

        self.abbrev_types.insert(
            abbrev_str.clone(),
            AbbreviationType::Learned {
                score,
                with_period,
                without_period,
                confidence,
            },
        );
        self.frozen_abbrev_types = None;
    }

    /// Add an abbreviation (legacy method for compatibility)
    pub fn add_abbreviation(&mut self, abbrev: impl Into<String>) {
        // Default to learned with minimal info for backward compatibility
        self.add_learned_abbreviation(abbrev, 10.0, 10, 1);
    }

    /// Add a collocation
    pub fn add_collocation(&mut self, first: impl Into<String>, second: impl Into<String>) {
        // Convert to lowercase to match token_type
        let first = first.into().to_lowercase();
        let second = second.into().to_lowercase();
        self.collocations.insert((first, second));
        self.frozen_collocations = None;
    }

    /// Add a sentence starter
    pub fn add_sent_starter(&mut self, starter: impl Into<String>) {
        self.sent_starters.insert(starter.into());
        self.frozen_sent_starters = None;
    }

    /// Add orthographic context for a token type
    pub fn add_ortho_context(&mut self, token_type: impl Into<String>, flag: u32) {
        let token_type = token_type.into();
        *self.ortho_context.entry(token_type).or_insert(0) |= flag;
    }

    /// Check if a token is ANY kind of abbreviation
    #[inline]
    pub fn is_abbreviation(&self, token: &str) -> bool {
        // Normalize to lowercase for case-insensitive matching
        let normalized = token.to_lowercase();
        
        // Try the thread-local cache first
        ABBREV_CACHE.with(|cache| {
            let mut cache = cache.borrow_mut();
            
            // Check if we have a cached result
            if let Some(&cached_result) = cache.get(&normalized) {
                return cached_result;
            }
            
            // Cache miss - do the actual lookup
            let result = if let Some(frozen) = &self.frozen_abbrev_types {
                frozen.contains(&normalized)
            } else {
                self.abbrev_types.contains_key(&normalized)
            };
            
            // Store in cache for next time
            cache.put(normalized, result);
            result
        })
    }

    /// Check if a token is a PROVIDED abbreviation (critical for training)
    #[inline]
    pub fn is_provided_abbreviation(&self, token: &str) -> bool {
        // Normalize to lowercase for case-insensitive matching
        let normalized = token.to_lowercase();
        self.abbrev_types
            .get(&normalized)
            .map(|t| t.is_provided())
            .unwrap_or(false)
    }

    /// Get abbreviation type for a token
    #[inline]
    pub fn get_abbreviation_type(&self, token: &str) -> Option<&AbbreviationType> {
        // Normalize to lowercase for case-insensitive matching
        let normalized = token.to_lowercase();
        
        // Note: We can't easily cache references, so we check the cache
        // to see if the key exists, but still return the actual reference
        // This at least saves the normalization step on cache hits
        ABBREV_CACHE.with(|cache| {
            let mut cache = cache.borrow_mut();
            
            // Update cache with whether this abbreviation exists
            if !cache.contains(&normalized) {
                let exists = self.abbrev_types.contains_key(&normalized);
                cache.put(normalized.clone(), exists);
            }
        });
        
        self.abbrev_types.get(&normalized)
    }

    /// Clear thread-local caches (useful when parameters change)
    pub fn clear_caches() {
        ABBREV_CACHE.with(|cache| cache.borrow_mut().clear());
        ABBREV_TYPE_CACHE.with(|cache| cache.borrow_mut().clear());
    }
    
    /// Check if a pair is a collocation
    #[inline]
    pub fn is_collocation(&self, first: &str, second: &str) -> bool {
        // Normalize to lowercase for case-insensitive matching
        let pair = (first.to_lowercase(), second.to_lowercase());
        if let Some(frozen) = &self.frozen_collocations {
            frozen.contains(&pair)
        } else {
            self.collocations.contains(&pair)
        }
    }

    /// Check if a token is a sentence starter
    pub fn is_sent_starter(&self, token: &str) -> bool {
        // Note: sentence starters are stored in their original case
        // as capitalization matters for starters
        if let Some(frozen) = &self.frozen_sent_starters {
            frozen.contains(token)
        } else {
            self.sent_starters.contains(token)
        }
    }

    /// Get orthographic context for a token type
    pub fn get_ortho_context(&self, token_type: &str) -> u32 {
        self.ortho_context.get(token_type).copied().unwrap_or(0)
    }

    /// Get token statistics
    #[inline]
    pub fn get_token_stats(&self, token_type: &str) -> Option<&TokenStats> {
        self.token_stats.get(token_type)
    }

    /// Add or update token statistics
    pub fn update_token_stats(
        &mut self,
        token_type: impl Into<String>,
        update_fn: impl FnOnce(&mut TokenStats),
    ) {
        let token_type = token_type.into();
        let stats = self.token_stats.entry(token_type).or_default();
        update_fn(stats);
    }

    /// Freeze sets for faster lookups during inference
    pub fn freeze(&mut self) {
        // Extract just the keys from the HashMap for the frozen set
        self.frozen_abbrev_types = Some(Arc::new(self.abbrev_types.keys().cloned().collect()));
        self.frozen_collocations = Some(Arc::new(self.collocations.iter().cloned().collect()));
        self.frozen_sent_starters = Some(Arc::new(self.sent_starters.iter().cloned().collect()));
    }

    /// Load parameters from JSON string
    pub fn from_json(json: &str) -> Result<Self, serde_json::Error> {
        let mut params: Self = serde_json::from_str(json)?;
        params.freeze(); // Freeze sets for performance
        Ok(params)
    }

    /// Save parameters to JSON string
    pub fn to_json(&self) -> Result<String, serde_json::Error> {
        serde_json::to_string(self)
    }

    /// Save parameters to compressed JSON
    pub fn save_compressed(&self, path: &str) -> Result<()> {
        use flate2::write::GzEncoder;
        use flate2::Compression;
        use std::fs::File;
        use std::io::Write;

        let json = self.to_json().context("Failed to serialize to JSON")?;
        let file =
            File::create(path).with_context(|| format!("Failed to create file: {}", path))?;
        let mut encoder = GzEncoder::new(file, Compression::default());
        encoder
            .write_all(json.as_bytes())
            .context("Failed to write compressed data")?;
        encoder.finish().context("Failed to finish compression")?;
        Ok(())
    }

    /// Load parameters from compressed JSON
    pub fn load_compressed(path: &str) -> Result<Self> {
        use flate2::read::GzDecoder;
        use std::fs::File;
        use std::io::Read;

        let file = File::open(path).with_context(|| format!("Failed to open file: {}", path))?;
        let mut decoder = GzDecoder::new(file);
        let mut json = String::new();
        decoder
            .read_to_string(&mut json)
            .context("Failed to decompress data")?;

        let mut params = Self::from_json(&json).context("Failed to parse JSON")?;
        params.freeze();
        Ok(params)
    }

    /// Load parameters from compressed bytes (for embedded models)
    pub fn from_compressed_bytes(bytes: &[u8]) -> Result<Self> {
        use flate2::read::GzDecoder;
        use std::io::Read;

        let mut decoder = GzDecoder::new(bytes);
        let mut json = String::new();
        decoder
            .read_to_string(&mut json)
            .context("Failed to decompress data")?;

        let mut params = Self::from_json(&json).context("Failed to parse JSON")?;
        params.freeze();
        Ok(params)
    }

    /// Filter token statistics to reduce model size
    ///
    /// This removes rare tokens to significantly reduce model size
    /// while preserving quality. Abbreviations are never filtered.
    ///
    /// Returns (original_token_count, filtered_token_count)
    pub fn filter_tokens(
        &mut self,
        min_frequency: usize,
        max_tokens: Option<usize>,
        verbose: bool,
    ) -> (usize, usize) {
        let original_count = self.token_stats.len();

        if verbose {
            eprintln!("Filtering tokens from {} entries...", original_count);
        }

        // Build frequency map
        let mut token_frequencies: Vec<(String, usize)> = Vec::new();

        for (token, stats) in &self.token_stats {
            // Calculate total frequency
            let frequency = stats.count_with_period as usize
                + stats.count_without_period as usize
                + stats.count_as_starter as usize;

            // Skip rare tokens
            if frequency < min_frequency {
                continue;
            }

            token_frequencies.push((token.clone(), frequency));
        }

        // Sort by frequency and limit if max_tokens specified
        token_frequencies.sort_by(|a, b| b.1.cmp(&a.1));

        if let Some(max) = max_tokens {
            token_frequencies.truncate(max);
        }

        // Build set of tokens to keep
        let tokens_to_keep: HashSet<String> = token_frequencies
            .into_iter()
            .map(|(token, _)| token)
            .collect();

        // Filter token_stats
        let mut filtered_stats = HashMap::new();
        for (token, mut stats) in self.token_stats.drain() {
            if tokens_to_keep.contains(&token) {
                // Also filter collocation counts to only include kept tokens
                let mut filtered_collocations = HashMap::new();
                for (colloc_token, count) in stats.collocation_counts {
                    if tokens_to_keep.contains(&colloc_token) {
                        filtered_collocations.insert(colloc_token, count);
                    }
                }
                stats.collocation_counts = filtered_collocations;
                filtered_stats.insert(token, stats);
            }
        }
        self.token_stats = filtered_stats;

        // Filter ortho_context to match
        let mut filtered_ortho = HashMap::new();
        for (token, value) in self.ortho_context.drain() {
            if tokens_to_keep.contains(&token) {
                filtered_ortho.insert(token, value);
            }
        }
        self.ortho_context = filtered_ortho;

        let filtered_count = self.token_stats.len();

        if verbose {
            eprintln!(
                "  Kept {} tokens ({:.1}% reduction)",
                filtered_count,
                (1.0 - filtered_count as f64 / original_count as f64) * 100.0
            );
        }

        // Invalidate frozen sets since we modified the data
        self.frozen_abbrev_types = None;
        self.frozen_collocations = None;
        self.frozen_sent_starters = None;

        (original_count, filtered_count)
    }
}

impl Default for PunktParameters {
    fn default() -> Self {
        Self::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_provided_abbreviation_creation() {
        let mut params = PunktParameters::new();

        // Add a provided abbreviation
        params.add_provided_abbreviation("Mr", "test.json");

        // Check it exists and is marked as provided
        assert!(params.is_abbreviation("Mr"));
        assert!(params.is_provided_abbreviation("Mr"));

        // Check the type
        let abbrev_type = params.get_abbreviation_type("Mr").unwrap();
        assert!(abbrev_type.is_provided());
        assert_eq!(abbrev_type.confidence(), 1.0);
    }

    #[test]
    fn test_learned_abbreviation_creation() {
        let mut params = PunktParameters::new();

        // Add a learned abbreviation
        params.add_learned_abbreviation("Dr", 15.5, 50, 10);

        // Check it exists but is NOT provided
        assert!(params.is_abbreviation("Dr"));
        assert!(!params.is_provided_abbreviation("Dr"));

        // Check the type
        let abbrev_type = params.get_abbreviation_type("Dr").unwrap();
        assert!(!abbrev_type.is_provided());
        assert!(abbrev_type.confidence() < 1.0);
    }

    #[test]
    fn test_provided_not_overridden() {
        let mut params = PunktParameters::new();

        // First add as provided
        params.add_provided_abbreviation("Inc", "external.json");
        assert!(params.is_provided_abbreviation("Inc"));

        // Try to override with learned - should be ignored
        params.add_learned_abbreviation("Inc", 10.0, 20, 5);

        // Should still be provided
        assert!(params.is_provided_abbreviation("Inc"));
    }

    #[test]
    fn test_abbreviation_weights() {
        // Test that provided abbreviations get stronger weights
        let provided = AbbreviationType::Provided {
            source: "test".to_string(),
            added_at: 0,
        };

        let learned = AbbreviationType::Learned {
            score: 10.0,
            with_period: 50,
            without_period: 10,
            confidence: 0.8,
        };

        // Use default weights
        let weights = DecisionWeights::default();

        // At PR=0.3
        let pr = 0.3;
        let provided_weight = provided.get_weight(pr, &weights);
        let learned_weight = learned.get_weight(pr, &weights);

        // Provided should have stronger negative weight (more negative)
        assert!(provided_weight < learned_weight);
        assert!(provided_weight < -0.3); // Check it's negative
        assert!(learned_weight < 0.0); // Also negative but weaker
    }

    #[test]
    fn test_period_removal_in_provided() {
        let mut params = PunktParameters::new();

        // Add with trailing period
        params.add_provided_abbreviation("U.S.", "test.json");

        // Should be stored without the trailing period
        assert!(params.is_abbreviation("U.S"));
        assert!(params.is_provided_abbreviation("U.S"));

        // But not with the period
        assert!(!params.is_abbreviation("U.S."));
    }

    #[test]
    fn test_confidence_calculation() {
        let mut params = PunktParameters::new();

        // Rare token (< 10 occurrences)
        params.add_learned_abbreviation("rare", 5.0, 3, 2);

        if let Some(AbbreviationType::Learned { confidence, .. }) =
            params.get_abbreviation_type("rare")
        {
            // Should have low confidence (ratio * 0.5)
            assert!(*confidence <= 0.5);
        }

        // Consistent token (high ratio)
        params.add_learned_abbreviation("consistent", 50.0, 95, 5);

        if let Some(AbbreviationType::Learned { confidence, .. }) =
            params.get_abbreviation_type("consistent")
        {
            // Should have high confidence (> 0.9)
            assert!(*confidence > 0.9);
        }
    }
}

/// Python wrapper for PunktParameters
#[pyclass(name = "Parameters")]
#[derive(Clone)]
pub struct PyParameters {
    pub inner: Arc<PunktParameters>,
}

#[pymethods]
impl PyParameters {
    /// Create new empty parameters
    #[new]
    fn new() -> Self {
        Self {
            inner: Arc::new(PunktParameters::new()),
        }
    }

    /// Get the number of abbreviations
    #[getter]
    fn num_abbreviations(&self) -> usize {
        self.inner.abbrev_types.len()
    }

    /// Get the number of collocations
    #[getter]
    fn num_collocations(&self) -> usize {
        self.inner.collocations.len()
    }

    /// Get the number of sentence starters
    #[getter]
    fn num_sent_starters(&self) -> usize {
        self.inner.sent_starters.len()
    }

    /// Get abbreviations as a list
    #[getter]
    fn abbreviations(&self) -> Vec<String> {
        // Extract just the keys (abbreviation strings) from the HashMap
        self.inner.abbrev_types.keys().cloned().collect()
    }

    /// Get collocations as a list of tuples
    #[getter]
    fn collocations(&self) -> Vec<(String, String)> {
        self.inner.collocations.iter().cloned().collect()
    }

    /// Get sentence starters as a list
    #[getter]
    fn sent_starters(&self) -> Vec<String> {
        self.inner.sent_starters.iter().cloned().collect()
    }

    /// Save parameters to a file
    fn save(&self, path: &str) -> PyResult<()> {
        self.inner
            .save_compressed(path)
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyIOError, _>(e.to_string()))
    }

    /// Load parameters from a file
    #[staticmethod]
    fn load(path: &str) -> PyResult<Self> {
        PunktParameters::load_compressed(path)
            .map(|params| Self {
                inner: Arc::new(params),
            })
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyIOError, _>(e.to_string()))
    }

    /// Convert to JSON string
    fn to_json(&self) -> PyResult<String> {
        self.inner
            .to_json()
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))
    }

    /// Create from JSON string
    #[staticmethod]
    fn from_json(json: &str) -> PyResult<Self> {
        PunktParameters::from_json(json)
            .map(|params| Self {
                inner: Arc::new(params),
            })
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))
    }

    /// Get the decision weights at a specific PR value
    #[pyo3(signature = (pr))]
    fn get_weights_at_pr(&self, pr: f64) -> PyResult<Vec<(String, f64)>> {
        let weights = &self.inner.decision_weights;
        let result = vec![
            (
                "provided_abbrev".to_string(),
                weights.provided_abbrev_weight(pr),
            ),
            (
                "learned_abbrev".to_string(),
                weights.learned_abbrev_weight(pr),
            ),
            ("capital".to_string(), weights.capital_weight(pr)),
            ("collocation".to_string(), weights.colloc_weight(pr)),
            ("starter".to_string(), weights.starter_weight(pr)),
            ("threshold".to_string(), weights.break_threshold(pr)),
        ];
        Ok(result)
    }

    /// Get all decision weights as lists
    #[getter]
    fn decision_weights(&self) -> PyResult<Vec<(String, Vec<f64>)>> {
        let weights = &self.inner.decision_weights;
        let result = vec![
            (
                "provided_abbrev_weights".to_string(),
                weights.provided_abbrev_weights.clone(),
            ),
            (
                "learned_abbrev_weights".to_string(),
                weights.learned_abbrev_weights.clone(),
            ),
            (
                "capital_weights".to_string(),
                weights.capital_weights.clone(),
            ),
            ("colloc_weights".to_string(), weights.colloc_weights.clone()),
            (
                "starter_weights".to_string(),
                weights.starter_weights.clone(),
            ),
            (
                "break_thresholds".to_string(),
                weights.break_thresholds.clone(),
            ),
        ];
        Ok(result)
    }

    /// Set decision weights (creates a new Parameters object)
    #[pyo3(signature = (provided_abbrev_weights=None, learned_abbrev_weights=None, capital_weights=None, colloc_weights=None, starter_weights=None, break_thresholds=None))]
    fn with_weights(
        &self,
        provided_abbrev_weights: Option<Vec<f64>>,
        learned_abbrev_weights: Option<Vec<f64>>,
        capital_weights: Option<Vec<f64>>,
        colloc_weights: Option<Vec<f64>>,
        starter_weights: Option<Vec<f64>>,
        break_thresholds: Option<Vec<f64>>,
    ) -> PyResult<Self> {
        let mut params = (*self.inner).clone();

        if let Some(w) = provided_abbrev_weights {
            if w.len() != 11 {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    "Weights must have exactly 11 values (for PR 0.0 to 1.0 in 0.1 increments)",
                ));
            }
            params.decision_weights.provided_abbrev_weights = w;
        }

        if let Some(w) = learned_abbrev_weights {
            if w.len() != 11 {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    "Weights must have exactly 11 values",
                ));
            }
            params.decision_weights.learned_abbrev_weights = w;
        }

        if let Some(w) = capital_weights {
            if w.len() != 11 {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    "Weights must have exactly 11 values",
                ));
            }
            params.decision_weights.capital_weights = w;
        }

        if let Some(w) = colloc_weights {
            if w.len() != 11 {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    "Weights must have exactly 11 values",
                ));
            }
            params.decision_weights.colloc_weights = w;
        }

        if let Some(w) = starter_weights {
            if w.len() != 11 {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    "Weights must have exactly 11 values",
                ));
            }
            params.decision_weights.starter_weights = w;
        }

        if let Some(w) = break_thresholds {
            if w.len() != 11 {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    "Weights must have exactly 11 values",
                ));
            }
            params.decision_weights.break_thresholds = w;
        }

        Ok(Self {
            inner: Arc::new(params),
        })
    }
}
