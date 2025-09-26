use nupunkt_rs::parameters::PunktParameters;
/// Test that token positions are tracked correctly even with repeated tokens
use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
use std::sync::Arc;

#[test]
fn test_repeated_token_positions() {
    // Create a tokenizer
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(PunktParameters::default()));

    // Text with repeated tokens "the"
    let text = "The cat sat on the mat. The dog ran.";

    // Analyze tokens
    let analysis = tokenizer.analyze_tokens(text);

    // Find all instances of "the" (case variations)
    let the_positions: Vec<(usize, &str)> = analysis
        .tokens
        .iter()
        .filter(|t| t.text.to_lowercase() == "the")
        .map(|t| (t.position, t.text.as_str()))
        .collect();

    // Should find 3 instances of "the/The"
    assert_eq!(the_positions.len(), 3, "Should find 3 instances of 'the'");

    // Check that positions are different
    assert_eq!(the_positions[0].0, 0, "First 'The' at position 0");
    assert_eq!(the_positions[1].0, 15, "Second 'the' at position 15");
    assert_eq!(the_positions[2].0, 24, "Third 'The' at position 24");

    // Verify the actual text at those positions
    assert_eq!(&text[0..3], "The");
    assert_eq!(&text[15..18], "the");
    assert_eq!(&text[24..27], "The");
}

#[test]
fn test_token_positions_with_punctuation() {
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(PunktParameters::default()));

    // Text with various punctuation (be careful with how punctuation is tokenized)
    let text = "Hello, world! How are you? I'm fine.";

    let analysis = tokenizer.analyze_tokens(text);

    // Check specific tokens (note: punctuation is included with tokens)
    let hello = analysis
        .tokens
        .iter()
        .find(|t| t.text.starts_with("Hello"))
        .unwrap();
    let world = analysis
        .tokens
        .iter()
        .find(|t| t.text.starts_with("world"))
        .unwrap();
    let how = analysis.tokens.iter().find(|t| t.text == "How").unwrap();

    assert_eq!(hello.position, 0, "Hello, at position 0");
    assert_eq!(world.position, 7, "world! at position 7");
    assert_eq!(how.position, 14, "How at position 14"); // After "world! "

    // Verify actual text
    assert_eq!(&text[0..6], "Hello,");
    assert_eq!(&text[7..13], "world!");
    assert_eq!(&text[14..17], "How");
}

#[test]
fn test_consecutive_repeated_tokens() {
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(PunktParameters::default()));

    // Text with consecutive repeated words
    let text = "No no no! Yes yes yes.";

    let analysis = tokenizer.analyze_tokens(text);

    // Find all tokens containing "no" (some may have punctuation)
    let no_tokens: Vec<usize> = analysis
        .tokens
        .iter()
        .filter(|t| t.text.to_lowercase().starts_with("no"))
        .map(|t| t.position)
        .collect();

    // Should find 3 different positions
    assert_eq!(no_tokens.len(), 3);
    assert_eq!(no_tokens[0], 0); // First "No"
    assert_eq!(no_tokens[1], 3); // Second "no"
    assert_eq!(no_tokens[2], 6); // Third "no!"

    // Find all tokens containing "yes" (some may have punctuation)
    let yes_tokens: Vec<usize> = analysis
        .tokens
        .iter()
        .filter(|t| t.text.to_lowercase().starts_with("yes"))
        .map(|t| t.position)
        .collect();

    assert_eq!(yes_tokens.len(), 3);
    assert_eq!(yes_tokens[0], 10); // First "Yes" starts at 10
    assert_eq!(yes_tokens[1], 14); // Second "yes" starts at 14
    assert_eq!(yes_tokens[2], 18); // Third "yes." starts at 18
}
