use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
use nupunkt_rs::trainers::PunktTrainer;
use std::sync::Arc;

#[test]
fn test_explain_decision_basic() {
    let training_text = "Dr. Smith is a doctor. He works at the hospital. 
                         Mr. Jones is a teacher. He teaches math.
                         The U.S. has fifty states. It is a large country.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let test_text = "Dr. Smith arrived. He was late.";

    // Try to explain decision at position of "Dr."
    let explanation = tokenizer.explain_decision(test_text, 0);
    assert!(explanation.is_some());

    let explanation_text = explanation.unwrap();
    println!("Explanation for position 0:\n{}", explanation_text);

    // Check that explanation contains expected elements
    assert!(explanation_text.contains("Token:"));
    assert!(explanation_text.contains("Decision:"));
    assert!(explanation_text.contains("Confidence:"));
    assert!(explanation_text.contains("Primary reason:"));
}

#[test]
fn test_explain_decision_at_period() {
    let training_text = "This is training. More training here. And more.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let test_text = "Hello world. Next sentence.";

    // Find position of period after "world"
    let period_pos = test_text.find("world.").unwrap() + 5; // Position of period

    let explanation = tokenizer.explain_decision(test_text, period_pos);
    assert!(explanation.is_some());

    let explanation_text = explanation.unwrap();
    println!("Explanation for period position:\n{}", explanation_text);

    // Should contain analysis details
    assert!(explanation_text.contains("Analysis:"));
    assert!(explanation_text.contains("abbreviation list:"));
}

#[test]
fn test_explain_decision_with_factors() {
    let training_text = "Dr. Smith and Mr. Jones work together. They are colleagues.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let test_text = "Dr. Smith said something important.";

    // Get explanation for "Dr."
    let explanation = tokenizer.explain_decision(test_text, 0);
    assert!(explanation.is_some());

    let explanation_text = explanation.unwrap();

    // Should contain decision factors
    if explanation_text.contains("Decision factors:") {
        assert!(explanation_text.contains("weight:"));
        assert!(
            explanation_text.contains("Abbreviation")
                || explanation_text.contains("Capitalization")
                || explanation_text.contains("Score")
        );
        println!("Found decision factors in explanation");
    }

    println!("Full explanation:\n{}", explanation_text);
}

#[test]
fn test_explain_decision_no_period() {
    let tokenizer = PunktSentenceTokenizer::new();
    let test_text = "Hello world no period here";

    // Try to explain at a position without period
    let explanation = tokenizer.explain_decision(test_text, 5); // Position in "world"

    if let Some(exp) = explanation {
        println!("Explanation for non-period token:\n{}", exp);
        assert!(exp.contains("Decision: Continue"));
    }
}

#[test]
fn test_explain_decision_abbreviation() {
    let training_text = "Dr. Smith is a doctor. Mr. Jones is not.
                         The U.S.A. is a country. So is the U.K. today.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    // Test with known abbreviation
    let test_text = "Dr. Smith and Mr. Jones met.";

    // Explain "Dr."
    let dr_explanation = tokenizer.explain_decision(test_text, 0);
    assert!(dr_explanation.is_some());

    let dr_exp_text = dr_explanation.unwrap();
    println!("Explanation for 'Dr.':\n{}", dr_exp_text);

    // Should indicate it's an abbreviation
    assert!(dr_exp_text.contains("Dr."));
    if dr_exp_text.contains("In abbreviation list: YES") {
        println!("Correctly identified as abbreviation");
    }

    // Explain "Mr."
    let mr_pos = test_text.find("Mr.").unwrap();
    let mr_explanation = tokenizer.explain_decision(test_text, mr_pos);
    assert!(mr_explanation.is_some());

    let mr_exp_text = mr_explanation.unwrap();
    println!("\nExplanation for 'Mr.':\n{}", mr_exp_text);
}

#[test]
fn test_explain_decision_collocation() {
    let training_text = "Hello Mr. Jones. Goodbye Mr. Smith. 
                         See you Mr. Brown. Thank you Mr. White.";

    let mut trainer = PunktTrainer::new();
    let params = trainer.train(training_text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    let test_text = "Hello Mr. Jones today.";

    // Explain decision after "Mr."
    let mr_pos = test_text.find("Mr.").unwrap();
    let explanation = tokenizer.explain_decision(test_text, mr_pos);

    if let Some(exp) = explanation {
        println!("Collocation explanation:\n{}", exp);

        // Might indicate collocation
        if exp.contains("Forms collocation: YES") {
            println!("Identified collocation pattern");
        }
    }
}

#[test]
fn test_explain_decision_invalid_position() {
    let tokenizer = PunktSentenceTokenizer::new();
    let test_text = "Hello world.";

    // Try position beyond text length
    let explanation = tokenizer.explain_decision(test_text, 1000);
    assert!(explanation.is_none());

    // Try empty text
    let explanation_empty = tokenizer.explain_decision("", 0);
    assert!(explanation_empty.is_none());
}
