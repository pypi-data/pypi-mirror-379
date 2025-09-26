# cici pipeline

Build and publish CI/CD pipeline components with cici.

cici, short for Continuous Integration Catalog Interface, is a framework and
toolkit for managing the integration and lifecycle of packaged CI/CD
components in a software delivery pipeline.

cici enables the efficient sharing of CI/CD code in an organization, and
eliminates a major source of friction that otherwise leads to poor adoption of
automation and DevOps practices.

cici is a foundational component of [saferatday0](https://saferatday0.dev/)
and powers the [saferatday0 library](https://gitlab.com/saferatday0/library).

## Targets

| Name                        | [GitLab include](https://docs.gitlab.com/ee/ci/yaml/includes.html) | [pre-commit hook](https://pre-commit.com/) | Description                                               |
| --------------------------- | ------------------------------------------------------------------ | ------------------------------------------ | --------------------------------------------------------- |
| [cici-bundle](#cici-bundle) | ✓                                                                  | ✓                                          | Bundle GitLab CI/CD includes into single files.           |
| [cici-readme](#cici-readme) | ✓                                                                  | ✓                                          | Generate READMEs for CI pipelines.                        |
| [cici-update](#cici-update) | ✓                                                                  | ✓                                          | Update GitLab CI/CD includes to latest released versions. |

### `cici-bundle`

Bundle GitLab CI/CD includes into single files.

As a GitLab include:

```yaml
# .gitlab-ci.yml
include:
  - project: saferatday0/cici
    file:
      - cici-bundle.yml
```

As a pre-commit hook:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://gitlab.com/saferatday0/cici
    rev: ""
    hooks:
      - id: cici-bundle
```

### `cici-readme`

Generate READMEs for CI pipelines.

As a GitLab include:

```yaml
# .gitlab-ci.yml
include:
  - project: saferatday0/cici
    file:
      - cici-readme.yml
```

As a pre-commit hook:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://gitlab.com/saferatday0/cici
    rev: ""
    hooks:
      - id: cici-readme
```

### `cici-update`

Update GitLab CI/CD includes to latest released versions.

As a GitLab include:

```yaml
# .gitlab-ci.yml
include:
  - project: saferatday0/cici
    file:
      - cici-update.yml
```

As a pre-commit hook:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://gitlab.com/saferatday0/cici
    rev: ""
    hooks:
      - id: cici-update
```
