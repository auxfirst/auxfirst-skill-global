#!/usr/bin/env python3
"""Score an agent action on the Action Heat Ladder.

The band is the *highest* single dimension score, never the mean. Doing this by
hand is where averaging creeps back in, which is the one failure the ladder
exists to prevent - so run this instead of reading the tables.

Usage:
    python heat.py --score 1,0,3,3,1 --action "send a routine invoice"
    python heat.py --score 1,0,3,3,1 --json
    python heat.py --file actions.csv        # action,rev,blast,exp,commit,auth

Scores are five integers 0-4 in dimension order:
    reversibility, blast radius, exposure, commitment, authority

Exit code is 0 on success, 2 on bad input. No third-party dependencies.
"""

import argparse
import csv
import json
import sys

DIMENSIONS = [
    ("reversibility", "Can we take it back?"),
    ("blast radius", "How far does it spread?"),
    ("exposure", "Who sees it?"),
    ("commitment", "What does it bind us to?"),
    ("authority", "What is it allowed to touch?"),
]

BANDS = ["LOW", "LOW-MED", "MEDIUM", "HIGH", "CRITICAL"]

MODE = {
    "LOW": "Autonomous",
    "LOW-MED": "Act-and-notify",
    "MEDIUM": "Review-before-act",
    "HIGH": "Approve-each-action",
    "CRITICAL": "Human-only",
}

POSTURE = {
    "LOW": "Auto-run. Log everything. The log is the control.",
    "LOW-MED": "Auto-run with sampled review on a cadence; every write has one-click undo.",
    "MEDIUM": "Propose, then batch-approve. The agent queues the action with its rationale.",
    "HIGH": "A named accountable human approves each instance before execution, logged with rationale and identity.",
    "CRITICAL": "The agent prepares evidence, draft and checklist. A human - sometimes two - performs the action.",
}

# Cumulative: each mode owes everything above it plus its own row.
PATTERNS = [
    ("CRITICAL", "Human-only", ["confidence ribbon", "reasoning trace", "permission scope", "activity stream"]),
    ("HIGH", "Approve-each-action", ["source citation", "version diff", "escape hatch", "approval queue"]),
    ("MEDIUM", "Review-before-act", ["dissent surface", "dry-run mode", "intervention point"]),
    ("LOW-MED", "Act-and-notify", ["calibration cue", "budget governor", "audit trail"]),
    ("LOW", "Autonomous", ["kill switch", "hand-off", "parallel session view"]),
]

PRIMITIVES = [
    ("agent identity and disclosure", 0),
    ("action receipt", 1),
    ("reversal", 1),
    ("consequence-scaled approval", 2),
    ("escalation handoff", 2),
    ("provenance at the decision point", 2),
]


def assess(scores):
    """Return the full obligation set implied by five dimension scores."""
    peak = max(scores)
    band = BANDS[peak]
    band_index = BANDS.index(band)

    # Every mode at or below this band's ceiling contributes its patterns.
    required = []
    for row_band, _mode, items in PATTERNS:
        if BANDS.index(row_band) >= band_index:
            required.extend(items)

    primitives = [name for name, threshold in PRIMITIVES if band_index >= threshold]

    drivers = [
        DIMENSIONS[i][0] for i, value in enumerate(scores) if value == peak
    ]

    return {
        "scores": {DIMENSIONS[i][0]: scores[i] for i in range(5)},
        "peak": peak,
        "driven_by": drivers,
        "band": band,
        "max_autonomy_mode": MODE[band],
        "control_posture": POSTURE[band],
        "required_patterns": required,
        "required_supervision_primitives": primitives,
    }


def render(action, result):
    lines = []
    title = action or "action"
    lines.append(f"# {title}")
    lines.append("")
    for name, _q in DIMENSIONS:
        marker = "  <- hottest" if name in result["driven_by"] else ""
        lines.append(f"  {name:<14} {result['scores'][name]}{marker}")
    lines.append("")
    lines.append(f"  BAND            {result['band']}  (highest single score, never the mean)")
    lines.append(f"  MAX AUTONOMY    {result['max_autonomy_mode']}")
    lines.append(f"  POSTURE         {result['control_posture']}")
    lines.append("")
    lines.append("  Required patterns (cumulative):")
    for item in result["required_patterns"]:
        lines.append(f"    - {item}")
    lines.append("")
    lines.append("  Required supervision primitives:")
    for item in result["required_supervision_primitives"]:
        lines.append(f"    - {item}")
    lines.append("")
    lines.append("  Next: can a de-escalator move this down a band? Dry-run, hard cap,")
    lines.append("  hold window, short-lived scoped credential, or a reversible")
    lines.append("  representation that a separate cheaper action promotes.")
    return "\n".join(lines)


def parse_scores(raw):
    parts = [p.strip() for p in raw.replace(" ", ",").split(",") if p.strip()]
    if len(parts) != 5:
        raise ValueError(
            f"expected 5 scores (reversibility,blast,exposure,commitment,authority), got {len(parts)}"
        )
    scores = []
    for part in parts:
        try:
            value = int(part)
        except ValueError:
            raise ValueError(f"'{part}' is not an integer 0-4")
        if not 0 <= value <= 4:
            raise ValueError(f"score {value} out of range; each dimension is 0-4")
        scores.append(value)
    return scores


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Score an agent action on the Action Heat Ladder."
    )
    parser.add_argument("--score", help="five comma-separated scores 0-4")
    parser.add_argument("--action", default="", help="what the action is called")
    parser.add_argument(
        "--file",
        help="CSV of action,reversibility,blast,exposure,commitment,authority",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args(argv)

    if not args.score and not args.file:
        parser.error("pass --score or --file")

    rows = []
    try:
        if args.file:
            with open(args.file, newline="", encoding="utf-8") as handle:
                for line_no, row in enumerate(csv.reader(handle), start=1):
                    if not row or row[0].strip().startswith("#"):
                        continue
                    if len(row) != 6:
                        raise ValueError(
                            f"line {line_no}: expected 6 columns, got {len(row)}"
                        )
                    if line_no == 1 and not row[1].strip().lstrip("-").isdigit():
                        continue  # header row
                    rows.append((row[0].strip(), parse_scores(",".join(row[1:]))))
        else:
            rows.append((args.action, parse_scores(args.score)))
    except (ValueError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    results = []
    for action, scores in rows:
        result = assess(scores)
        result["action"] = action
        results.append(result)

    if args.json:
        print(json.dumps(results if args.file else results[0], indent=2))
    else:
        print("\n\n".join(render(r["action"], r) for r in results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
