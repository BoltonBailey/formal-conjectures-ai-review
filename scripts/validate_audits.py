#!/usr/bin/env python3
"""Validate models.json and the audit JSON files under `audits/`.

Usage: python3 scripts/validate_audits.py [--upstream PATH]

With `--upstream`, pointing at a checkout of formal-conjectures, also check that each audited
Lean file exists and mentions the last component of the declaration name.
"""

import argparse
import json
import re
import sys
from pathlib import Path

from common import AUDITS, ROOT, audit_files, lean_file_for, load_models, validate_models

FIELDS = {"hash", "model", "effort", "severity", "explanation"}
HASH_RE = re.compile(r"^[0-9a-f]{40}$")


def validate_entry(entry, model_ids):
    if not isinstance(entry, dict):
        return ["entry is not an object"]
    errors = []
    if set(entry) != FIELDS:
        missing, extra = FIELDS - set(entry), set(entry) - FIELDS
        if missing:
            errors.append(f"missing fields {sorted(missing)}")
        if extra:
            errors.append(f"unknown fields {sorted(extra)}")
    if "hash" in entry and not (isinstance(entry["hash"], str) and HASH_RE.match(entry["hash"])):
        errors.append("`hash` must be a full 40-character lowercase hex commit hash")
    if "model" in entry and entry["model"] not in model_ids:
        errors.append(f"`model` {entry['model']!r} is not listed in models.json")
    if "effort" in entry and not (entry["effort"] is None or isinstance(entry["effort"], str)):
        errors.append("`effort` must be a string or null")
    severity = entry.get("severity")
    if "severity" in entry and not (type(severity) is int and 1 <= severity <= 5):
        errors.append("`severity` must be an integer from 1 to 5")
    explanation = entry.get("explanation")
    if "explanation" in entry and not (isinstance(explanation, str) and explanation.strip()):
        errors.append("`explanation` must be a non-empty string")
    return errors


def validate_file(path, model_ids, upstream):
    rel = path.relative_to(AUDITS)
    errors = []
    if len(rel.parts) < 2:
        errors.append("audit files must live in a directory named after the audited Lean file")
    if path.suffix != ".json":
        return errors + ["audit files must have a .json extension"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return errors + [f"invalid JSON: {e}"]
    if not isinstance(data, list) or not data:
        return errors + ["top level must be a non-empty list of audit entries"]
    for i, entry in enumerate(data):
        errors += [f"entry {i}: {e}" for e in validate_entry(entry, model_ids)]
    if upstream is not None and len(rel.parts) >= 2:
        lean_file = lean_file_for(path)
        short_name = path.stem.split("-")[-1]
        if not (upstream / lean_file).is_file():
            errors.append(f"{lean_file} does not exist upstream")
        elif short_name not in (upstream / lean_file).read_text(encoding="utf-8"):
            errors.append(f"{short_name!r} does not appear in {lean_file}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--upstream", type=Path, help="path to a formal-conjectures checkout")
    args = parser.parse_args()

    models = load_models()
    model_errors = validate_models(models)
    if model_errors:
        print("\n".join(model_errors))
        return 1
    model_ids = {m["id"] for m in models}

    failed = False
    files = audit_files()
    for path in files:
        for error in validate_file(path, model_ids, args.upstream):
            failed = True
            print(f"{path.relative_to(ROOT)}: {error}")
    if not failed:
        print(f"OK: {len(models)} model entries and {len(files)} audit file(s) valid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
