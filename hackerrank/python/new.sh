#!/usr/bin/env bash

# Usage: ./new.sh <category> <hackerrank url>
# e.g.:
# $ ./new.sh lists https://www.hackerrank.com/challenges/list-comprehensions/problem

category=$1
hackerrank_url=$2

# Requires pup and jq on the PATH:
# https://github.com/ericchiang/pup/releases/tag/v0.4.0 
# sudo apt install jq

# Prepare handle to temp file and ensure it gets cleaned up if script crashes
tmpfile=$(mktemp /tmp/hackerrank.html.XXXXXX)
exec 3>"$tmpfile"
exec 4<"$tmpfile"
rm "$tmpfile"

curl -s -S $hackerrank_url >&3
# Converting to json and using jq because pup could not print the data-attr1 attribute for some reason
link_json=$(cat <&4 | pup 'a#pdf-link json{}')
pdf_link=$(echo $link_json | jq -r '.[0]."href"')
problem_name=$(echo $link_json | jq -r '.[0]."data-attr1"')

mkdir -p $category > /dev/null
pushd $category > /dev/null

max_dir_num=$(ls -1 | cut -c1-3 | awk -v idx=1 'NR==1 || $idx>max{max=$idx} END{print max}')
new_max_num="$(($max_dir_num + 1))"
seq_num=$(printf "%03d" $new_max_num)
new_dir_name="$seq_num-$problem_name"
mkdir $new_dir_name
pushd $new_dir_name > /dev/null
curl -s -S -O -J -L "https://www.hackerrank.com$pdf_link" # TODO: use url parsing lib here instead of hard-coding
touch "$problem_name.py"
popd > /dev/null

popd > /dev/null

find "$category/$new_dir_name"