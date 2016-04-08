
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