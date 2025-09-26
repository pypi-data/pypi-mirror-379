use nupunkt_rs::analysis::BreakDecision;
use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
use nupunkt_rs::trainers::PunktTrainer;
use std::sync::Arc;

#[test]
fn test_analyze_tokens() {
    let training_text = "Dr. Smith is a doctor. He works at the hospital. 
                         Mr. Jones is a teacher. The U.S. has fifty states.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let test_text = "Dr. Smith arrived. He was late.";
    let analysis = tokenizer.analyze_tokens(test_text);

    // Check that we get token analysis
    assert!(!analysis.tokens.is_empty());

    // Find tokens with periods
    let period_tokens: Vec<_> = analysis.tokens.iter().filter(|t| t.has_period).collect();

    assert!(!period_tokens.is_empty());

    // Check that decisions were made
    for token in &period_tokens {
        assert!(token.confidence >= 0.0 && token.confidence <= 1.0);
        assert!(!token.primary_reason.is_empty());
    }

    // Check statistics
    assert_eq!(analysis.statistics.total_tokens, analysis.tokens.len());
    assert!(analysis.statistics.average_confidence >= 0.0);
    assert!(analysis.statistics.average_confidence <= 1.0);

    println!("Analysis statistics: {:?}", analysis.statistics);
}

#[test]
fn test_tokenize_with_analysis() {
    let training_text = "This is training data. It has multiple sentences. 
                         Some sentences are short. Others are longer with more words.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let test_text = "This is a test. Another sentence here.";
    let (sentences, analysis) = tokenizer.tokenize_with_analysis(test_text);

    // Should return both sentences and analysis
    assert!(!sentences.is_empty());
    assert!(!analysis.tokens.is_empty());

    // Sentences from both methods should match
    assert_eq!(sentences, analysis.sentences);

    println!("Sentences: {:?}", sentences);
    println!("Total tokens analyzed: {}", analysis.tokens.len());
}

#[test]
fn test_token_analysis_fields() {
    let mut trainer = PunktTrainer::new();
    let params = trainer
        .train("Dr. Smith works here. He is a doctor.", false)
        .unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let analysis = tokenizer.analyze_tokens("Dr. Smith said hello.");

    // Find the "Dr." token
    let dr_token = analysis
        .tokens
        .iter()
        .find(|t| t.text == "Dr.")
        .expect("Should find Dr. token");

    // Check that all fields are populated appropriately
    assert_eq!(dr_token.text, "Dr.");
    assert!(dr_token.has_period);
    assert!(dr_token.position < 10); // Should be near the beginning
    assert_eq!(dr_token.length, 3);

    // Should have abbreviation analysis
    if dr_token.in_abbrev_list {
        println!("Dr. is in abbreviation list");
    }
    if let Some(score) = dr_token.abbrev_score {
        println!("Dr. abbreviation score: {}", score);
    }

    // Check decision
    assert!(
        dr_token.decision == BreakDecision::NoBreak || dr_token.decision == BreakDecision::Break
    );

    // Should have factors
    assert!(!dr_token.factors.is_empty());
    for factor in &dr_token.factors {
        println!(
            "Factor: {:?} - {} (weight: {})",
            factor.factor_type, factor.description, factor.weight
        );
    }
}

#[test]
fn test_break_positions() {
    let training_text = "Sentence one. Sentence two. Sentence three.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let test_text = "First sentence. Second sentence. Third.";
    let analysis = tokenizer.analyze_tokens(test_text);

    // Check break positions
    assert!(!analysis.break_positions.is_empty());

    // Break positions should be at sentence boundaries
    for pos in &analysis.break_positions {
        // Position should be within text bounds
        assert!(*pos <= test_text.len());

        // Character before position should typically be punctuation
        if *pos > 0 {
            let prev_char = test_text.chars().nth(pos - 1);
            println!("Break at position {}, after '{:?}'", pos, prev_char);
        }
    }

    // Number of breaks should typically be one less than number of sentences
    // but this depends on how the text ends
    println!(
        "Breaks: {}, Sentences: {}",
        analysis.break_positions.len(),
        analysis.sentences.len()
    );
}

#[test]
fn test_confidence_levels() {
    let training_text = "Dr. Smith is here. Mr. Jones too. U.S.A. is a country.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let mut tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    // Test with different precision/recall settings
    let test_text = "Dr. Smith arrived. Maybe this continues.";

    // High precision - break less often
    tokenizer.set_precision_recall_balance(0.9);
    let analysis_high = tokenizer.analyze_tokens(test_text);

    // High recall - break more often
    tokenizer.set_precision_recall_balance(0.1);
    let analysis_low = tokenizer.analyze_tokens(test_text);

    // The number of breaks might differ
    println!(
        "High precision breaks: {}",
        analysis_high.statistics.total_breaks
    );
    println!(
        "High recall breaks: {}",
        analysis_low.statistics.total_breaks
    );

    // Check for low confidence decisions
    let low_conf_count = analysis_high.statistics.low_confidence_decisions;
    println!("Low confidence decisions: {}", low_conf_count);
}
