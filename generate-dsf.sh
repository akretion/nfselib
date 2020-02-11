#!/usr/bin/env bash

SCHEMA_NAME='nfse'
SERVICE='dsf'
PATH="$SCHEMA_NAME"lib/"$SERVICE"
echo $PATH
ls $PATH
#mkdir $PATH -p
#pwd   $PATH
#python3 "$GENERATEDS_HOME"/generateDS.py -o