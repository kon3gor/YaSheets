#!/bin/sh

curdir=$(pwd)
export CREDS_FILE_NAME="$curdir/res/credentials.json"
python3 app.py
