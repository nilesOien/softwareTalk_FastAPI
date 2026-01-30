#!/bin/bash

# Run this before giving the talk to
# install all packages that the talk really needs,
# and start the relevant servers.

thisDir=`pwd`

for dir in \
  section_03_ruff \
  section_04_fastapi_dict \
  section_05_fastapi_dict_pydantic \
  section_06_unit_tests_and_git_hooks \
  section_07_databases_SQL \
  section_08_databases_ORM \
  section_09_databases_ORM_input_args \
  section_10_download_client \
  section_13_rust_comparison/Python
do
 cd "$dir"
 if [ ! -f uv.lock ]
 then
  ./installPackages.sh
 fi
 cd "$thisDir"
done


for dir in \
  section_04_fastapi_dict \
  section_05_fastapi_dict_pydantic \
  section_06_unit_tests_and_git_hooks \
  section_07_databases_SQL \
  section_08_databases_ORM \
  section_09_databases_ORM_input_args
do
 cd "$dir"
 ./startServer.sh &> /dev/null &
 cd "$thisDir"
done

cd section_06_unit_tests_and_git_hooks
./generate_test_coverage.sh
./installHook.sh
cp demoFastapi.py demoFastapi.py.good
cp demoFastapi.py.bad demoFastapi.py

