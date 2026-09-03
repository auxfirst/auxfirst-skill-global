#!/usr/bin/env python3
"""Repo-side validation, so CI can check the skill without skill-creator installed.

Mirrors the skill-creator frontmatter rules (they are what the Skills API and
claude.ai enforce on upload) and adds the checks specific to this repo: every
file the SKILL.md points at exists, and the scoring script still produces the
bands the documentation claims.

    python tools/validate.py
"""

import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "auxfirst"
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}

failures = []


def check(condition, message):
    if not condition:
        failures.append(message)


def parse_frontmatter(text):
    """Minimal front-matter reader: enough for the flat keys a SKILL.md may use."""
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    data, current = {}, None
    for line in match.group(1).split("\n"):
        if not line.strip():
            continue
        if line.startswith(("  ", "\t")):
            if current:
                data.setdefault(current, {})
            continue
        key, _, value = line.partition(":")
        current = key.strip()
        data[current] = value.strip()
    return data


def main():
    skill_files = [p for p in SKILL_DIR.rglob("SKILL.md")]
    check(len(skill_files) == 1, f"expected exactly one SKILL.md, found {len(skill_files)}")
    if not skill_files:
        report()
        return 1

    text = skill_files[0].read_text(encoding="utf-8")
    front = parse_frontmatter(text)
    check(front is not None, "SKILL.md has no YAML frontmatter")
    if front is None:
        report()
        return 1

    unexpected = set(front) - ALLOWED_KEYS
    check(not unexpected, f"unexpected frontmatter keys: {sorted(unexpected)}")

    name = front.get("name", "")
    check(bool(name), "frontmatter is missing 'name'")
    check(bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name)), f"name '{name}' is not kebab-case")
    check(len(name) <= 64, "name exceeds 64 characters")
    check(name == SKILL_DIR.name, f"name '{name}' does not match directory '{SKILL_DIR.name}'")

    description = front.get("description", "")
    check(bool(description), "frontmatter is missing 'description'")
    check(len(description) <= 1024, f"description is {len(description)} characters, max is 1024")
    check("<" not in description and ">" not in description, "description contains angle brackets")

    # Every bundled path the body points at must exist - a dangling pointer sends
    # the model looking for guidance that is not there.
    for rel in sorted(set(re.findall(r"`((?:references|assets|scripts)/[\w./-]+)`", text))):
        check((SKILL_DIR / rel).exists(), f"SKILL.md references missing file: {rel}")

    for path in (ROOT / ".claude-plugin").glob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            failures.append(f"{path.name} is not valid JSON: {error}")

    eval_set = json.loads((SKILL_DIR / "evals" / "trigger-eval.json").read_text(encoding="utf-8"))
    positives = sum(1 for case in eval_set if case["should_trigger"])
    check(len(eval_set) >= 20, f"trigger eval has {len(eval_set)} cases, want at least 20")
    check(6 <= positives <= len(eval_set) - 6, "trigger eval is lopsided; keep both sides substantial")

    # The bands in the docs and the bands the script emits have to stay in step,
    # because the script is what teams will actually run.
    for scores, expected in (("0,0,0,0,0", "LOW"), ("1,0,3,3,1", "HIGH"),
                             ("0,0,1,0,1", "LOW-MED"), ("2,3,1,0,4", "CRITICAL")):
        out = subprocess.run(
            [sys.executable, str(SKILL_DIR / "scripts" / "heat.py"), "--score", scores, "--json"],
            capture_output=True, text=True, check=False,
        )
        check(out.returncode == 0, f"heat.py failed on {scores}: {out.stderr.strip()}")
        if out.returncode == 0:
            band = json.loads(out.stdout)["band"]
            check(band == expected, f"heat.py scored {scores} as {band}, expected {expected}")

    bad = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "heat.py"), "--score", "5,0,0,0,0"],
        capture_output=True, text=True, check=False,
    )
    check(bad.returncode == 2, "heat.py should exit 2 on an out-of-range score")

    return report()


def report():
    if failures:
        for message in failures:
            print(f"FAIL  {message}")
        print(f"\n{len(failures)} problem(s).")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
