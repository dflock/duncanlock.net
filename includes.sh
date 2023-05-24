#!/usr/bin/env bash

# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -o nounset   # Using an undefined variable is fatal
set -o errexit   # A sub-process/shell returning non-zero is fatal
# set -o pipefail  # If a pipeline step fails, the pipelines RC is the RC of the failed step
# set -o xtrace    # Output a complete trace of all bash actions; uncomment for debugging

# IFS=$'\n\t'  # Only split strings on newlines & tabs, not spaces.

function setup_colors() {
  if [[ -t 2 ]] && [[ -z "${NO_COLOR-}" ]] && [[ "${TERM-}" != "dumb" ]]; then
    # Control sequences for fancy colours
    readonly gry="$(tput setaf 240 2> /dev/null || true)"
    readonly bld="$(tput bold 2> /dev/null || true)"
    readonly off="$(tput sgr0 2> /dev/null || true)"
  else
    readonly gry=''
    readonly bld=''
    readonly off=''
  fi
}

function msg() {
  echo >&2 -e "${1:-}"
}

function die() {
  local msg=$1
  local code=${2:-1} # default exit status 1
  msg "$msg"
  exit "$code"
}

function slugify() {
  iconv -t ascii//TRANSLIT \
  | tr -d "'" \
  | sed -E 's/[^a-zA-Z0-9]+/-/g' \
  | sed -E 's/^-+|-+$//g' \
  | tr "[:upper:]" "[:lower:]"
}

function trim() {
  # Merge all passed in arguments into $var
  local var="$*"
  # remove leading whitespace characters
  var="${var#"${var%%[![:space:]]*}"}"
  # remove trailing whitespace characters
  var="${var%"${var##*[![:space:]]}"}"   
  printf '%s' "$var"
}