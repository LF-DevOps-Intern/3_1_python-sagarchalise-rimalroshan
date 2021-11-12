#!/bin/bash
VERSION="python3.8.10"
VENV_DIRECTORY=".venv"

#create a virtual env named .venv and activate it if it doesn't exist in the current working directory.
if [ ! -d "$VENV_DIRECTORY" ]; then
   virtualenv -p $VERSION .venv
   source .venv/bin/activate
fi

pip install -r requirements.txt > /dev/null

#pass the arguments to the python script pulldata

python3 pulldata.py "$@"  


