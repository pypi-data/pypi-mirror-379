/// Test that the precision_recall_balance parameter works correctly
use nupunkt_rs::core::SentenceTokenizer;
use nupunkt_rs::tokenizers::{sentence::InferenceConfig, PunktSentenceTokenizer};
use nupunkt_rs::trainers::PunktTrainer;
use std::sync::Arc;

#[test]
fn test_precision_recall_parameter_effect() {
    // Train on sample text with ambiguous boundaries
    let training_text = "
        Dr. Smith works at the hospital. He is a doctor.
        Dr. Jones teaches at the university. She has a PhD.
        Mr. Brown runs the clinic. The clinic is busy.
        The U.S. has fifty states. California is one of them.
        The meeting is at 3 p.m. today. Don't be late.
        We close at 5 p.m. daily. Please arrive before then.
    ";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let params = Arc::new(params);

    // Test text with multiple potential boundaries
    let test_text = "Dr. Smith arrived at the U.S. embassy at 3 p.m. yesterday.";

    // Test 1: Maximum recall (0.0) - should break more often
    let mut tokenizer = PunktSentenceTokenizer::from_parameters(params.clone());
    tokenizer.set_max_recall();
    let sentences_max_recall = tokenizer.tokenize(test_text);
    println!("Max recall (0.0): {} sentences", sentences_max_recall.len());
    for s in &sentences_max_recall {
        println!("  - {}", s);
    }

    // Test 2: Balanced (0.5) - moderate breaking
    tokenizer.set_balanced();
    let sentences_balanced = tokenizer.tokenize(test_text);
    println!("Balanced (0.5): {} sentences", sentences_balanced.len());
    for s in &sentences_balanced {
        println!("  - {}", s);
    }

    // Test 3: Maximum precision (1.0) - should break less often
    tokenizer.set_max_precision();
    let sentences_max_precision = tokenizer.tokenize(test_text);
    println!(
        "Max precision (1.0): {} sentences",
        sentences_max_precision.len()
    );
    for s in &sentences_max_precision {
        println!("  - {}", s);
    }

    // Verify the parameter has an effect
    // In recall mode, we expect more breaks (or equal)
    // In precision mode, we expect fewer breaks (or equal)
    assert!(
        sentences_max_recall.len() >= sentences_max_precision.len(),
        "Max recall should produce at least as many sentences as max precision"
    );
}

#[test]
fn test_precision_recall_gradual_change() {
    // Train a model
    let training_text = "
        This is a sentence. Here is another one.
        Dr. Smith works here. Mr. Jones does too.
        The U.S. is large. It has many states.
    ";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let params = Arc::new(params);

    // Test text with ambiguous boundaries
    let test_text =
        "Dr. Smith studied at the U.S. university. Mr. Jones graduated from M.I.T. yesterday.";

    // Test at different precision/recall levels
    let levels = vec![0.0, 0.25, 0.5, 0.75, 1.0];
    let mut previous_count = None;

    for level in levels {
        let mut tokenizer = PunktSentenceTokenizer::from_parameters(params.clone());
        tokenizer.set_precision_recall_balance(level);
        let sentences = tokenizer.tokenize(test_text);

        println!("PR={:.2}: {} sentences", level, sentences.len());

        // Generally, higher precision/recall should lead to fewer or equal breaks
        if let Some(prev) = previous_count {
            assert!(
                sentences.len() <= prev || sentences.len() == prev,
                "Sentence count should generally decrease or stay the same as PR increases"
            );
        }
        previous_count = Some(sentences.len());
    }
}

#[test]
fn test_inference_config_creation() {
    // Test creating InferenceConfig with different values
    let config_recall = InferenceConfig {
        precision_recall_balance: 0.0,
    };
    assert_eq!(config_recall.precision_recall_balance, 0.0);

    let config_balanced = InferenceConfig::default();
    assert_eq!(config_balanced.precision_recall_balance, 0.5);

    let config_precision = InferenceConfig {
        precision_recall_balance: 1.0,
    };
    assert_eq!(config_precision.precision_recall_balance, 1.0);
}

#[test]
fn test_analysis_shows_threshold_info() {
    // Train a simple model
    let training_text = "This is text. More text here.";
    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let params = Arc::new(params);

    let test_text = "Dr. Smith arrived. Mr. Jones left.";

    // Test with different PR values and check that analysis shows the threshold
    for pr in [0.0, 0.5, 1.0] {
        let mut tokenizer = PunktSentenceTokenizer::from_parameters(params.clone());
        tokenizer.set_precision_recall_balance(pr);

        let analysis = tokenizer.analyze_tokens(test_text);

        // The primary_reason should include threshold info
        for token in &analysis.tokens {
            if token.has_period && token.primary_reason.contains("[conf=") {
                println!("PR={:.1}: {}", pr, token.primary_reason);
                // Verify threshold changes with PR
                let expected_threshold = 0.3 + 0.4 * pr;
                assert!(
                    token
                        .primary_reason
                        .contains(&format!("thr={:.2}", expected_threshold)),
                    "Primary reason should show correct threshold"
                );
            }
        }
    }
}

#[test]
fn test_extreme_text_cases() {
    // Test with text that has many abbreviations
    let training_text = "
        Dr. Mr. Mrs. Ms. Prof. Rev. Sr. Jr. Ph.D. M.D. B.A. M.A.
        U.S. U.K. U.N. E.U. etc. vs. Inc. Corp. Ltd. Co.
    ";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let params = Arc::new(params);

    // Text with many potential breaks
    let test_text = "Dr. Smith and Mr. Jones work at ABC Inc. in the U.S. today.";

    let mut tokenizer = PunktSentenceTokenizer::from_parameters(params.clone());

    // In max recall mode, might break more
    tokenizer.set_max_recall();
    let recall_sentences = tokenizer.tokenize(test_text);

    // In max precision mode, should preserve as single sentence
    tokenizer.set_max_precision();
    let precision_sentences = tokenizer.tokenize(test_text);

    println!("Recall mode: {} sentences", recall_sentences.len());
    println!("Precision mode: {} sentences", precision_sentences.len());

    // Precision mode should have fewer or equal sentences
    assert!(precision_sentences.len() <= recall_sentences.len());
}
