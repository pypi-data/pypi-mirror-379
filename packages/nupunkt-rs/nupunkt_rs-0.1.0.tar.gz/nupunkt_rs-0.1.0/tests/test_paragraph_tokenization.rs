use nupunkt_rs::tokenizers::sentence::PunktSentenceTokenizer;
use nupunkt_rs::models::create_default_tokenizer;

#[test]
fn test_paragraph_tokenization_basic() {
    let tokenizer = PunktSentenceTokenizer::new();
    
    let text = "This is the first sentence. This is the second sentence.\n\nThis is a new paragraph. It has multiple sentences.";
    
    let paragraphs = tokenizer.tokenize_paragraphs(text);
    
    assert_eq!(paragraphs.len(), 2);
    assert_eq!(paragraphs[0].len(), 2);
    assert_eq!(paragraphs[1].len(), 2);
    
    assert!(paragraphs[0][0].contains("first sentence"));
    assert!(paragraphs[0][1].contains("second sentence"));
    assert!(paragraphs[1][0].contains("new paragraph"));
    assert!(paragraphs[1][1].contains("multiple sentences"));
}

#[test]
fn test_paragraph_tokenization_flat() {
    let tokenizer = PunktSentenceTokenizer::new();
    
    let text = "First sentence. Second sentence.\n\nNew paragraph. Another sentence.";
    
    let paragraphs = tokenizer.tokenize_paragraphs_flat(text);
    
    assert_eq!(paragraphs.len(), 2);
    assert!(paragraphs[0].contains("First sentence"));
    assert!(paragraphs[0].contains("Second sentence"));
    assert!(paragraphs[1].contains("New paragraph"));
    assert!(paragraphs[1].contains("Another sentence"));
}

#[test]
fn test_paragraph_with_abbreviations() {
    let tokenizer = create_default_tokenizer().expect("Failed to load default tokenizer");
    
    let text = "Dr. Smith works at the U.S. Department.\n\nMr. Jones works at NASA.";
    
    let paragraphs = tokenizer.tokenize_paragraphs(text);
    
    assert_eq!(paragraphs.len(), 2);
    assert_eq!(paragraphs[0].len(), 1); // Should not break at abbreviations
    assert_eq!(paragraphs[1].len(), 1);
}

#[test]
fn test_multiple_newlines() {
    let tokenizer = PunktSentenceTokenizer::new();
    
    let text = "First paragraph.\n\n\n\nSecond paragraph after multiple newlines.";
    
    let paragraphs = tokenizer.tokenize_paragraphs(text);
    
    assert_eq!(paragraphs.len(), 2);
    assert!(paragraphs[0][0].contains("First paragraph"));
    assert!(paragraphs[1][0].contains("Second paragraph"));
}

#[test]
fn test_single_paragraph() {
    let tokenizer = PunktSentenceTokenizer::new();
    
    let text = "This is a single paragraph. It has multiple sentences. But no paragraph breaks.";
    
    let paragraphs = tokenizer.tokenize_paragraphs(text);
    
    assert_eq!(paragraphs.len(), 1);
    assert_eq!(paragraphs[0].len(), 3);
}

#[test]
fn test_empty_text() {
    let tokenizer = PunktSentenceTokenizer::new();
    
    let paragraphs = tokenizer.tokenize_paragraphs("");
    assert_eq!(paragraphs.len(), 0);
    
    let paragraphs_flat = tokenizer.tokenize_paragraphs_flat("");
    assert_eq!(paragraphs_flat.len(), 0);
}

#[test]
fn test_legal_text_paragraphs() {
    let tokenizer = create_default_tokenizer().expect("Failed to load default tokenizer");
    
    let text = "As we explained in Daubert v. Merrell Dow Pharmaceuticals, Inc., 509 U.S. 579, 597 (1993), Rule 702's requirement establishes a standard.\n\nThis Court addressed the application in Kumho Tire Co. v. Carmichael, 526 U.S. 137 (1999).";
    
    let paragraphs = tokenizer.tokenize_paragraphs(text);
    
    assert_eq!(paragraphs.len(), 2);
    // Should not break at "v." since it's a legal abbreviation
    assert!(paragraphs[0][0].contains("Daubert v. Merrell"));
    assert!(paragraphs[1][0].contains("Kumho Tire Co. v. Carmichael"));
}

#[test]
fn test_paragraph_ending_combinations() {
    let tokenizer = PunktSentenceTokenizer::new();
    
    // Test various paragraph ending combinations
    let text1 = "End with period.\n\nNew paragraph.";
    let text2 = "End with exclamation!\n\nNew paragraph.";
    let text3 = "End with question?\n\nNew paragraph.";
    
    for text in &[text1, text2, text3] {
        let paragraphs = tokenizer.tokenize_paragraphs(text);
        assert_eq!(paragraphs.len(), 2, "Failed for text: {}", text);
    }
}