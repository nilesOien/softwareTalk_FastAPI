#!/bin/bash

# This starts the uvicorn server, which in turn
# runs the code in demoFastapi.py. The syntax is :
# uvicorn path:appName
#
# So that
# uvicorn demoFastapi:demoApp
# means look in demoFastapi.py and start the application demoApp in there
#
# Run the server under UV management.
uv run uvicorn demoFastapi:demoApp --host 127.0.0.1 --port 8000 --workers 1

exit 0

