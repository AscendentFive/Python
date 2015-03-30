class Humano:
	def __init__(self,edad):
		self.edad = edad

	def hablar(self,mensaje):
		print self.edad
		print mensaje

class IngSistemas(Humano):
	def programar(self,lenguaje):
		print 'Voy a programar en', lenguaje

class LicDerecho(Humano):
	def estudiarCaso(self,de):
		print 'Debo estudiar el caso de', de

pedro = IngSistemas(26)
raul = LicDerecho(27)

pedro.programar('Python')
raul.estudiarCaso('Pedro')

pedro.hablar("Hola! raul")
raul.hablar("Hola Pedro")