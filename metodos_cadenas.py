#Funcion saber cuantos caracteres tiene un str
s = "Hola Mundo"
print len(s)

#Funcion saber cuantas veces se repite un caracter
s = "Hola Mundo"
print s.count("o")

#Funcion Desde donde buscar los caracteres
s = "Hola Mundo"
print s.count("o",0,4) #Buscar en Hola
print s.count("o",6,10) #Buscar en Mundo

#Funcion Convertir caracteres a minusculas o mayuscula
s = "Hola Mundo"
print s.lower()
print s.upper()

#Funcion cambiar una letra de la cadena
s = "Hola Mundo"
print s.replace('o','x')
print s.replace('Hola',"Hello")

#Funcion Split,Cortar un caracter indicado
s = "Hola Mundo"
print s.split("a")

#Funcion Buscar la ubicacion de una letra o cadena
s = "Hola Mundo"
print s.find('Hola')

#Funcion Join separar caracteres
t = ("H","O","L","A")
s = ";"

print s.join(t)