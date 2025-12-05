#!/bin/bash

rm -f *.db
cat small_table.sql | sqlite3 little.db
cat halpha_table.sql | sqlite3 halphaOct2025.db
cat scanKeep.sql | sqlite3 halphaOct2025.db

exit 0

