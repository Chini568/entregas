import pygame
from random import randint
from math import sqrt
from config_mi_juego import velocidad_enemigo , velocidad_bala


def mostrar_texto(superficie, texto, fuente, cordenadas, color_fuente, color_fondo = (0,0,0)):
    superficie_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rect_texto = superficie_texto.get_rect()
    rect_texto.center = cordenadas
    superficie.blit(superficie_texto, rect_texto)

def mostrar_texto_abajo_derecha(superficie, texto, fuente, cordenadas, color_fuente, color_fondo = (0,0,0)):
    superficie_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rect_texto = superficie_texto.get_rect()
    rect_texto.bottomright = cordenadas
    superficie.blit(superficie_texto, rect_texto)
    
def mostrar_texto_abajo_izquierda(superficie, texto, fuente, cordenadas, color_fuente, color_fondo = (0,0,0)):
    superficie_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rect_texto = superficie_texto.get_rect()
    rect_texto.bottomleft = cordenadas
    superficie.blit(superficie_texto, rect_texto)
    
def mostrar_texto_arriba_derecha(superficie, texto, fuente, cordenadas, color_fuente, color_fondo = (0,0,0)):
    superficie_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rect_texto = superficie_texto.get_rect()
    rect_texto.topright = cordenadas
    superficie.blit(superficie_texto, rect_texto)

def mostrar_texto_boton(superficie, texto, x, y, font_size = 36, color = (0,0,0) ):
    fuente = pygame.font.SysFont('8-bit Arcade In', font_size)
    render = fuente.render(texto, True, color)
    rect_texto = render.get_rect(center = (x, y))
    superficie.blit(render, rect_texto)

def crear_boton(screen, rect:pygame.Rect ,texto, color, color_hover):
    posicion_mouse = pygame.mouse.get_pos()
    if rect.collidepoint(posicion_mouse):
        pygame.draw.rect(screen, color_hover, rect, border_radius= 10)
    else:
        pygame.draw.rect(screen, color, rect, border_radius= 10)
    mostrar_texto_boton(screen, texto, rect.centerx, rect.centery)

def crear_bloques(imagen = None, left = 0, top = 0, ancho = 40, alto = 40, color = (255, 255, 255),  radio = -1, speed_x = 5, speed_y = 5):
    rec = pygame.Rect(left, top, ancho, alto)
    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
    return {'rect' : rec, 'color' : color, 'radio' : radio, 'speed_x' : speed_x, 'speed_y' : speed_y, 'img' : imagen}

def crear_enemigo(imagen, ancho, alto, color, lista, ancho_bloque, alto_bloque):
    return lista.append(crear_bloques(imagen, ancho, alto, ancho_bloque, alto_bloque, color))

def dibujar_enemigos(superficie , enemigos):
    for enemigo in enemigos:
        superficie.blit(enemigo['img'], enemigo['rect'])

def movimiento_enemigos(jugador, enemigo):
    objetivo = jugador['rect']
    diferencia_x_enemigos = objetivo.centerx - enemigo['rect'].centerx
    diferencia_y_enemigos = objetivo.centery - enemigo['rect'].centery
    longitud = sqrt(diferencia_x_enemigos ** 2 + diferencia_y_enemigos ** 2) 
    if longitud > 0:  
        velocidad_x_enemigo = (diferencia_x_enemigos / longitud) * velocidad_enemigo
        velocidad_y_enemigo = (diferencia_y_enemigos / longitud) * velocidad_enemigo
    else:
        velocidad_x_enemigo = 0
        velocidad_y_enemigo = 0

    #movimiento enemigo
    enemigo['speed_x'] = velocidad_x_enemigo
    enemigo['speed_y'] = velocidad_y_enemigo

def movimiento_bala(jugador, enemigos):
    objetivo = enemigos[0]
    diferencia_x = objetivo['rect'].centerx - jugador['rect'].centerx
    diferencia_y = objetivo['rect'].centery - jugador['rect'].centery
    longitud = sqrt(diferencia_x ** 2 + diferencia_y ** 2)
    velocidad_x_bala = diferencia_x / longitud * velocidad_bala
    velocidad_y_bala = diferencia_y / longitud * velocidad_bala
    return velocidad_x_bala, velocidad_y_bala

def crear_balas(enemigos, jugador, doble, imagen_bala, posicion, ancho_bala, alto_bala, negro, disparos, disparo):
    if enemigos:  
        if not disparo :
            velocidad_x_bala, velocidad_y_bala = movimiento_bala(jugador, enemigos)
            if doble:
                bala = crear_bloques(imagen_bala, posicion[0] - ancho_bala // 2, posicion[1] - 15, ancho_bala, alto_bala, negro, radio = 5, speed_x= velocidad_x_bala, speed_y= velocidad_y_bala)
                bala_1 = crear_bloques(imagen_bala, posicion[0] - ancho_bala // 2 , posicion[1] + 15 , ancho_bala, alto_bala, negro, radio = 5, speed_x= velocidad_x_bala, speed_y= velocidad_y_bala)
                disparos.append(bala)
                disparos.append(bala_1)
                disparo = True
            else:
                bala = crear_bloques(imagen_bala, posicion[0] - ancho_bala // 2, posicion[1], ancho_bala, alto_bala, negro, radio = 5, speed_x= velocidad_x_bala, speed_y= velocidad_y_bala)
                disparos.append(bala)
                disparo = True
    