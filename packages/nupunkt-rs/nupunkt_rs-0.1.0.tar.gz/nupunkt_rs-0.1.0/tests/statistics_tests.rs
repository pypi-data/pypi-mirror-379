use nupunkt_rs::statistics::{
    calculate_abbreviation_score, collocation_log_likelihood, dunning_log_likelihood,
    AbbreviationScorer,
};

#[test]
fn test_dunning_no_nan() {
    // Test all edge cases that could produce NaN
    let test_cases = vec![
        // (count_a, count_b, count_ab, n)
        (0, 0, 0, 100),                       // No occurrences
        (10, 10, 10, 100),                    // All tokens have periods
        (10, 0, 0, 100),                      // No periods at all
        (10, 100, 10, 100),                   // All tokens are period tokens
        (1, 1, 1, 1),                         // Single token
        (100, 50, 100, 100),                  // count_ab > count_a (invalid but shouldn't NaN)
        (50, 100, 50, 100),                   // Half tokens have periods
        (1000000, 1000000, 1000000, 1000000), // Large numbers
    ];

    for (count_a, count_b, count_ab, n) in test_cases {
        let result = dunning_log_likelihood(count_a, count_b, count_ab, n);
        assert!(
            !result.is_nan(),
            "NaN produced for ({}, {}, {}, {})",
            count_a,
            count_b,
            count_ab,
            n
        );
        assert!(
            !result.is_infinite(),
            "Infinity produced for ({}, {}, {}, {})",
            count_a,
            count_b,
            count_ab,
            n
        );
    }
}

#[test]
fn test_collocation_no_nan() {
    let test_cases = vec![
        (0, 0, 0, 100),
        (10, 10, 10, 100),
        (10, 10, 0, 100),
        (100, 100, 50, 1000),
        (1, 1, 1, 1),
    ];

    for (count_a, count_b, count_ab, n) in test_cases {
        let result = collocation_log_likelihood(count_a, count_b, count_ab, n);
        assert!(
            !result.is_nan(),
            "NaN produced for ({}, {}, {}, {})",
            count_a,
            count_b,
            count_ab,
            n
        );
    }
}

#[test]
fn test_abbreviation_scorer_no_nan() {
    let scorer = AbbreviationScorer::new(0.1, 1.5, 0.25);

    // Test edge cases
    assert!(!scorer.is_abbreviation("test", 0, 0, 100, 1000));
    assert!(!scorer.is_abbreviation("test", 10, 10, 100, 1000));

    // Should not produce NaN in score calculation
    let score = calculate_abbreviation_score("test", 10, 5, 100, 1000);
    assert!(!score.is_nan());
}
