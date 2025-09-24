# PyPI Deployment Checklist - MCP Mathematics

## Pre-Deployment Validation

### ✅ Code Quality & Standards
- [ ] All code follows PEP 8 standards
- [ ] No debug statements or console.log calls
- [ ] No unnecessary code comments
- [ ] Type annotations are complete
- [ ] Code passes Ruff linting
- [ ] Code is formatted with Black

### ✅ Package Configuration
- [ ] `pyproject.toml` has correct package name: `mcp-mathematics`
- [ ] Version number is accurate: `1.0.0`
- [ ] Author information is correct: `Md. Sazzad Hossain Sharkar <md@szd.sh>`
- [ ] Repository URL updated: `https://github.com/SHSharkar/MCP-Mathematics`
- [ ] License specified: `MIT`
- [ ] Keywords are relevant and comprehensive
- [ ] Python version compatibility: `>=3.10`
- [ ] Dependencies are minimal and correct: `mcp>=1.4.1`

### ✅ Project Structure
- [ ] Source code in `src/mcp_mathematics/` directory
- [ ] Tests in `tests/` directory
- [ ] Entry point script configured: `mcp-mathematics = "mcp_mathematics:main"`
- [ ] Build packages specified: `["src/mcp_mathematics"]`
- [ ] No unnecessary files in distribution

### ✅ Documentation
- [ ] README.md is comprehensive and up-to-date
- [ ] Installation instructions are accurate
- [ ] Usage examples work correctly
- [ ] MCP configuration examples are correct
- [ ] All display names updated to "MCP Mathematics"
- [ ] Repository references updated consistently

### ✅ Testing & Functionality
- [ ] All 61 unit tests pass
- [ ] Test coverage >90%
- [ ] MCP tools function correctly
- [ ] Mathematical operations work as expected
- [ ] AST security validation working
- [ ] Rate limiting configured appropriately
- [ ] Error handling comprehensive

## Build & Distribution

### ✅ Environment Setup
- [ ] Python 3.10+ installed and active
- [ ] Latest `build` package installed: `pip install build`
- [ ] Latest `twine` package installed: `pip install twine`
- [ ] PyPI account created and verified
- [ ] TestPyPI account created (optional but recommended)

### ✅ Build Process
- [ ] Clean previous builds: `rm -rf dist/ build/`
- [ ] Build package: `python -m build`
- [ ] Verify wheel created: `dist/mcp_mathematics-1.0.0-py3-none-any.whl`
- [ ] Verify source distribution: `dist/mcp-mathematics-1.0.0.tar.gz`
- [ ] Check package contents: `python -m zipfile -l dist/mcp_mathematics-1.0.0-py3-none-any.whl`

### ✅ Package Validation
- [ ] Run package checks: `twine check dist/*`
- [ ] No errors in package metadata
- [ ] All required files included
- [ ] No sensitive files included

### ✅ Local Testing
- [ ] Install package locally: `pip install dist/mcp_mathematics-1.0.0-py3-none-any.whl`
- [ ] Test command line entry: `mcp-mathematics --help`
- [ ] Test MCP server functionality
- [ ] Verify mathematical operations work
- [ ] Test with Claude Desktop configuration
- [ ] Uninstall test package: `pip uninstall mcp-mathematics`

## TestPyPI Deployment (Recommended)

### ✅ TestPyPI Upload
- [ ] Configure TestPyPI credentials
- [ ] Upload to TestPyPI: `twine upload --repository testpypi dist/*`
- [ ] Verify upload successful
- [ ] Check package page: `https://test.pypi.org/project/mcp-mathematics/`

### ✅ TestPyPI Installation Testing
- [ ] Install from TestPyPI: `pip install --index-url https://test.pypi.org/simple/ mcp-mathematics`
- [ ] Test functionality works correctly
- [ ] Test MCP integration
- [ ] Verify all dependencies resolve
- [ ] Uninstall: `pip uninstall mcp-mathematics`

## Production PyPI Deployment

### ✅ Final Verification
- [ ] All tests pass on clean environment
- [ ] Package builds without warnings
- [ ] Documentation is accurate
- [ ] Version number is correct
- [ ] No test dependencies in production package

### ✅ PyPI Upload
- [ ] Configure PyPI credentials (API token recommended)
- [ ] Upload to PyPI: `twine upload dist/*`
- [ ] Verify upload successful
- [ ] Check package page: `https://pypi.org/project/mcp-mathematics/`

### ✅ Post-Deployment Verification
- [ ] Install from PyPI: `pip install mcp-mathematics`
- [ ] Test basic functionality: `python -c "import mcp_mathematics; print('Success')"`
- [ ] Test CLI entry point: `mcp-mathematics --help`
- [ ] Test MCP server: Configure with Claude Desktop and verify
- [ ] Test mathematical operations work correctly
- [ ] Verify package metadata on PyPI is correct

## Release Management

### ✅ Repository Updates
- [ ] Create GitHub release for v1.0.0
- [ ] Update repository name to `MCP-Mathematics`
- [ ] Tag release: `git tag v1.0.0 && git push origin v1.0.0`
- [ ] Update any package managers or distribution lists

### ✅ Documentation Updates
- [ ] Update README.md with PyPI installation instructions
- [ ] Verify all URLs and links work
- [ ] Update any external documentation references

### ✅ Community & Distribution
- [ ] Announce release appropriately
- [ ] Update any relevant package registries
- [ ] Monitor for initial user feedback
- [ ] Prepare for potential bug reports or feature requests

## Security Considerations

### ✅ Security Checklist
- [ ] No API keys or secrets in code
- [ ] Dependencies are from trusted sources
- [ ] AST evaluation prevents code injection
- [ ] Input validation is comprehensive
- [ ] Error messages don't leak sensitive information
- [ ] Rate limiting protects against abuse

## Emergency Procedures

### ✅ Rollback Plan
- [ ] Document procedure to yank release if needed
- [ ] Have contact information for PyPI support
- [ ] Backup of working version maintained
- [ ] Know how to push emergency patch

---

## Commands Summary

```bash
# Preparation
rm -rf dist/ build/
pip install build twine

# Build
python -m build

# Validate
twine check dist/*

# Test locally
pip install dist/mcp_mathematics-1.0.0-py3-none-any.whl
mcp-mathematics --help
pip uninstall mcp-mathematics

# Deploy to TestPyPI (optional)
twine upload --repository testpypi dist/*

# Deploy to PyPI
twine upload dist/*

# Verify deployment
pip install mcp-mathematics
python -c "import mcp_mathematics; print('Success')"
```

## Estimated Timeline

- **Preparation & Validation**: 30-45 minutes
- **Build & Testing**: 15-20 minutes
- **TestPyPI Deployment**: 10-15 minutes
- **Production Deployment**: 10-15 minutes
- **Post-deployment Verification**: 15-20 minutes

**Total Estimated Time**: 1.5 - 2 hours for complete deployment process

---

*Last Updated: 2025-09-23 18:48 (Asia/Dhaka)*