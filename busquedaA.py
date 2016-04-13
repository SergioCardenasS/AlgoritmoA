import pygame
from constants import *
from functions import * 
from Aasterisco import *
import threading

def main():
        grid = crear_matriz()
        punto_inicial = ()
        punto_final = ()
        puntos_seleccionados = 0
        lista_total = []
        lista_respuesta = []
        # Inicializamos pygame
        pygame.init()
        # Establecemos el LARGO y ALTO de la pantalla
        DIMENSION_VENTANA = [width, height]
        pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
        #Titulo
        pygame.display.set_caption("Busqueda Algoritmo A*")

        done = False
        reloj = pygame.time.Clock()
 
        while not done:
            for evento in pygame.event.get(): 
                if (evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == 27)): 
                    done = True
                elif (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT):
                    pos = pygame.mouse.get_pos()
                    # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
                    columna = ((pos[0]- xGrid)/ (LARGO + MARGEN))
                    fila = ((pos[1]-yGrid) / (ALTO + MARGEN))
                    if(columna>-1 and columna<tam and fila>-1 and fila<tam):
                        if (grid[fila][columna] == 1):
                                grid[fila][columna] = 0
                        elif(grid[fila][columna] == 2):
                            grid[fila][columna] = 1
                            puntos_seleccionados -=1
                        else :
                                grid[fila][columna] = 1
                        #print("Click ", pos, "Coordenadas de la reticula: ", fila, columna)

                elif (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT) :
                    pos = pygame.mouse.get_pos()
                    # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
                    columna = ((pos[0]- xGrid)/ (LARGO + MARGEN))
                    fila = ((pos[1]-yGrid) / (ALTO + MARGEN))
                    if(columna>-1 and columna<tam and fila>-1 and fila<tam):
                        if (grid[fila][columna] == 2):
                                grid[fila][columna] = 0
                                puntos_seleccionados -=1
                        elif(grid[fila][columna] < 2 and puntos_seleccionados!=2):
                                grid[fila][columna] = 2
                                puntos_seleccionados +=1
                                if (puntos_seleccionados==1):
                                    punto_inicial = (fila,columna)
                                elif (puntos_seleccionados==2):
                                    punto_final = (fila,columna)
                elif (evento.type == pygame.KEYDOWN and evento.key == 13):
                    pantalla.fill(NEGRO)
                    lista_respuesta = []
                    AlgoritmoA(grid,punto_inicial,punto_final,lista_respuesta)
                elif (evento.type == pygame.KEYDOWN and evento.key == 32):
                    lista_respuesta = []
                    lista_total = []
                    thread_ida = threading.Thread(target=AlgoritmoA, args = (grid,punto_inicial,punto_final,lista_respuesta))
                    thread_vuelta = threading.Thread(target=AlgoritmoA, args = (grid,punto_final,punto_inicial,lista_total))
                    thread_ida.start()
                    thread_vuelta.start()
                    thread_vuelta.join()
                    thread_ida.join()
                    if(distancia_total(lista_total)<distancia_total(lista_respuesta)):
                        lista_respuesta=lista_total
                        
            # Establecemos el fondo de pantalla.
            pantalla.fill(NEGRO)
            for fila in range(tam):
                for columna in range(tam):
                    color = BLANCO
                    if grid[fila][columna] == 1:
                        color = VERDE
                    elif grid[fila][columna] == 2:
                        color = ROJO
                    xRect = (MARGEN+LARGO) * columna + MARGEN + xGrid
                    yRect = (MARGEN+ALTO) * fila + MARGEN + yGrid
                    if (xRect < heightGrid and yRect < widthGrid):
                        pygame.draw.rect(pantalla,color, [xRect, yRect, LARGO, ALTO])
                        
            if(len(lista_respuesta)>0):
                for index in range(len(lista_respuesta)-1):
                    pygame.draw.line(pantalla, (0,255,255),encontrar_centro(lista_respuesta[index]),encontrar_centro(lista_respuesta[index+1]), 2)

            #pygame.draw.line(pantalla, (0,255,255),encontrar_centro(colum1,fila1),encontrar_centro(colum2,fila2), 2)
            # Limitamos a 20 fotogramas por segundo.
            reloj.tick(20)
         
            # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
            pygame.display.flip()
             
        pygame.quit()

main()