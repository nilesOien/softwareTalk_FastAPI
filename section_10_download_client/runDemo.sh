#!/bin/bash

# Run the demo and download some H-Alpha data.
# The demo server in section 9 must be running
# for this to work.
#
# Note that you can :
# uv run downloadClient.py --help
# to get command line help, since standard argument parsing is used.
#

rm -rf data
startSec=`date --utc +%s`
uv run ./downloadClient.py --minTime 20251027000000 --maxTime 20251027235959 \
	                    --outDir ./data --siteCSV L,C

endSec=`date --utc +%s`
elapsedSec=`expr "$endSec" - "$startSec"`

echo Download size in $elapsedSec seconds :
du -sh data/

exit 0

