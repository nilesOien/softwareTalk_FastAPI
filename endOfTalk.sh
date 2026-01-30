#!/bin/bash

# Run this after talk to stop all uvicorn servers.

ps aux | grep uvicorn | grep -v grep | awk '{print $2}' | while IFS= read -r pid
do
 echo $pid
 kill -11 "$pid"
done

ps aux | grep startServer.sh | grep -v grep | awk '{print $2}' | while IFS= read -r pid
do
 echo $pid
 kill -11 "$pid"
done

thisDir=`pwd`
for dir in \
./section_02_uv/pip \
./section_02_uv/uv \
./section_03_ruff \
./section_04_fastapi_dict \
./section_05_fastapi_dict_pydantic \
./section_06_unit_tests_and_git_hooks \
./section_07_databases_SQL \
./section_08_databases_ORM \
./section_09_databases_ORM_input_args \
./section_10_download_client \
./section_13_rust_comparison/Python
do
 cd "$dir"
 ./cleanup.sh
 cd "$thisDir"
done


cd section_06_unit_tests_and_git_hooks
./removeHook.sh
cp demoFastapi.py demoFastapi.py.bad
cp demoFastapi.py.good demoFastapi.py
