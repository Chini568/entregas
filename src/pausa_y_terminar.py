import pygame
from sys import exit
from crear_bloques_y_textos import crear_boton
from config_mi_juego import *
from crear_bloques_y_textos import mostrar_texto, mostrar_texto_boton

def terminar():
    pygame.quit()
    exit()

def pausa():
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                terminar()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    terminar()           
                return
            
def esperar_click(screen, rect_1, rect_2, texto_1, texto_2, color, segundo_color):
    while True:
        crear_boton(screen, rect_1, texto_1, color, segundo_color)
        crear_boton(screen, rect_2, texto_2, color, segundo_color)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                terminar()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    terminar()           
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1 :
                    cursor = e.pos
                    if rect_1.collidepoint(cursor[0], cursor[1]):
                        return None 
                    elif  rect_2.collidepoint(cursor[0], cursor[1]):
                        return terminar() 
                    
