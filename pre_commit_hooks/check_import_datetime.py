from __future__ import annotations

import argparse
import re
from typing import Sequence

PATTERN = re.compile(r"^\s*import datetime$")


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
                        f'{filename}:{i}: `import datetime` found, '
                        'use `from datetime import ...` instead'
                    )
                    retcode = 1

    return retcode


if __name__ == '__main__':
    raise SystemExit(main())
