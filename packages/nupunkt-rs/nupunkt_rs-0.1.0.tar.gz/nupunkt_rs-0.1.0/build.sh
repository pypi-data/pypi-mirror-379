#!/usr/bin/env bash
# Build script for nupunkt-rs
# Performs clean build, tests, and installation

set -e  # Exit on error
set -u  # Exit on undefined variable

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_step() {
    echo -e "${GREEN}==>${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Parse arguments
RELEASE_BUILD=false
SKIP_TESTS=false
EDITABLE=true

while [[ $# -gt 0 ]]; do
    case $1 in
        --release)
            RELEASE_BUILD=true
            shift
            ;;
        --skip-tests)
            SKIP_TESTS=true
            shift
            ;;
        --no-editable)
            EDITABLE=false
            shift
            ;;
        --help)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --release      Build in release mode (optimized)"
            echo "  --skip-tests   Skip running tests"
            echo "  --no-editable  Install from wheel instead of editable mode"
            echo "  --help         Show this help message"
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            echo "Run '$0 --help' for usage information"
            exit 1
            ;;
    esac
done

# Check for required tools
print_step "Checking required tools..."

if ! command -v cargo &> /dev/null; then
    print_error "cargo not found. Please install Rust."
    exit 1
fi

if ! command -v maturin &> /dev/null; then
    print_warning "maturin not found. Installing..."
    pip install maturin
fi

if ! command -v uv &> /dev/null; then
    print_error "uv not found. Please install uv."
    exit 1
fi

print_success "All required tools found"

# Step 1: Clean Rust build artifacts
print_step "Cleaning Rust build artifacts..."
cargo clean
rm -rf dist/ build/ *.egg-info/
print_success "Cleaned build artifacts"

# Step 2: Run Rust tests
if [ "$SKIP_TESTS" = false ]; then
    print_step "Running Rust tests..."
    if cargo test --all; then
        print_success "All Rust tests passed"
    else
        print_error "Rust tests failed"
        exit 1
    fi
else
    print_warning "Skipping Rust tests"
fi

# Step 3: Build Rust CLI binary
print_step "Building Rust CLI binary..."

if [ "$RELEASE_BUILD" = true ]; then
    print_step "Building in RELEASE mode..."
    BUILD_FLAGS="--release"
    BINARY_PATH="target/release/nupunkt"
else
    print_step "Building in DEBUG mode..."
    BUILD_FLAGS=""
    BINARY_PATH="target/debug/nupunkt"
fi

if cargo build $BUILD_FLAGS --bin nupunkt; then
    print_success "Built CLI binary at $BINARY_PATH"
    # Make it easily accessible
    if [ -f "$BINARY_PATH" ]; then
        ls -lh "$BINARY_PATH" | awk '{print "  Size: " $5}'
    fi
else
    print_error "Failed to build CLI binary"
    exit 1
fi

# Step 4: Build Python/Maturin package
print_step "Building Python package..."

if [ "$EDITABLE" = true ]; then
    # Use maturin develop for editable install
    print_step "Building and installing in editable mode..."
    maturin develop $BUILD_FLAGS
    print_success "Built and installed in editable mode"
else
    # Build wheel for distribution
    print_step "Building wheel..."
    maturin build $BUILD_FLAGS
    print_success "Built wheel in dist/"
    
    # Step 5: Install the package
    print_step "Installing package from wheel..."
    # Find the latest wheel file
    WHEEL_FILE=$(ls -t dist/*.whl 2>/dev/null | head -n1)
    
    if [ -z "$WHEEL_FILE" ]; then
        print_error "No wheel file found in dist/"
        exit 1
    fi
    
    print_step "Installing $WHEEL_FILE..."
    uv pip install --force-reinstall "$WHEEL_FILE"
    print_success "Installed package from wheel"
fi

# Step 6: Install Python test dependencies
print_step "Checking Python test dependencies..."
if ! uv pip show pytest &> /dev/null; then
    print_step "Installing pytest..."
    uv pip install pytest
fi

# Step 7: Run Python tests
if [ "$SKIP_TESTS" = false ]; then
    print_step "Running Python tests..."
    
    # Check if pytest tests exist
    if [ -d "python/tests" ]; then
        print_step "Running pytest tests..."
        if uv run pytest python/tests -q; then
            print_success "All Python tests passed"
        else
            print_error "Some Python tests failed"
            exit 1
        fi
    else
        print_warning "No Python test directory found"
    fi
    
    # Run our custom test script as a fallback
    print_step "Running custom verification tests..."
    cat << 'EOF' > /tmp/verify_build.py
#!/usr/bin/env python3
"""Verify the build works correctly"""
import nupunkt_rs

print("Testing nupunkt_rs installation...")

# Test 1: Basic tokenization
tokenizer = nupunkt_rs.SentenceTokenizer(None)
text = "Hello world. How are you?"
sentences = tokenizer.tokenize(text)
assert len(sentences) == 2, f"Expected 2 sentences, got {len(sentences)}"
print("✓ Basic tokenization works")

# Test 2: Exclamation and question marks
text2 = "Amazing! Really? Yes."
sentences2 = tokenizer.tokenize(text2)
assert len(sentences2) == 3, f"Expected 3 sentences, got {len(sentences2)}"
print("✓ Exclamation and question marks work")

# Test 3: Training
trainer = nupunkt_rs.Trainer()
params = trainer.train("Dr. Smith works here.", False)
tokenizer2 = nupunkt_rs.SentenceTokenizer(params)
print("✓ Training works")

# Test 4: PR adjustment
tokenizer.set_precision_recall_balance(0.1)
tokenizer.set_precision_recall_balance(0.9)
print("✓ PR adjustment works")

print("\n✅ All verification tests passed!")
EOF
    
    if uv run python /tmp/verify_build.py; then
        print_success "Build verification passed"
    else
        print_error "Build verification failed"
        exit 1
    fi
else
    print_warning "Skipping Python tests"
fi

# Final summary
echo ""
echo "======================================"
if [ "$RELEASE_BUILD" = true ]; then
    echo -e "${GREEN}✓ RELEASE BUILD COMPLETE${NC}"
else
    echo -e "${GREEN}✓ DEBUG BUILD COMPLETE${NC}"
fi

if [ "$EDITABLE" = true ]; then
    echo "  Package installed in editable mode"
else
    echo "  Package installed from wheel"
fi

if [ "$SKIP_TESTS" = false ]; then
    echo "  All tests passed"
else
    echo "  Tests were skipped"
fi
echo "======================================"

# Show how to use the package
echo ""
print_step "You can now use nupunkt-rs:"
echo "  Python:  import nupunkt_rs"
if [ "$RELEASE_BUILD" = true ]; then
    echo "  CLI:     ./target/release/nupunkt <command>"
else
    echo "  CLI:     ./target/debug/nupunkt <command>"
fi
echo "  Install: cargo install --path . (to install CLI globally)"
echo ""