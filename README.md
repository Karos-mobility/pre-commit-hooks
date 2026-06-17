pre-commit-hooks
================

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/Karos-mobility/pre-commit-hooks.git
    rev: v0.3.0  # Use the ref you want to point at
    hooks:
    -   id: check-import-datetime
    -   id: check-import-unittest-testcase
    -   id: check-branch-name
```

`check-branch-name` runs at the `pre-push` stage, so consumers must install that
hook type as well as the default `pre-commit` one. Either set it in the config:

```yaml
default_install_hook_types: [pre-commit, pre-push]
```

or install it explicitly: `pre-commit install --hook-type pre-push`.

### Hooks available

#### `check-import-datetime`
Checks that datetime module is not imported directly.

#### `check-import-unittest-testcase`
Checks that unittest.TestCase is not used.

#### `check-branch-name`
Checks that the current branch matches the Karos naming convention,
`<type>/<JIRA-ID>-<description>` (e.g. `feat/GB-105-fraud-logs`), with `NOJIRA`
allowed in place of the ticket. This is a `pre-push` hook (see the install note
above).
