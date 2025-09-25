#!/bin/bash
# test-uv-install.sh - Test uv installation in clean environment
# This script tests that louieai can be installed via uv and imported successfully

set -e  # Exit on any error

echo "🧪 Testing uv installation of louieai"
echo "====================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo -e "${RED}❌ uv is not installed. Install with: curl -LsSf https://astral.sh/uv/install.sh | sh${NC}"
    exit 1
fi

# Create temporary directory for test
TEST_DIR=$(mktemp -d)
echo "📁 Created test directory: $TEST_DIR"

# Cleanup function
cleanup() {
    echo "🧹 Cleaning up test environment..."
    rm -rf "$TEST_DIR"
}
trap cleanup EXIT

# Change to test directory
cd "$TEST_DIR"

# Create virtual environment with uv
echo ""
echo "🔧 Creating virtual environment with uv..."
uv venv --python 3.11 test_env
source test_env/bin/activate

# Build the package from source
echo ""
echo "🏗️  Building package from source..."
ORIGINAL_DIR=$(dirname "$(dirname "$(readlink -f "$0")")")
cd "$ORIGINAL_DIR"
python -m build . > /dev/null 2>&1

# Find the built wheel
WHEEL_FILE=$(ls -t dist/*.whl | head -1)
if [ -z "$WHEEL_FILE" ]; then
    echo -e "${RED}❌ No wheel file found in dist/${NC}"
    exit 1
fi
echo "📦 Found wheel: $(basename "$WHEEL_FILE")"

# Go back to test directory
cd "$TEST_DIR"

# Install the package with uv
echo ""
echo "📥 Installing louieai via uv..."
uv pip install "$ORIGINAL_DIR/$WHEEL_FILE"

# Test import
echo ""
echo "🔍 Testing import..."
python -c "
import louieai
print(f'✅ Successfully imported louieai version {louieai.__version__}')

# Test that main class is available
from louieai import LouieClient
print('✅ LouieClient class is available')

# Verify basic instantiation (without API calls)
try:
    client = LouieClient()
    print('✅ LouieClient can be instantiated')
except Exception as e:
    print(f'❌ Failed to instantiate LouieClient: {e}')
    exit(1)
"

# Check installed packages
echo ""
echo "📋 Installed packages:"
uv pip list | grep -E "(louieai|graphistry|httpx|pandas|pyarrow)" || true

echo ""
echo -e "${GREEN}🎉 uv installation test PASSED!${NC}"
echo "====================================="