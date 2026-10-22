#!/usr/bin/env python3
"""Print audits in order of urgency, following CONTRIBUTING.md.

Usage: python3 scripts/sort_audits.py [--upstream PATH] [--all]

Without `--upstream` the commit-recency criterion is skipped. `--upstream` must be a clone of
formal-conjectures with full history, so that commit dates can be looked up; a blobless clone
(`git clone --filter=blob:none`) is enough. By default only audits reporting a
misformalization (severity 4 or 5) are shown; `--all` shows every audit.
"""

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path

from common import ROOT, audit_files, load_models, model_score

MISFORMALIZED = 4


@dataclass
class Audit:
    path: Path
    entry: dict
    time: int | None
    score: float | None

    @property
    def date(self) -> date | None:
        return datetime.fromtimestamp(self.time, timezone.utc).date() if self.time else None


def commit_time(upstream, commit, cache):
    """The commit timestamp of `commit` in the upstream checkout, or None if unknown."""
    if commit not in cache:
        result = subprocess.run(
            ["git", "-C", str(upstream), "show", "-s", "--format=%ct", commit],
            capture_output=True, text=True,
        )
        cache[commit] = int(result.stdout) if result.returncode == 0 else None
    return cache[commit]


def urgency(audit):
    return (
        audit.entry["severity"] < MISFORMALIZED,
        -(audit.score if audit.score is not None else -1),
        # Most recent commit first; unknown commits last.
        -(audit.time if audit.time is not None else -1),
        -audit.entry["severity"],
    )


def prioritized_audits(upstream=None, include_all=False):
    """All audits (only misformalizations unless `include_all`), most urgent first."""
    models = load_models()
    cache = {}
    audits = []
    for path in audit_files():
        for entry in json.loads(path.read_text(encoding="utf-8")):
            if entry["severity"] < MISFORMALIZED and not include_all:
                continue
            time = commit_time(upstream, entry["hash"], cache) if upstream is not None else None
            score = model_score(models, entry["model"], entry["effort"])
            audits.append(Audit(path, entry, time, score))
    return sorted(audits, key=urgency)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--upstream", type=Path, help="formal-conjectures clone with full history")
    parser.add_argument("--all", action="store_true", help="include audits with severity < 4")
    args = parser.parse_args()

    for a in prioritized_audits(args.upstream, args.all):
        score_text = f"{a.score:.1f}" if a.score is not None else "-"
        print(f"severity {a.entry['severity']}  commit {str(a.date or 'unknown'):10}  "
              f"score {score_text:>5}  {a.entry['model']} ({a.entry['effort']})  "
              f"{a.path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
