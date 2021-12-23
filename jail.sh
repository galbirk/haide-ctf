#!/bin/bash
function check_space {
    if [[ $1 == *[bdks';''&'' ']* ]]
    then
            return 0
    fi

    return 1
}
input=$1
if check_space "$input"
then
    echo -e '\033[0;31mRestricted characters has been used\033[0m'
else
    output="echo Your command is: $input"
    eval $output
fi
