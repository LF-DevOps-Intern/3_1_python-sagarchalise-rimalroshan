#!/bin/bash
VERSION="python3.8.10"
VENV_DIRECTORY=".venv"

#help content to be displayed
display_help(){
cat << EOF
usage: wrapper.sh [-h] [--http_server HTTP_SERVER] [--port PORT] url

positional arguments:
  url                   the url of the page to fetch

optional arguments:
  -h, --help            show this help message and exit
  --http_server HTTP_SERVER
                        setup an http server if specified. Specify 0 or 1
  --port PORT           port for the server to run
EOF
}


#show help if user passes the help command
if [ "$1" = "-h" -o "$1" = "--help" -o $# -eq 0 ] ; then
   display_help;
   exit 0
fi

#create a virtual env named .venv and activate it if it doesn't exist in the current working directory.
if [ ! -d "$VENV_DIRECTORY" ]; then
   virtualenv -p $VERSION .venv
   source .venv/bin/activate
fi

pip install -r requirements.txt > /dev/null

#pass the arguments to the python script pulldata

python3 pulldata.py "$@"  


