from math import sqrt

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


def calcular_radio_rectangulo(rect):
    return rect.width // 2


def distancia_centros_rect(rect1, rect2):
    return distancia_entre_puntos(rect1.center, rect2.center)
