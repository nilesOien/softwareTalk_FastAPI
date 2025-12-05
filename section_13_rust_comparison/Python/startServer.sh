#!/bin/bash

# This starts the uvicorn server, which in turn
# runs the code in getWholeDatabase.py. The syntax is :
# uvicorn path:appName
#
# So that
# uvicorn getWholeDatabase:dumpWholeDBapp
# means look in getWholeDatabase.py and start the application dumpWholeDBapp in there
#
# Run the server under UV management.
uv run uvicorn getWholeDatabase:dumpWholeDBapp --host 127.0.0.1 --port 8001 --workers 1

exit 0

