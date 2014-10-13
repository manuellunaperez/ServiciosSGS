#coding: utf-8
import sys
import commands

if sys.argv[1] == "-l":
	concesiones = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep lease.*.{ |sort |uniq")
	concesiones = concesiones.replace("lease", "IP Concedida:");
	concesiones = concesiones.replace("{", "");
	RESERVAS = commands.getoutput("cat /etc/dhcp/dhcpd.conf |grep host -A2|grep 'fixed-address' |sort |uniq")
	RESERVAS= RESERVAS.replace("fixed-address", "IP Reservada:");
	RESERVAS= RESERVAS.replace(";", "");
	print "Listado de concesiones del servidor dhcp"
	print concesiones
	print "Listado de IP's reservadas"
	print RESERVAS

else: 
	concesiones = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep -A6 '%s' |grep 'hardware ethernet' | sort |uniq" % sys.argv[1])
	concesiones = concesiones.replace("hardware ethernet", "Dirección MAC:");
	concesiones = concesiones.replace(";", "");
	if len(concesiones) > 0:
		print "La ip %s ha sido concedida: " % sys.argv[1]
		print concesiones
	else:
		print "No hay ninguna concesión con la ip %s " % sys.argv[1] 
