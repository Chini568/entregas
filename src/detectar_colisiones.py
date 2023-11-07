from math import sqrt
from random import randint
# colliderect

def detectar_colision(rec_1, rec_2):
    for r1, r2 in [(rec_1, rec_2), (rec_2, rec_1)]:
        
        return punto_en_rectangulo(r1.topleft, r2) or \
        punto_en_rectangulo(r1.topright, r2) or\
        punto_en_rectangulo(r1.bottomleft, r2) or\
        punto_en_rectangulo(r1.bottomright, r2)
    

# collidepoint

def punto_en_rectangulo(punto,rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom
         

def detectar_colision_circulo(rect1,rect2):
    distancia = distancia_entre_puntos(rect1.center, rect2.center)
    r1 = calcular_radio_rectangulo(rect1)
    r2 = calcular_radio_rectangulo(rect2)
    return distancia <= (r1 + r2)


def distancia_entre_puntos(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return sqrt((y1-y2) ** 2 + (x1 - x2) ** 2)

def distancia_rect_aleatorios(jugador, width, height, ancho_rect, alto_rect):
    enemigo_x = randint(0, width - ancho_rect)
    enemigo_y = randint(0, height - alto_rect)
    distancia = sqrt((enemigo_x - jugador['rect'].x)**2 + (enemigo_y - jugador['rect'].y)**2)
    return enemigo_x, enemigo_y,  distancia

def calcular_radio_rectangulo(rect):
    return rect.width // 2


def distancia_centros_rect(rect1, rect2):
    return distancia_entre_puntos(rect1.center, rect2.center)

