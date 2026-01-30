#!/bin/bash

if [ ! -d "$HOME/softwareTalk_FastAPI" ]
then
 echo Looks like repo was not cloned into $HOME, exiting
 exit
fi

# Make a virtual environment
python -m venv $HOME/softwareTalk_FastAPI/section_02_uv/pip/pyEnv

# Enter the virtual environment
source $HOME/softwareTalk_FastAPI/section_02_uv/pip/pyEnv/bin/activate

# Check that we did enter the environment, exit if not
n=`which python | grep pip/pyEnv/bin/python | wc -l`
if [ "$n" -ne 1 ]
then
 echo Did not enter virtual environment, exiting
 exit -1
fi

# Jump to the latest version of pip (to avoid warnings)
pip install --upgrade pip

# Install sunpy with dependencies
pip install "sunpy[all]"

