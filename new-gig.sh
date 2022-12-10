#!/usr/bin/env bash

# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -o nounset   # Using an undefined variable is fatal
set -o errexit   # A sub-process/shell returning non-zero is fatal
# set -o pipefail  # If a pipeline step fails, the pipelines RC is the RC of the failed step
# set -o xtrace    # Output a complete trace of all bash actions; uncomment for debugging

# IFS=$'\n\t'  # Only split strings on newlines & tabs, not spaces.

function init() {
  readonly script_path="${BASH_SOURCE[0]:-$0}"
  readonly script_dir="$(dirname "$(readlink -f "$script_path")")"
  readonly script_name="$(basename "$script_path")"

  tags="gig,review,music"
  category="personal"
  venue=''
  rating=''
  artist=''

  setup_colors
  parse_params "$@"
}

function usage() {
  cat <<EOF

Create a new draft gig review for the blog

${bld}USAGE${off}
  $script_name [options] ARTIST

${bld}OPTIONS${off}
  -h, --help       show this help
  -t, --tags       Extra tags for this post. Prepended with 'gig,music,review'. Comma separated, no spaces.
  -c, --category   Category for the post, no spaces. If none, defaults to personal.
  -v, --venue      Sets the Venue metadata
  -r, --rating     Sets the rating metadata, out of 5

${bld}ARGUMENTS${off}
  ARTIST     Sets the artists metadata & used in the title of the post. Spaces are allowed.

${bld}EXAMPLES${off}
  ${gry}# Create a new draft gig review called "Review: Nick Cave & Warren Ellis Gig"${off}
  $ $script_name --venue 'Queen Elizabeth Theatre' --rating 5 Nick Cave & Warren Ellis
EOF
  exit
}

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

function parse_params() {
  local param
  while [[ $# -gt 0 ]]; do
    param="$1"

    case $param in
      -h | --help | help)
        usage
        ;;
      -t | --tags)
        tags="$tags,$2"
        shift
        ;;
      -c | --category)
        category="$2"
        shift
        ;;
      -v | --venue)
        venue="$2"
        shift
        ;; 
      -r | --rating)
        rating="$2"
        shift
        ;;               
      *)
        artist="${artist:-} $param"
        artist=$(trim "${artist:-}")
        title="Review: $artist Gig"
        ;;
    esac
    shift
  done
  title=$(trim "${title:-}")
  title_slug=$(echo "$title" | slugify)
  post="$script_dir/content/posts/$category/$title_slug.adoc"
}

init "$@"

if [[ $# == 0 ]]; then
  msg "Missing parameter: ARTIST."
  usage
fi

cat << EOF > "$post"
:title: $title
:slug: $title_slug
:created: $(date --rfc-3339=s)
:date: $(date --rfc-3339=s)
:tags: $tags,$artist,$venue
:status: draft
:category: $category
:artist: $artist
:venue: $venue
:rating: $rating
:setlist: 
:meta_description: 


---
=== Footnotes & References

EOF