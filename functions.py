
from constants import *
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
