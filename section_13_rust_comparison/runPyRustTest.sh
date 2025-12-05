#!/bin/bash

echo Python service :
count=1
while [ "$count" -le 3 ]
do
 rm -f py.json
 echo Python pass $count
 /usr/bin/time -f "%e" wget -q "http://127.0.0.1:8001/getWholeDatabase" -O py.json
 count=`expr "$count" + 1`
done

echo Rust service :
count=1
while [ "$count" -le 3 ]
do
 rm -f rust.json
 echo Rust pass $count
 /usr/bin/time -f "%e" wget -q "http://127.0.0.1:8002/getWholeDatabase" -O rust.json
 count=`expr "$count" + 1`
done

