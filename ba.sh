#!/bin/bash


echo ${@:0}
echo "$@"
echo $#
python -m pyargs.py "$@"
python -m pyargs.py $@


