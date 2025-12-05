#!/bin/bash

# List November 2025's H-Alpha files.
rm -f scanKeepNov.sql
for dir in /isilon_ro/keeps/gong/HA/haf/202511/*
do
 bn=`basename "$dir"`
 if [ "$bn" == "20251120" ]
 then
  cat scanKeepNov.sql | sqlite3 halphaOct2025.db
  exit 0
 fi
 for file in "$dir"/*h.fits.fz
 do
  size=`cat "$file" | wc -c`
  path=`echo "$file" | awk -F/ '{print $(NF-2)"/"$(NF-1)"/"$NF}'`
  site=${path:30:1}
  bn=`basename "$file"`
  dt="${bn:0:14}"
  day="${bn:0:8}"
  hour="${bn:0:10}"
  url="https://gong2.nso.edu/HA/haf/""$path"
  echo INSERT INTO halpha \(url, datatime, day, hour, site, size\) VALUES \(\'$url\', \'$dt\', \'$day\', \'$hour\', \'$site\', $size\)\; >> scanKeepNov.sql
#  exit 0
 done

done

exit 0

