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
	#for index in  range(len(nodo.lista_hijos_visitados)):
	#	print nodo.lista_hijos_visitados[index],
	#	if (nodo.lista_hijos_visitados[index] == 1):
	#		print nodo.lista_hijos[index],
	#print ""
	menor = lista[0]
	for index in range(len(lista)):
		if not (nodo.hijo_buscado(lista[index])):
			menor = lista[index]
			break;
	#print "El primenor es :", menor
	for tupla in lista:
		print "Distancia de tupla:", tupla,"es :",distan_eucli(punto_actual,tupla)+distan_eucli(punto_final,tupla)
		print "Distancia de menor:", menor,"es :",distan_eucli(punto_actual,menor)+distan_eucli(punto_final,menor)
		if ((distan_eucli(punto_actual,tupla)+distan_eucli(tupla,punto_final)< distan_eucli(punto_actual,menor)+distan_eucli(menor,punto_final))):
			#print "Nodo buscado : ",tupla ," - ",nodo.hijo_buscado(tupla)
			if not(nodo.hijo_buscado(tupla)):
				menor = tupla
	return menor

def AlgoritmoA(matriz,punto_inicial,punto_final):
	is_final = True
	lista_total = []
	lista_respuesta = []
	lista = []
	pila = []

	lista_respuesta.append(punto_inicial)
	lista_total.append(punto_inicial)

	punto_actual = punto_inicial

	nodo = punto(punto_actual)
	lista = encontrar_hijos(matriz,punto_actual, lista_respuesta)
	nodo.insertar_hijos(lista)
	pila.append(nodo)

	cont = 0

	while(is_final):
		if not (nodo.todos_evaluados()):
			#print "Tiene hijos por visitar"
			#print "La tupla es :",nodo.pos
			#print "lista de hijos ", nodo.imprimir_lista_hijos()
			#lista_total.remove(punto_actual)
			#lista = encontrar_hijos(matriz,punto_actual, lista_respuesta)
			#nodo.insertar_hijos(lista)

			punto_actual = menor_evaluacion(nodo.pos,punto_final,nodo.lista_hijos,nodo)
			nodo.actualizar_hijo(punto_actual)
			#print "El menor es : ", punto_actual
			punt = pila[len(pila)-1]
			if(nodo.pos == punto_final):
				lista_respuesta.append(nodo.pos)
				return (lista_total,lista_respuesta)
			if not (punto_actual in lista_respuesta):
				for tupla in lista:
					lista_total.append(tupla)
				#print "Agregando el nodo", nodo.pos
				if not (nodo.pos in lista_respuesta):
					lista_respuesta.append(nodo.pos)
					pila.append(nodo)
				for tupla in lista_respuesta:
					print tupla,
				print ""
				nodo = punto(punto_actual)
				lista = encontrar_hijos(matriz,punto_actual, lista_respuesta)
				nodo.insertar_hijos(lista)

				if (punto_final in lista_respuesta):
					is_final = False
		else:
			#pila.remove(nodo)
			p = pila.pop()
			lista_respuesta.pop()
			#print "Eliminando el nodo", p.pos
			nodo = pila[len(pila)-1]			
			#print "Nuevo nodo", nodo.pos
			for tupla in lista_respuesta:
				print tupla,
			print ""
		#cont +=1
	return (lista_total,lista_respuesta)