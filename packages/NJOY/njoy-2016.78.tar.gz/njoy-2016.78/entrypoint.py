import argparse as ap
from pathlib import Path
import subprocess
import sys
import os

__njoy_exe_path: Path = Path(__file__).parent / "bin" / "njoy"


def main():
    parser = ap.ArgumentParser()
    parser.add_argument('input_deck')
    args = parser.parse_args()

    with open(args.input_deck) as stdin:
        subprocess.run([__njoy_exe_path], stdin=stdin, capture_output=False, shell=False, check=True)


if __name__ == '__main__':
    main()
