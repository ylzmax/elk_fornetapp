#!/usr/bin/python
import sys

def fix(filepath):
	file=open(filepath,"r")
	for i in file:
		line=i.strip().split(" ")
		if len(line)==9:
			date=line[7].split("-")
			if len(date)==3:
				month=date[1]
				day=date[2]
				if len(date[1]) <2:
					month="0"+date[1]
				if len(date[2]) <2:
					day="0"+date[2]
				newdate=date[0]+"-"+month+"-"+day
				line[7]=newdate
				print " ".join(line)

if sys.argv[1]:
	fix(sys.argv[1])
