from constants import *
from functions import *
from grafo import *


def encontrar_hijos(matriz, punto_actual, lista_respuesta):
	lista = []
	dis = 3
	fil = -1
	while(fil < 2):
		col = -1
		while(col<2):
			x = punto_actual[0]+fil
			y = punto_actual[1]+col
			tupla = (x,y)
			if (x>-1 and x<tam and y>-1 and y<tam and matriz[x][y]!=1 and tupla!=punto_actual):
				lista.append(tupla)	
			col +=1
		fil+=1
	return lista

def menor_evaluacion(punto_actual, punto_final, lista, nodo):
	menor = lista[0]
	for index in range(len(lista)):
		if not (nodo.hijo_buscado(lista[index])):
			menor = lista[index]
			break;
	#print "El primenor es :", menor
	for tupla in lista:
		#print "Distancia de tupla:", tupla,"es :",distan_eucli(punto_actual,tupla)+distan_eucli(punto_final,tupla)
		#print "Distancia de menor:", menor,"es :",distan_eucli(punto_actual,menor)+distan_eucli(punto_final,menor)
		if ((distan_eucli(punto_actual,tupla)+distan_eucli(tupla,punto_final)< distan_eucli(punto_actual,menor)+distan_eucli(menor,punto_final))):
			if not(nodo.hijo_buscado(tupla)):
				menor = tupla
	return menor



def AlgoritmoA(matriz,punto_inicial,punto_final):	
	grafo = crear_grafo()
	is_final = True
	lista_total = []
	lista_respuesta = []
	lista = []
	pila = []

	lista_respuesta.append(punto_inicial)
	lista_total.append(punto_inicial)

	punto_actual = punto_inicial

	index = index_grafo(grafo, punto_actual)
	nodo = grafo[index]
	lista = encontrar_hijos(matriz,nodo.pos, lista_respuesta)
	nodo.insertar_hijos(lista)
	pila.append(nodo)
	cont = 0
	while(is_final):
		if not (nodo.todos_evaluados()):
			print "La tupla es :",nodo.pos
			print "lista de hijos;",
			for a in range(len(nodo.lista_hijos)):
				print nodo.lista_hijos[a],
			print ""
			punto_actual = menor_evaluacion(nodo.pos,punto_final,nodo.lista_hijos,nodo)
			nodo.actualizar_hijo(punto_actual)
			print "hijos visitados"
			for a in range(len(nodo.lista_hijos_visitados)):
				print nodo.lista_hijos_visitados[a],
				if (nodo.lista_hijos_visitados==1):
					print nodo.lista_hijos[a],
			print ""
			grafo[index] = nodo
			print "El menor es : ", punto_actual
			if(nodo.pos == punto_final):
				lista_respuesta.append(nodo.pos)
				return (lista_total,lista_respuesta)
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
			print "Sacando el elemento", p.pos
			lista_respuesta.pop()
			for p in pila:
				print p.pos,
			print ""
			index = index_grafo(grafo,(pila[len(pila)-1]).pos)
			nodo = grafo[index]
			print "nuevo nodo luego de borrar es:",nodo.pos
		cont +=1
	return (lista_total,lista_respuesta)