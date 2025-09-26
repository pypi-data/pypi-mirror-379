use nupunkt_rs::core::SentenceTokenizer; // Need this trait in scope
use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
/// Integration tests for abbreviation handling
/// These tests demonstrate the current bugs and expected behavior after fixes
use nupunkt_rs::trainers::PunktTrainer;
use std::sync::Arc;

/// This test currently FAILS but should pass after implementing provided abbreviations
#[test]
#[ignore] // Remove ignore after implementing the fix
fn test_provided_abbreviations_prevent_bad_learning() {
    // Setup: Create trainer with provided abbreviations
    let mut trainer = PunktTrainer::new();

    // Load legal abbreviations BEFORE training
    let abbreviations = vec!["v".to_string(), "U.S".to_string()];
    trainer.add_abbreviations(abbreviations);

    // Train on text with legal citations
    let training_text = r#"
        The case Smith v. Jones established precedent.
        In Brown v. Board of Education, the court ruled differently.
        The U.S. Supreme Court agreed.
        Microsoft v. United States was also relevant.
    "#;

    let params = trainer
        .train(training_text, false)
        .expect("Training should succeed");

    // CRITICAL ASSERTIONS:

    // 1. "v" should be an abbreviation
    assert!(
        params.is_abbreviation("v"),
        "v should be recognized as an abbreviation"
    );

    // 2. Names after "v." should NOT be sentence starters
    assert!(
        !params.is_sent_starter("Jones"),
        "Jones should NOT be a sentence starter (it follows v.)"
    );
    assert!(
        !params.is_sent_starter("Board"),
        "Board should NOT be a sentence starter (it follows v.)"
    );
    assert!(
        !params.is_sent_starter("United"),
        "United should NOT be a sentence starter when following v."
    );

    // 3. The tokenizer should not break at "v."
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));
    let test_text = "The case was Smith v. Jones in 2023.";
    let sentences = tokenizer.tokenize(test_text);

    assert_eq!(
        sentences.len(),
        1,
        "Should not break at 'v.' - got {} sentences: {:?}",
        sentences.len(),
        sentences
    );
}

/// Test that provided abbreviations work even at very low precision_recall values
#[test]
#[ignore] // Remove after implementing provided abbreviations
fn test_provided_abbreviations_work_at_all_pr_values() {
    let mut trainer = PunktTrainer::new();
    trainer.add_abbreviations(vec!["v".to_string()]);

    let params = trainer
        .train("Smith v. Jones was the case.", false)
        .unwrap();
    let mut tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    // Test at various PR values
    for pr in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] {
        tokenizer.set_precision_recall_balance(pr);
        let sentences = tokenizer.tokenize("Smith v. Jones");

        assert_eq!(
            sentences.len(),
            1,
            "At PR={}, should not break at 'v.' but got {} sentences: {:?}",
            pr,
            sentences.len(),
            sentences
        );
    }
}

/// Test that we can distinguish provided from learned abbreviations
#[test]
#[ignore] // Requires AbbreviationType implementation
fn test_distinguish_provided_from_learned() {
    let mut trainer = PunktTrainer::new();

    // Add "Mr" as provided
    trainer.add_abbreviations(vec!["Mr".to_string()]);

    // Train on text that will learn "Dr" statistically
    let text = r#"
        Mr. Smith arrived first.
        Dr. Jones came later. Dr. Brown was there. Dr. Wilson too.
        Dr. Anderson joined. Dr. Taylor as well. Dr. Thomas came.
    "#;

    let params = trainer.train(text, false).unwrap();

    // Both should be abbreviations
    assert!(params.is_abbreviation("Mr"), "Mr should be an abbreviation");
    assert!(
        params.is_abbreviation("Dr"),
        "Dr should be learned as abbreviation"
    );

    // But we should be able to distinguish them
    // These methods don't exist yet - will add with AbbreviationType
    // assert!(params.is_provided_abbreviation("Mr"), "Mr should be marked as provided");
    // assert!(!params.is_provided_abbreviation("Dr"), "Dr should be marked as learned");
}

/// Test the actual annotation phase respects provided abbreviations
#[test]
#[ignore] // Requires internal API changes
fn test_annotation_phase_respects_provided() {
    // This test requires access to internal annotation methods
    // Will need to expose them or test differently

    // The key behavior we want:
    // 1. Load "v" as abbreviation
    // 2. During annotation of "v. Jones", the "v." token should have:
    //    - abbr = true
    //    - sentbreak = false
    // 3. This prevents "Jones" from being learned as sentence starter
}

/// Regression test for the weight cancellation bug
#[test]
fn test_weights_dont_cancel() {
    use nupunkt_rs::parameters::DecisionWeights;

    let weights = DecisionWeights::default();

    // At PR=0.4, check that abbreviation and capitalization don't cancel
    let pr = 0.4;
    let abbrev_weight = weights.provided_abbrev_weight(pr);
    let capital_weight = weights.capital_weight(pr);

    let total = abbrev_weight + capital_weight;

    // They should NOT cancel out
    assert!(
        total.abs() > 0.1,
        "Weights should not cancel: abbrev={:.3} + capital={:.3} = {:.3}",
        abbrev_weight,
        capital_weight,
        total
    );

    // Abbreviation should dominate (negative total means don't break)
    assert!(
        total < 0.0,
        "Total weight should favor not breaking for abbreviations: {:.3}",
        total
    );
}
