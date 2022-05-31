#!/usr/bin/env bash

# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -o nounset   # Using an undefined variable is fatal
set -o errexit   # A sub-process/shell returning non-zero is fatal
# set -o pipefail  # If a pipeline step fails, the pipelines RC is the RC of the failed step
# set -o xtrace    # Output a complete trace of all bash actions; uncomment for debugging

# IFS=$'\n\t'  # Only split strings on newlines & tabs, not spaces.

echo -n "plot_words_per_post.py..."
poetry run python plot_words_per_post.py
svgo --input=plot_words_per_post.svg --output=plot_words_per_post.svg

echo
echo -n "plot_posts_per_year.py..."
poetry run python plot_posts_per_year.py
svgo --input=plot_posts_per_year.svg --output=plot_posts_per_year.svg

echo
echo -n "plot_cumulative_posts.py..."
poetry run python plot_cumulative_posts.py
svgo --input=plot_cumulative_posts.svg --output=plot_cumulative_posts.svg

echo
echo -n "plot_cumulative_words.py..."
poetry run python plot_cumulative_words.py
svgo --input=plot_cumulative_words.svg --output=plot_cumulative_words.svg