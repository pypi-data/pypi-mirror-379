/// Utility functions for nupunkt-rs
use ahash::AHashMap;
use regex::Regex;

/// Iterate over pairs of consecutive items
pub struct PairIter<I, T>
where
    I: Iterator<Item = T>,
    T: Clone,
{
    iter: I,
    prev: Option<T>,
}

impl<I, T> PairIter<I, T>
where
    I: Iterator<Item = T>,
    T: Clone,
{
    pub fn new(mut iter: I) -> Self {
        let prev = iter.next();
        Self { iter, prev }
    }
}

impl<I, T> Iterator for PairIter<I, T>
where
    I: Iterator<Item = T>,
    T: Clone,
{
    type Item = (T, Option<T>);

    fn next(&mut self) -> Option<Self::Item> {
        if let Some(prev) = self.prev.take() {
            let next = self.iter.next();
            self.prev = next.clone();
            Some((prev, next))
        } else {
            None
        }
    }
}

/// Create a pair iterator from an iterator
pub fn pair_iter<I, T>(iter: I) -> PairIter<I::IntoIter, T>
where
    I: IntoIterator<Item = T>,
    T: Clone,
{
    PairIter::new(iter.into_iter())
}

/// Text preprocessing utilities
#[derive(Clone)]
pub struct TextPreprocessor {
    word_tokenize_pattern: Regex,
}

impl TextPreprocessor {
    pub fn new(pattern: &str) -> Result<Self, regex::Error> {
        Ok(Self {
            word_tokenize_pattern: Regex::new(pattern)?,
        })
    }

    /// Tokenize text into words
    pub fn word_tokenize(&self, text: &str) -> Vec<String> {
        self.word_tokenize_pattern
            .find_iter(text)
            .map(|m| m.as_str().to_string())
            .collect()
    }

    /// Tokenize text into words with whitespace information
    /// Returns (word, spaces_after, has_newline, byte_position)
    pub fn word_tokenize_with_spacing(&self, text: &str) -> Vec<(String, u8, bool, usize)> {
        let mut result = Vec::new();

        let matches: Vec<_> = self.word_tokenize_pattern.find_iter(text).collect();

        for (i, m) in matches.iter().enumerate() {
            let word = m.as_str().to_string();
            let byte_pos = m.start(); // Store the byte position

            // Check whitespace after this token
            let mut spaces_after = 0u8;
            let mut has_newline = false;

            // Determine where to look for whitespace
            let start_pos = m.end();
            let end_pos = if i + 1 < matches.len() {
                matches[i + 1].start()
            } else {
                text.len()
            };

            // Analyze the whitespace
            if start_pos < end_pos {
                let between = &text[start_pos..end_pos];
                has_newline = between.contains('\n');

                // Count spaces (not including newlines)
                if !has_newline {
                    spaces_after = between.chars().filter(|&c| c == ' ').count().min(255) as u8;
                } else {
                    // If there's a newline, we don't count spaces
                    spaces_after = 0;
                }
            }

            result.push((word, spaces_after, has_newline, byte_pos));
        }

        result
    }

    /// Align tokens with their character positions in the original text
    pub fn align_tokens(&self, text: &str, tokens: &[String]) -> Vec<(usize, usize)> {
        let mut positions = Vec::new();
        let mut search_start = 0;

        for token in tokens {
            if let Some(pos) = text[search_start..].find(token) {
                let start = search_start + pos;
                let end = start + token.len();
                positions.push((start, end));
                search_start = end;
            }
        }

        positions
    }
}

impl Default for TextPreprocessor {
    fn default() -> Self {
        // Tokenization regex that handles:
        // - Words with internal punctuation (contractions, abbreviations)
        // - Numbers with decimal points or commas
        // - Sequences of punctuation
        // - Single non-whitespace characters
        // This matches the original \S+ but we keep it for now to avoid breaking changes
        Self::new(r"\S+").unwrap()
    }
}

/// Frequency distribution for counting items
#[derive(Debug, Clone)]
pub struct FreqDist<T: Eq + std::hash::Hash> {
    counts: AHashMap<T, usize>,
    total: usize,
}

impl<T: Eq + std::hash::Hash> FreqDist<T> {
    pub fn new() -> Self {
        Self {
            counts: AHashMap::new(),
            total: 0,
        }
    }

    /// Add an item to the distribution
    pub fn add(&mut self, item: T) {
        *self.counts.entry(item).or_insert(0) += 1;
        self.total += 1;
    }

    /// Add an item with a specific count
    pub fn add_count(&mut self, item: T, count: usize) {
        *self.counts.entry(item).or_insert(0) += count;
        self.total += count;
    }

    /// Get the count for an item
    pub fn get(&self, item: &T) -> usize {
        self.counts.get(item).copied().unwrap_or(0)
    }

    /// Get the total count
    pub fn total(&self) -> usize {
        self.total
    }

    /// Get the frequency of an item (count / total)
    pub fn frequency(&self, item: &T) -> f64 {
        if self.total == 0 {
            0.0
        } else {
            self.get(item) as f64 / self.total as f64
        }
    }

    /// Get items sorted by count (descending)
    pub fn most_common(&self) -> Vec<(&T, usize)> {
        let mut items: Vec<_> = self.counts.iter().map(|(k, &v)| (k, v)).collect();
        items.sort_by(|a, b| b.1.cmp(&a.1));
        items
    }

    /// Prune items below a minimum frequency
    pub fn prune(&mut self, min_count: usize) {
        self.counts.retain(|_, &mut count| count >= min_count);
        self.total = self.counts.values().sum();
    }

    /// Get the number of unique items
    pub fn len(&self) -> usize {
        self.counts.len()
    }

    /// Check if the distribution is empty
    pub fn is_empty(&self) -> bool {
        self.counts.is_empty()
    }
}

impl<T: Eq + std::hash::Hash> Default for FreqDist<T> {
    fn default() -> Self {
        Self::new()
    }
}

/// Cache for frequently accessed computations
pub struct ComputationCache<K: Eq + std::hash::Hash, V> {
    cache: AHashMap<K, V>,
    max_size: usize,
}

impl<K: Eq + std::hash::Hash + Clone, V: Clone> ComputationCache<K, V> {
    pub fn new(max_size: usize) -> Self {
        Self {
            cache: AHashMap::new(),
            max_size,
        }
    }

    /// Get a value from the cache or compute it
    pub fn get_or_compute<F>(&mut self, key: K, compute: F) -> V
    where
        F: FnOnce() -> V,
    {
        if let Some(value) = self.cache.get(&key) {
            return value.clone();
        }

        let value = compute();

        // Only cache if below size limit
        if self.cache.len() < self.max_size {
            self.cache.insert(key, value.clone());
        }

        value
    }

    /// Clear the cache
    pub fn clear(&mut self) {
        self.cache.clear();
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_pair_iter() {
        let items = vec![1, 2, 3, 4];
        let pairs: Vec<_> = pair_iter(items).collect();

        assert_eq!(pairs.len(), 4);
        assert_eq!(pairs[0], (1, Some(2)));
        assert_eq!(pairs[1], (2, Some(3)));
        assert_eq!(pairs[2], (3, Some(4)));
        assert_eq!(pairs[3], (4, None));
    }

    #[test]
    fn test_freq_dist() {
        let mut dist = FreqDist::new();
        dist.add("hello");
        dist.add("world");
        dist.add("hello");

        assert_eq!(dist.get(&"hello"), 2);
        assert_eq!(dist.get(&"world"), 1);
        assert_eq!(dist.total(), 3);
        assert_eq!(dist.frequency(&"hello"), 2.0 / 3.0);
    }

    #[test]
    fn test_text_preprocessor() {
        let preprocessor = TextPreprocessor::default();
        let tokens = preprocessor.word_tokenize("Hello, world! How are you?");

        assert_eq!(tokens.len(), 5);
        assert_eq!(tokens[0], "Hello,");
        assert_eq!(tokens[1], "world!");
    }
}
