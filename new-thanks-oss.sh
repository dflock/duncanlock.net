#!/usr/bin/env bash

# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -o nounset   # Using an undefined variable is fatal
set -o errexit   # A sub-process/shell returning non-zero is fatal
# set -o pipefail  # If a pipeline step fails, the pipelines RC is the RC of the failed step
# set -o xtrace    # Output a complete trace of all bash actions; uncomment for debugging

# IFS=$'\n\t'  # Only split strings on newlines & tabs, not spaces.

# shellcheck source-path=SCRIPTDIR
source ./includes.sh

if [ -z "$GITHUB_TOKEN" ]; then
  die '$GITHUB_TOKEN not found or empty.'
fi

function init() {
  readonly script_path="${BASH_SOURCE[0]:-$0}"
  readonly script_dir="$(dirname "$(readlink -f "$script_path")")"
  readonly script_name="$(basename "$script_path")"

  tags="gratitude,opensource"
  category="tech"
  homepage=''
  username=''
  repos=''

  setup_colors
  parse_params "$@"
}

function usage() {
  cat <<EOF

Create a new draft open source gratitude post for the blog

${bld}USAGE${off}
  $script_name [options]

${bld}OPTIONS${off}
  -h, --help       show this help
  -t, --tags       Extra tags for the post. Prepended with 'gratitude,opensource'. Comma separated, no spaces.
  -c, --category   Category for the post, no spaces. If none, defaults to tech.
  -p, --homepage   Homepage, if not set on GitHub profile
  -u, --username   GitHub username
  -r, --repos      List of github repo names. Comma separated, no spaces.

${bld}EXAMPLES${off}
  ${gry}# Create a new draft open source gratitude post called "Thanks Zachary Yedidia!"${off}
  $ $script_name --homepage 'https://zyedidia.github.io/' --username zyedidia --repos eget,micro
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
        tags="$tags,$2"
        shift
        ;;
      -c | --category)
        category="$2"
        shift
        ;;
      -p | --homepage)
        homepage="$2"
        shift
        ;; 
      -u | --username)
        username="$2"
        shift
        ;;   
      -r | --repos)
        repos="$repos,$2"
        shift
        ;;
    esac
    shift
  done

}

init "$@"

# Get user info from GitHub API
user_info=$(curl -s --header "Authorization: Bearer $GITHUB_TOKEN" "https://api.github.com/users/$username")
# Get the user's avatar URL
avatar_url=$(echo "$user_info" | jq -r .avatar_url)
# Get the userse full name
full_name=$(echo "$user_info" | jq -r .name)
# Get the userse blog url
blog=$(echo "$user_info" | jq -r .blog)

if [ -z "$homepage" ] && [ -n "$blog" ]; then
  homepage="$blog"
fi

# Get the users company, if any
company=$(echo "$user_info" | jq -r .company)
if [ "$company" == "null" ]; then
  company=''
else
  company="* $company"
fi

bio=$(echo "$user_info" | jq -r .bio)
if [ "$bio" == "null" ]; then
  bio=''
else
  printf -v bio "____\n%s\n____" "$bio"
fi

title="Thanks, $full_name ($username)!"
title=$(trim "${title:-}")
title_slug=$(echo "$title" | slugify)
post_dir="$script_dir/content/posts/$category/thanks"
post="$post_dir/$title_slug.adoc"
include_dir="$script_dir/content/includes/posts/$title_slug"

echo "Generating $title..."

# Create intro doc for you to fill in, if it doesn't exist
mkdir -p "$include_dir"

superlatives=("invaluable" "awesome" "fantastic" "great" "brilliant" "wonderful" "magnificent" "heroic")
random=$(date +%s)
superlative=${superlatives[ $random % ${#superlatives[@]} ]}

if [ ! -s "$include_dir/intro.adoc" ]; then
  touch "$include_dir/intro.adoc"
  cat << EOF > "$include_dir/intro.adoc"
Open source developers are often the unsung heroes of the technology world, creating & maintaining the software that powers our digital lives. Sadly, their contributions often go unnoticed, but without their dedication and expertise, much of the software & digital infrastructure what we take for granted today wouldn't exist.

I want to recognize the $superlative work of one developer and express my gratitude to them for making the world a better place through open source:
EOF
fi

# Figure out sponsorship
sponsor_url=https://github.com/sponsors/"$username"
rc=$(curl -s -o /dev/null -w "%{http_code}" "$sponsor_url")
if [ "$rc" == "200" ]; then
  heart='{static}/images/icons/custom/github_sponsor_heart.svg[role=icon]'
  sponsor="* image:$heart https://github.com/sponsors/$username[Sponsor $full_name ($username)]"

  touch "$include_dir/sponsor.adoc"
  cat << EOF > "$include_dir/sponsor.adoc"
'''
=== Sponsor $full_name ($username)

image::$heart[100,100]

[.lead]
If you use any of their software, or just want to support the $superlative work of $full_name ($username) -- you should $sponsor_url[sponsor them on GitHub.]
EOF
  sponsor_include="include::../../../includes/posts/{slug}/sponsor.adoc[]"

else
  sponsor=''
  sponsor_include=''
fi

# Generate user profile info as Asciidoc
content=$(cat <<EOF
include::../../../includes/posts/{slug}/intro.adoc[]

== $full_name / $username

=== https://github.com/$username[GitHub Profile]
$bio

.https://github.com/$username[GitHub Profile]
image::$avatar_url[Avatar,100,link='https://github.com/$username']

* Location: $(echo "$user_info" | jq -r .location)
* Followers: $(echo "$user_info" | jq -r .followers)
* https://github.com/$username?tab=repositories&type=source[Public Repositories]: $(echo "$user_info" | jq -r .public_repos)
$company
* $blog
$sponsor

//-
[.lead.clear]
These are the projects of theirs that I love & use the most:

EOF
)

# Loop through the remaining parameters to retrieve the repository information
for repo in ${repos//,/ }; do
  # Make a request to the GitHub API to retrieve the repository information
  if [[ "$repo" =~ '/' || "$repo" =~ '\' ]]
  then
    response=$(curl -s --header "Authorization: Bearer $GITHUB_TOKEN" "https://api.github.com/repos/$repo")
  else
    response=$(curl -s --header "Authorization: Bearer $GITHUB_TOKEN" "https://api.github.com/repos/$username/$repo")
  fi

  # Parse the response to extract the name and description
  name=$(echo "$response" | jq -r '.name')
  description=$(echo "$response" | jq -r '.description')
  url=$(echo "$response" | jq -r '.html_url')

  # Print the name and description to the console
  printf -v content "%s\n\n=== %s[%s]\n\n" "$content" "$url" "$name"
  printf -v content "%s____\n%s\n____\n\n" "$content" "$description"

  # Create an include file for reach repo, for you to fill in, if it doesn't already exist
  touch "$include_dir/$name.adoc"
  printf -v content "%s%s" "$content" "include::../../../includes/posts/{slug}/$name.adoc[]"
done

# Create an include file for an outro, for you to fill in, if it doesn't already exist
touch "$include_dir/outro.adoc"

# Create the main post page
datetime=$(date --rfc-3339=s)

cat << EOF > "$post"
:title: $title
:slug: $title_slug
:created: $datetime
:date: $datetime
:modified: $datetime
:tags: $tags,$full_name
:status: draft
:category: $category
:github: $username
:homepage: $homepage
:figure-caption!:
:meta_description: Thank you to $full_name for your hard work making the world a better place through open source.

$content

$sponsor_include

include::../../../includes/posts/{slug}/outro.adoc[]

EOF