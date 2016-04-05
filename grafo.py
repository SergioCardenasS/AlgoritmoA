
class punto:
	pos = ()
	funcion_evaluacion = 0
	lista_hijos = []
	lista_hijos_visitados = []
	
	def __init__(self,tupla):
		self.pos = tupla
		self.lista_hijos = []
		self.lista_hijos_visitados = []

	def imprimir(self):
		print self.pos

	def insertar_hijos(self, lista):
		self.lista_hijos = lista
		for index in range(len(lista)):
			self.lista_hijos_visitados.append(0)

	def hijo_buscado(self,tupla):
		pos = self.lista_hijos.index(tupla)
		return self.lista_hijos_visitados[pos]

	def actualizar_hijo(self, tupla):
		pos = self.lista_hijos.index(tupla)
		self.lista_hijos_visitados[pos] = 1

	def todos_evaluados(self):
		for index in range(len(self.lista_hijos_visitados)):
			if(self.lista_hijos_visitados[index]==0):
				return False
		return True
	def imprimir_lista_hijos(self):
		for index in range(len(self.lista_hijos)):
			print self.lista_hijos[index],
