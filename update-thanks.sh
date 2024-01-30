#!/usr/bin/env bash

# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -o nounset   # Using an undefined variable is fatal
set -o errexit   # A sub-process/shell returning non-zero is fatal
# set -o pipefail  # If a pipeline step fails, the pipelines RC is the RC of the failed step
# set -o xtrace    # Output a complete trace of all bash actions; uncomment for debugging

# IFS=$'\n\t'  # Only split strings on newlines & tabs, not spaces.

./new-thanks-oss.sh --username burntsushi --repos ripgrep,xsv
./new-thanks-oss.sh --username sharkdp --repos bat,fd,hyperfine,numbat
./new-thanks-oss.sh --username zyedidia --repos eget,micro
./new-thanks-oss.sh --username antfu --repos 'unocss/unocss',unplugin-auto-import,'vueuse/vueuse',vitesse,taze
./new-thanks-oss.sh --username codecalm --repos 'tabler/tabler-icons'
