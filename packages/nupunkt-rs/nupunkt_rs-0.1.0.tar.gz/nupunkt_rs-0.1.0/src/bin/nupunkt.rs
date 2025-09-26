use anyhow::{Context, Result};
use clap::{Parser, Subcommand, ValueEnum};
use nupunkt_rs::core::{ScoringConfig, SentenceTokenizer};
use nupunkt_rs::parameters::PunktParameters;
use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
use nupunkt_rs::trainers::PunktTrainer;
use std::fs;
use std::io::{self, Read};
use std::path::PathBuf;
use std::sync::Arc;

/// Training profile presets
#[derive(Debug, Clone, Copy, ValueEnum)]
enum TrainingProfile {
    /// Conservative: Breaks less often, high precision (finds more abbreviations/collocations, fewer starters)
    Conservative,
    /// Balanced: Default settings
    Balanced,
    /// Aggressive: Breaks more often, high recall (finds fewer abbreviations/collocations, more starters)
    Aggressive,
}

impl TrainingProfile {
    fn to_config(self) -> ScoringConfig {
        match self {
            TrainingProfile::Conservative => ScoringConfig {
                // Lower thresholds = detect MORE abbreviations/collocations = FEWER breaks
                abbrev_threshold: 0.05,
                abbrev_boost: 2.0,
                abbrev_consistency: 0.15,
                collocation_threshold: 2.5,
                min_colloc_rate: 0.00001, // 1 per 100k tokens
                max_abbrev_length: 12,
                // Higher threshold = detect FEWER starters = FEWER breaks
                sent_starter_threshold: 50.0,
                min_starter_rate: 0.0001, // 10 per 100k tokens (stricter)
                require_alpha_starters: true,
            },
            TrainingProfile::Balanced => ScoringConfig::default(),
            TrainingProfile::Aggressive => ScoringConfig {
                // Higher thresholds = detect FEWER abbreviations/collocations = MORE breaks
                abbrev_threshold: 0.3,
                abbrev_boost: 1.2,
                abbrev_consistency: 0.4,
                collocation_threshold: 10.0,
                min_colloc_rate: 0.0001, // 10 per 100k tokens (stricter)
                max_abbrev_length: 7,
                // Lower threshold = detect MORE starters = MORE breaks
                sent_starter_threshold: 10.0,
                min_starter_rate: 0.00001, // 1 per 100k tokens (looser)
                require_alpha_starters: true,
            },
        }
    }
}

/// Parse and validate threshold values
fn parse_threshold(s: &str) -> Result<f64, String> {
    let val: f64 = s
        .parse()
        .map_err(|_| format!("'{}' is not a valid number", s))?;
    if val < 0.0 {
        return Err(format!("Threshold must be non-negative, got {}", val));
    }
    Ok(val)
}

#[derive(Parser)]
#[command(name = "nupunkt")]
#[command(about = "A fast sentence tokenizer using the Punkt algorithm", long_about = None)]
#[command(version)]
struct Cli {
    /// Input text or file path (reads from stdin if not provided)
    input: Option<String>,

    /// Model file to use (uses default if not specified)
    #[arg(short, long, global = true)]
    model: Option<PathBuf>,

    /// Output format
    #[arg(short = 'f', long, value_enum, default_value = "lines", global = true)]
    format: OutputFormat,

    /// Output file (writes to stdout if not specified)
    #[arg(short, long, global = true)]
    output: Option<PathBuf>,

    /// Verbose output
    #[arg(short, long, global = true)]
    verbose: bool,

    /// Quiet mode (suppress non-essential output)
    #[arg(short, long, global = true)]
    quiet: bool,

    #[command(subcommand)]
    command: Option<Commands>,
}

#[derive(Subcommand)]
enum Commands {
    /// Tokenize text into sentences (default command)
    Tokenize {
        /// Input text or file path
        input: Option<String>,

        /// Precision/recall balance (0.0=max recall, 1.0=max precision)
        #[arg(long, short = 'p', value_parser = parse_confidence)]
        precision_recall: Option<f64>,

        /// Use maximum recall mode (breaks at most boundaries)
        #[arg(
            long,
            conflicts_with = "precision_recall",
            conflicts_with = "max_precision"
        )]
        max_recall: bool,

        /// Use maximum precision mode (breaks only at clear boundaries)
        #[arg(
            long,
            conflicts_with = "precision_recall",
            conflicts_with = "max_recall"
        )]
        max_precision: bool,

        /// Enable debug mode (prints decision info to stderr)
        #[arg(long)]
        debug: bool,

        /// Show model statistics
        #[arg(long)]
        stats: bool,

        /// Explain decision at specific character position
        #[arg(long)]
        explain: Option<usize>,

        /// Analyze tokens and show detailed scoring
        #[arg(long)]
        analyze: bool,
    },

    /// Train a new model from text
    Train {
        /// Training corpus file(s)
        #[arg(required = true)]
        corpus: Vec<PathBuf>,

        /// Output model file
        #[arg(short, long, default_value = "model.npkt.gz")]
        output: PathBuf,

        /// Abbreviations file (JSON array of strings)
        #[arg(long, short = 'a')]
        abbreviations: Option<PathBuf>,

        /// Verbose output during training
        #[arg(long, short = 'v')]
        verbose: bool,

        /// Test the model immediately with provided text
        #[arg(long)]
        test: Option<String>,

        // Training hyperparameters
        /// Training profile preset (conservative/balanced/aggressive)
        #[arg(long, value_enum, conflicts_with_all = ["abbrev_threshold", "collocation_threshold", "sent_starter_threshold"])]
        profile: Option<TrainingProfile>,

        /// Abbreviation detection threshold (default: 0.1, lower=more abbrevs)
        #[arg(long, value_parser = parse_threshold)]
        abbrev_threshold: Option<f64>,

        /// Abbreviation consistency requirement (default: 0.25)
        #[arg(long, value_parser = parse_threshold)]
        abbrev_consistency: Option<f64>,

        /// Collocation detection threshold (default: 5.0, lower=more collocations)
        #[arg(long, value_parser = parse_threshold)]
        collocation_threshold: Option<f64>,

        /// Sentence starter threshold (default: 25.0, lower=more starters)
        #[arg(long, value_parser = parse_threshold)]
        sent_starter_threshold: Option<f64>,

        /// Minimum rate for collocations (e.g., 0.00001 = 1 per 100k tokens)
        #[arg(long, value_parser = parse_threshold)]
        min_colloc_rate: Option<f64>,

        /// Maximum abbreviation length (default: 9)
        #[arg(long)]
        max_abbrev_length: Option<usize>,

        /// Load complete config from JSON file
        #[arg(long, conflicts_with = "profile")]
        config_json: Option<PathBuf>,

        // Token filtering options (to reduce model size)
        /// Don't filter tokens (by default, filtering is enabled to reduce model size)
        #[arg(long = "no-filter-tokens")]
        no_filter_tokens: bool,

        /// Minimum frequency for tokens to be kept
        #[arg(long, default_value = "5")]
        min_token_frequency: usize,

        /// Maximum number of tokens to keep
        #[arg(long, default_value = "50000")]
        max_tokens: usize,
    },

    /// Show model information
    Info {
        /// Model file to inspect
        model: PathBuf,
    },

    /// Benchmark tokenization performance
    Bench {
        /// Input file to benchmark
        input: PathBuf,

        /// Number of iterations
        #[arg(short = 'n', long, default_value = "100")]
        iterations: usize,
    },
}

#[derive(Clone, ValueEnum)]
enum OutputFormat {
    /// One sentence per line (default)
    Lines,
    /// JSON format
    Json,
    /// Character spans (start:end)
    Spans,
    /// Debug format with detailed information
    Debug,
}

fn parse_confidence(s: &str) -> Result<f64, String> {
    let val: f64 = s.parse().map_err(|_| format!("Invalid number: {}", s))?;
    if !(0.0..=1.0).contains(&val) {
        Err(format!("Value must be between 0.0 and 1.0, got {}", val))
    } else {
        Ok(val)
    }
}

fn main() -> Result<()> {
    let cli = Cli::parse();

    match cli.command {
        None => {
            // Default command is tokenize with no extra options
            tokenize_command(
                cli.input,
                cli.model,
                cli.format,
                cli.output,
                cli.verbose,
                cli.quiet,
                None,  // precision_recall
                false, // max_recall
                false, // max_precision
                false, // debug
                false, // stats
                None,  // explain
                false, // analyze
            )
        }
        Some(Commands::Tokenize {
            input,
            precision_recall,
            max_recall,
            max_precision,
            debug,
            stats,
            explain,
            analyze,
        }) => tokenize_command(
            input.or(cli.input),
            cli.model,
            cli.format,
            cli.output,
            cli.verbose,
            cli.quiet,
            precision_recall,
            max_recall,
            max_precision,
            debug,
            stats,
            explain,
            analyze,
        ),
        Some(Commands::Train {
            corpus,
            output,
            abbreviations,
            verbose,
            test,
            profile,
            abbrev_threshold,
            abbrev_consistency,
            collocation_threshold,
            sent_starter_threshold,
            min_colloc_rate,
            max_abbrev_length,
            config_json,
            no_filter_tokens,
            min_token_frequency,
            max_tokens,
        }) => train_command(
            corpus,
            output,
            abbreviations,
            verbose || cli.verbose,
            test,
            profile,
            abbrev_threshold,
            abbrev_consistency,
            collocation_threshold,
            sent_starter_threshold,
            min_colloc_rate,
            max_abbrev_length,
            config_json,
            no_filter_tokens,
            min_token_frequency,
            max_tokens,
        ),
        Some(Commands::Info { model }) => info_command(model),
        Some(Commands::Bench { input, iterations }) => {
            bench_command(input, cli.model, iterations, cli.quiet)
        }
    }
}

#[allow(clippy::too_many_arguments)]
fn tokenize_command(
    input: Option<String>,
    model_path: Option<PathBuf>,
    format: OutputFormat,
    output_path: Option<PathBuf>,
    verbose: bool,
    quiet: bool,
    precision_recall: Option<f64>,
    max_recall: bool,
    max_precision: bool,
    debug: bool,
    stats: bool,
    explain: Option<usize>,
    analyze: bool,
) -> Result<()> {
    // Get input text
    let text = get_input_text(input)?;

    if verbose && !quiet {
        eprintln!("Processing {} characters...", text.len());
    }

    // Load model
    let mut tokenizer = load_tokenizer(model_path, verbose && !quiet)?;

    // Apply inference configuration if specified
    if let Some(pr) = precision_recall {
        tokenizer.set_precision_recall_balance(pr);
        if verbose && !quiet {
            eprintln!("Set precision/recall balance to {:.2}", pr);
        }
    } else if max_recall {
        tokenizer.set_max_recall();
        if verbose && !quiet {
            eprintln!("Set to maximum recall mode (0.0)");
        }
    } else if max_precision {
        tokenizer.set_max_precision();
        if verbose && !quiet {
            eprintln!("Set to maximum precision mode (1.0)");
        }
    }

    // Enable debug mode if requested
    if debug {
        tokenizer.set_debug_mode(true);
        if verbose && !quiet {
            eprintln!("Debug mode enabled");
        }
    }

    // Show statistics if requested
    if stats {
        println!("{}", tokenizer.get_statistics());
        return Ok(());
    }

    // Explain decision at specific position if requested
    if let Some(pos) = explain {
        if let Some(explanation) = tokenizer.explain_decision(&text, pos) {
            println!("{}", explanation);
        } else {
            eprintln!("No token found at position {}", pos);
        }
        return Ok(());
    }

    // Analyze tokens if requested
    if analyze {
        let analysis = tokenizer.analyze_tokens(&text);

        // Print analysis in JSON format
        let output =
            serde_json::to_string_pretty(&analysis).context("Failed to serialize analysis")?;
        println!("{}", output);

        if verbose && !quiet {
            eprintln!(
                "Analysis complete: {} tokens, {} breaks, avg confidence: {:.2}",
                analysis.statistics.total_tokens,
                analysis.statistics.total_breaks,
                analysis.statistics.average_confidence
            );
        }
        return Ok(());
    }

    // Regular tokenization
    let sentences = tokenizer.tokenize(&text);
    let spans = if matches!(format, OutputFormat::Spans | OutputFormat::Debug) {
        Some(tokenizer.tokenize_spans(&text))
    } else {
        None
    };

    if verbose && !quiet {
        eprintln!("Found {} sentences", sentences.len());
    }

    // Format output
    let output = format_output(&sentences, spans.as_deref(), &text, format)?;

    // Write output
    write_output(&output, output_path)?;

    Ok(())
}

#[allow(clippy::too_many_arguments)]
fn train_command(
    corpus_files: Vec<PathBuf>,
    output_path: PathBuf,
    abbreviations_path: Option<PathBuf>,
    verbose: bool,
    test_text: Option<String>,
    profile: Option<TrainingProfile>,
    abbrev_threshold: Option<f64>,
    abbrev_consistency: Option<f64>,
    collocation_threshold: Option<f64>,
    sent_starter_threshold: Option<f64>,
    min_colloc_rate: Option<f64>,
    max_abbrev_length: Option<usize>,
    config_json: Option<PathBuf>,
    no_filter_tokens: bool,
    min_token_frequency: usize,
    max_tokens: usize,
) -> Result<()> {
    // Build scoring config
    let mut config = if let Some(json_path) = config_json {
        // Load config from JSON file
        let json_str = fs::read_to_string(&json_path)
            .with_context(|| format!("Failed to read config file: {}", json_path.display()))?;
        serde_json::from_str(&json_str)
            .with_context(|| format!("Failed to parse config JSON from {}", json_path.display()))?
    } else if let Some(profile) = profile {
        // Use profile preset
        profile.to_config()
    } else {
        // Start with defaults
        ScoringConfig::default()
    };

    // Apply individual overrides
    if let Some(val) = abbrev_threshold {
        config.abbrev_threshold = val;
    }
    if let Some(val) = abbrev_consistency {
        config.abbrev_consistency = val;
    }
    if let Some(val) = collocation_threshold {
        config.collocation_threshold = val;
    }
    if let Some(val) = sent_starter_threshold {
        config.sent_starter_threshold = val;
    }
    if let Some(val) = min_colloc_rate {
        config.min_colloc_rate = val;
    }
    if let Some(val) = max_abbrev_length {
        config.max_abbrev_length = val;
    }

    // Create trainer with config
    let mut trainer = PunktTrainer::with_config(config.clone());

    if verbose {
        eprintln!("Training configuration:");
        eprintln!("  Abbreviation threshold: {}", config.abbrev_threshold);
        eprintln!("  Abbreviation consistency: {}", config.abbrev_consistency);
        eprintln!("  Collocation threshold: {}", config.collocation_threshold);
        eprintln!(
            "  Sentence starter threshold: {}",
            config.sent_starter_threshold
        );
        eprintln!("  Min collocation rate: {:.6}", config.min_colloc_rate);
        eprintln!("  Min starter rate: {:.6}", config.min_starter_rate);
        eprintln!("  Max abbreviation length: {}", config.max_abbrev_length);
        eprintln!();
    }

    // Load abbreviations if provided
    if let Some(abbrev_path) = abbreviations_path {
        match trainer.load_abbreviations_from_json(abbrev_path.to_str().unwrap()) {
            Ok(count) => {
                if verbose {
                    eprintln!(
                        "Loaded {} abbreviations from {}",
                        count,
                        abbrev_path.display()
                    );
                }
            }
            Err(e) => {
                eprintln!("Warning: Failed to load abbreviations: {}", e);
            }
        }
    }

    if verbose {
        eprintln!(
            "Starting streaming training from {} file(s)...",
            corpus_files.len()
        );
    }

    // Process all corpus files in streaming fashion
    let mut total_chars = 0usize;
    let mut chunk_buffer = String::with_capacity(1024 * 1024); // 1MB buffer

    for path in &corpus_files {
        if verbose {
            eprintln!("Processing: {}", path.display());
        }

        // Handle JSONL.gz files
        if path.extension() == Some("gz".as_ref()) {
            use flate2::read::GzDecoder;
            use std::io::{BufRead, BufReader};

            let file = fs::File::open(path)
                .with_context(|| format!("Failed to open corpus file: {}", path.display()))?;
            let decoder = GzDecoder::new(file);
            let reader = BufReader::new(decoder);

            let mut doc_count = 0;
            for line in reader.lines() {
                let line = line?;
                // Try to parse as JSON and extract text field
                if let Ok(json_val) = serde_json::from_str::<serde_json::Value>(&line) {
                    if let Some(text) = json_val.get("text").and_then(|v| v.as_str()) {
                        chunk_buffer.push_str(text);
                        chunk_buffer.push_str("\n\n");
                        doc_count += 1;
                        total_chars += text.len() + 2;
                    }
                } else {
                    // If not JSON, treat as plain text
                    chunk_buffer.push_str(&line);
                    chunk_buffer.push('\n');
                    total_chars += line.len() + 1;
                }

                // Process buffer when it gets large enough
                if chunk_buffer.len() > 1024 * 1024 {
                    // 1MB chunks
                    trainer
                        .train_incremental(&chunk_buffer, verbose)
                        .map_err(|e| anyhow::anyhow!("Training failed: {}", e))?;

                    if verbose && doc_count % 1000 == 0 {
                        eprintln!(
                            "  Processed {} documents, {} total chars",
                            doc_count, total_chars
                        );
                    }

                    chunk_buffer.clear();
                }
            }

            // Process remaining buffer
            if !chunk_buffer.is_empty() {
                trainer
                    .train_incremental(&chunk_buffer, verbose)
                    .map_err(|e| anyhow::anyhow!("Training failed: {}", e))?;
                chunk_buffer.clear();
            }

            if verbose {
                eprintln!(
                    "  Completed {} documents from {}",
                    doc_count,
                    path.display()
                );
            }
        } else {
            // Regular text file - read in chunks
            use std::io::{BufRead, BufReader};

            let file = fs::File::open(path)
                .with_context(|| format!("Failed to open corpus file: {}", path.display()))?;
            let reader = BufReader::new(file);

            for line in reader.lines() {
                let line = line?;
                chunk_buffer.push_str(&line);
                chunk_buffer.push('\n');
                total_chars += line.len() + 1;

                // Process buffer when it gets large enough
                if chunk_buffer.len() > 1024 * 1024 {
                    // 1MB chunks
                    trainer
                        .train_incremental(&chunk_buffer, verbose)
                        .map_err(|e| anyhow::anyhow!("Training failed: {}", e))?;
                    chunk_buffer.clear();
                }
            }

            // Process remaining buffer
            if !chunk_buffer.is_empty() {
                trainer
                    .train_incremental(&chunk_buffer, verbose)
                    .map_err(|e| anyhow::anyhow!("Training failed: {}", e))?;
                chunk_buffer.clear();
            }
        }
    }

    if verbose {
        eprintln!(
            "Processed {} total characters, finalizing model...",
            total_chars
        );
    }

    // Finalize training
    let mut params = trainer
        .finalize_training(verbose)
        .map_err(|e| anyhow::anyhow!("Training finalization failed: {}", e))?;

    // Apply token filtering if enabled (default)
    if !no_filter_tokens {
        if verbose {
            eprintln!("\nFiltering model to reduce size...");
            eprintln!("  Min token frequency: {}", min_token_frequency);
            eprintln!("  Max tokens: {}", max_tokens);
        }

        let (original_tokens, filtered_tokens) =
            params.filter_tokens(min_token_frequency, Some(max_tokens), verbose);

        if verbose {
            eprintln!("\nToken filtering complete:");
            eprintln!("  Original: {} tokens", original_tokens);
            eprintln!("  Filtered: {} tokens", filtered_tokens);
            eprintln!(
                "  Reduction: {:.1}%",
                (1.0 - filtered_tokens as f64 / original_tokens as f64) * 100.0
            );
        }
    }

    // Save model
    params
        .save_compressed(output_path.to_str().unwrap())
        .map_err(|e| anyhow::anyhow!("Failed to save model: {}", e))?;

    if verbose {
        eprintln!("\nModel saved to: {}", output_path.display());
        eprintln!("  Abbreviations: {}", params.abbrev_types.len());
        eprintln!("  Collocations: {}", params.collocations.len());
        eprintln!("  Sentence starters: {}", params.sent_starters.len());
        eprintln!("  Token stats: {}", params.token_stats.len());
    }

    // Test if requested
    if let Some(test) = test_text {
        eprintln!("\nTesting model:");
        let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));
        let sentences = tokenizer.tokenize(&test);
        for (i, sent) in sentences.iter().enumerate() {
            println!("  [{}] {}", i + 1, sent);
        }
    }

    Ok(())
}

fn info_command(model_path: PathBuf) -> Result<()> {
    let params = PunktParameters::load_compressed(model_path.to_str().unwrap())
        .map_err(|e| anyhow::anyhow!("Failed to load model: {}", e))?;

    println!("Model: {}", model_path.display());
    println!("Abbreviations: {}", params.abbrev_types.len());

    if !params.abbrev_types.is_empty() {
        // Extract and sort just the abbreviation strings (keys)
        let mut abbrevs: Vec<String> = params.abbrev_types.keys().cloned().collect();
        abbrevs.sort();
        let preview: Vec<_> = abbrevs.iter().take(20).map(|s| s.as_str()).collect();
        println!("  {}", preview.join(", "));
        if abbrevs.len() > 20 {
            println!("  ... and {} more", abbrevs.len() - 20);
        }
    }

    println!("Collocations: {}", params.collocations.len());
    if !params.collocations.is_empty() {
        let preview: Vec<_> = params
            .collocations
            .iter()
            .take(5)
            .map(|(a, b)| format!("({}, {})", a, b))
            .collect();
        println!("  {}", preview.join(", "));
    }

    println!("Sentence starters: {}", params.sent_starters.len());
    if !params.sent_starters.is_empty() {
        let preview: Vec<_> = params.sent_starters.iter().take(10).collect();
        println!("  {:?}", preview);
    }

    // Get file size
    let metadata = fs::metadata(&model_path)?;
    println!("File size: {} bytes", metadata.len());

    Ok(())
}

fn bench_command(
    input_path: PathBuf,
    model_path: Option<PathBuf>,
    iterations: usize,
    quiet: bool,
) -> Result<()> {
    let text = fs::read_to_string(&input_path)
        .with_context(|| format!("Failed to read input file: {}", input_path.display()))?;

    let tokenizer = load_tokenizer(model_path, !quiet)?;

    if !quiet {
        eprintln!(
            "Benchmarking with {} iterations on {} characters...",
            iterations,
            text.len()
        );
    }

    // Warm up
    for _ in 0..10 {
        let _ = tokenizer.tokenize(&text);
    }

    // Benchmark
    let start = std::time::Instant::now();
    let mut total_sentences = 0;

    for _ in 0..iterations {
        let sentences = tokenizer.tokenize(&text);
        total_sentences = sentences.len();
    }

    let elapsed = start.elapsed();
    let total_chars = text.len() * iterations;
    let chars_per_sec = total_chars as f64 / elapsed.as_secs_f64();
    let ms_per_iter = elapsed.as_millis() as f64 / iterations as f64;

    println!("Results:");
    println!(
        "  Processed: {} characters × {} iterations",
        text.len(),
        iterations
    );
    println!("  Sentences found: {}", total_sentences);
    println!("  Total time: {:.3}s", elapsed.as_secs_f64());
    println!("  Time per iteration: {:.2}ms", ms_per_iter);
    println!("  Speed: {:.2}M chars/sec", chars_per_sec / 1_000_000.0);

    Ok(())
}

fn get_input_text(input: Option<String>) -> Result<String> {
    match input {
        Some(input) => {
            // Check if it's a file path
            if std::path::Path::new(&input).exists() {
                fs::read_to_string(&input)
                    .with_context(|| format!("Failed to read file: {}", input))
            } else {
                // Treat as literal text
                Ok(input)
            }
        }
        None => {
            // Read from stdin
            let mut buffer = String::new();
            io::stdin()
                .read_to_string(&mut buffer)
                .context("Failed to read from stdin")?;
            Ok(buffer)
        }
    }
}

fn load_tokenizer(model_path: Option<PathBuf>, verbose: bool) -> Result<PunktSentenceTokenizer> {
    use nupunkt_rs::models;

    let tokenizer = match model_path {
        Some(path) => {
            if verbose {
                eprintln!("Loading model: {}", path.display());
            }
            let params = if let Some(path_str) = path.to_str() {
                models::load_model(path_str)?
            } else {
                PunktParameters::load_compressed(path.to_str().unwrap())
                    .map_err(|e| anyhow::anyhow!("Failed to load model: {}", e))?
                    .into()
            };
            PunktSentenceTokenizer::from_parameters(params)
        }
        None => {
            if verbose {
                eprintln!("Loading default model");
            }
            models::create_default_tokenizer()?
        }
    };

    Ok(tokenizer)
}

fn format_output(
    sentences: &[String],
    spans: Option<&[(usize, usize)]>,
    _text: &str,
    format: OutputFormat,
) -> Result<String> {
    match format {
        OutputFormat::Lines => Ok(sentences.join("\n")),
        OutputFormat::Json => {
            let json = serde_json::json!({
                "sentences": sentences,
                "count": sentences.len(),
            });
            serde_json::to_string_pretty(&json).context("Failed to serialize JSON")
        }
        OutputFormat::Spans => match spans {
            Some(spans) => {
                let formatted: Vec<String> = spans
                    .iter()
                    .map(|(start, end)| format!("{}:{}", start, end))
                    .collect();
                Ok(formatted.join("\n"))
            }
            None => Ok(String::new()),
        },
        OutputFormat::Debug => {
            let mut output = String::new();
            if let Some(spans) = spans {
                for (i, ((start, end), sent)) in spans.iter().zip(sentences.iter()).enumerate() {
                    output.push_str(&format!("[{}] ({:>4}:{:<4}) {}\n", i + 1, start, end, sent));
                }
            } else {
                for (i, sent) in sentences.iter().enumerate() {
                    output.push_str(&format!("[{}] {}\n", i + 1, sent));
                }
            }
            Ok(output)
        }
    }
}

fn write_output(output: &str, path: Option<PathBuf>) -> Result<()> {
    match path {
        Some(path) => {
            fs::write(&path, output)
                .with_context(|| format!("Failed to write output to: {}", path.display()))?;
        }
        None => {
            print!("{}", output);
            if !output.ends_with('\n') {
                println!();
            }
        }
    }
    Ok(())
}
