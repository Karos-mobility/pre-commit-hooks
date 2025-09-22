from __future__ import annotations

import argparse
import re
from typing import Sequence

PATTERN = re.compile(r"^\s*from unittest import TestCase$")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retcode = 0
    for filename in args.filenames:
        with open(filename, 'r') as inputfile:
            for i, line in enumerate(inputfile, start=1):
                if PATTERN.match(line) is not None:
                    print(
                        f'{filename}:{i}: `unittest.TestCase` found, '
                        'use `django.test.SimpleTestCase` for tests not using the database '
                        'or `django.test.TestCase` for tests using the database instead'
                    )
                    retcode = 1

    return retcode


if __name__ == '__main__':
    raise SystemExit(main())
