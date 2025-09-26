/// Token representation for Punkt algorithm
use once_cell::sync::Lazy;
use regex::Regex;

/// Compiled regex patterns for token analysis
static RE_NUMBER: Lazy<Regex> = Lazy::new(|| Regex::new(r"^-?[\.,]?\d[\d,\.-]*\.?$").unwrap());

static RE_ELLIPSIS: Lazy<Regex> = Lazy::new(|| Regex::new(r"\.\.+$").unwrap());

static RE_INITIAL: Lazy<Regex> = Lazy::new(|| Regex::new(r"^[^\W\d]\.$").unwrap());

static RE_ALPHA: Lazy<Regex> = Lazy::new(|| Regex::new(r"^[^\W\d]+$").unwrap());

/// A token in the Punkt algorithm
#[derive(Debug, Clone)]
pub struct PunktToken {
    /// The token text
    pub tok: String,

    /// Whether this token starts a paragraph
    pub parastart: bool,

    /// Whether this token starts a line
    pub linestart: bool,

    /// Whether this token ends a sentence
    pub sentbreak: bool,

    /// Whether this token is an abbreviation
    pub abbr: bool,

    /// Whether this token is an ellipsis
    pub ellipsis: bool,

    /// Whether the token ends with a period
    pub period_final: bool,

    /// Whether the token ends with an exclamation mark
    pub exclamation_final: bool,

    /// Whether the token ends with a question mark
    pub question_final: bool,

    /// Whether the token ends with a semicolon
    pub semicolon_final: bool,

    /// Whether the token ends with sentence-ending punctuation (. ! ?)
    pub sentence_end_punct: bool,

    /// The normalized token type
    pub token_type: String,

    /// Whether this is a valid abbreviation candidate
    pub valid_abbrev_candidate: bool,

    /// Number of spaces after this token (0, 1, 2+)
    pub spaces_after: u8,

    /// Whether there's a newline after this token
    pub has_newline_after: bool,

    /// Character position in original text (if known)
    pub char_position: Option<usize>,
    
    /// Byte position in original text (if known)
    pub byte_position: Option<usize>,

    // Cached properties
    first_upper: bool,
    first_lower: bool,
}

impl PunktToken {
    /// Create a new PunktToken
    pub fn new(tok: impl Into<String>, parastart: bool, linestart: bool) -> Self {
        let tok = tok.into();
        let period_final = tok.ends_with('.');
        let exclamation_final = tok.ends_with('!');
        let question_final = tok.ends_with('?');
        let semicolon_final = tok.ends_with(';');
        let sentence_end_punct = period_final || exclamation_final || question_final;
        let token_type = Self::get_token_type(&tok);

        let first_char = tok.chars().next();
        let first_upper = first_char.is_some_and(|c| c.is_uppercase());
        let first_lower = first_char.is_some_and(|c| c.is_lowercase());

        // Check if it's a valid abbreviation candidate
        let valid_abbrev_candidate = if period_final {
            let has_alpha = tok.chars().any(|c| c.is_alphabetic());
            let alpha_count = tok.chars().filter(|c| c.is_alphabetic()).count();
            let digit_count = tok.chars().filter(|c| c.is_numeric()).count();

            has_alpha && token_type != "##number##" && alpha_count >= digit_count && tok.len() <= 10
        // Max abbreviation length
        } else {
            false
        };

        Self {
            tok,
            parastart,
            linestart,
            sentbreak: false,
            abbr: false,
            ellipsis: false,
            period_final,
            exclamation_final,
            question_final,
            semicolon_final,
            sentence_end_punct,
            token_type,
            valid_abbrev_candidate,
            spaces_after: 1, // Default to single space
            has_newline_after: false,
            char_position: None,
            byte_position: None,
            first_upper,
            first_lower,
        }
    }

    /// Get the normalized token type
    fn get_token_type(tok: &str) -> String {
        // Fast path for simple numbers
        if !tok.is_empty() && tok.chars().all(|c| c.is_ascii_digit()) {
            return "##number##".to_string();
        }
        
        // Fast path for obviously non-numeric tokens
        if tok.chars().any(|c| c.is_alphabetic() && !c.is_ascii_digit()) {
            return tok.to_lowercase();
        }
        
        // Use regex for complex number patterns (decimals, negatives, etc.)
        if RE_NUMBER.is_match(tok) {
            "##number##".to_string()
        } else {
            tok.to_lowercase()
        }
    }

    /// Get the token type without a trailing period
    #[inline]
    pub fn type_no_period(&self) -> String {
        if self.token_type.ends_with('.') && self.token_type.len() > 1 {
            self.token_type[..self.token_type.len() - 1].to_string()
        } else {
            self.token_type.clone()
        }
    }

    /// Get the token type without any sentence-ending punctuation (. ! ?)
    #[inline]
    pub fn type_no_sentence_punct(&self) -> String {
        if self.token_type.len() > 1 {
            if self.token_type.ends_with('.')
                || self.token_type.ends_with('!')
                || self.token_type.ends_with('?')
            {
                self.token_type[..self.token_type.len() - 1].to_string()
            } else {
                self.token_type.clone()
            }
        } else {
            self.token_type.clone()
        }
    }

    /// Get the token type without a sentence-final period
    #[inline]
    pub fn type_no_sentperiod(&self) -> String {
        if self.sentbreak {
            self.type_no_period()
        } else {
            self.token_type.clone()
        }
    }

    /// Check if the first character is uppercase
    #[inline]
    pub fn first_upper(&self) -> bool {
        self.first_upper
    }

    /// Check if the first character is lowercase
    #[inline]
    pub fn first_lower(&self) -> bool {
        self.first_lower
    }

    /// Check if the token is an ellipsis
    #[inline]
    pub fn is_ellipsis(&self) -> bool {
        // Fast path for common ellipsis patterns
        match self.tok.as_str() {
            "..." | ".." | "\u{2026}" => true,
            _ if self.tok.ends_with("\u{2026}") => true,
            _ if self.tok.len() >= 2 && self.tok.ends_with("..") => RE_ELLIPSIS.is_match(&self.tok),
            _ => false,
        }
    }

    /// Check if the token is a number
    #[inline]
    pub fn is_number(&self) -> bool {
        self.token_type == "##number##"
    }

    /// Check if the token is an initial (e.g., "J.")
    #[inline]
    pub fn is_initial(&self) -> bool {
        // Fast path: initials are typically 2 chars (letter + period)
        if self.tok.len() == 2 && self.tok.ends_with('.') {
            if let Some(first) = self.tok.chars().next() {
                if first.is_alphabetic() && !first.is_numeric() {
                    return true;
                }
            }
        }
        // Fallback to regex for edge cases
        RE_INITIAL.is_match(&self.tok)
    }

    /// Check if the token is alphabetic
    #[inline]
    pub fn is_alpha(&self) -> bool {
        // Fast path: check if all chars are alphabetic
        if !self.tok.is_empty() && self.tok.chars().all(|c| c.is_alphabetic()) {
            return true;
        }
        // Fallback to regex for Unicode edge cases
        RE_ALPHA.is_match(&self.tok)
    }

    /// Check if the token contains non-punctuation
    #[inline]
    pub fn is_non_punct(&self) -> bool {
        self.tok.chars().any(|c| c.is_alphanumeric())
    }
}
