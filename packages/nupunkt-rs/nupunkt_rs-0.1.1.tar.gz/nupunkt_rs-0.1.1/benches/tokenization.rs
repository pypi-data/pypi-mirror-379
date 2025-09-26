use criterion::{criterion_group, criterion_main, Criterion};
use nupunkt_rs::core::SentenceTokenizer;
use nupunkt_rs::tokenizers::PunktSentenceTokenizer;
use nupunkt_rs::trainers::PunktTrainer;
use std::hint::black_box;
use std::sync::Arc;

fn benchmark_tokenization(c: &mut Criterion) {
    // Sample text for benchmarking
    let text = "Dr. Smith went to the store. He bought milk, eggs, and bread. The total was $12.50. 
                He paid with a $20 bill. The cashier gave him $7.50 in change. Dr. Smith thanked 
                the cashier and left. On his way home, he stopped at the U.S. Post Office. He needed 
                to mail a package to his friend in Washington, D.C. The package weighed 2.5 lbs. 
                The postal worker said it would arrive in 3-5 business days. Dr. Smith was satisfied.";

    // Train a model
    let mut trainer = PunktTrainer::new();
    let params = trainer.train(text, false).unwrap();
    let tokenizer = PunktSentenceTokenizer::from_parameters(Arc::new(params));

    c.bench_function("tokenize_sentences", |b| {
        b.iter(|| tokenizer.tokenize(black_box(text)));
    });

    c.bench_function("tokenize_spans", |b| {
        b.iter(|| tokenizer.tokenize_spans(black_box(text)));
    });

    // Benchmark with longer text
    let long_text = text.repeat(100);

    c.bench_function("tokenize_long_text", |b| {
        b.iter(|| tokenizer.tokenize(black_box(&long_text)));
    });
}

fn benchmark_training(c: &mut Criterion) {
    let training_text = "This is a training text. It contains multiple sentences. Dr. Smith is a doctor. 
                         He works at the hospital. The hospital is located in New York, N.Y. It has 500 beds. 
                         The U.S. government provides funding. The funding amounts to $10 million per year. 
                         Dr. Smith sees 30 patients per day on average. His specialty is internal medicine. 
                         He graduated from Harvard Medical School in 2010. His colleague, Dr. Jones, graduated 
                         from Yale. They often collaborate on research projects. Their latest paper was published 
                         in the New England Journal of Medicine. It received positive reviews from peers.";

    c.bench_function("train_model", |b| {
        b.iter(|| {
            let mut trainer = PunktTrainer::new();
            trainer.train(black_box(training_text), false).unwrap()
        });
    });
}

criterion_group!(benches, benchmark_tokenization, benchmark_training);
criterion_main!(benches);
