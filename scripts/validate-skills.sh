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
  echo "Validating $skill"
  if ! "$validator" validate "$skill"; then
    failed=$((failed + 1))
  fi
done

if [[ $count -eq 0 ]]; then
  echo "No skills found." >&2
  exit 1
fi

if [[ $failed -ne 0 ]]; then
  echo "$failed skill(s) failed validation." >&2
  exit 1
fi

echo "All $count skills passed Agent Skills validation."
