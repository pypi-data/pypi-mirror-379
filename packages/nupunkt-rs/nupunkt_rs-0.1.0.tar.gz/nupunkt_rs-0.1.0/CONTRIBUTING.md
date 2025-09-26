# Contributing to nupunkt-rs

Thank you for your interest in contributing to nupunkt-rs! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our code of conduct:
- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive criticism
- Accept feedback gracefully

## How to Contribute

### Reporting Issues

1. Check existing issues to avoid duplicates
2. Use issue templates when available
3. Provide minimal reproducible examples
4. Include system information (OS, Python version, Rust version)

### Suggesting Features

1. Open a discussion first for major features
2. Explain the use case and benefits
3. Consider implementation complexity
4. Be open to alternative solutions

### Submitting Code

#### Setup Development Environment

1. **Fork and clone the repository**:
```bash
git clone https://github.com/YOUR_USERNAME/nupunkt-rs.git
cd nupunkt-rs
```

2. **Install development dependencies**:
```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Create Python virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install Python dependencies
pip install maturin
pip install -e ".[dev]"

# Build the Rust extension
maturin develop
```

3. **Create a feature branch**:
```bash
git checkout -b feature/your-feature-name
```

#### Development Workflow

1. **Make your changes**:
   - Write clean, documented code
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation as needed

2. **Run tests**:
```bash
# Rust tests
cargo test

# Python tests
pytest python/tests/

# Integration tests
cargo test --all-features
```

3. **Check code quality**:
```bash
# Format Rust code
cargo fmt

# Lint Rust code
cargo clippy -- -D warnings

# Format Python code
black python/
ruff format python/

# Lint Python code
ruff check python/

# Type checking
mypy python/
```

4. **Commit your changes**:
```bash
git add .
git commit -m "feat: add new feature"  # Use conventional commits
```

#### Commit Message Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Test additions or changes
- `perf:` Performance improvements
- `refactor:` Code refactoring
- `style:` Code style changes
- `chore:` Maintenance tasks

Examples:
```
feat: add support for custom abbreviation lists
fix: correct tokenization of ellipsis
docs: update API documentation for SentenceTokenizer
perf: optimize token analysis for large texts
```

#### Pull Request Process

1. **Push to your fork**:
```bash
git push origin feature/your-feature-name
```

2. **Create a Pull Request**:
   - Use a descriptive title
   - Reference related issues
   - Describe what changes you made and why
   - Include test results if applicable

3. **Code Review**:
   - Address reviewer feedback
   - Keep discussions focused and professional
   - Update your branch with main if needed

### Testing Guidelines

#### Writing Tests

- **Rust tests**: Place in `src/` modules or `tests/` directory
- **Python tests**: Place in `python/tests/`
- **Benchmarks**: Place in `benches/`

Example Rust test:
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_tokenization() {
        let text = "Hello. World.";
        let result = tokenize(text);
        assert_eq!(result, vec!["Hello.", "World."]);
    }
}
```

Example Python test:
```python
def test_tokenization():
    tokenizer = SentenceTokenizer()
    result = tokenizer.tokenize("Hello. World.")
    assert result == ["Hello.", "World."]
```

#### Running Benchmarks

```bash
# Run all benchmarks
cargo bench

# Run specific benchmark
cargo bench --bench tokenization
```

### Documentation

#### Code Documentation

- **Rust**: Use rustdoc comments
```rust
/// Tokenizes text into sentences.
/// 
/// # Arguments
/// * `text` - The input text to tokenize
/// 
/// # Returns
/// A vector of sentence strings
pub fn tokenize(text: &str) -> Vec<String> {
    // implementation
}
```

- **Python**: Use docstrings
```python
def tokenize(text: str) -> List[str]:
    """
    Tokenize text into sentences.
    
    Args:
        text: The input text to tokenize
        
    Returns:
        List of sentence strings
    """
    pass
```

#### Updating Documentation

1. Update README.md for user-facing changes
2. Update API documentation in code
3. Add examples for new features
4. Update CHANGELOG.md

### Performance Considerations

- Profile before optimizing
- Benchmark changes that claim performance improvements
- Consider memory usage, not just speed
- Document performance characteristics

### Platform Support

Ensure changes work on:
- Linux (x86_64, aarch64)
- macOS (x86_64, Apple Silicon)
- Windows (x86_64)
- Python 3.11+

### Release Process

Maintainers handle releases, but contributors should:
1. Update version numbers if requested
2. Update CHANGELOG.md with your changes
3. Ensure CI passes on all platforms

## Development Tips

### Debugging Rust

```bash
# Run with debug output
RUST_LOG=debug cargo run

# Use GDB/LLDB
cargo build
gdb target/debug/nupunkt
```

### Debugging Python

```python
import pdb; pdb.set_trace()  # Add breakpoint
```

### Profiling

```bash
# Profile Rust code
cargo build --release
perf record --call-graph=dwarf ./target/release/nupunkt
perf report

# Profile Python code
python -m cProfile -o profile.stats your_script.py
```

## Getting Help

- Open a discussion for questions
- Join our community chat (if available)
- Check documentation and examples
- Ask in pull request comments

## Recognition

Contributors are recognized in:
- The AUTHORS file
- Release notes
- Project documentation

Thank you for contributing to nupunkt-rs!