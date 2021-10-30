#!/usr/bin/env bash

# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -o nounset   # Using an undefined variable is fatal
set -o errexit   # A sub-process/shell returning non-zero is fatal
# set -o pipefail  # If a pipeline step fails, the pipelines RC is the RC of the failed step
# set -o xtrace    # Output a complete trace of all bash actions; uncomment for debugging

# IFS=$'\n\t'  # Only split strings on newlines & tabs, not spaces.

# Pull out all the meta :tags: lines from your posts
  # Remove the :tags: part and keep the tag values
  # Put each tag on it's own line
  # Remove blank lines
  # Group by tag, with count
  # Sort by count, desc
grep -R --no-filename ':tags:' ./content/posts/* \
  | cut -d':' -f3 \
  | tr ', ' '\n' \
  | sed '/^$/d' \
  | sort | uniq -c \
  | sort -nr
