use nupunkt_rs::core::SentenceTokenizer;
use nupunkt_rs::tokenizers::{sentence::InferenceConfig, PunktSentenceTokenizer};
use nupunkt_rs::trainers::PunktTrainer;
use std::sync::Arc;

#[test]
fn test_full_integration() {
    // Training phase
    let training_corpus = "
        Dr. Smith works at the hospital. He is a renowned surgeon.
        Mr. Jones teaches at the university. His students love him.
        The U.S. government has three branches. They provide checks and balances.
        Mrs. Brown owns a bakery. She makes excellent bread.
        The temperature is 98.6 degrees. That's normal body temperature.
        Prof. Williams wrote a book. It became a bestseller.
        
        Sometimes sentences start with lowercase. sometimes they don't.
        Abbreviations like etc. and e.g. are common. So are units like km. and kg.
        
        The meeting is at 3 p.m. today. Don't be late!
        We visited Washington, D.C. last summer. It was wonderful.
    ";

    println!("=== INTEGRATION TEST: nupunkt-rs ===\n");

    // Train model
    println!("1. Training model on corpus...");
    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_corpus, true).unwrap();
    println!("   Training complete!\n");

    // Create tokenizer
    let mut tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    // Test text with various challenges
    let test_text = "Dr. Smith said the patient arrived at 2 p.m. yesterday. \
                     The U.S. doctor was concerned. Mrs. Brown, the patient's \
                     mother, was worried too. The temperature was 101.5 degrees.";

    // Test 1: Basic tokenization
    println!("2. Basic tokenization:");
    let sentences = tokenizer.tokenize(test_text);
    for (i, sent) in sentences.iter().enumerate() {
        println!("   [{}] {}", i + 1, sent);
    }
    println!();

    // Test 2: Runtime adjustment - High precision (conservative)
    println!("3. Runtime adjustment - High precision (fewer breaks):");
    tokenizer.set_precision_recall_balance(0.9);
    let sentences_high = tokenizer.tokenize(test_text);
    println!(
        "   Found {} sentences with high precision",
        sentences_high.len()
    );

    // Test 3: Runtime adjustment - High recall (aggressive)
    println!("\n4. Runtime adjustment - High recall (more breaks):");
    tokenizer.set_precision_recall_balance(0.2);
    let sentences_low = tokenizer.tokenize(test_text);
    println!(
        "   Found {} sentences with high recall",
        sentences_low.len()
    );

    // Reset to default
    tokenizer.set_inference_config(InferenceConfig::default());

    // Test 4: Token analysis
    println!("\n5. Token-level analysis:");
    let analysis = tokenizer.analyze_tokens("Dr. Smith arrived.");

    for token in &analysis.tokens {
        if token.has_period {
            println!("   Token: '{}' at position {}", token.text, token.position);
            println!("     Decision: {:?}", token.decision);
            println!("     Confidence: {:.2}", token.confidence);
            println!("     In abbrev list: {}", token.in_abbrev_list);
            if let Some(score) = token.abbrev_score {
                println!("     Abbrev score: {:.2}", score);
            }
            println!("     Primary reason: {}", token.primary_reason);
        }
    }

    // Test 5: Explain decision
    println!("\n6. Decision explanation:");
    let explain_text = "Dr. Smith arrived.";
    if let Some(explanation) = tokenizer.explain_decision(explain_text, 0) {
        println!("{}", explanation);
    }

    // Test 6: Model statistics
    println!("\n7. Model statistics:");
    let stats = tokenizer.get_statistics();
    // Print first few lines of stats
    for line in stats.lines().take(10) {
        println!("   {}", line);
    }
    println!("   ...");

    // Test 7: Tokenize with analysis
    println!("\n8. Combined tokenization and analysis:");
    let (sentences_with_analysis, full_analysis) = tokenizer.tokenize_with_analysis(test_text);
    println!("   Sentences: {}", sentences_with_analysis.len());
    println!("   Tokens analyzed: {}", full_analysis.tokens.len());
    println!(
        "   Average confidence: {:.2}",
        full_analysis.statistics.average_confidence
    );
    println!(
        "   Low confidence decisions: {}",
        full_analysis.statistics.low_confidence_decisions
    );

    // Test 8: Debug mode
    println!("\n9. Debug mode test:");
    tokenizer.set_debug_mode(true);
    println!("   Debug mode enabled, tokenizing...");
    // This will print debug info to stderr
    let _ = tokenizer.tokenize("Dr. Smith said hello.");
    tokenizer.set_debug_mode(false);

    // Test 9: Different inference configurations
    println!("\n10. Testing different inference configurations:");

    // High precision - break less often
    let config = InferenceConfig {
        precision_recall_balance: 0.9,
    };
    tokenizer.set_inference_config(config);
    let high_precision = tokenizer.tokenize("Dr. Smith and Mr. Jones met.");
    println!("   High precision: {} sentences", high_precision.len());

    // High recall - break more often
    let config = InferenceConfig {
        precision_recall_balance: 0.1,
    };
    tokenizer.set_inference_config(config);
    let high_recall = tokenizer.tokenize("Dr. Smith and Mr. Jones met.");
    println!("   High recall: {} sentences", high_recall.len());

    // Balanced mode
    let config = InferenceConfig {
        precision_recall_balance: 0.5,
    };
    tokenizer.set_inference_config(config);
    let balanced = tokenizer.tokenize("Hello world. the next is lowercase.");
    println!("   Balanced: {} sentences", balanced.len());

    println!("\n=== All integration tests completed successfully! ===");
}

#[test]
fn test_edge_cases() {
    let tokenizer = PunktSentenceTokenizer::new();

    // Empty text
    assert_eq!(tokenizer.tokenize(""), Vec::<String>::new());

    // Single word
    assert_eq!(tokenizer.tokenize("Hello").len(), 1);

    // Only punctuation
    assert_eq!(tokenizer.tokenize("...").len(), 1);

    // Very long sentence
    let long_text = "This is a very ".repeat(100) + "long sentence.";
    assert!(!tokenizer.tokenize(&long_text).is_empty());

    // Unicode text
    let unicode_text = "Hello world. 你好世界。Здравствуй мир.";
    let sentences = tokenizer.tokenize(unicode_text);
    assert!(!sentences.is_empty());

    // Nested quotes and parentheses
    let complex = "He said, \"Dr. Smith (the surgeon) arrived.\" Then he left.";
    let sentences = tokenizer.tokenize(complex);
    assert!(!sentences.is_empty());
}

#[test]
fn test_thread_safety() {
    use std::sync::Arc;
    use std::thread;

    // Train a model
    let mut trainer = PunktTrainer::new();
    let params = trainer
        .train("Dr. Smith works here. He is busy.", false)
        .unwrap();
    let params = Arc::new(params);

    // Spawn multiple threads using the same parameters
    let mut handles = vec![];

    for i in 0..4 {
        let params_clone = params.clone();
        let handle = thread::spawn(move || {
            let tokenizer = PunktSentenceTokenizer::from_parameters(params_clone);
            let text = format!("Thread {} test. Dr. Smith arrived.", i);
            let sentences = tokenizer.tokenize(&text);
            sentences.len()
        });
        handles.push(handle);
    }

    // Wait for all threads
    for handle in handles {
        let result = handle.join().unwrap();
        assert!(result > 0);
    }
}
