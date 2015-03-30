print "1 - Suma"
print "2 - Resta"
print "3 - Multiplicar"
print "4 - Dividir"


operador = int(raw_input("Que necesita: "))

if operador == 1:
	def suma():
		n1= int(raw_input("ingresa un numero: "))
		n2= int(raw_input("ingresa otro numero: "))
		print "El Resultado es: ",n1+n2
	suma()
elif operador == 2:
	def resta():
		n1= int(raw_input("ingresa un numero: "))
		n2= int(raw_input("ingresa otro numero: "))
		print "El Resultado es: ",n1-n2
	resta()
elif operador == 3:
	def multi():
		n1= int(raw_input("ingresa un numero: "))
		n2= int(raw_input("ingresa otro numero: "))
		print "El Resultado es: ",n1*n2
	multi()
elif operador == 4:
	def division():
		n1= int(raw_input("ingresa un numero: "))
		n2= int(raw_input("ingresa otro numero: "))
		print "El Resultado es: ",n1/n2
		print "El Resto es: ",n1%n2
	division()
else:
	print "Opcion no valida"


