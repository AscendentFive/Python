#Funcion Buscar variable de buscar en la lista
lista = [1,"Dos",3]
buscar = 1
print buscar in lista

#Funcion el Indice de una variable buscada
lista = [1,"Dos",3]
buscar = 1
print lista.index(buscar)

#Funcion el Indice de una variable buscada con if
lista = [1,"Dos",3]
buscar = 0

if buscar in lista:
	print lista.index(buscar)
else:
	print "No esta el Elemento"

#Funcion Open, Agregar un elemento a la lista
lista = [1,"Dos",3]
print lista
lista.append("Nuevo Elemento")
print lista

#Funcion Buscar elementos repetidos en la lista
lista = [1,"Dos",3,3,3]
print lista.count(3)

#Funcion Remover un elemento de la lista
lista = [1,"Dos",3]
lista.remove(3)
print lista

#Funcion Invertir lista
lista = [1,"Dos",3]
lista.reverse()
print lista


