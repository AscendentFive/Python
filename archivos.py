try:
	f = open("reporte de errores.txt","w")
except:
	exit()
	print "Error"
f.write("Escrito desde python")
f.close()
