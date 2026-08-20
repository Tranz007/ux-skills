#!/usr/bin/env bash
set -euo pipefail

if command -v skills-ref >/dev/null 2>&1; then
  validator="skills-ref"
elif command -v agentskills >/dev/null 2>&1; then
  validator="agentskills"
else
  echo "Agent Skills reference validator not found." >&2
  echo "Install it from the official agentskills/agentskills skills-ref directory, then run this script again." >&2
  exit 1
fi

failed=0
count=0

for skill in skills/*/; do
  [[ -d "$skill" ]] || continue
  count=$((count + 1))
  skill_file="${skill}SKILL.md"

  echo "Validating $skill"

  if ! "$validator" validate "$skill"; then
    failed=$((failed + 1))
  fi

  if [[ ! -f "$skill_file" ]]; then
    echo "Missing $skill_file" >&2
    failed=$((failed + 1))
    continue
  fi

  if ! grep -q '^## Always$' "$skill_file"; then
    echo "$skill_file is missing the shared ## Always behavior contract." >&2
    failed=$((failed + 1))
    continue
  fi

  for principle in Context Evidence System Clear Trust; do
    if ! grep -q "\*\*${principle}\*\*" "$skill_file"; then
      echo "$skill_file is missing shared principle: $principle" >&2
      failed=$((failed + 1))
    fi
  done
done

if [[ $count -eq 0 ]]; then
  echo "No skills found." >&2
  exit 1
fi

if [[ $failed -ne 0 ]]; then
  echo "$failed validation check(s) failed." >&2
  exit 1
fi

echo "All $count skills passed Agent Skills validation and the shared UX behavior contract."
