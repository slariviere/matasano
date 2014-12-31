#!/bin/bash

nbChallengeStated=$(find . -name test.sh | grep -v "\./test.sh" | wc -l | sed 's/ //g');


for test in $(find . -name test.sh | grep -v "\./test.sh");
do
    dir=$(echo $test | cut -d'/' -f 2)
    if [ $(cd $dir && ./test.sh) ]; then
        echo "Challenge $dir completed"
        challengeCompleted=$((challengeCompleted+1))
    else
        echo "Challenge $dir failing"
    fi 
done

echo -e "\n${challengeCompleted} out of ${nbChallengeStated} challenge started are correct"
echo "${challengeCompleted} out of the 56 total challenges are completed"
