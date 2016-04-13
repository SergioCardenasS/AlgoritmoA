
from constants import *
from grafo import *
from math import sqrt

def crear_matriz():
    grid = []
    for fila in range(tam):
        grid.append([])
        for columna in range(tam):
            grid[fila].append(0) 
    return grid

def encontrar_centro(tupla):
    x = (tupla[1]*(LARGO + MARGEN)+xGrid)+LARGO/2
    y = (tupla[0]*(LARGO + MARGEN)+yGrid)+ALTO/2
    return (x,y)

def distan_eucli(first,second):
	return sqrt(sum( (second - first)**2 for first, second in zip(first, second)))

def distancia_total(lista):
    distancia = 0
    for index in range(len(lista)-1):
        distancia += distan_eucli(lista[index],lista[index+1])
    return distancia

def crear_grafo():
    grafo = []
    for x in range(tam):
        for y in range(tam):
            grafo.append(punto((x,y)))
    return grafo

def index_grafo(grafo,punto_actual):
    for index in range(len(grafo)):
        if(punto_actual == grafo[index].pos):
            return index

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
    for tupla in lista:
        if ((distan_eucli(punto_actual,tupla)+distan_eucli(tupla,punto_final)< distan_eucli(punto_actual,menor)+distan_eucli(menor,punto_final))):
            if not(nodo.hijo_buscado(tupla)):
                menor = tupla
    return menor

