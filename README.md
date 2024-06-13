pre-commit-hooks
================

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/KgaevskiT/pre-commit-hooks
    rev: v0.1.1  # Use the ref you want to point at
    hooks:
    -   id: check-import-datetime
```

### Hooks available

#### `check-import-datetime`
Checks that datetime module is not imported directly.
