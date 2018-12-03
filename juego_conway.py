import pygame, sys
from pygame import *
import random

frames = 10
negro = (0,0,0)
blanco = (255,255,255)
gris = (128, 128, 128)
verde = (0,255,0)

ancho = 1000
alto = 700
celula = 10

ancho_celula = ancho // celula 
alto_celula = alto // celula 

def cuadricula():
    """
    Funcion que dibuja la cuadricula del tablero
    """
    for x in range(0, ancho, celula): # draw vertical lines
        pygame.draw.line(display_game, negro, (x,0),(x,alto))
    for y in range (0, alto, celula): # draw horizontal lines
        pygame.draw.line(display_game, negro, (0,y), (ancho, y))

def color(i, lifeDict):
    """
    Esta funcion pinta las celulas vivas de verde
    y las celulas muertas de gris
    """
    x,y = i[0],i[1]
    y = y * celula 
    x = x * celula 
    if lifeDict[i] == 0:
        pygame.draw.rect(display_game, gris, (x, y, celula, celula))
    if lifeDict[i] == 1:
        pygame.draw.rect(display_game, verde, (x, y, celula, celula))
    return None


def dic_celulas():
    """Funcion que crea un diccionario
    estableciendo todas las celulas = 0
    celula = 0 --> celula muerta
    """
    dict_celulas = {}
    for y in range (alto_celula):
        for x in range (ancho_celula):
            dict_celulas[x,y] = 0 
    return dict_celulas

#Assigns a 0 or a 1 to all cells
def celulas_vivas(dict_celulas):
    """
    Funcion que retorna un diccionario con:
    celulas muertas (0) y celulas vivas(1) 
    al azar
    """
    for i in dict_celulas:
        dict_celulas[i] = random.randint(0,1)
    return dict_celulas


def celulas_vecinas(i,dict_celulas):
    """
    Funcion que evalua la casillas y retorna el conteo de celulas vecinas
    """
    celua_vecina = 0
    for x in range (-1,2):
        for y in range (-1,2):
            cel = (i[0]+x,i[1]+y)
            if cel[0] < ancho_celula  and cel[0] >=0:
                if cel [1] < alto_celula and cel[1]>= 0:
                    if dict_celulas[cel] == 1:
                        if x == 0 and y == 0: 
                            celua_vecina += 0
                        else:
                            celua_vecina += 1
    return celua_vecina

def nueva_iteracion(dict_celulas):
    """
    Esta funcion evaluas las reglas del juego para cada nueva iteracion.
    """
    iteracion = {}
    for i in dict_celulas:
        num_celulas_vecinas = celulas_vecinas(i, dict_celulas)
        if dict_celulas[i] == 1: 
            if num_celulas_vecinas < 2: 
                iteracion[i] = 0
            elif num_celulas_vecinas > 3: 
                iteracion[i] = 0
            else:
                iteracion[i] = 1 
        elif dict_celulas[i] == 0:
            if num_celulas_vecinas == 3: 
                iteracion[i] = 1
            else:
                iteracion[i] = 0 
    return iteracion

def main():
    """
    Funcion princial que invoca las anteriores funciones
    """
    pygame.init()
    global display_game
    reloj = pygame.time.Clock()
    display_game = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Juego de la Vida")

    display_game.fill(blanco)

    dict_celulas = dic_celulas() 
    dict_celulas = celulas_vivas(dict_celulas) 
    for item in dict_celulas:
        color(item, dict_celulas)
    cuadricula()
    
    pygame.display.update()
    
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        dict_celulas = nueva_iteracion(dict_celulas)
        for item in dict_celulas:
            color(item, dict_celulas)
        cuadricula()

        pygame.display.update()    
        reloj.tick(frames)
        
if __name__=='__main__':
    main()
