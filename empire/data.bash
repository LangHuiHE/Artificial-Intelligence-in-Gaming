#!/bin/bash

/usr/citlocal/cs4300/bin/empire << EOF
reso *
cens *
com *
level *
xdump sect * | ./reader.py
xdump ship * | ./reader.py
EOF
