print "1 - Suma"
print "2 - Resta"
print "3 - Multiplicacion"
print "4 - Division\n"

operador = int(raw_input("Ingrese que necesita: "))
print "\n"

if operador == 1:
	print "Usted quiere sumar \n"
	n1 = raw_input("Ingrese un Numero: ")
	n2 = raw_input("Ingrese otro Numero: ")
	print "El Resultado es", int(n1) + int(n2)

elif operador == 2:
	print "Usted quiere Restar \n"
	n1 = raw_input("Ingrese un Numero ")
	n2 = raw_input("Ingrese otro Numero ")
	print "El Resultado es", int(n1) - int(n2)	

elif operador == 3:
	print "Usted quiere Multiplicar \n"
	n1 = raw_input("Ingrese un Numero ")
	n2 = raw_input("Ingrese otro Numero ")
	print "El Resultado es", int(n1) * int(n2)	

elif operador == 4:
	print "Usted quiere Division \n"
	n1 = raw_input("Ingrese un Numero ")
	n2 = raw_input("Ingrese otro Numero ")
	print "El Resultado es", int(n1) / int(n2)	
	
else:
	print "Opcion no Valida\n"



