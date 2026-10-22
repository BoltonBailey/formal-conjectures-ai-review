#!/usr/bin/env python3
"""Write a Markdown report of the most urgent misformalizations reported by audits.

Usage: python3 scripts/top_issues.py [--upstream PATH] [-n 10] [-o top_issues.md]

Audits are ranked as in sort_audits.py (see CONTRIBUTING.md); `--upstream` is as there. Each
issue is one declaration, represented by its most urgent audit, with details collapsed.
"""

import argparse
import os
import sys
from pathlib import Path

from common import lean_file_for
from sort_audits import prioritized_audits

UPSTREAM_URL = "https://github.com/google-deepmind/formal-conjectures"
SEVERITY = {
    4: "essentially misformalized",
    5: "misformulated (provability differs)",
}


def relpath(path, start):
    return Path(os.path.relpath(path, start)).as_posix()


def declaration_name(audit_path):
    return audit_path.stem.replace("-", ".")


def render(issues, others, out_dir):
    lines = [
        "# Top issues",
        "",
        "The most urgent misformalizations reported by audits, ranked as described in "
        "CONTRIBUTING.md.",
        "",
    ]
    if not issues:
        lines.append("No audits currently report a misformalization.")
    for rank, a in enumerate(issues, 1):
        e = a.entry
        lean_file = lean_file_for(a.path).as_posix()
        name = declaration_name(a.path)
        score = f"{a.score:.1f}" if a.score is not None else "unscored"
        lines += [
            f"{rank}. `{name}`: severity {e['severity']}, {SEVERITY[e['severity']]}",
            "",
            "   <details>",
            "   <summary>Details</summary>",
            "",
            f"   - **File:** [{lean_file}]({UPSTREAM_URL}/blob/{e['hash']}/{lean_file})",
            f"   - **Commit:** [`{e['hash'][:12]}`]({UPSTREAM_URL}/commit/{e['hash']})"
            + (f" ({a.date})" if a.date else ""),
            f"   - **Model:** {e['model']}"
            + (f" ({e['effort']})" if e["effort"] else "")
            + f", MathArena score {score}",
            f"   - **Audit file:** [{a.path.name}]({relpath(a.path, out_dir)})",
        ]
        if others[name]:
            lines.append(f"   - **Other audits reporting a misformalization:** {others[name]}")
        lines += ["", "   " + e["explanation"], "", "   </details>", ""]
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--upstream", type=Path, help="formal-conjectures clone with full history")
    parser.add_argument("-n", type=int, default=10, help="number of issues to list (default 10)")
    parser.add_argument("-o", "--output", type=Path, default=Path("top_issues.md"),
                        help="output file (default top_issues.md)")
    args = parser.parse_args()

    issues, others = [], {}
    for a in prioritized_audits(args.upstream):
        name = declaration_name(a.path)
        if name in others:
            others[name] += 1
        else:
            others[name] = 0
            issues.append(a)
    report = render(issues[:args.n], others, args.output.resolve().parent)
    args.output.write_text(report, encoding="utf-8")
    print(f"Wrote {min(len(issues), args.n)} issue(s) to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
