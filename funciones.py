#Funcion declarando valores cuando se llama
def mi_funcion(num1,num2):
	print num1 + num2

mi_funcion(3,4)

#Funcion declarando valor
def mi_funcion(num1=3,num2=4):
	print num1 + num2
	
mi_funcion()

#Funcion con cadena
def mi_funcion(cad,v=2):
	print cad * v
	
mi_funcion('Hola ')

#Funcion con tuplas
def mi_funcion(cad,v=2,*algomas):
	print cad * v
	for cadena in algomas:
		print cadena * v
	
mi_funcion('Hola ',5,'Hola ','Adios ','N ','cadenas ')

#Funcion con Diccionario
def mi_funcion(cad,v=2,**algomas):
	print cad * v
	
	print algomas['cadenaextra']
	print algomas['cadenademas']
	
mi_funcion('Hola ',5,cadenaextra = 'Hola', cadenademas = 'adios')


