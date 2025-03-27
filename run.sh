#!/bin/bash
#
# run the mapping for $1 to $2 inputs
# there are 13167 inputs
for i in $(seq "$1" "$2");
do
    echo $i
    python3 Main.py $((i*3))
done
