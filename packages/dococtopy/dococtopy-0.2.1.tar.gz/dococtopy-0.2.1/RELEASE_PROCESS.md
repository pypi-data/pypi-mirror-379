# Release Process Guide

This document outlines the step-by-step process for releasing new versions of DocOctopy.

## Pre-Release Checklist

### 1. Code Quality & Testing

- [ ] All tests pass: `uv run task test:fast`
- [ ] Linting passes: `uv run task lint` (includes black, isort, mypy, bandit, vulture, radon)
- [ ] Code is formatted: `uv run task format`
- [ ] Coverage is acceptable (aim for >70%)
- [ ] No critical issues or TODOs in release code
- [ ] Code complexity is acceptable (no Grade D or E functions)
- [ ] Security scan passes (bandit)
- [ ] Dead code analysis passes (vulture)

### 2. Documentation Updates

- [ ] README.md is up to date with new features
- [ ] CHANGELOG.md has been updated with new version
- [ ] All new features are documented
- [ ] Breaking changes are clearly marked

### 3. Version Management

- [ ] Version bumped using automated tools: `uv run task version:bump:patch|minor|major`
- [ ] Version consistency verified: `uv run task version:show`
- [ ] All version references are automatically updated by the version management system

## Release Process

### Step 1: Prepare the Release

1. **Update CHANGELOG.md**

   ```bash
   # Add new version section at the top
   ## [X.Y.Z] - YYYY-MM-DD
   
   ### Added
   - New feature 1
   - New feature 2
   
   ### Changed
   - Improved feature 1
   
   ### Fixed
   - Bug fix 1
   ```

2. **Update Version Numbers**

   ```bash
   # Use the automated version management system
   uv run task version:bump:patch    # For bug fixes (0.2.1 → 0.2.2)
   uv run task version:bump:minor     # For new features (0.2.1 → 0.3.0)
   uv run task version:bump:major     # For breaking changes (0.2.1 → 1.0.0)
   
   # Or set a specific version
   uv run task version:set 1.0.0
   
   # Verify version consistency
   uv run task version:show
   ```

   **Note**: The version management system automatically updates:
   - `src/dococtopy/_version.py` (single source of truth)
   - All test files that check version
   - All components that import `__version__`

### Step 2: Commit and Tag

1. **Commit Changes**

   ```bash
   git add .
   git commit -m "feat: Bump version to X.Y.Z with [brief description]

   - Add feature 1
   - Add feature 2
   - Fix bug 1
   - Update documentation
   - Update version in pyproject.toml and __init__.py"
   ```

2. **Create Git Tag**

   ```bash
   git tag -a vX.Y.Z -m "Release vX.Y.Z: [Brief description]

   Features:
   - Feature 1: Description
   - Feature 2: Description
   - Bug fix 1: Description
   - Documentation updates
   - Performance improvements

   All X tests passing with Y% coverage."
   ```

### Step 3: Push to GitHub

1. **Push Changes and Tag**

   ```bash
   git push origin main
   git push origin vX.Y.Z
   ```

2. **Wait for GitHub Actions**
   - Monitor the Actions tab
   - Ensure all tests pass
   - Fix any failing tests before proceeding

### Step 4: Create GitHub Release

1. **Go to GitHub Releases**
   - Navigate to: <https://github.com/CrazyBonze/DocOctopy/releases>
   - Click "Create a new release"

2. **Fill Release Details**
   - **Tag version**: Select `vX.Y.Z`
   - **Release title**: `Release vX.Y.Z: [Brief description]`
   - **Description**: Copy from git tag message
   - **Attach files**: Upload built packages if needed

3. **Publish Release**
   - Click "Publish release"
   - This will trigger any release workflows

### Step 5: Build and Test Package

1. **Build Package**

   ```bash
   uv run task build
   ```

2. **Verify Package**

   ```bash
   uv run task check
   ```

3. **Test Installation**

   ```bash
   # Test local installation
   pip install dist/dococtopy-X.Y.Z-py3-none-any.whl
   dococtopy --version  # Should show X.Y.Z
   ```

### Step 6: Publish to PyPI (Optional)

1. **Publish Package**

   ```bash
   uv run task publish
   ```

2. **Verify on PyPI**
   - Check: <https://pypi.org/project/dococtopy/>
   - Verify version and description

## Version Numbering

### Semantic Versioning (SemVer)

- **MAJOR** (X.0.0): Breaking changes
- **MINOR** (X.Y.0): New features, backward compatible
- **PATCH** (X.Y.Z): Bug fixes, backward compatible

### Current Versioning Strategy

- **0.1.x**: Alpha releases with new features
- **0.2.x**: Beta releases with significant improvements
- **1.0.0**: First stable release

## Common Issues & Solutions

### Issue: Tests Fail After Version Bump

**Solution**: Update version expectations in test files

```bash
# Search for old version in tests
grep -r "0.1.0" tests/
# Update to new version
```

### Issue: GitHub Actions Fail

**Solution**:

1. Check test failures
2. Fix issues locally
3. Push fixes
4. Wait for Actions to pass

### Issue: Package Build Fails

**Solution**:

1. Check for syntax errors: `uv run task lint`
2. Verify dependencies: `uv run task install`
3. Clean and rebuild: `uv run task clean && uv run task build`

### Issue: Version Inconsistency

**Solution**: Ensure all version references are updated

```bash
# Check all version references
grep -r "0.1.0" . --exclude-dir=.git --exclude-dir=__pycache__ --exclude-dir=dist
```

## Post-Release Tasks

1. **Update Documentation**
   - Update any version-specific docs
   - Update installation instructions if needed

2. **Monitor Issues**
   - Watch for bug reports
   - Respond to user feedback

3. **Plan Next Release**
   - Review roadmap
   - Prioritize next features
   - Update TASKS.md

## Code Quality Standards

### Complexity Management

- **Target Complexity**: Functions should be Grade C or better (radon complexity)
- **High Complexity Functions**: Grade D or E functions should be refactored
- **Refactoring Process**:
  1. Identify high-complexity functions: `uv run task complexity:high`
  2. Extract helper functions to reduce complexity
  3. Write unit tests for new helper functions
  4. Verify all tests still pass

### Linting Tools

- **black**: Code formatting
- **isort**: Import sorting
- **mypy**: Type checking
- **bandit**: Security analysis
- **vulture**: Dead code detection
- **radon**: Code complexity analysis

### Testing Standards

- **Unit Tests**: All new functions must have unit tests
- **Integration Tests**: Test complete workflows
- **Coverage**: Maintain >70% test coverage
- **Edge Cases**: Test error conditions and edge cases

## Automation Opportunities

### Future Improvements

- [ ] Automated version bumping
- [ ] Automated changelog generation
- [ ] Automated PyPI publishing
- [ ] Automated GitHub release creation
- [ ] Pre-release validation scripts

### GitHub Actions Integration

- [ ] Release workflow that triggers on tag creation
- [ ] Automated PyPI publishing on release
- [ ] Automated GitHub release creation

## Release Notes Template

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- **New Feature 1**: Description of what it does and why it's useful
- **New Feature 2**: Description with examples if applicable

### Changed
- **Improved Feature**: What changed and why
- **Performance**: Specific improvements with metrics

### Fixed
- **Bug Fix**: Description of the issue and how it was resolved
- **Compatibility**: Any compatibility improvements

### Technical Improvements
- **Code Quality**: Refactoring, cleanup, etc.
- **Testing**: New tests, improved coverage
- **Documentation**: Updates and improvements

### Breaking Changes
- **If any**: Clear description of what breaks and migration path

### Migration Guide
- **If needed**: Step-by-step instructions for upgrading
```

## Version Management System

DocOctopy uses a centralized version management system to prevent version inconsistencies.

### Single Source of Truth

- **Version File**: `src/dococtopy/_version.py` contains the only version definition
- **Dynamic Import**: All components import version from `dococtopy.__version__`
- **Build Integration**: Hatchling automatically reads version from the centralized file

### Available Commands

```bash
# Show current version
uv run task version:show

# Bump versions
uv run task version:bump:patch    # Bug fixes (0.2.1 → 0.2.2)
uv run task version:bump:minor    # New features (0.2.1 → 0.3.0)
uv run task version:bump:major    # Breaking changes (0.2.1 → 1.0.0)

# Set specific version
uv run task version:set 1.0.0
```

### Automatic Updates

The version management system automatically updates:

- Version definition in `_version.py`
- Test files that check version output
- All components that import `__version__`
- Build metadata for packaging

### Benefits

- ✅ **No Version Drift**: Single source prevents inconsistencies
- ✅ **Automated Updates**: All dependent files updated automatically
- ✅ **Easy Management**: Simple CLI commands for version operations
- ✅ **Build Integration**: Works seamlessly with Hatchling

## Quick Reference Commands

```bash
# Full release process
git add .
git commit -m "feat: Bump version to X.Y.Z"
git tag -a vX.Y.Z -m "Release vX.Y.Z: Description"
git push origin main
git push origin vX.Y.Z

# Build and test
uv run task build
uv run task check
uv run task test:fast

# Publish (when ready)
uv run task publish
```

---

**Last Updated**: 2024-12-19  
**Current Version**: 0.2.1  
**Next Version**: Use `uv run task version:show` to check current version
