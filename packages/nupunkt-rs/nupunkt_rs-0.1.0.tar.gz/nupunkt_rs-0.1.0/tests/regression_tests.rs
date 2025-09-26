/// Regression tests for critical bugs identified in code review
use nupunkt_rs::core::SentenceTokenizer;
use nupunkt_rs::parameters::PunktParameters;
use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
use nupunkt_rs::trainers::PunktTrainer;
use std::sync::Arc;

#[test]
fn test_collocation_parity_single_vs_incremental() {
    // Test that single-pass and incremental training produce the same collocations
    let test_text = r#"
    Dr. Smith works at the hospital. Mr. Jones is his patient.
    The U.S. economy is strong. Fed. regulations apply here.
    v. Smith is a famous case. Co. executives met today.
    "#;

    // Single-pass training
    let mut single_trainer = PunktTrainer::new();
    single_trainer
        .load_abbreviations_from_json("data/legal_abbreviations.json")
        .ok();
    let single_params = single_trainer.train(test_text, false).unwrap();

    // Incremental training (simulate streaming)
    let mut incremental_trainer = PunktTrainer::new();
    incremental_trainer
        .load_abbreviations_from_json("data/legal_abbreviations.json")
        .ok();

    // Split text into chunks to simulate streaming
    let chunks: Vec<&str> = test_text.split('\n').collect();
    for chunk in chunks {
        incremental_trainer.train_incremental(chunk, false).unwrap();
    }
    let incremental_params = incremental_trainer.finalize_training(false).unwrap();

    // Compare collocation sets - allow some variation due to chunking
    let single_collocations = &single_params.collocations;
    let incremental_collocations = &incremental_params.collocations;

    println!("Single-pass collocations: {:?}", single_collocations);
    println!("Incremental collocations: {:?}", incremental_collocations);

    // Find the differences
    let missing_in_incremental: Vec<_> = single_collocations
        .difference(incremental_collocations)
        .collect();
    let extra_in_incremental: Vec<_> = incremental_collocations
        .difference(single_collocations)
        .collect();

    if !missing_in_incremental.is_empty() {
        println!("Missing in incremental: {:?}", missing_in_incremental);
    }
    if !extra_in_incremental.is_empty() {
        println!("Extra in incremental: {:?}", extra_in_incremental);
    }

    // Allow small differences due to edge effects in chunking
    let diff_count = missing_in_incremental.len() + extra_in_incremental.len();
    assert!(
        diff_count <= 2,
        "Too many differences between single-pass and incremental: {} differences",
        diff_count
    );
}

#[test]
fn test_provided_abbreviations_protected_from_whitespace() {
    // Test that provided abbreviations are not broken by whitespace
    let mut params = PunktParameters::new();

    // Add some provided abbreviations
    params.add_provided_abbreviation("v", "test");
    params.add_provided_abbreviation("U.S", "test");
    params.add_provided_abbreviation("Fed", "test");
    params.add_provided_abbreviation("Co", "test");
    params.add_provided_abbreviation("Id", "test");
    params.add_provided_abbreviation("Ibid", "test");

    params.freeze();

    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    // Test cases with various whitespace patterns
    let test_cases = vec![
        // Single newline after abbreviation (common in wrapped text)
        ("This is v.\nSmith case.", vec!["This is v. Smith case."]),
        // Double space after abbreviation
        (
            "The U.S.  economy is strong.",
            vec!["The U.S. economy is strong."],
        ),
        // Abbreviation at line end with capitalized next word
        (
            "See Fed.\nRegulations apply.",
            vec!["See Fed. Regulations apply."],
        ),
        // Multiple abbreviations with whitespace
        (
            "The Co.\n\nExecutives met.",
            vec!["The Co.", "Executives met."],
        ), // Paragraph break should still work
        // Legal citations with newlines (these are common soft wraps in legal text)
        ("Id.\nat 234.", vec!["Id. at 234."]),
        // Note: "p." is also an abbreviation (page), but without it being marked,
        // the period after "p" followed by a number might look like a sentence break
    ];

    for (input, expected) in test_cases {
        let result = tokenizer.tokenize(input);
        assert_eq!(
            result, expected,
            "\nInput: {:?}\nExpected: {:?}\nGot: {:?}",
            input, expected, result
        );
    }
}

#[test]
fn test_whitespace_not_amplified() {
    // Test that whitespace evidence is not amplified to force breaks
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(PunktParameters::default()));

    // These should NOT break just because of a single newline
    let test_cases = vec![
        // Mid-sentence newline (soft wrap)
        (
            "This is a long sentence that\nwraps to the next line.",
            vec!["This is a long sentence that wraps to the next line."],
        ),
        // Multiple soft wraps
        (
            "The quick brown\nfox jumps over\nthe lazy dog.",
            vec!["The quick brown fox jumps over the lazy dog."],
        ),
    ];

    for (input, expected) in test_cases {
        let result = tokenizer.tokenize(input);
        assert_eq!(
            result, expected,
            "\nInput: {:?}\nExpected: {:?}\nGot: {:?}",
            input, expected, result
        );
    }
}

#[test]
fn test_paragraph_breaks_still_work() {
    // Test that genuine paragraph breaks (double newline) still cause sentence breaks
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(PunktParameters::default()));

    let input = "First paragraph ends here.\n\nSecond paragraph starts here.";
    let expected = vec![
        "First paragraph ends here.",
        "Second paragraph starts here.",
    ];

    let result = tokenizer.tokenize(input);
    assert_eq!(result, expected);
}

#[test]
fn test_case_normalization_consistency() {
    // Test that abbreviations are matched case-insensitively
    let mut params = PunktParameters::new();

    // Add abbreviation in lowercase
    params.add_provided_abbreviation("dr", "test");

    // Should match all case variants
    assert!(params.is_abbreviation("dr"));
    assert!(params.is_abbreviation("Dr")); // This should be normalized
    assert!(params.is_abbreviation("DR")); // This too

    // Test with period variants
    params.add_provided_abbreviation("U.S.", "test"); // Added with period
    assert!(params.is_abbreviation("u.s")); // Should be stored without trailing period, lowercase
    assert!(params.is_abbreviation("U.S"));
}
