#!/usr/bin/env python3
"""Write a Markdown report of the issues that audits currently report, most severe first.

Usage: python3 scripts/top_issues.py --upstream PATH [--min-severity 3] [-n N] [-o top_issues.md]

This follows the procedure in the "Prioritizing Issues" section of README.md:

1. Take every (declaration, model) pair with at least one audit, where the declaration is
   still present in the most recent version of formal-conjectures.
2. The pair's current severity is that of the model's most recent audit of the declaration,
   i.e. the one conducted on the most recent formal-conjectures commit.
3. Sort the pairs by severity, then by how recent that audit is.

`--upstream` must be a clone of formal-conjectures (a bare clone is enough) whose HEAD is the
version to check declarations against. It is also used to look up the dates of audited commits.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from common import audit_files, lean_file_for

UPSTREAM_URL = "https://github.com/google-deepmind/formal-conjectures"
SEVERITY = {
    1: "correctly formulated",
    2: "mostly correct, perhaps with unclear documentation",
    3: "edge cases or discrepancies, but still equivalent",
    4: "essentially misformalized",
    5: "misformulated (provability differs)",
}
NAME = r"[^\s:({\[]+"
SCOPE_RE = re.compile(rf"^\s*(namespace|section|end)\b[ \t]*({NAME})?")
DECL_RE = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)*"
    r"(?:(?:private|protected|public|noncomputable|unsafe|partial|nonrec)\s+)*"
    r"(?:theorem|lemma|def|abbrev|instance|structure|class|inductive|opaque|axiom)\s+"
    rf"({NAME})"
)


@dataclass
class Assessment:
    """The current assessment of one declaration by one model."""
    name: str
    path: Path
    entry: dict
    time: int | None

    @property
    def date(self):
        return datetime.fromtimestamp(self.time, timezone.utc).date() if self.time else None


def git(upstream, *args):
    result = subprocess.run(["git", "-C", str(upstream), *args], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None


def declarations_in(source):
    """The fully qualified names of the declarations in a Lean source file."""
    names, scopes = set(), []  # scopes: the namespace name, or None for a section
    for line in source.splitlines():
        if m := SCOPE_RE.match(line):
            kind, name = m.groups()
            if kind == "end":
                if scopes:
                    scopes.pop()
            else:
                scopes.append(name if kind == "namespace" else None)
        elif m := DECL_RE.match(line):
            name = m.group(1)
            if name.startswith("_root_."):
                names.add(name.removeprefix("_root_."))
            else:
                names.add(".".join([s for s in scopes if s] + [name]))
    return names


class Upstream:
    """Cached lookups in a formal-conjectures clone."""

    def __init__(self, path):
        self.path = path
        self.times = {}
        self.declarations = {}

    def commit_time(self, commit):
        """The commit timestamp of `commit`, or None if upstream does not have it."""
        if commit not in self.times:
            out = git(self.path, "show", "-s", "--format=%ct", commit)
            self.times[commit] = int(out) if out else None
        return self.times[commit]

    def has_declaration(self, lean_file, name):
        """Whether `name` is declared in `lean_file` at upstream HEAD."""
        if lean_file not in self.declarations:
            source = git(self.path, "show", f"HEAD:{lean_file}")
            self.declarations[lean_file] = declarations_in(source) if source else set()
        return name in self.declarations[lean_file]


def declaration_name(audit_path):
    return audit_path.stem.replace("-", ".")


def current_assessments(upstream):
    """Each model's most recent audit of each declaration, keyed by declaration then model."""
    current = {}
    for path in audit_files():
        by_model = current.setdefault(declaration_name(path), {})
        for entry in json.loads(path.read_text(encoding="utf-8")):
            a = Assessment(declaration_name(path), path, entry, upstream.commit_time(entry["hash"]))
            previous = by_model.get(entry["model"])
            # Entries are appended to audit files, so on a tie the later entry is the newer one.
            if previous is None or (a.time or -1) >= (previous.time or -1):
                by_model[entry["model"]] = a
    return current


def prioritized(current, upstream, min_severity):
    """Assessments of at least `min_severity` for declarations still present, most urgent first."""
    issues = [
        a for by_model in current.values() for a in by_model.values()
        if a.entry["severity"] >= min_severity
        and upstream.has_declaration(lean_file_for(a.path).as_posix(), a.name)
    ]
    return sorted(issues, key=lambda a: (-a.entry["severity"], -(a.time or -1), a.name,
                                         a.entry["model"]))


def render(issues, current, min_severity, out_dir):
    lines = [
        "# Top issues",
        "",
        "The issues that audits currently report, ranked as described in the "
        "[Prioritizing Issues](README.md#prioritizing-issues) section of the README: each "
        "entry is a model's most recent audit of a declaration that is still present in "
        f"`formal-conjectures`, with severity at least {min_severity}, sorted by severity and "
        "then by how recent the audited commit is.",
        "",
    ]
    if not issues:
        lines.append("No audits currently report an issue.")
    for rank, a in enumerate(issues, 1):
        e = a.entry
        lean_file = lean_file_for(a.path).as_posix()
        audit_link = Path(os.path.relpath(a.path, out_dir)).as_posix()
        others = [o for model, o in sorted(current[a.name].items()) if model != e["model"]]
        lines += [
            f"{rank}. `{a.name}`: severity {e['severity']}, {SEVERITY[e['severity']]}",
            "",
            "   <details>",
            "   <summary>Details</summary>",
            "",
            f"   - **File:** [{lean_file}]({UPSTREAM_URL}/blob/{e['hash']}/{lean_file})",
            f"   - **Commit:** [`{e['hash'][:12]}`]({UPSTREAM_URL}/commit/{e['hash']})"
            + (f" ({a.date})" if a.date else ""),
            f"   - **Model:** {e['model']}" + (f" ({e['effort']})" if e["effort"] else ""),
            f"   - **Audit file:** [{a.path.name}]({audit_link})",
        ]
        if others:
            lines.append("   - **Other models:** " + ", ".join(
                f"{o.entry['model']} severity {o.entry['severity']}" for o in others))
        lines += ["", "   " + e["explanation"], "", "   </details>", ""]
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--upstream", type=Path, required=True,
                        help="formal-conjectures clone, with HEAD at the most recent version")
    parser.add_argument("--min-severity", type=int, default=3, choices=range(1, 6),
                        help="lowest severity to list (default 3)")
    parser.add_argument("-n", type=int, help="list at most this many issues (default: all)")
    parser.add_argument("-o", "--output", type=Path, default=Path("top_issues.md"),
                        help="output file (default top_issues.md)")
    args = parser.parse_args()

    if git(args.upstream, "rev-parse", "HEAD") is None:
        print(f"error: {args.upstream} is not a git repository with a HEAD", file=sys.stderr)
        return 1
    upstream = Upstream(args.upstream)
    current = current_assessments(upstream)
    issues = prioritized(current, upstream, args.min_severity)[:args.n]
    args.output.write_text(render(issues, current, args.min_severity,
                                  args.output.resolve().parent), encoding="utf-8")
    print(f"Wrote {len(issues)} issue(s) to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
