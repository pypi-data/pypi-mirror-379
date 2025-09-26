/// Token analysis and scoring information
use pyo3::prelude::*;
use serde::{Deserialize, Serialize};
use crate::decision::FactorVec;

/// Detailed information about a token's scoring and decision
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TokenAnalysis {
    /// The token text
    pub text: String,

    /// Position in the original text
    pub position: usize,

    /// Length of the token
    pub length: usize,

    /// Whether the token ends with a period
    pub has_period: bool,

    /// Abbreviation score (if applicable)
    pub abbrev_score: Option<f64>,

    /// Whether it's in the abbreviation list
    pub in_abbrev_list: bool,

    /// Collocation score with next token (if applicable)
    pub collocation_score: Option<f64>,

    /// Whether it forms a collocation with the next token
    pub is_collocation: bool,

    /// Capitalization of next token
    pub next_is_capital: Option<bool>,

    /// Decision made for this token
    pub decision: BreakDecision,

    /// Confidence in the decision (0.0 to 1.0)
    pub confidence: f64,

    /// Primary reason for the decision
    pub primary_reason: String,

    /// All contributing factors
    pub factors: FactorVec,
}

/// Decision made at a token boundary
#[derive(Debug, Clone, Copy, PartialEq, Serialize, Deserialize)]
pub enum BreakDecision {
    /// Definitely break here
    Break,
    /// Definitely don't break here
    NoBreak,
    /// No period, continue
    Continue,
    /// Uncertain, use default
    Uncertain,
}

/// Factors contributing to a decision
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DecisionFactor {
    pub factor_type: FactorType,
    pub weight: f64,
    pub description: String,
}

#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub enum FactorType {
    Abbreviation,
    Collocation,
    Capitalization,
    SentenceStarter,
    Consistency,
    Score,
    EndOfText,
    Whitespace,
}

/// Result of analyzing a full text
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TextAnalysis {
    pub tokens: Vec<TokenAnalysis>,
    pub sentences: Vec<String>,
    pub break_positions: Vec<usize>,
    pub statistics: AnalysisStatistics,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AnalysisStatistics {
    pub total_tokens: usize,
    pub total_breaks: usize,
    pub abbreviations_found: usize,
    pub collocations_found: usize,
    pub average_confidence: f64,
    pub low_confidence_decisions: usize,
}

// Python bindings
/// Python wrapper for TokenAnalysis
#[pyclass(name = "TokenAnalysis")]
#[derive(Clone)]
pub struct PyTokenAnalysis {
    pub inner: TokenAnalysis,
}

#[pymethods]
impl PyTokenAnalysis {
    #[getter]
    fn text(&self) -> String {
        self.inner.text.clone()
    }

    #[getter]
    fn position(&self) -> usize {
        self.inner.position
    }

    #[getter]
    fn length(&self) -> usize {
        self.inner.length
    }

    #[getter]
    fn has_period(&self) -> bool {
        self.inner.has_period
    }

    #[getter]
    fn abbrev_score(&self) -> Option<f64> {
        self.inner.abbrev_score
    }

    #[getter]
    fn in_abbrev_list(&self) -> bool {
        self.inner.in_abbrev_list
    }

    #[getter]
    fn collocation_score(&self) -> Option<f64> {
        self.inner.collocation_score
    }

    #[getter]
    fn is_collocation(&self) -> bool {
        self.inner.is_collocation
    }

    #[getter]
    fn next_is_capital(&self) -> Option<bool> {
        self.inner.next_is_capital
    }

    #[getter]
    fn decision(&self) -> String {
        format!("{:?}", self.inner.decision)
    }

    #[getter]
    fn confidence(&self) -> f64 {
        self.inner.confidence
    }

    #[getter]
    fn primary_reason(&self) -> String {
        self.inner.primary_reason.clone()
    }

    #[getter]
    fn factors(&self) -> Vec<PyDecisionFactor> {
        self.inner
            .factors
            .iter()
            .map(|f| PyDecisionFactor { inner: f.clone() })
            .collect()
    }

    fn __repr__(&self) -> String {
        format!(
            "TokenAnalysis(text='{}', position={}, decision={:?}, confidence={:.2})",
            self.inner.text, self.inner.position, self.inner.decision, self.inner.confidence
        )
    }
}

/// Python wrapper for DecisionFactor
#[pyclass(name = "DecisionFactor")]
#[derive(Clone)]
pub struct PyDecisionFactor {
    pub inner: DecisionFactor,
}

#[pymethods]
impl PyDecisionFactor {
    #[getter]
    fn factor_type(&self) -> String {
        format!("{:?}", self.inner.factor_type)
    }

    #[getter]
    fn weight(&self) -> f64 {
        self.inner.weight
    }

    #[getter]
    fn description(&self) -> String {
        self.inner.description.clone()
    }

    fn __repr__(&self) -> String {
        format!(
            "DecisionFactor(type={:?}, weight={:.2}, desc='{}')",
            self.inner.factor_type, self.inner.weight, self.inner.description
        )
    }
}

/// Python wrapper for AnalysisStatistics
#[pyclass(name = "AnalysisStatistics")]
#[derive(Clone)]
pub struct PyAnalysisStatistics {
    pub inner: AnalysisStatistics,
}

#[pymethods]
impl PyAnalysisStatistics {
    #[getter]
    fn total_tokens(&self) -> usize {
        self.inner.total_tokens
    }

    #[getter]
    fn total_breaks(&self) -> usize {
        self.inner.total_breaks
    }

    #[getter]
    fn abbreviations_found(&self) -> usize {
        self.inner.abbreviations_found
    }

    #[getter]
    fn collocations_found(&self) -> usize {
        self.inner.collocations_found
    }

    #[getter]
    fn average_confidence(&self) -> f64 {
        self.inner.average_confidence
    }

    #[getter]
    fn low_confidence_decisions(&self) -> usize {
        self.inner.low_confidence_decisions
    }

    fn __repr__(&self) -> String {
        format!(
            "AnalysisStatistics(tokens={}, breaks={}, avg_confidence={:.2})",
            self.inner.total_tokens, self.inner.total_breaks, self.inner.average_confidence
        )
    }
}

/// Python wrapper for TextAnalysis
#[pyclass(name = "TextAnalysis")]
#[derive(Clone)]
pub struct PyTextAnalysis {
    pub inner: TextAnalysis,
}

#[pymethods]
impl PyTextAnalysis {
    #[getter]
    fn tokens(&self) -> Vec<PyTokenAnalysis> {
        self.inner
            .tokens
            .iter()
            .map(|t| PyTokenAnalysis { inner: t.clone() })
            .collect()
    }

    #[getter]
    fn sentences(&self) -> Vec<String> {
        self.inner.sentences.clone()
    }

    #[getter]
    fn break_positions(&self) -> Vec<usize> {
        self.inner.break_positions.clone()
    }

    #[getter]
    fn statistics(&self) -> PyAnalysisStatistics {
        PyAnalysisStatistics {
            inner: self.inner.statistics.clone(),
        }
    }

    fn __repr__(&self) -> String {
        format!(
            "TextAnalysis(tokens={}, sentences={}, breaks={})",
            self.inner.tokens.len(),
            self.inner.sentences.len(),
            self.inner.break_positions.len()
        )
    }
}
