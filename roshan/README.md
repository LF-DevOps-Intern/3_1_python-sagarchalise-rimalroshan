# PullData Py

**This is a script that fetches given url and optionally starts a webserver to serve the content.**

### Prerequisites

Python version: 3.8.10

### Installation:

This is a simple script and doesn't require any installation. You can start directly using it.

### 1. Clone the repo using

```bash
git clone https://github.com/LF-DevOps-Intern/3_1_python-sagarchalise-rimalroshan.git
```

### 2. Copy the files inside the directory named "roshan" which contains all the required files.

```bash
cp -r 3_1_python-sagarchalise-rimalroshan/roshan/* <your_custom_folder>
```

### 3. Run the "wrapper.sh" providing the arguments needed.

### Usuage:

```bash
usage: wrapper.sh [-h] [--http_server HTTP_SERVER] [--port PORT] url

positional arguments:
  url                   the url of the page to fetch

optional arguments:
  -h, --help            show this help message and exit
  --http_server HTTP_SERVER
                        setup an http server if specified. Specify 0 or 1
  --port PORT           port for the server to run
```
