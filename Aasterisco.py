
from constants import *
from functions import *


def encontrar_hijos(matriz, punto_actual, lista_respuesta, lista_total):
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
				if not (tupla in lista_respuesta):
					lista.append(tupla)	
			col +=1
		fil+=1
	return lista

def menor_evaluacion(punto_actual, punto_final, lista):
	menor = lista[0]
	for tupla in lista:
		#print "Distancia de :", tupla,"es :",distan_eucli(punto_actual,tupla)+distan_eucli(punto_final,tupla)
		#print "Distancia de :", menor,"es :",distan_eucli(punto_actual,menor)+distan_eucli(punto_final,menor)
		if (distan_eucli(punto_actual,tupla)+distan_eucli(punto_final,tupla)<= distan_eucli(punto_actual,menor)+distan_eucli(punto_final,menor)):
			menor = tupla
	return menor



def AlgoritmoA(matriz,punto_inicial,punto_final):
	is_final = True
	lista_total = []
	lista_respuesta = []
	lista = []

	lista_total.append(punto_inicial)
	lista_respuesta.append(punto_inicial)

	punto_actual = punto_inicial
	while(is_final):
		print "La tupla es :",punto_actual
		lista_total.remove(punto_actual)
		lista = encontrar_hijos(matriz,punto_actual, lista_respuesta, lista_total)
		print "lista de hijos",lista
		punto_actual = menor_evaluacion(punto_actual,punto_final,lista)
		for tupla in lista:
			lista_total.append(tupla)

		lista_respuesta.append(punto_actual)

		if (punto_final in lista_respuesta):
			is_final = False
	return (lista_total,lista_respuesta)




