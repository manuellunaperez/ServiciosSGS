# -*- coding: utf-8 -*-
import sys
import os
opcion = sys.argv[1]

if opcion == '-a':
	rdirecta = open('/var/cache/bind/db.iesgn.org', 'a')
	rinversa = open('/var/cache/bind/db.192.168.100','a')
	registro = sys.argv[2]
	if registro == '-dir':
		nombre = sys.argv[3]
		ip = sys.argv[4]
		rdirecta.write(nombre+'		IN	A	'+ip+'\n')
		rinversa.write(ip+'	IN	PTR	'+nombre+'.iesgn.org.\n')
	elif registro == '-alias':
		nombre = sys.argv[3]
		alias = sys.argv[4]
		rdirecta.write(nombre+'		IN	CNAME	'+alias+'.iesgn.org.\n')
	rinversa.close()
	rdirecta.close()
	
if opcion == '-b':
	registro = sys.argv[2]
	os.system("sed -i '/^"+registro+".*$/d' /var/cache/bind/db.iesgn.org") 
	os.system("sed -i '/"+registro+".*$/d' /var/cache/bind/db.192.168.100")

os.system('service bind9 restart')
