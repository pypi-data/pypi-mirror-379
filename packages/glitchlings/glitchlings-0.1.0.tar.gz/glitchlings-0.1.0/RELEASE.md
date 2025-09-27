# Releasing glitchlings to PyPI

This project is configured to publish to PyPI via GitHub Actions when you push a version tag.

## 1) One-time setup

- Decide publishing auth method:
  - Preferred: PyPI Trusted Publishing using OIDC. Enable it for the `glitchlings` project in PyPI and grant the GitHub repo `osoleve/glitchlings` permission.
  - Alternative: Create a PyPI token (scoped to the project) and add it as a repository secret `PYPI_API_TOKEN`.
- (Optional) Add `TEST_PYPI_API_TOKEN` if you want automatic TestPyPI uploads on pushes to `trunk`.

## 2) Versioning

- Update `version` in `pyproject.toml`.
- Follow SemVer tags like `v0.1.1`.

## 3) Dry-run on TestPyPI (optional)

- Push to `trunk`. If `TEST_PYPI_API_TOKEN` is set, a wheel and sdist will be uploaded to TestPyPI automatically.

## 4) Publish to PyPI

- Create and push a tag from the repository root:

  ```pwsh
  git tag v0.1.1
  git push origin v0.1.1
  ```

- The workflow `.github/workflows/publish.yml` will build the package from the `glitchlings/` directory and publish the artifacts to PyPI.

## 5) Verify

- Check the run in GitHub Actions.
- Verify the release on PyPI project page.

## Notes

- The package uses Hatchling and includes a console script `glitchlings` that runs `glitchlings.main:main`.
- Build locally:

  ```pwsh
  python -m pip install --upgrade build
  python -m build glitchlings
  ```

- If adding new modules, ensure they live under the `glitchlings/` directory so they are included in the wheel.
