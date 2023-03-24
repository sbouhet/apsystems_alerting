#!/bin/bash
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
vars=$SCRIPTPATH"/export-vars.sh"
source $vars
cmd="/usr/bin/python "$SCRIPTPATH"/aps_monitoring.py --action check "$1
$cmd
