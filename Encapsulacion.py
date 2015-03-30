class Prueba(object):
	def __init__(self):
		self.__privado = "Soy Privado"
		self.privado = "Soy Publico"

	def __metodoPrivado(self):
		return "Soy Privado"

	def metodoPublico(self):
		print "Soy Publico"

	def getPrivado(self):
		return self.__privado

	def setPrivado(self,valor):
		self.__privado = self.__metodoPrivado()


obj = Prueba()

#print obj.privado
obj.setPrivado("Tengo nuevo Valor")
print obj.getPrivado()
