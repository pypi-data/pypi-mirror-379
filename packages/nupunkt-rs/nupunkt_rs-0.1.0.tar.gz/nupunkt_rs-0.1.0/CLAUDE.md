# CLAUDE.md - Implementation Notes

## PR Calibration for Legal Text

After extensive testing and calibration, the optimal PR values for legal text are:
- **PR=0.1**: Produces 11 sentences (high recall mode)
- **PR=0.3**: Produces 9 sentences (balanced for legal)
- **PR=0.5**: Produces 7 sentences (too conservative for legal text with many abbreviations)

Legal text requires lower PR values (0.1-0.3) than general text due to the high frequency of abbreviations that shouldn't cause breaks (e.g., "v.", "U.S.", "Fed.", "Co.").

The system is working correctly - it's protecting abbreviations as designed. Users working with legal text should use PR=0.1 or PR=0.3 for best results.

## Abbreviation Handling

### Normalization Process

The system uses consistent normalization for abbreviations:

1. **JSON Input Format**: Abbreviations in `data/legal_abbreviations.json` include terminal periods and proper case
   - Example: `"Id."`, `"Ibid."`, `"Fed."`, `"U.S."`

2. **Storage Normalization** (in `src/parameters.rs::add_provided_abbreviation`):
   - Remove terminal period: `"Id."` → `"Id"`
   - Convert to lowercase: `"Id"` → `"id"`
   - Final stored form: `"id"`

3. **Token Processing** (in `src/tokens.rs`):
   - `get_token_type()`: Converts token to lowercase: `"Id."` → `"id."`
   - `type_no_period()`: Removes period: `"id."` → `"id"`

4. **Lookup Process**:
   - Token `"Id."` → normalized to `"id"` → found in abbreviations ✓
   - This ensures case-insensitive matching

### Provided vs Learned Abbreviations

The system distinguishes between:
- **Provided abbreviations**: Loaded from JSON files, get strong negative weights (-1.45 at PR=0.5)
- **Learned abbreviations**: Discovered from training data, get weaker weights

This ensures that known legal abbreviations like "v.", "Id.", "Ibid." are reliably preserved.

### Current Status (Post Domain-Logic Removal)

After removing all domain-specific hard-coded logic:
- Legal citations like "v." correctly don't break (e.g., "Daubert v. Merrell" stays together)
- "Id." and "Ibid." are recognized as abbreviations and don't cause breaks
- The Daubert test produces 7 sentences at default PR=0.5 (9-11 at PR=0.1)
- All behavior now comes from:
  1. Provided abbreviations in JSON files
  2. Statistical learning from training data
  3. Generic hyperparameters (no domain-specific code)

### Training Data Characteristics

Analysis of training corpus (`data/train-sample-10k.jsonl.gz`, first 500 docs):
- Contains 350 "v." patterns (legal citations)
- ALL "v." patterns correctly continue (don't break)
- Only 21 "Id." occurrences, 0 "Ibid." 
- Model correctly learns that "v." shouldn't break
- Limited examples of "Id."/"Ibid." but handled via provided abbreviations

### Key Files

- `src/parameters.rs`: Abbreviation storage and normalization
- `src/tokens.rs`: Token type computation  
- `src/decision.rs`: Sentence boundary decisions (uses normalized abbreviations)
- `src/trainers/trainer.rs`: Loading abbreviations from JSON
- `data/legal_abbreviations.json`: 1995 legal abbreviations including "Id.", "Ibid.", "Fed.", etc.