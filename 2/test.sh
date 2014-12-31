#!/bin/bash 

test="python fixedxor.py 1c0111001f010100061a024b53535009181c"
result="746865206b696420646f6e277420706c6179"

if [[ $(eval $test) == $result ]]; then
    echo -e "\nPass"
    exit 0
else
    echo -e "\nFail"
    eval $test
    exit 1
fi
