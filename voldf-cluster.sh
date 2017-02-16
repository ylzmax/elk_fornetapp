#!/bin/bash

for i in proj21 proj22 proj23 ;
do 
	line=`df /proj/$i|grep -v "File"` 
	con=`echo $line |awk -F :  '{print $1}'`
	vol=`echo $line |awk  '{print $1}'| awk  -F : '{print $2}'`
	used=`echo $line |awk  '{print $3}'`
	avail=`echo $line |awk  '{print $4}'`
	echo "VOLDF" $vol $used $avail $con
done
