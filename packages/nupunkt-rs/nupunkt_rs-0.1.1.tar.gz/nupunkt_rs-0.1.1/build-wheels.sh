#!/bin/bash
# Build manylinux-compliant wheels using maturin's official Docker image
# This is the recommended approach for 2025

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${GREEN}🦀 Building manylinux wheels for nupunkt-rs${NC}"
echo ""

# Parse command line arguments
MANYLINUX_VERSION="2_28"  # Default to manylinux_2_28 for good compatibility
PUBLISH=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --manylinux)
            MANYLINUX_VERSION="$2"
            shift 2
            ;;
        --publish)
            PUBLISH=true
            shift
            ;;
        --help)
            echo "Usage: $0 [--manylinux VERSION] [--publish]"
            echo ""
            echo "Options:"
            echo "  --manylinux VERSION  Set manylinux version (default: 2_28)"
            echo "                       Options: 2_17, 2_28, 2_34"
            echo "  --publish           Publish to PyPI after building"
            echo ""
            echo "Examples:"
            echo "  $0                    # Build with manylinux_2_28"
            echo "  $0 --manylinux 2_17   # Build with manylinux2014"
            echo "  $0 --publish          # Build and publish to PyPI"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Get version from Cargo.toml
VERSION=$(grep "^version" Cargo.toml | head -1 | cut -d'"' -f2)
echo -e "📦 Package version: ${BLUE}$VERSION${NC}"
echo -e "🏗️  Manylinux version: ${BLUE}manylinux_${MANYLINUX_VERSION}${NC}"
echo ""

# Build using maturin's official Docker image
echo -e "${YELLOW}🐳 Building wheels in Docker...${NC}"
echo ""

# The ghcr.io/pyo3/maturin image is the official maturin Docker image
# It's based on manylinux and includes everything needed
docker run --rm \
    -v $(pwd):/io \
    -w /io \
    ghcr.io/pyo3/maturin:latest \
    build --release \
    --strip \
    --manylinux $MANYLINUX_VERSION \
    -o dist

echo ""
echo -e "${GREEN}✅ Wheels built successfully!${NC}"
echo ""
echo "📦 Built wheels:"
ls -lh dist/*.whl

if [ "$PUBLISH" = true ]; then
    if [ -z "$MATURIN_PYPI_TOKEN" ]; then
        echo ""
        echo -e "${YELLOW}⚠️  MATURIN_PYPI_TOKEN not set${NC}"
        echo "To publish, set your PyPI token:"
        echo "  export MATURIN_PYPI_TOKEN=pypi-..."
        exit 1
    fi
    
    echo ""
    echo -e "${YELLOW}📤 Publishing to PyPI...${NC}"
    docker run --rm \
        -v $(pwd):/io \
        -w /io \
        -e MATURIN_PYPI_TOKEN="$MATURIN_PYPI_TOKEN" \
        ghcr.io/pyo3/maturin:latest \
        upload dist/*.whl
    
    echo ""
    echo -e "${GREEN}🎉 Successfully published to PyPI!${NC}"
    echo ""
    echo "Don't forget to:"
    echo "  1. Create a git tag: git tag -a v$VERSION -m 'Release v$VERSION'"
    echo "  2. Push the tag: git push origin v$VERSION"
else
    echo ""
    echo "To publish these wheels to PyPI:"
    echo "  1. Set your token: export MATURIN_PYPI_TOKEN=pypi-..."
    echo "  2. Run: $0 --publish"
    echo ""
    echo "Or manually upload:"
    echo "  maturin upload dist/*.whl"
fi