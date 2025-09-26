use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use once_cell::sync::Lazy;
use std::sync::Arc;

pub mod analysis;
pub mod core;
pub mod decision;
pub mod models;
pub mod parameters;
pub mod statistics;
pub mod tokenizers;
pub mod tokens;
pub mod trainers;
pub mod utils;

#[cfg(test)]
mod tests {
    mod position_tracking;
}

use crate::core::SentenceTokenizer;
use crate::tokenizers::PunktSentenceTokenizer as RustSentenceTokenizer;
use crate::trainers::PunktTrainer as RustTrainer;

// Cache for the default model to avoid reloading it
static DEFAULT_MODEL_CACHE: Lazy<Arc<RustSentenceTokenizer>> = Lazy::new(|| {
    Arc::new(
        models::create_default_tokenizer()
            .expect("Failed to load default model")
    )
});

/// Python module for nupunkt-rs
#[pymodule]
fn _nupunkt_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    // Add version information
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;

    // Register Python classes
    m.add_class::<tokenizers::sentence::PySentenceTokenizer>()?;
    m.add_class::<tokenizers::sentence::PyInferenceConfig>()?;
    m.add_class::<trainers::trainer::PyTrainer>()?;
    m.add_class::<trainers::trainer::PyScoringConfig>()?;
    m.add_class::<parameters::PyParameters>()?;

    // Register analysis classes
    m.add_class::<analysis::PyTextAnalysis>()?;
    m.add_class::<analysis::PyTokenAnalysis>()?;
    m.add_class::<analysis::PyDecisionFactor>()?;
    m.add_class::<analysis::PyAnalysisStatistics>()?;

    // Add functions
    m.add_function(wrap_pyfunction!(sent_tokenize, m)?)?;
    m.add_function(wrap_pyfunction!(para_tokenize, m)?)?;
    m.add_function(wrap_pyfunction!(para_tokenize_joined, m)?)?;
    m.add_function(wrap_pyfunction!(train_model, m)?)?;
    m.add_function(wrap_pyfunction!(load_model, m)?)?;
    m.add_function(wrap_pyfunction!(load_default_model, m)?)?;
    m.add_function(wrap_pyfunction!(create_default_tokenizer, m)?)?;

    Ok(())
}

/// Tokenize text into sentences
#[pyfunction]
#[pyo3(signature = (text, model_params=None, precision_recall=None))]
fn sent_tokenize(
    text: &str,
    model_params: Option<&parameters::PyParameters>,
    precision_recall: Option<f64>,
) -> PyResult<Vec<String>> {
    let mut tokenizer = if let Some(params) = model_params {
        RustSentenceTokenizer::from_parameters(params.inner.clone())
    } else {
        // Use the cached default model instead of creating an empty tokenizer
        (**DEFAULT_MODEL_CACHE).clone()
    };
    
    // Apply precision_recall if provided
    if let Some(pr) = precision_recall {
        tokenizer.set_precision_recall_balance(pr);
    }
    
    Ok(tokenizer.tokenize(text))
}

/// Tokenize text into paragraphs, where each paragraph is a list of sentences
#[pyfunction]
#[pyo3(signature = (text, model_params=None, precision_recall=None))]
fn para_tokenize(
    text: &str,
    model_params: Option<&parameters::PyParameters>,
    precision_recall: Option<f64>,
) -> PyResult<Vec<Vec<String>>> {
    let mut tokenizer = if let Some(params) = model_params {
        RustSentenceTokenizer::from_parameters(params.inner.clone())
    } else {
        // Use the cached default model instead of creating an empty tokenizer
        (**DEFAULT_MODEL_CACHE).clone()
    };
    
    // Apply precision_recall if provided
    if let Some(pr) = precision_recall {
        tokenizer.set_precision_recall_balance(pr);
    }
    
    Ok(tokenizer.tokenize_paragraphs(text))
}

/// Tokenize text into paragraphs as flat strings (sentences joined with spaces)
#[pyfunction]
#[pyo3(signature = (text, model_params=None, precision_recall=None))]
fn para_tokenize_joined(
    text: &str,
    model_params: Option<&parameters::PyParameters>,
    precision_recall: Option<f64>,
) -> PyResult<Vec<String>> {
    let mut tokenizer = if let Some(params) = model_params {
        RustSentenceTokenizer::from_parameters(params.inner.clone())
    } else {
        // Use the cached default model instead of creating an empty tokenizer
        (**DEFAULT_MODEL_CACHE).clone()
    };
    
    // Apply precision_recall if provided
    if let Some(pr) = precision_recall {
        tokenizer.set_precision_recall_balance(pr);
    }
    
    Ok(tokenizer.tokenize_paragraphs_flat(text))
}

/// Train a new model from text
#[pyfunction]
#[pyo3(signature = (text, verbose=false))]
fn train_model(text: &str, verbose: bool) -> PyResult<parameters::PyParameters> {
    let mut trainer = RustTrainer::new();
    let params = trainer
        .train(text, verbose)
        .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))?;
    Ok(parameters::PyParameters {
        inner: std::sync::Arc::new(params),
    })
}

/// Load a model by name or path
#[pyfunction]
fn load_model(model: &str) -> PyResult<crate::parameters::PyParameters> {
    let params = crate::models::load_model(model)
        .map_err(|e| pyo3::exceptions::PyIOError::new_err(e.to_string()))?;

    Ok(crate::parameters::PyParameters { inner: params })
}

/// Load the default model
#[pyfunction]
fn load_default_model() -> PyResult<parameters::PyParameters> {
    let params = models::load_default_model()
        .map_err(|e| pyo3::exceptions::PyIOError::new_err(e.to_string()))?;

    Ok(parameters::PyParameters { inner: params })
}

/// Create a tokenizer with the default model
#[pyfunction]
fn create_default_tokenizer() -> PyResult<crate::tokenizers::sentence::PySentenceTokenizer> {
    let tokenizer = crate::models::create_default_tokenizer()
        .map_err(|e| pyo3::exceptions::PyIOError::new_err(e.to_string()))?;

    Ok(crate::tokenizers::sentence::PySentenceTokenizer { inner: tokenizer })
}
