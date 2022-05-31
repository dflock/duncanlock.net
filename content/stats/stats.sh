#!/usr/bin/env bash

# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -o nounset   # Using an undefined variable is fatal
set -o errexit   # A sub-process/shell returning non-zero is fatal
# set -o pipefail  # If a pipeline step fails, the pipelines RC is the RC of the failed step
# set -o xtrace    # Output a complete trace of all bash actions; uncomment for debugging

# IFS=$'\n\t'  # Only split strings on newlines & tabs, not spaces.

cd ../posts
echo "filename,wc,date,slug,status"
# grep --recursive --fixed-strings --files-without-match --include '*.adoc' ':status: draft'| while read -r f ; do
find . -name "*.adoc"| while read -r filename ; do
  # Get a rough word-count, excluding metadata, image & video tags
  wc=$(sed '/^:/d' "$filename" | sed '/^video::/d' | sed '/^image::/d' | wc --words)
  # Pull out some peices of metadata
  date=$(grep --only-matching ':date: .*' "$filename" | cut -d' ' -f2)
  slug=$(grep --only-matching ':slug: .*' "$filename" | cut -d' ' -f2)
  status=$(grep --only-matching ':status: .*' "$filename" | cut -d' ' -f2)
  # Output the data for this file
  echo "\"$filename\",$wc,$date,\"$slug\",${status:-published}"
done
