/// Core traits and types for nupunkt-rs
/// Trait for tokenizers that can split text into sentences
pub trait SentenceTokenizer: Send + Sync {
    /// Tokenize text into sentences
    fn tokenize(&self, text: &str) -> Vec<String>;

    /// Tokenize text and return sentence boundaries as character spans
    fn tokenize_spans(&self, text: &str) -> Vec<(usize, usize)>;

    /// Check if a position in text is a sentence boundary
    fn is_sentence_boundary(&self, text: &str, pos: usize) -> bool;
}

/// Trait for scoring potential abbreviations
pub trait AbbreviationScorer: Send + Sync {
    /// Calculate abbreviation score using Dunning log-likelihood
    fn score_abbreviation(
        &self,
        count_with_period: usize,
        count_without_period: usize,
        total_period_tokens: usize,
        total_tokens: usize,
    ) -> f64;

    /// Check if a score exceeds the abbreviation threshold
    fn is_abbreviation(&self, score: f64) -> bool;
}

/// Trait for scoring collocations  
pub trait CollocationScorer: Send + Sync {
    /// Calculate collocation score
    fn score_collocation(
        &self,
        count_first: usize,
        count_second: usize,
        count_together: usize,
        total_tokens: usize,
    ) -> f64;

    /// Check if a score exceeds the collocation threshold
    fn is_collocation(&self, score: f64) -> bool;
}

/// Trait for scoring sentence starters
pub trait SentenceStarterScorer: Send + Sync {
    /// Calculate sentence starter score
    fn score_sentence_starter(
        &self,
        sentbreak_count: usize,
        token_count: usize,
        starter_count: usize,
        total_tokens: usize,
    ) -> f64;

    /// Check if a score exceeds the sentence starter threshold
    fn is_sentence_starter(&self, score: f64) -> bool;
}

/// Configuration for scoring thresholds
#[derive(Debug, Clone, serde::Serialize, serde::Deserialize)]
pub struct ScoringConfig {
    /// Threshold for abbreviation detection (default: 0.1)
    pub abbrev_threshold: f64,

    /// Boosting factor for abbreviation scores (default: 1.5)
    pub abbrev_boost: f64,

    /// Threshold for collocation detection (default: 5.0)
    pub collocation_threshold: f64,

    /// Threshold for sentence starter detection (default: 25.0)
    pub sent_starter_threshold: f64,

    /// Minimum frequency for collocations as a rate (default: 0.00001 = 1 per 100k tokens)
    /// Changed from absolute count to rate for corpus-size independence
    pub min_colloc_rate: f64,

    /// Maximum length for abbreviation candidates (default: 9)
    pub max_abbrev_length: usize,

    /// Consistency threshold for abbreviations (default: 0.25)
    pub abbrev_consistency: f64,

    /// Minimum rate for sentence starters (default: 0.00005 = 5 per 100k tokens)
    pub min_starter_rate: f64,

    /// Require sentence starters to be alphabetic (default: true)
    pub require_alpha_starters: bool,
}

impl Default for ScoringConfig {
    fn default() -> Self {
        Self {
            abbrev_threshold: 0.1,
            abbrev_boost: 1.5,
            collocation_threshold: 5.0,
            sent_starter_threshold: 25.0,
            min_colloc_rate: 0.00001, // 1 per 100k tokens
            max_abbrev_length: 9,
            abbrev_consistency: 0.25,
            min_starter_rate: 0.00005, // 5 per 100k tokens
            require_alpha_starters: true,
        }
    }
}

/// Orthographic context flags
pub const ORTHO_BEG_UC: u32 = 1 << 1; // Uppercase at sentence beginning
pub const ORTHO_MID_UC: u32 = 1 << 2; // Uppercase mid-sentence
pub const ORTHO_UNK_UC: u32 = 1 << 3; // Unknown position uppercase
pub const ORTHO_BEG_LC: u32 = 1 << 4; // Lowercase at sentence beginning
pub const ORTHO_MID_LC: u32 = 1 << 5; // Lowercase mid-sentence
pub const ORTHO_UNK_LC: u32 = 1 << 6; // Unknown position lowercase
pub const ORTHO_UC: u32 = ORTHO_BEG_UC | ORTHO_MID_UC | ORTHO_UNK_UC; // Any uppercase
pub const ORTHO_LC: u32 = ORTHO_BEG_LC | ORTHO_MID_LC | ORTHO_UNK_LC; // Any lowercase

/// Language-specific variables for customization
#[derive(Debug, Clone)]
pub struct LanguageVars {
    /// Characters that mark sentence endings
    pub sent_end_chars: Vec<char>,

    /// Regular expression pattern for word tokenization
    pub word_tokenize_pattern: String,

    /// Characters that can appear inside words
    pub internal_punctuation: Vec<char>,
}

impl Default for LanguageVars {
    fn default() -> Self {
        Self {
            sent_end_chars: vec!['.', '!', '?'],
            word_tokenize_pattern: r"\S+".to_string(),
            internal_punctuation: vec!['-', '\'', '"'],
        }
    }
}

/// Cache configuration for performance optimization
#[derive(Debug, Clone)]
pub struct CacheConfig {
    /// Size of the token cache
    pub token_cache_size: usize,

    /// Size of the orthographic context cache
    pub ortho_cache_size: usize,

    /// Size of the sentence starter cache
    pub sent_starter_cache_size: usize,
}

impl Default for CacheConfig {
    fn default() -> Self {
        Self {
            token_cache_size: 16000,
            ortho_cache_size: 8000,
            sent_starter_cache_size: 4000,
        }
    }
}
