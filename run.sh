#!/bin/bash
ROOT=`pwd`

for i in `cat proj.conf`;
do
	ls /proj/$i | grep -v .snapshot | xargs -i -n 1 -P 3 $ROOT/check.py /proj/$i/{}  > $i.log 
	#ls $i | grep -v .snapshot | xargs -n 1 -i -P 3 ls  $i/{}

done
