def decorador(funcion):
	def funcionDecorada(*args,**kwargs):
		print "Funcion:",funcion.__name__	
		funcion(*args,**kwargs)

	return funcionDecorada	

def resta(n,m):
	print n-m
def suma(n,m):
	print n+m
def multi(n,m):
	print n+m
def division(n,m):
	print n+m


#Decorado
decorador(suma)(5,3)
decorador(resta)(5,3)
decorador(multi)(5,3)
decorador(division)(5,3)