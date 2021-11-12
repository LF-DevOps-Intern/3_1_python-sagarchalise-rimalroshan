from requests import request
import argparse
import logging
import subprocess
import os
from datetime import datetime
import validators

"""
Initialize a logger object and set the default logging level to DEBUG unless otherwise supplied.
All the logs will be kept in a file named "logs" in the directory from where you invoke the script.
Only ERROR and higher severity logs will be printed to the console.
"""

# Todo: Create a format to match the syslog logging format

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

#create a stream handler for logging out to console.
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)

#create a file handler for logging to file
file_handler = logging.FileHandler('logs',mode='a')
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


"""
setup a parser and define the arguments to be used
"""
parser = argparse.ArgumentParser('wrapper.sh')

# declaring the arguments that could be passed
parser.add_argument("url", help="the url of the page to fetch", type=str)
parser.add_argument("--http_server",
                    help="setup an http server if specified. Specify 0 or 1",
                    type=bool)
parser.add_argument("--port", help="port for the server to run",
                    type=int, default=8080)


#Extracting the arguments
arguments_ = parser.parse_args()
url=arguments_.url
enable_http_server=arguments_.http_server
server_port=str(arguments_.port)

if not validators.url(url):
    logger.critical("Invalid URL try again.")
    exit(1)


#Fetch the page using requests

url = "https://google.com"

response_ = request(method='GET', url=url)
webpage_content = response_.text

logger.info("Fetched the Webpage")

#write the content of the webpage into a file using with statement
with open('fetched_data_'+str(datetime.now()), 'w') as file:
	file.write(webpage_content)

logger.info("Written file successfully")

if enable_http_server:
    try:
        server_process = subprocess.Popen(["python3", "-m", "http.server", server_port],
                                        shell=False,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
        logger.info("Started the http server module on port {server_port}")
        print("Started the http server module on port {server_port}")
        
    except:
        raise NotImplementedError


    try:
        out_,err_=server_process.communicate()
    except:
        # Todo:  if time permits catch the sigterm and sigkill and stop the above server and proceed.
        raise NotImplementedError



    logger.info("Stopped the http server module")


