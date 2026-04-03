#!/bin/bash

# Usage: ./update-ranks.sh ordered_list.txt

list_file="$1"

if [[ -z "$list_file" || ! -f "$list_file" ]]; then
  echo "Usage: $0 ordered_list.txt"
  exit 1
fi

rank=10

while IFS= read -r filename; do
  [[ -z "$filename" ]] && continue

  if [[ -f "$filename" ]]; then
    sed -i '' -E "s/^rank: [0-9]+$/rank: $rank/" "$filename"
    echo "Updated: $filename -> rank: $rank"
  else
    echo "Not found: $filename"
  fi

  rank=$((rank + 10))
done < "$list_file"
