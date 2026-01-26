#!/bin/bash

# Make a coverage report. Needs the packages pytest and pytest-cov.

# The --cov=. specifies a package which in this case is this
# directory. This directory can be treated as a pckage
# because it has a __init__.py file (even though that file
# does nothing).

rm -rf coverageReport
uv run pytest --verbose --cov=. --cov-report=html:coverageReport

if [ -f coverageReport/index.html ]
then
 echo Success : Coverage web page top level is coverageReport/index.html
else
 echo There was a problem
fi

exit 0

