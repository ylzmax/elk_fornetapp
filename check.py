#!/usr/bin/python
import os
import pwd
import sys
import time


def run(path,vol,proj):
	if path:
		walker=os.walk(path)
		try:
			while 1:
				res=walker.next()
				if len(res)>2:
					if ".snapshot"	in res[0]:
						pass
					else:
						for i in res[2]:
							resmid=os.path.join(res[0],i) 
							#print resmid
							if os.path.isfile(resmid):
								fileinfo=os.stat(resmid)
								USERNAME=pwd.getpwuid(fileinfo[4]).pw_name
								USERGROUP=fileinfo[5]
								SIZE=fileinfo[6]
								MTIMEmd=fileinfo[8]
								year,month,day=time.gmtime(MTIMEmd)[0:3]
								MTIME="%d-%d-%d"%(year,month,day)
								filetypemid=i.split(".")	
								if len(filetypemid) > 1 :
									TYPE=filetypemid[-1]
								else:
									TYPE="file"
								#print resmid
								#print "username:%s group:%d size:%d mtime:%s type:%s"%(USERNAME,USERGROUP,SIZE,MTIME,TYPE)
								print "PROJFILE %s %s %s %s %d %d %s %s"%(vol,proj,resmid,USERNAME,USERGROUP,SIZE,MTIME,TYPE)
		except:
			print "END!"
								

if len(sys.argv) > 1 :
	if os.path.islink(sys.argv[1]):
		#print "%s is link"%sys.argv[1]
		pass
	else:
		path=sys.argv[1].split("/")
		#print path
		if len(path)>3:
			VOL=path[2]
			PROJ=path[3]
			run(sys.argv[1],VOL,PROJ)

