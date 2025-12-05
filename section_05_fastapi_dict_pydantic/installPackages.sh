#!/bin/bash

# For this to work, uv has to be installed, either through
# your linux package manager or from uv directly like so :
#
# curl -LsSf https://astral.sh/uv/install.sh | sh
# source $HOME/.local/bin/env

# Check if uv is installed, exit if not.
which uv &> /dev/null
status="$?"
if [ "$status" -ne 0 ]
then
 echo uv is not installed, exiting
 exit -1
fi

# Initialize a bare bones uv project.
uv init --name fastapi_static_dict_pydantic --description "An example of Fast API" --bare .

# Install ruff and sunpy with all dependencies.
uv add -r requirements.in

