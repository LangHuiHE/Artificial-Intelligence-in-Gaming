#!/bin/bash
export EMPIREHOST=empire.cs.dixie.edu
export EMPIREPORT=2838
export COUNTRY=28
export PLAYER=28

rm empire.p command.txt

python3 explore.py

done=0
while [ $done != 1 ];do
    ./data.bash
    ./search-and-run.bash
    done=$?
    ./wait_for_update.bash
done
