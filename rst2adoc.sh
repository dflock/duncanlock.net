#!/usr/bin/env bash

# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -o nounset   # Using an undefined variable is fatal
set -o errexit   # A sub-process/shell returning non-zero is fatal
# set -o pipefail  # If a pipeline step fails, the pipelines RC is the RC of the failed step
# set -o xtrace    # Output a complete trace of all bash actions; uncomment for debugging

# IFS=$'\n\t'  # Only split strings on newlines & tabs, not spaces.

function init() {
  # readonly script_path="${BASH_SOURCE[0]:-$0}"
  # readonly script_dir="$(dirname "$(readlink -f "$script_path")")"
  # readonly script_name="$(basename "$script_path")"

  readonly src_path="$1"
  readonly src_folder="$(dirname "$src_path")"
  readonly src_filename="$(basename "$src_path")"
  readonly src_name="${src_filename%.*}"
}

function msg() {
  echo >&2 -e "${1:-}"
}

if [[ $# == 0 ]]; then
  msg "Missing parameter: Rst FILE."
  # usage
fi

init "$@"

# 
# Pre-process
# 
cat "$src_path" | \
# Remove :alt: tags from figures & images, otherwise they get lost
sed -r 's/:alt: /\n/g' | \
# Tabs to spaces
sed -r 's/\t/  /g' | \
# 
# Convert rst to asciidoc using pandoc
# 
pandoc --wrap=preserve --from rst --to asciidoctor | \
# 
# Post-process
# 
# Fix metadata syntax, from date:: to :date:
sed -r 'N; s/^(.*)::\n /:\1:/g; P; D' | \
# Remove extra breaks created from figure caption conversion
sed -r 'N; s/____\n//g; P; D' | \
# Fix alt text for images/figures
# perl -p0e 's/\[image\]\n\n(.*?)\n/[$1]\n/g' | \
# Make the line below the image into its caption
# perl -p0e 's/image::(.*?)]\n\n(.*?)\n/\.$2\nimage::$1]\n/g' | \
# Fix Pelican {static} links
sed -e 's/%7B/{/g' -e 's/%7D/}/g' \
> "$src_folder/$src_name".adoc