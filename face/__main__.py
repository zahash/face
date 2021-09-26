import sys
import json
import argparse
from .detect import recognize

ap = argparse.ArgumentParser(allow_abbrev=False)
ap.add_argument(
    "filepaths",
    nargs="+",
    help="one or more space separated image filepaths",
)
args = ap.parse_args()

for fpath in args.filepaths:
    try:
        faces = recognize(fpath)
        for f in faces:
            json.dump(f, sys.stdout)
            sys.stdout.write("\n")
    except FileNotFoundError as e:
        sys.stderr.write(f"{e}\n")
