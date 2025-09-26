use nupunkt_rs::core::SentenceTokenizer;
use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
use nupunkt_rs::trainers::PunktTrainer;
use std::sync::Arc;

#[test]
fn test_inference_adjustment() {
    // Create test text with ambiguous abbreviations
    let training_text = "Dr. Smith went to the store. He bought milk. 
                         Mr. Jones is a teacher. He teaches math.
                         The U.S. government is large. It has many departments.
                         The temperature is 32.5 degrees. It is cold outside.";

    // Train a model
    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let mut tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    // Test text with potential sentence boundaries
    let test_text = "Dr. Smith said hello. The patient was fine.";

    // Test with default confidence (0.5)
    let sentences_default = tokenizer.tokenize(test_text);
    // Just check that we get some sentences
    assert!(!sentences_default.is_empty());

    // Test with high precision (more conservative, fewer breaks)
    tokenizer.set_precision_recall_balance(0.9);
    let sentences_high = tokenizer.tokenize(test_text);
    // Should potentially merge sentences if confidence is low

    // Test with high recall (more aggressive, more breaks)
    tokenizer.set_precision_recall_balance(0.1);
    let sentences_low = tokenizer.tokenize(test_text);
    // Should potentially split more aggressively

    // Test balanced mode
    tokenizer.set_precision_recall_balance(0.5);
    let sentences_balanced = tokenizer.tokenize("Dr. Smith arrived.");

    // The behavior should differ based on precision/recall balance
    println!("Default: {:?}", sentences_default);
    println!("High precision: {:?}", sentences_high);
    println!("High recall: {:?}", sentences_low);
    println!("Balanced: {:?}", sentences_balanced);
}

#[test]
fn test_precision_recall_adjustment() {
    let training_text = "This is a sentence. This is another. 
                         sometimes lowercase starts. Sometimes uppercase.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let mut tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let test_text = "Hello world. the next sentence is lowercase.";

    // High precision - break less often
    tokenizer.set_precision_recall_balance(0.9);
    let sentences_high_precision = tokenizer.tokenize(test_text);

    // High recall - break more often
    tokenizer.set_precision_recall_balance(0.1);
    let sentences_high_recall = tokenizer.tokenize(test_text);

    println!("High precision: {:?}", sentences_high_precision);
    println!("High recall: {:?}", sentences_high_recall);
}

#[test]
fn test_inference_config_struct() {
    use nupunkt_rs::tokenizers::sentence::InferenceConfig;

    let config = InferenceConfig {
        precision_recall_balance: 0.7,
    };

    let mut tokenizer = PunktSentenceTokenizer::new();
    tokenizer.set_inference_config(config.clone());

    let retrieved_config = tokenizer.inference_config();
    assert_eq!(retrieved_config.precision_recall_balance, 0.7);
}

#[test]
fn test_debug_mode() {
    let mut tokenizer = PunktSentenceTokenizer::new();

    // Debug mode should be off by default
    assert!(!tokenizer.is_debug_mode());

    // Enable debug mode
    tokenizer.set_debug_mode(true);
    assert!(tokenizer.is_debug_mode());

    // When debug mode is on, tokenization should produce debug output
    // (This would print to stderr during testing)
    let text = "This is a test. Another sentence here.";
    let _sentences = tokenizer.tokenize(text);

    // Disable debug mode
    tokenizer.set_debug_mode(false);
    assert!(!tokenizer.is_debug_mode());
}

#[test]
fn test_get_statistics() {
    let training_text = "Dr. Smith and Mr. Jones work together. 
                         The U.S. government has many departments.
                         The temperature is 98.6 degrees.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let stats = tokenizer.get_statistics();

    // Check that statistics contain expected sections
    assert!(stats.contains("Punkt Model Statistics"));
    assert!(stats.contains("Abbreviations:"));
    assert!(stats.contains("Collocations:"));
    assert!(stats.contains("Sentence starters:"));
    assert!(stats.contains("Inference Configuration:"));
    assert!(stats.contains("Precision/recall balance:"));

    println!("Model statistics:\n{}", stats);
}
