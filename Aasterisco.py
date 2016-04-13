from constants import *
from functions import *
from grafo import *

def AlgoritmoA(matriz,punto_inicial,punto_final,lista_respuesta):	
	grafo = crear_grafo()
	is_final = True
	distancia_recorrida = 0
	lista = []
	pila = []
	lista_respuesta.append(punto_inicial)

	punto_actual = punto_inicial
	index = index_grafo(grafo, punto_actual)
	nodo = grafo[index]
	lista = encontrar_hijos(matriz,nodo.pos, lista_respuesta)
	nodo.insertar_hijos(lista)
	pila.append(nodo)
	while(is_final):
		if not (nodo.todos_evaluados()):
			punto_actual = menor_evaluacion(nodo.pos,punto_final,nodo.lista_hijos,nodo)
			nodo.actualizar_hijo(punto_actual)
			grafo[index] = nodo
			if(nodo.pos == punto_final):
				lista_respuesta.append(nodo.pos)
				return lista_respuesta
			if not (punto_actual in lista_respuesta):
				if not (nodo.pos in lista_respuesta):
					lista_respuesta.append(nodo.pos)
					pila.append(nodo)
				index = index_grafo(grafo, punto_actual)
				nodo = grafo[index]
				if(len(nodo.lista_hijos_visitados)==0):
					lista = encontrar_hijos(matriz,punto_actual, lista_respuesta)
					nodo.insertar_hijos(lista)
				if (punto_final in lista_respuesta):
					is_final = False
		else:
			p = pila.pop()
			lista_respuesta.pop()
			index = index_grafo(grafo,(pila[len(pila)-1]).pos)
			nodo = grafo[index]
	return lista_respuesta