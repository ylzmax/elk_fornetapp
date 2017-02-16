#!/bin/bash
cat /tools_bj/quota_status/current/* | awk '{print "QUOTA"" " $2" "$3" "$5" "$6}' >/tmp/quotaelk
nc 192.168.18.5 5000 < /tmp/quotaelk &
