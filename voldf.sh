#!/bin/bash
if [ -e /tmp/VOLDF.tmp ];
then
	rm -f /tmp/VOLDF.tmp && echo "Delete tmp file" || echo "Delete tmp file failed,Please check" 
fi 

for i in  `cat /tools_bj/bjrc/elk/netapp.conf`
	do
	ssh $i df  | grep -v "snap" | awk -v ctr="$i" '{print "VOLDF"" " $1" "$3" "$4 " " ctr}' >> /tmp/VOLDF.tmp
	done
/tools_bj/bjrc/elk/voldf-cluster.sh >>/tmp/VOLDF.tmp
nc 192.168.18.5 5000 < /tmp/VOLDF.tmp &
