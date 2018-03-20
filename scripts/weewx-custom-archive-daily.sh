#!/bin/sh
#/usr/bin/sqlite3 /var/lib/wview/archive/wview-archive.sdb < /opt/scripts/wview-daily-archive.sql > /var/www/weather/Archive/CUSTOM-ARC-`date +%Y-%m-%d -d "yesterday"`.csv

#so this defaults to "yesterday" but can take any GNU date command string, e.g 2012-07-08, "last Sunday", etc.
DATE=${1:-yesterday}
cat /opt/scripts/weewx-daily-archive.sql | sed -e "s/%%DATE%%/`date +%Y-%m-%d --date=\"$DATE\"`/g" | sqlite3 /var/lib/weewx/weewx.sdb
