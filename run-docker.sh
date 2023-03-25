#!/bin/bash
/usr/bin/docker run -e APSYSTEMS_USER="$1" -e APSYSTEMS_PWD="$2" --rm --ipc=host apsystems-alerting pytest /app/aps_website_test.py
