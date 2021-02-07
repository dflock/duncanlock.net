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

pandoc --wrap=preserve -f rst -t asciidoctor "$src_path" > "$src_folder/$src_name".adoc