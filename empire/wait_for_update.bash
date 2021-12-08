#!/bin/bash

if [ "$EMPIREHOST" == "" ]; then
    echo "Must set the environment variable EMPIREHOST."
    exit 1
fi
if [ "$EMPIREPORT" == "" ]; then
    echo "Must set the environment variable EMPIREPORT."
    exit 1
fi
if [ "$COUNTRY" == "" ]; then
    echo "Must set the environment variable COUNTRY."
    exit 1
fi
if [ "$PLAYER" == "" ]; then
    echo "Must set the environment variable PLAYER."
    exit 1
fi

function provide_input() {
    echo user update@checker.com
    echo coun $COUNTRY
    echo pass $PLAYER
    echo play
    echo update
    echo quit
    sleep 1
}

function get_next_update_time() {
    provide_input | telnet $EMPIREHOST $EMPIREPORT 2>&1 | egrep '^1 The next update is at' | sed 's/1 The next update is at //'
}

next_update_time=$(get_next_update_time)
update_time=$(get_next_update_time)
echo -n "waiting"
while [ "$update_time" == "$next_update_time" ]; do
    echo -n "."
    sleep 5
    update_time=$(get_next_update_time)
done
echo ""
echo "was $next_update_time is $update_time"

