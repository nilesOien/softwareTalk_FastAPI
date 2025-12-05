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
uv init --name section_06_unit_tests_and_git_hooks --description "An example of Fast API unit tests" --bare .

# Install packages.
uv add -r requirements.in

