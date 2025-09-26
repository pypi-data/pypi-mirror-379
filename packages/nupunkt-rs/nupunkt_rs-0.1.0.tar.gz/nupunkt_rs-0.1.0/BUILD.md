# Building nupunkt-rs

## Prerequisites

- Rust toolchain (`cargo`)
- Python 3.11+
- `uv` (for Python package management)
- `maturin` (will be installed automatically if missing)

## Quick Start

```bash
./build.sh              # Full build with tests
./build.sh --release    # Optimized release build
./build.sh --skip-tests # Quick build without tests
```

## Build Script Options

The `build.sh` script provides fine-grained control:

- `--release`: Build in release mode (optimized)
- `--skip-tests`: Skip running tests for faster builds
- `--no-editable`: Install from wheel instead of editable mode
- `--help`: Show usage information

## Build Workflow

The build script follows this workflow:

1. **Clean**: Remove previous build artifacts
2. **Test Rust**: Run `cargo test` to ensure Rust code is correct
3. **Build**: Use `maturin` to build the Python extension
4. **Install**: Install the package (editable or from wheel)
5. **Test Python**: Run Python tests with pytest

## Development Workflow

For development, use the quick build:

```bash
./build.sh --skip-tests
```

## Release Workflow

For releases, always run full tests:

```bash
./build.sh --release
```

## Testing

Run tests independently:

```bash
# Rust tests only
cargo test

# Python tests only (requires package installed)
uv run pytest python/tests

# All tests
./build.sh
```

## Troubleshooting

If the build fails:

1. Ensure all prerequisites are installed
2. Run `cargo clean` to remove stale artifacts
3. Check that Python version is 3.11+
4. Verify `uv` is installed: `uv --version`
5. Check Rust toolchain: `cargo --version`

## CI/CD Integration

For CI/CD pipelines, use the build script with appropriate flags:

```bash
# CI build with all tests
./build.sh --release

# Quick validation build
./build.sh --skip-tests
```