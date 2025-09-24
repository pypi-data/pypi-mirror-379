# GitHub Actions Publishing Setup

This guide explains how to set up automated publishing to PyPI using GitHub Actions.

## Option 1: Traditional Publishing (with API tokens)

### Step 1: Create PyPI API Token

1. Go to [pypi.org](https://pypi.org) and log in
2. Go to Account Settings → API tokens
3. Click "Add API token"
4. Give it a name like "eml-to-pdf-github-actions"
5. Set scope to "Entire account" (or create a project-specific token)
6. Copy the token (starts with `pypi-`)

### Step 2: Add Secret to GitHub

1. Go to your GitHub repository
2. Click Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `PYPI_API_TOKEN`
5. Value: Your PyPI API token
6. Click "Add secret"

### Step 3: Use the Workflow

The `publish.yml` workflow will automatically run when you:
- Create a new release
- Manually trigger it from the Actions tab

## Option 2: Trusted Publishing (Recommended)

This is the modern, more secure approach that doesn't require API tokens.

### Step 1: Enable Trusted Publishing on PyPI

1. Go to [pypi.org](https://pypi.org) and log in
2. Go to Account Settings → Publishing
3. Click "Add a new pending publisher"
4. Fill in the form:
   - **PyPI Project Name**: `eml-to-pdf`
   - **Owner**: `AlienZaki` (your GitHub username)
   - **Repository name**: `eml-to-pdf`
   - **Workflow name**: `publish-trusted.yml`
   - **Environment name**: `pypi` (optional but recommended)
5. Click "Add"

### Step 2: Create GitHub Environment (Optional but Recommended)

1. Go to your GitHub repository
2. Click Settings → Environments
3. Click "New environment"
4. Name: `pypi`
5. Add protection rules if desired (e.g., require approval)
6. Click "Create environment"

### Step 3: Use the Trusted Publishing Workflow

The `publish-trusted.yml` workflow will automatically run when you:
- Create a new release
- Manually trigger it from the Actions tab

## Workflow Files Explained

### `ci.yml` - Continuous Integration
- Runs on every push and pull request
- Tests on multiple Python versions (3.8-3.12)
- Runs linting, type checking, and tests
- Builds the package to ensure it works

### `publish.yml` - Traditional Publishing
- Uses API tokens for authentication
- Requires `PYPI_API_TOKEN` secret
- Runs on releases and manual triggers

### `publish-trusted.yml` - Trusted Publishing
- Uses PyPI's trusted publishing feature
- No secrets required
- More secure and modern approach

## Publishing Process

### Method 1: Create a Release

1. Go to your GitHub repository
2. Click "Releases" → "Create a new release"
3. Choose a tag (e.g., `v1.0.0`)
4. Add release title and description
5. Click "Publish release"
6. GitHub Actions will automatically build and publish to PyPI

### Method 2: Manual Trigger

1. Go to your GitHub repository
2. Click "Actions" tab
3. Select "Publish to PyPI" workflow
4. Click "Run workflow"
5. Choose branch and click "Run workflow"

## Version Management

To update the package version:

1. Update version in these files:
   - `src/eml_to_pdf/__init__.py`
   - `setup.py`
   - `pyproject.toml`

2. Commit and push changes:
   ```bash
   git add .
   git commit -m "Bump version to 1.0.1"
   git push
   ```

3. Create a new release with the same version tag

## Monitoring

- Check the Actions tab for workflow status
- Monitor PyPI for successful uploads
- Check package downloads and issues

## Troubleshooting

### Common Issues

1. **Workflow fails**: Check the Actions tab for error details
2. **Package not found**: Ensure the package name matches exactly
3. **Permission denied**: Check your PyPI API token or trusted publishing setup
4. **Version already exists**: Increment the version number

### Useful Commands

```bash
# Check workflow status
gh run list

# View workflow logs
gh run view <run-id>

# Trigger workflow manually
gh workflow run publish.yml
```

## Security Best Practices

1. **Use trusted publishing** instead of API tokens when possible
2. **Protect your main branch** with branch protection rules
3. **Use environment protection** for production releases
4. **Review all changes** before merging to main
5. **Keep dependencies updated** regularly

## Package Information

- **Package Name**: `eml-to-pdf`
- **GitHub Repository**: `AlienZaki/eml-to-pdf`
- **PyPI Project**: https://pypi.org/project/eml-to-pdf/
- **Workflow Files**: `.github/workflows/`

## Next Steps

1. Choose your publishing method (traditional or trusted)
2. Set up the required configuration
3. Test with a pre-release version
4. Create your first release
5. Monitor the publishing process
