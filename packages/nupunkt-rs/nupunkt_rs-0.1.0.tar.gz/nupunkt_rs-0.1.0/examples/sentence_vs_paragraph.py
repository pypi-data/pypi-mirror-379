#!/usr/bin/env python3
"""
Example demonstrating the difference between sentence and paragraph tokenization.
Both functions now properly load and cache the default model, handling legal abbreviations correctly.
"""

import nupunkt_rs

# Sample legal text with paragraph breaks
legal_text = """As we explained in Daubert v. Merrell Dow Pharmaceuticals, Inc., 509 U.S. 579, 597 (1993), Rule 702's requirement that an expert's testimony pertain to "scientific knowledge" establishes a standard of evidentiary reliability. This Court addressed the application of this standard to technical, as opposed to scientific, expert testimony in Kumho Tire Co. v. Carmichael, 526 U.S. 137 (1999).

There, we explained that the gatekeeping inquiry must be tied to the facts of a particular case. Id. at 150. This Court further noted that Rule 702 was amended in response to Daubert and this Court's subsequent cases. See Fed. Rule Evid. 702, Advisory Committee Notes to 2000 Amendments.

The amendment affirms the trial court's role as gatekeeper but provides that "all types of expert testimony present questions of admissibility for the trial court." Ibid. Consequently, whether the specific expert testimony on the question at issue focuses on specialized observations, the specialized translation of those observations into theory, a specialized theory itself, or the application of such a theory in a particular case, the expert's testimony often will rest "upon an experience confessedly foreign in kind to [the jury's] own." Hand, Historical and Practical Considerations Regarding Expert Testimony, 15 Harv. L. Rev. 40, 54 (1901)."""

def demonstrate_sent_tokenize():
    """Demonstrate sentence tokenization."""
    print("=" * 80)
    print("SENTENCE TOKENIZATION (sent_tokenize)")
    print("=" * 80)
    
    sentences = nupunkt_rs.sent_tokenize(legal_text)
    
    print(f"\nFound {len(sentences)} sentences:\n")
    for i, sentence in enumerate(sentences, 1):
        print(f"Sentence {i}:")
        print(f"  {sentence[:100]}..." if len(sentence) > 100 else f"  {sentence}")
        print()
    
    # Show that abbreviations are properly handled
    print("Note: Legal abbreviations like 'v.', 'U.S.', 'Id.', 'Fed.' are correctly preserved!")
    print()

def demonstrate_para_tokenize():
    """Demonstrate paragraph tokenization."""
    print("=" * 80)
    print("PARAGRAPH TOKENIZATION (para_tokenize)")
    print("=" * 80)
    
    paragraphs = nupunkt_rs.para_tokenize(legal_text)
    
    print(f"\nFound {len(paragraphs)} paragraphs:\n")
    for i, paragraph in enumerate(paragraphs, 1):
        print(f"Paragraph {i}: {len(paragraph)} sentences")
        for j, sentence in enumerate(paragraph, 1):
            print(f"  {i}.{j}: {sentence[:80]}..." if len(sentence) > 80 else f"  {i}.{j}: {sentence}")
        print()

def demonstrate_para_tokenize_joined():
    """Demonstrate flat paragraph tokenization."""
    print("=" * 80)
    print("FLAT PARAGRAPH TOKENIZATION (para_tokenize_joined)")
    print("=" * 80)
    
    paragraphs_flat = nupunkt_rs.para_tokenize_joined(legal_text)
    
    print(f"\nFound {len(paragraphs_flat)} paragraphs (as strings):\n")
    for i, paragraph in enumerate(paragraphs_flat, 1):
        print(f"Paragraph {i}:")
        print(f"  {paragraph[:150]}..." if len(paragraph) > 150 else f"  {paragraph}")
        print()

def demonstrate_tokenizer_methods():
    """Demonstrate using the SentenceTokenizer class methods."""
    print("=" * 80)
    print("USING SentenceTokenizer CLASS")
    print("=" * 80)
    
    # Create tokenizer with default model
    tokenizer = nupunkt_rs.create_default_tokenizer()
    
    simple_text = "Dr. Smith works at the U.S. Department.\n\nMr. Jones works at NASA."
    
    print("\nOriginal text:")
    print(simple_text)
    print()
    
    # Sentence tokenization
    sentences = tokenizer.tokenize(simple_text)
    print(f"Sentences ({len(sentences)}):")
    for s in sentences:
        print(f"  - {s}")
    print()
    
    # Paragraph tokenization
    paragraphs = tokenizer.tokenize_paragraphs(simple_text)
    print(f"Paragraphs ({len(paragraphs)}):")
    for i, para in enumerate(paragraphs, 1):
        print(f"  Paragraph {i}: {para}")
    print()

def compare_before_after():
    """Compare old behavior (without default model) vs new behavior."""
    print("=" * 80)
    print("BEFORE vs AFTER: Default Model Loading")
    print("=" * 80)
    
    test_text = "Daubert v. Merrell Dow Pharmaceuticals, Inc., 509 U.S. 579."
    
    print(f"\nTest text: '{test_text}'")
    print()
    
    # New behavior (with default model loaded)
    result = nupunkt_rs.sent_tokenize(test_text)
    print(f"WITH default model (correct): {len(result)} sentence(s)")
    print(f"  Result: {result}")
    print()
    
    # The old behavior would have broken at "v." and "U.S."
    # but now it correctly treats them as abbreviations
    print("Old behavior would have incorrectly split at 'v.' and 'U.S.'")
    print("New behavior correctly preserves legal abbreviations!")

if __name__ == "__main__":
    # Run all demonstrations
    demonstrate_sent_tokenize()
    demonstrate_para_tokenize()
    demonstrate_para_tokenize_joined()
    demonstrate_tokenizer_methods()
    compare_before_after()
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("""
Both sent_tokenize() and para_tokenize() now:
1. Load and cache the default model automatically
2. Handle legal abbreviations correctly (v., U.S., Fed., Id., Ibid., etc.)
3. Accept optional model_params for custom models
4. Provide consistent behavior with the tokenizer class methods

The default model is loaded once and cached for performance.
""")