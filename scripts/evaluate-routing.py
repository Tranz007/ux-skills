#!/usr/bin/env python3
"""Evaluate UX Skills routing cases through a model-specific JSON-lines adapter."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CASES = ROOT / "tests" / "routing-cases.jsonl"
SKILLS_DIR = ROOT / "skills"


def load_cases(path: Path) -> list[dict[str, str]]:
    cases: list[dict[str, str]] = []
    for line_number, line in enumerate(path.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"line {line_number}: invalid JSON: {error.msg}") from error
        utterance = row.get("utterance")
        expected = row.get("expected")
        if not isinstance(utterance, str) or not utterance:
            raise ValueError(f"line {line_number}: missing utterance")
        if not isinstance(expected, str) or not expected:
            raise ValueError(f"line {line_number}: missing expected skill")
        if not (SKILLS_DIR / expected / "SKILL.md").is_file():
            raise ValueError(f"line {line_number}: unknown expected skill {expected}")
        cases.append({"utterance": utterance, "expected": expected})
    if not cases:
        raise ValueError("routing corpus is empty")
    return cases


def load_skills() -> list[dict[str, str]]:
    skills: list[dict[str, str]] = []
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        lines = skill_file.read_text().splitlines()
        if not lines or lines[0] != "---":
            raise ValueError(f"{skill_file.relative_to(ROOT)}: missing frontmatter")
        try:
            end = lines.index("---", 1)
        except ValueError as error:
            raise ValueError(f"{skill_file.relative_to(ROOT)}: unclosed frontmatter") from error
        frontmatter = lines[1:end]
        name = next((line.removeprefix("name: ") for line in frontmatter if line.startswith("name: ")), None)
        description = next(
            (line.removeprefix("description: ") for line in frontmatter if line.startswith("description: ")),
            None,
        )
        if not name or not description:
            raise ValueError(f"{skill_file.relative_to(ROOT)}: missing name or description")
        skills.append({"name": name, "description": description})
    return skills


def run_adapter(command: str, cases: list[dict[str, str]], skills: list[dict[str, str]]) -> int:
    process = subprocess.Popen(
        command,
        cwd=ROOT,
        shell=True,
        text=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=None,
    )
    assert process.stdin is not None
    assert process.stdout is not None

    failures = 0
    for case in cases:
        request = {"utterance": case["utterance"], "skills": skills}
        process.stdin.write(json.dumps(request) + "\n")
        process.stdin.flush()
        response = process.stdout.readline()
        if not response:
            process.kill()
            raise RuntimeError("adapter stopped before returning a prediction")
        try:
            prediction: Any = json.loads(response).get("predicted")
        except json.JSONDecodeError as error:
            raise RuntimeError(f"adapter returned invalid JSON: {error.msg}") from error
        if not isinstance(prediction, str):
            raise RuntimeError("adapter response must contain a string 'predicted' field")
        outcome = "PASS" if prediction == case["expected"] else "FAIL"
        print(f"{outcome}\t{case['expected']}\t{prediction}\t{case['utterance']}")
        failures += outcome == "FAIL"

    process.stdin.close()
    if process.wait() != 0:
        raise RuntimeError("adapter exited with a non-zero status")
    print(f"{len(cases) - failures}/{len(cases)} routing cases passed.")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate routing cases with a model-specific JSON-lines adapter.",
        epilog=(
            "The adapter receives {utterance, skills} and must return {predicted}. "
            "For example: python scripts/evaluate-routing.py --command './my-router'"
        ),
    )
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES, help="JSONL routing corpus")
    parser.add_argument("--command", help="adapter command; reads and writes one JSON object per line")
    parser.add_argument("--check", action="store_true", help="validate the corpus and skill metadata without calling an adapter")
    args = parser.parse_args()

    if bool(args.command) == bool(args.check):
        parser.error("provide exactly one of --command or --check")
    try:
        cases = load_cases(args.cases)
        skills = load_skills()
    except (OSError, ValueError) as error:
        parser.error(str(error))
    if args.check:
        print(f"Validated {len(cases)} routing cases and {len(skills)} skill descriptions.")
        return 0
    return run_adapter(args.command, cases, skills)


if __name__ == "__main__":
    raise SystemExit(main())
