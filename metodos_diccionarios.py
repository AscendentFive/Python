#Diccionario
diccionario = {
	"redes_sociales": ['Twitter','Facebook','Linkedin'],
	3: 'Tres',
	'Hola': "Mundo"
}

#Comprobar una palabra dentro de un diccionario
print ("Hola") in diccionario

#Devolver lista de tuplas
print diccionario.items()

#Devolver claves del diccionario
print diccionario.keys()

#Devolver solamente valores del diccionario
print diccionario.values()

#Devolver el valor del elemento borrado y lo borra
print diccionario #Mostrar que el valor existe
print diccionario.pop(3) #borrar el valor
print diccionario #Comprobar que el valor fue borrado

#Metodo Copy
diccionario_2 = diccionario.copy()
print diccionario
print diccionario_2