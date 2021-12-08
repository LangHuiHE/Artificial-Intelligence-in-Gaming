#!/bin/bash

rm command.txt

python3 Search.py

/usr/citlocal/cs4300/bin/empire < command.txt

if [ -s command.txt ]; then
    exit 0
else
    exit 1
fi