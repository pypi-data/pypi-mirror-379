use nupunkt_rs::core::SentenceTokenizer;
use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
/// Test that training and inference use the same decision logic
use nupunkt_rs::trainers::PunktTrainer;
use std::sync::Arc;

#[test]
fn test_training_inference_consistency() {
    // Create a trainer with default config
    let mut trainer = PunktTrainer::new();

    // Add some provided abbreviations
    trainer.add_abbreviations(vec!["Dr".to_string(), "Mr".to_string(), "v".to_string()]);

    // Simple training text with known patterns
    let training_text = "Dr. Smith works here. Mr. Jones v. the company. Hello world.";

    // Train on the text
    trainer.train(training_text, false).unwrap();
    let params = Arc::new(trainer.finalize_training(false).unwrap());

    // Debug: check what abbreviations we have
    println!(
        "Abbreviations in params: dr={}, mr={}, v={}",
        params.is_abbreviation("dr"),
        params.is_abbreviation("mr"),
        params.is_abbreviation("v")
    );

    // Create tokenizer with the trained parameters
    let tokenizer = PunktSentenceTokenizer::from_parameters(params.clone());

    // Test that the same text gets tokenized consistently
    let sentences = tokenizer.tokenize(training_text);

    // Debug: print what we got
    println!("Sentences produced: {}", sentences.len());
    for (i, s) in sentences.iter().enumerate() {
        println!("  {}: {}", i + 1, s);
    }

    // With provided abbreviations and consistent logic, we should get 3 sentences:
    // 1. "Dr. Smith works here."
    // 2. "Mr. Jones vs. the company."
    // 3. "Hello world."
    assert_eq!(
        sentences.len(),
        3,
        "Should produce 3 sentences with consistent logic"
    );

    // Verify the actual sentences
    assert!(sentences[0].contains("Dr.") && sentences[0].contains("Smith"));
    assert!(sentences[1].contains("Mr.") && sentences[1].contains("v."));
    assert!(sentences[2].contains("Hello") && sentences[2].contains("world"));
}

#[test]
fn test_training_learns_correct_patterns() {
    let mut trainer = PunktTrainer::new();

    // Add a provided abbreviation
    trainer.add_abbreviations(vec!["U.S".to_string()]);

    // Training text with patterns to learn
    let training_texts = vec![
        "The U.S. economy is growing. Markets are up.",
        "In the U.S. markets are volatile. Investors are cautious.",
        "The U.S. dollar strengthened. Trade increased.",
    ];

    for text in &training_texts {
        trainer.train(text, false).unwrap();
    }

    let params = Arc::new(trainer.finalize_training(false).unwrap());

    // Verify that U.S. is recognized as an abbreviation
    assert!(
        params.is_abbreviation("u.s"),
        "U.S. should be recognized as abbreviation"
    );

    // Test inference on similar text
    let tokenizer = PunktSentenceTokenizer::from_parameters(params);
    let test_text = "The U.S. government announced new policies. Citizens responded.";
    let sentences = tokenizer.tokenize(test_text);

    // Should get 2 sentences, not breaking after "U.S."
    assert_eq!(sentences.len(), 2, "Should not break after U.S.");
    assert!(sentences[0].contains("U.S.") && sentences[0].contains("government"));
    assert!(sentences[1].contains("Citizens"));
}

#[test]
fn test_whitespace_handling_consistency() {
    let mut trainer = PunktTrainer::new();

    // Text with various whitespace patterns
    let training_text = "First sentence.\nSecond sentence.\n\nNew paragraph here.";

    trainer.train(training_text, false).unwrap();
    let params = Arc::new(trainer.finalize_training(false).unwrap());

    let tokenizer = PunktSentenceTokenizer::from_parameters(params);
    let sentences = tokenizer.tokenize(training_text);

    // Should handle whitespace consistently
    assert_eq!(sentences.len(), 3, "Should produce 3 sentences");

    // Test that double newline (paragraph break) causes a break
    let para_text = "End of paragraph.\n\nStart of new paragraph.";
    let para_sentences = tokenizer.tokenize(para_text);
    assert_eq!(
        para_sentences.len(),
        2,
        "Paragraph break should cause sentence break"
    );
}
