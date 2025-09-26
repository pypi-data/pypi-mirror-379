/// Default model management for nupunkt-rs
use crate::parameters::PunktParameters;
use crate::tokenizers::PunktSentenceTokenizer;
use anyhow::{Context, Result};
use std::fs;
use std::path::{Path, PathBuf};
use std::sync::Arc;

/// Default model bytes embedded in the binary
/// This is trained on a diverse corpus and provides good general-purpose tokenization
#[cfg(feature = "default-model")]
pub const DEFAULT_MODEL_BYTES: &[u8] = include_bytes!("../models/default.npkt.gz");

/// Get the path to look for user models
fn get_user_model_dir() -> PathBuf {
    if let Ok(data_dir) = std::env::var("XDG_DATA_HOME") {
        PathBuf::from(data_dir).join("nupunkt-rs/models")
    } else if let Ok(home) = std::env::var("HOME") {
        PathBuf::from(home).join(".local/share/nupunkt-rs/models")
    } else {
        PathBuf::from("models")
    }
}

/// Load the default model
///
/// This tries in order:
/// 1. Embedded default model (if feature enabled)
/// 2. User's default model in ~/.local/share/nupunkt-rs/models/default.npkt.gz
/// 3. Local models/default.npkt.gz
/// 4. Empty model as fallback
pub fn load_default_model() -> Result<Arc<PunktParameters>> {
    // Try embedded model first
    #[cfg(feature = "default-model")]
    {
        if let Ok(params) = PunktParameters::from_compressed_bytes(DEFAULT_MODEL_BYTES) {
            return Ok(Arc::new(params));
        }
    }

    // Try user model directory
    let user_model = get_user_model_dir().join("default.npkt.gz");
    if user_model.exists() {
        let params = PunktParameters::load_compressed(user_model.to_str().unwrap())
            .map_err(|e| anyhow::anyhow!("Failed to load user default model: {}", e))?;
        return Ok(Arc::new(params));
    }

    // Try local models directory
    let local_model = PathBuf::from("models/default.npkt.gz");
    if local_model.exists() {
        let params = PunktParameters::load_compressed(local_model.to_str().unwrap())
            .map_err(|e| anyhow::anyhow!("Failed to load local default model: {}", e))?;
        return Ok(Arc::new(params));
    }

    // Fallback to empty model
    Ok(Arc::new(PunktParameters::new()))
}

/// Create a tokenizer with the default model
pub fn create_default_tokenizer() -> Result<PunktSentenceTokenizer> {
    let params = load_default_model()?;
    Ok(PunktSentenceTokenizer::from_parameters(params))
}

/// Load a model by name or path
///
/// Special names:
/// - "default" or "en" - loads the default English model
/// - "empty" - creates an empty model
/// - Any other string is treated as a file path
pub fn load_model(model: &str) -> Result<Arc<PunktParameters>> {
    match model {
        "default" | "en" | "english" => load_default_model(),
        "empty" | "none" => Ok(Arc::new(PunktParameters::new())),
        path => {
            // First check if it's a simple name in the models directory
            if !path.contains('/') && !path.contains('\\') {
                // Try user models directory
                let user_model = get_user_model_dir().join(format!("{}.npkt.gz", path));
                if user_model.exists() {
                    let params = PunktParameters::load_compressed(user_model.to_str().unwrap())
                        .map_err(|e| anyhow::anyhow!("Failed to load model {}: {}", path, e))?;
                    return Ok(Arc::new(params));
                }

                // Try local models directory
                let local_model = PathBuf::from("models").join(format!("{}.npkt.gz", path));
                if local_model.exists() {
                    let params = PunktParameters::load_compressed(local_model.to_str().unwrap())
                        .map_err(|e| anyhow::anyhow!("Failed to load model {}: {}", path, e))?;
                    return Ok(Arc::new(params));
                }
            }

            // Treat as direct file path
            let params = PunktParameters::load_compressed(path)
                .map_err(|e| anyhow::anyhow!("Failed to load model from path {}: {}", path, e))?;
            Ok(Arc::new(params))
        }
    }
}

/// List available models
pub fn list_models() -> Vec<String> {
    let mut models = vec!["default".to_string(), "empty".to_string()];

    // Check user models directory
    if let Ok(entries) = fs::read_dir(get_user_model_dir()) {
        for entry in entries.flatten() {
            if let Some(name) = entry.file_name().to_str() {
                if name.ends_with(".npkt.gz") {
                    let model_name = name.trim_end_matches(".npkt.gz");
                    if model_name != "default" {
                        models.push(model_name.to_string());
                    }
                }
            }
        }
    }

    // Check local models directory
    if let Ok(entries) = fs::read_dir("models") {
        for entry in entries.flatten() {
            if let Some(name) = entry.file_name().to_str() {
                if name.ends_with(".npkt.gz") {
                    let model_name = name.trim_end_matches(".npkt.gz");
                    if !models.contains(&model_name.to_string()) {
                        models.push(model_name.to_string());
                    }
                }
            }
        }
    }

    models
}

/// Install a model to the user models directory
pub fn install_model(source: &Path, name: &str) -> Result<PathBuf> {
    let user_dir = get_user_model_dir();
    fs::create_dir_all(&user_dir).context("Failed to create user models directory")?;

    let dest = user_dir.join(format!("{}.npkt.gz", name));
    fs::copy(source, &dest)
        .map_err(|e| anyhow::anyhow!("Failed to install model to {}: {}", dest.display(), e))?;

    Ok(dest)
}
