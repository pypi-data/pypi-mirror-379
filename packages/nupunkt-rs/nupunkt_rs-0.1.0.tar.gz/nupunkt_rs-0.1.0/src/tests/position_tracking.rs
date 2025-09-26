/// Tests for position tracking in tokenization
use crate::core::SentenceTokenizer;
use crate::models::create_default_tokenizer;

#[test]
fn test_duplicate_tokens_position_tracking() {
    let tokenizer = create_default_tokenizer().expect("Failed to load default model");
    
    // Text with duplicate words that would fail with .find()
    let text = "The cat sat on the mat. The cat jumped off the mat.";
    
    let spans = tokenizer.tokenize_spans(text);
    
    // Should get two sentences with correct spans
    assert_eq!(spans.len(), 2);
    
    // First sentence: "The cat sat on the mat."
    assert_eq!(&text[spans[0].0..spans[0].1], "The cat sat on the mat.");
    
    // Second sentence: "The cat jumped off the mat."
    assert_eq!(&text[spans[1].0..spans[1].1], "The cat jumped off the mat.");
}

#[test]
fn test_unicode_position_tracking() {
    let tokenizer = create_default_tokenizer().expect("Failed to load default model");
    
    // Text with multi-byte Unicode characters
    let text = "Hello 世界! This is a test. Unicode café works.";
    
    let spans = tokenizer.tokenize_spans(text);
    
    // Should handle multi-byte characters correctly
    assert_eq!(spans.len(), 3);
    
    // Verify each span extracts the correct text
    assert_eq!(&text[spans[0].0..spans[0].1], "Hello 世界!");
    assert_eq!(&text[spans[1].0..spans[1].1], "This is a test.");
    assert_eq!(&text[spans[2].0..spans[2].1], "Unicode café works.");
}

#[test]
fn test_repeated_pattern_position_tracking() {
    let tokenizer = create_default_tokenizer().expect("Failed to load default model");
    
    // Text with many repeated patterns
    let text = "Test test test. Test test. Test.";
    
    let spans = tokenizer.tokenize_spans(text);
    
    assert_eq!(spans.len(), 3);
    assert_eq!(&text[spans[0].0..spans[0].1], "Test test test.");
    assert_eq!(&text[spans[1].0..spans[1].1], "Test test.");
    assert_eq!(&text[spans[2].0..spans[2].1], "Test.");
}

#[test]
fn test_emoji_position_tracking() {
    let tokenizer = create_default_tokenizer().expect("Failed to load default model");
    
    // Text with emojis (multi-byte)
    let text = "Hello! 😊 How are you? I'm great! 🎉";
    
    let spans = tokenizer.tokenize_spans(text);
    
    // Each span should correctly handle emoji byte positions
    for span in &spans {
        // This should not panic - the spans should be valid byte positions
        let _ = &text[span.0..span.1];
    }
    
    // Verify we get expected sentences
    assert!(spans.len() >= 2);
}

#[test]
fn test_newline_position_tracking() {
    let tokenizer = create_default_tokenizer().expect("Failed to load default model");
    
    // Text with newlines
    let text = "First sentence.\nSecond sentence.\n\nThird sentence after blank line.";
    
    let spans = tokenizer.tokenize_spans(text);
    
    assert_eq!(spans.len(), 3);
    assert_eq!(&text[spans[0].0..spans[0].1], "First sentence.");
    assert_eq!(&text[spans[1].0..spans[1].1], "Second sentence.");
    assert_eq!(&text[spans[2].0..spans[2].1], "Third sentence after blank line.");
}

#[test]
fn test_complex_duplicate_position_tracking() {
    let tokenizer = create_default_tokenizer().expect("Failed to load default model");
    
    // Complex text with many duplicates
    let text = "Dr. Smith and Dr. Jones met Dr. Brown. Dr. Smith said hello to Dr. Jones and Dr. Brown.";
    
    let spans = tokenizer.tokenize_spans(text);
    
    // Should handle all the duplicate "Dr." tokens correctly
    assert_eq!(spans.len(), 2);
    
    // Verify the spans are correct
    assert_eq!(&text[spans[0].0..spans[0].1], "Dr. Smith and Dr. Jones met Dr. Brown.");
    assert_eq!(&text[spans[1].0..spans[1].1], "Dr. Smith said hello to Dr. Jones and Dr. Brown.");
}

#[test]
fn test_position_tracking_performance() {
    use std::time::Instant;
    
    let tokenizer = create_default_tokenizer().expect("Failed to load default model");
    
    // Create a large text with many duplicates
    let sentence = "The quick brown fox jumps over the lazy dog. ";
    let large_text = sentence.repeat(1000); // 1000 repetitions
    
    let start = Instant::now();
    let spans = tokenizer.tokenize_spans(&large_text);
    let duration = start.elapsed();
    
    // Should be fast even with many duplicates
    assert!(duration.as_millis() < 100, "Tokenization took too long: {:?}", duration);
    
    // Should have found all 1000 sentences
    assert_eq!(spans.len(), 1000);
    
    // Spot check a few spans
    assert_eq!(&large_text[spans[0].0..spans[0].1], sentence.trim());
    assert_eq!(&large_text[spans[500].0..spans[500].1], sentence.trim());
    assert_eq!(&large_text[spans[999].0..spans[999].1], sentence.trim());
}