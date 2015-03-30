#Filtrar solo numeros mayores a 0
def filtro(elem):
	return (elem > 0)

l = [1,-3,2,-8,-9,10]
lr = filter(filtro,l)

print l
print lr

#Filtrar solamente las O
def filtro(elem):
	return (elem == "o")

s = "Hola Mundo"
lr = filter(filtro,s)

print s
print lr