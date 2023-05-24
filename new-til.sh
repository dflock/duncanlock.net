#!/usr/bin/env bash

# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -o nounset   # Using an undefined variable is fatal
set -o errexit   # A sub-process/shell returning non-zero is fatal
# set -o pipefail  # If a pipeline step fails, the pipelines RC is the RC of the failed step
# set -o xtrace    # Output a complete trace of all bash actions; uncomment for debugging

# IFS=$'\n\t'  # Only split strings on newlines & tabs, not spaces.

source ./includes.sh

function init() {
  readonly script_path="${BASH_SOURCE[0]:-$0}"
  readonly script_dir="$(dirname "$(readlink -f "$script_path")")"
  readonly script_name="$(basename "$script_path")"

  tags=""
  category="tech"

  setup_colors
  parse_params "$@"
}

function usage() {
  cat <<EOF

Create a new TIL post for the blog

${bld}USAGE${off}
  $script_name [options] TITLE

${bld}OPTIONS${off}
  -h, --help       show this help
  -t, --tags       tags for this post. Comma separated, no spaces.
  -c, --category   category for the post, no spaces. If none, defaults to 'tech'.

${bld}ARGUMENTS${off}
  TITLE     the title of the TIL post. Spaces are allowed.

${bld}EXAMPLES${off}
  ${gry}# Create a new post in the "tech" category, called "Promise.allSettled in JavaScript"${off}
  $ $script_name --tags javascript,es6 Promise.allSettled in JavaScript
  ${gry}# Create a new post in the "home & garden" category, called "Don't Put Eggs Under Your Tomatoes, if you have Raccoons"${off}
  $ $script_name --tags gardening --category 'home & garden' "Don't Put Eggs Under Your Tomatoes, if you have Raccoons"
EOF
  exit
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
        tags="$2"
        shift
        ;;
      -c | --category)
        category="$2"
        shift
        ;;
      *)
        title="${title:-} $param"
        ;;
    esac
    shift
  done
  title=$(trim "${title:-}")
  title_slug=$(echo "$title" | slugify)
  post="$script_dir/content/posts/$category/til/$title_slug.adoc"
  if [[ $tags ]]; then
    tags=",$tags"
  fi
}

init "$@"

if [[ $# == 0 ]]; then
  msg "Missing parameter: TITLE."
  usage
fi

cat << EOF > "$post"
:title: $title
:slug: $title_slug
:date: $(date --rfc-3339=s)
:tags: til$tags
:category: $category
:meta_description: 


== References

EOF