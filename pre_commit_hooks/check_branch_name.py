from __future__ import annotations

import argparse
import re
import subprocess
from typing import Sequence

TYPES = "feat|fix|refactor|chore|test|docs|ci|build|perf|hotfix"
PROJECTS = "CE|CG|CS|GB|GS|GM|GF"
PATTERN = re.compile(rf"^({TYPES})/((({PROJECTS})-[0-9]+)|NOJIRA)-.+")

# Branches that should never be validated: a detached HEAD, the protected
# branches, and the throwaway names the merge queue creates.
SKIP_EXACT = {"HEAD", "master", "main", "production"}
SKIP_PREFIXES = ("gh-readonly-queue/",)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")  # accepted & ignored
    parser.parse_args(argv)

    branch = subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True
    ).strip()

    if branch in SKIP_EXACT or branch.startswith(SKIP_PREFIXES):
        return 0

    if PATTERN.match(branch) is None:
        print(
            f"✗ Branch '{branch}' does not match "
            "<type>/<JIRA-ID>-<description>.\n"
            "\n"
            f"  Allowed types:    {TYPES}\n"
            f"  Allowed projects: {PROJECTS}  "
            "(or NOJIRA for minor <2h changes, max 2/week)\n"
            "\n"
            "  Examples:\n"
            "    feat/GB-105-fraud-logic-with-missing-email\n"
            "    fix/GS-87-session-timeout\n"
            "    hotfix/NOJIRA-bump-dependency\n"
            "\n"
            "  Rename before pushing:  git branch -m <new-name>"
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
