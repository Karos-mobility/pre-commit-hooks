pre-commit-hooks
================

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/Karos-mobility/pre-commit-hooks.git
    rev: v0.2.0  # Use the ref you want to point at
    hooks:
    -   id: check-import-datetime
    -   id: check-import-unittest-testcase
```

### Hooks available

#### `check-import-datetime`
Checks that datetime module is not imported directly.

#### `check-import-unittest-testcase`
Checks that unittest.TestCase is not used.
