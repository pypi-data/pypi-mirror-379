use nupunkt_rs::parameters::PunktParameters;
/// Test that verifies proper position tracking for pathological cases
use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
use std::sync::Arc;

#[test]
fn test_pathological_repeated_tokens() {
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(PunktParameters::default()));

    // Pathological case: many repeated "the the the"
    let text = "the the the cat the the dog the";

    let analysis = tokenizer.analyze_tokens(text);

    // Each "the" should have a unique, increasing position
    let the_positions: Vec<usize> = analysis
        .tokens
        .iter()
        .filter(|t| t.text == "the")
        .map(|t| t.position)
        .collect();

    // We should have 6 instances of "the"
    assert_eq!(the_positions.len(), 6, "Should find 6 instances of 'the'");

    // Positions should be: 0, 4, 8, 16, 20, 28
    let expected = vec![0, 4, 8, 16, 20, 28];
    assert_eq!(
        the_positions, expected,
        "Positions should match expected values"
    );

    // Verify each position is unique and increasing
    for i in 1..the_positions.len() {
        assert!(
            the_positions[i] > the_positions[i - 1],
            "Position {} should be greater than position {}",
            the_positions[i],
            the_positions[i - 1]
        );
    }
}

#[test]
fn test_unicode_positions() {
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(PunktParameters::default()));

    // Test with Unicode characters (multi-byte)
    let text = "Café résumé naïve";

    let analysis = tokenizer.analyze_tokens(text);

    // Positions should be in characters, not bytes
    assert_eq!(analysis.tokens[0].position, 0); // Café at 0
    assert_eq!(analysis.tokens[1].position, 5); // résumé at 5
    assert_eq!(analysis.tokens[2].position, 12); // naïve at 12
}
