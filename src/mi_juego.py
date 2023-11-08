import pygame
import os 
from random import randint
from sys import exit
from math import sqrt
from config_mi_juego import *
from detectar_colisiones import * 
from crear_bloques_y_textos import *
from pausa_y_terminar import *
def guardar_puntaje(puntaje):
    with open('./src/assets_mi_juego/puntaje.txt', 'w') as archivo:
        archivo.write(str(puntaje))

def leer_puntaje():
    try:
        with open('./src/assets_mi_juego/puntaje.txt', 'r') as archivo:
            return int(archivo.read())
    except:
        with open('./src/assets_mi_juego/puntaje.txt', 'w') as archivo:
            return archivo.write('0')

# nicializar los modulos de pygame
pygame.init()


# configuracion pantalla principal
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mi juego")
screen.fill


# creo un reloj
clock = pygame.time.Clock()

#direcciones
#imagenes
direccion_personaje = os.path.abspath("./src/assets_mi_juego/player.png")
direccion_personaje_derecha = os.path.abspath("./src/assets_mi_juego/player_derecha.png")
direccion_menu = os.path.abspath("./src/assets_mi_juego/fondo2.jpg")
direccion_enemigo = os.path.abspath("./src/assets_mi_juego/enemigo.png")
direccion_fondo = os.path.abspath("./src/assets_mi_juego/piso.jpg")
direccion_mejora = os.path.abspath("./src/assets_mi_juego/power up.png")
direccion_silencio = os.path.abspath("./src/assets_mi_juego/mute.png")
direccion_vida = os.path.abspath("./src/assets_mi_juego/vida.png")
direccion_bala = os.path.abspath("./src/assets_mi_juego/bala.png")
#sonido
direccion_daño = os.path.abspath("./src/assets_mi_juego/oof.mp3")
direccion_partida_perdida = os.path.abspath("./src/assets_mi_juego/game over.mp3")
direccion_musica_fondo = os.path.abspath("./src/assets_mi_juego/megalovania.mp3")
direccion_victoria = os.path.abspath("./src/assets_mi_juego/you win.mp3")

# seteo sonidos
pygame.mixer.music.load(direccion_musica_fondo)
pygame.mixer.music.set_volume(0.3)
daño = pygame.mixer.Sound(direccion_daño)
victoria = pygame.mixer.Sound(direccion_victoria)
partida_perdida = pygame.mixer.Sound(direccion_partida_perdida)
partida_perdida.set_volume(0.3)
sonando_musica = True

# cargo imagenes
#fondos
fondo = pygame.transform.scale(pygame.image.load(direccion_fondo), tamaño_pantalla)
fondo_menu = pygame.image.load(direccion_menu)

# player
imagen_jugador  = pygame.transform.scale(pygame.image.load(direccion_personaje), (ancho_jugador, alto_jugador))
rect_jugador = imagen_jugador.get_rect()
mascara_jugador = pygame.mask.from_surface(imagen_jugador, 2)
imagen_jugador_derecha = pygame.transform.scale(pygame.image.load(direccion_personaje_derecha), (ancho_jugador, alto_jugador))

# enemigo
imagen_enemigo = pygame.transform.scale(pygame.image.load(direccion_enemigo), (ancho_enemigo, alto_enemigo))
rect_enemigo = imagen_enemigo.get_rect()
mascara_enemigo = pygame.mask.from_surface(imagen_enemigo, 2)

#mejora
imagen_mejora = pygame.transform.scale(pygame.image.load(direccion_mejora), (ancho_mejora, alto_mejora))
rect_mejora = imagen_mejora.get_rect()
mascara_mejora = pygame.mask.from_surface(imagen_mejora, 2)

#silencio
imagen_silencio = pygame.transform.scale(pygame.image.load(direccion_silencio), (50, 50))

#vidas
image_vida = pygame.transform.scale(pygame.image.load(direccion_vida), (ancho_vida, ancho_vida))

#bala
imagen_bala = pygame.transform.scale(pygame.image.load(direccion_bala), (ancho_bala, alto_bala))
rect_bala = imagen_bala.get_rect()
mascara_bala = pygame.mask.from_surface(imagen_bala, 2)
# eventos
MEJORA_DE_PODER = pygame.USEREVENT + 1
APARECER_ENEMIGOS = pygame.USEREVENT + 2


# tiempo eventos
pygame.time.set_timer(MEJORA_DE_PODER, randint(20000, 35000))
pygame.time.set_timer(APARECER_ENEMIGOS, randint(2000, 4500))

# contadores
max_puntaje = 0

# direcciones de movimiento
mover_arriba = False
mover_derecha = False
mover_izquierda = False
mover_abajo = False
izquierda = False

# disparo
disparo = False

# seteo textos 
fuente_juego = pygame.font.SysFont('8-bit Arcade In', 75)
fuente_juego_pequeña = pygame.font.SysFont('8-bit Arcade In', 45)
fuente_arial = pygame.font.SysFont('Arial', 45)
fuente_titulo = pygame.font.SysFont('8-bit Arcade In', 75)


# bloques, botones
boton_jugar = pygame.Rect(centro_x - boton_ancho // 2, centro_y, boton_ancho, boton_alto)
boton_salir = pygame.Rect(centro_x - boton_ancho // 2, centro_y + boton_alto * 1.5, boton_ancho, boton_alto)
jugador = crear_bloques(imagen_jugador, centro_x, centro_y, ancho_jugador, alto_jugador, rosa)



while True:
    enemigos = []
    disparos = []
    doble = False
    validacion_mejora_poder = False
    mejora_activa = False
    vidas = 3
    puntaje = 0     
    tiempo_mejora = FPS * 10
    mostrar_tiempo = 60
    max_puntaje = leer_puntaje()
    screen.blit(fondo_menu, (0,0))  
    mostrar_texto_boton(screen, "Chitato", width // 2, 100, 120 ,blanco)
    esperar_click(screen, boton_jugar, boton_salir, 'Jugar', 'Salir', azul, verde)
    pygame.mixer.music.play(-1)
    funcionando = True  

    while funcionando:
        pygame.mouse.set_visible(0)
        clock.tick(FPS)
        # pasaje de milisegundos a segundos
        #restandole los segundos en juego para ir de 60 para abajo
        mostrar_tiempo = mostrar_tiempo - 1 / FPS   
        if puntaje > max_puntaje:
            max_puntaje = puntaje
            guardar_puntaje(max_puntaje)
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    funcionando = False
                if e.type == APARECER_ENEMIGOS:
                    if mostrar_tiempo > 30:
                        for i in range(3):
                            #valido que la posicion de spawn del enemigo sea mayor a una distancia de 100 pixeles entre el jugador 
                            enemigo_x, enemigo_y, distancia = distancia_rect_aleatorios(jugador, width, height, ancho_enemigo, alto_enemigo)
                            if distancia > 100:
                                crear_enemigo(imagen_enemigo, enemigo_x, enemigo_y, None, enemigos, ancho_enemigo, alto_enemigo)
                    else:
                        for i in range(5):
                            enemigo_x, enemigo_y, distancia = distancia_rect_aleatorios(jugador, width, height, ancho_enemigo, alto_enemigo)
                            if distancia > 100:
                                crear_enemigo(imagen_enemigo, randint(0, width - ancho_enemigo), randint(0, height - alto_enemigo), None, enemigos, ancho_enemigo, alto_enemigo)

                if e.type == MEJORA_DE_PODER:
                    validacion_mejora_poder = True
                    mejora = crear_bloques(imagen_mejora, randint(0, width - ancho_mejora),randint(0, height - alto_enemigo), ancho_mejora, alto_mejora, verde, radio= 25)    
                    
                    
                # apretando la tecla
                if e.type == pygame.KEYDOWN:
                    # movimiento
                    if e.key == pygame.K_w or e.key == pygame.K_UP:
                        mover_arriba = True
                    if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                        mover_derecha = True
                        jugador['img'] = imagen_jugador_derecha
                        mascara_jugador = pygame.mask.from_surface(imagen_jugador_derecha, 2)
                    if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                        mover_izquierda = True
                        jugador['img'] = imagen_jugador
                        mascara_jugador = pygame.mask.from_surface(imagen_jugador, 2)
                    if e.key == pygame.K_s or e.key == pygame.K_DOWN:
                        mover_abajo = True
                        
                # cuando se suelta la tecla 
                if e.type == pygame.KEYUP:
                    # parar movimiento 
                    if e.key == pygame.K_w or e.key == pygame.K_UP:
                        mover_arriba = False
                    if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                        mover_derecha = False
                    if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                        mover_izquierda = False
                    if e.key == pygame.K_s or e.key == pygame.K_DOWN:
                        mover_abajo = False

                    # parar musica 
                    if e.key == pygame.K_m:
                        if sonando_musica:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                        sonando_musica = not sonando_musica

                    # pausa juego 
                    if e.key == pygame.K_p:
                        if sonando_musica:
                            pygame.mixer.music.pause()
                        mostrar_texto(screen, 'Pausa', fuente_juego, superior_pantalla, blanco, None)
                        mostrar_texto(screen, 'Presiona alguna tecla para continuar', fuente_juego_pequeña, centro_pantalla, blanco, None)
                        pygame.display.flip() 
                        pausa()
                        if sonando_musica:
                            pygame.mixer.music.unpause()    

                    # cierre juego 
                    if e.key == pygame.K_ESCAPE:
                        pygame.mouse.set_visible(1)
                        pygame.mixer.music.stop()
                        partida_perdida.play()
                        screen.blit(fondo_menu, (0,0))   
                        mostrar_texto_boton(screen, "Game over", width // 2, 100, 120 ,rojo)
                        mostrar_texto(screen, f"Puntaje maximo  {max_puntaje}", fuente_juego_pequeña, inferior_pantalla, amarillo, None)
                        vidas = 3
                        esperar_click(screen, boton_jugar, boton_salir, 'Jugar', 'Salir', azul, verde)
                        funcionando = False
                        f.write(str(puntaje))
                        

        #colision power up con jugador
        if validacion_mejora_poder:
            offset_mejora = (mejora['rect'].x - jugador['rect'].x, mejora['rect'].y - jugador['rect'].y)
            if mascara_mejora.overlap(mascara_jugador, offset_mejora):
                try:
                    doble = True
                    mejora_activa = True
                    validacion_mejora_poder = False
                except:
                    pass

        #termina mejora
        if mejora_activa:
            tiempo_mejora -= 1
            if tiempo_mejora == 0:
                mejora_activa = False
                doble = False

        #sacando las cordenadas del enemigo a atacar
        #si el jgugador mira a la derecha 
        if jugador['img'] == imagen_jugador_derecha:
            posicion = jugador['rect'].midright
            crear_balas(enemigos, jugador, doble, imagen_bala, posicion, ancho_bala, alto_bala, negro, disparos, disparo)
        #si el jugador mira a la izquierda                 
        elif jugador['img'] == imagen_jugador:
            posicion = jugador['rect'].midleft
            crear_balas(enemigos, jugador, doble, imagen_bala, posicion, ancho_bala, alto_bala, negro, disparos, disparo)

        #cordenadas de movimiento de los enemigos
        for enemigo in enemigos[:]:
            movimiento_enemigos(jugador, enemigo)
            enemigo['rect'].move_ip(enemigo['speed_x'], enemigo['speed_y'])
            #eliminacion enemigo
            if disparo:
                for disparo in disparos[:]:      
                    offset_bala = (enemigo['rect'].x - disparo['rect'].x, enemigo['rect'].y - disparo['rect'].y)
                    if mascara_bala.overlap(mascara_enemigo, offset_bala):
                        try: 
                            enemigos.remove(enemigo)
                            disparos.remove(disparo)
                            puntaje += 100
                            disparo = False
                        except:
                            pass
            #daño
            offset = (enemigo['rect'].x - jugador['rect'].x, enemigo['rect'].y - jugador['rect'].y)
            if mascara_enemigo.overlap(mascara_jugador, offset):
                try:
                    enemigos.remove(enemigo)
                    daño.play()
                    if vidas > 0:
                        vidas -= 1
                        if puntaje > 100:
                            puntaje -= 100
                except:
                    pass

            #muerte 
            if vidas == 0:
                pygame.mouse.set_visible(1)
                pygame.mixer.music.stop()
                partida_perdida.play()
                screen.blit(fondo_menu, (0,0))   
                mostrar_texto_boton(screen, "Game over", width // 2, 100, 120 ,rojo)
                mostrar_texto(screen, f"Puntaje maximo  {max_puntaje}", fuente_juego_pequeña, inferior_pantalla, amarillo, None)
                vidas = 3
                esperar_click(screen, boton_jugar, boton_salir, 'Continuar', 'Salir', azul, verde)
                funcionando = False


            #victoria
            if int(mostrar_tiempo) == 0:
                pygame.mouse.set_visible(1)
                pygame.mixer.music.stop()
                victoria.play()
                screen.blit(fondo_menu, (0,0))   
                mostrar_texto_boton(screen, "You win", width // 2, 100, 120 ,amarillo)
                mostrar_texto(screen, f"Puntaje maximo  {max_puntaje}", fuente_juego_pequeña, inferior_pantalla, amarillo, None)
                mostrar_tiempo = 60
                esperar_click(screen, boton_jugar, boton_salir, 'Continuar', 'Salir', azul, verde)
                funcionando = False


        #movimiento bala
        for i in disparos[:]:
            i['rect'].move_ip(i['speed_x'], i['speed_y'])
            if i['rect'].bottom < 0:
                disparos.remove(i)
                disparo = False
            if i['rect'].right < 0:
                disparos.remove(i)
                disparo = False
            if i['rect'].top > height:
                disparos.remove(i)
                disparo = False
            if i['rect'].left > width:
                disparos.remove(i)
                disparo = False

        #movimiento en direccion       
        if mover_arriba and jugador['rect'].top >= (0 + velocidad) : 
            #arriba
            jugador['rect'].top -= velocidad
        if mover_derecha and jugador['rect'].right <= (width - velocidad): 
            #derecha
            jugador['rect'].left += velocidad
        if mover_izquierda and jugador['rect'].left >= (0 + velocidad):
            #izquierda
            jugador['rect'].left -= velocidad
        if mover_abajo and jugador['rect'].bottom <= (height - velocidad) :
            #abajo
            jugador['rect'].top += velocidad

       
        #dibujado y bliteo de imagenes y rectangulos
        screen.blit(fondo, (0,0))   
        screen.blit(jugador['img'], jugador['rect'])  
        for disparo in disparos:
            screen.blit(disparo['img'], disparo['rect'])
        if not sonando_musica:
            screen.blit(imagen_silencio, (0 - 4 , 0 - 7))   
        if vidas == 3:
            screen.blit(image_vida, (0, height - alto_vida))
            screen.blit(image_vida, (0 + ancho_vida + 5, height - alto_vida))
            screen.blit(image_vida, (0 + (ancho_vida*2) + 10, height - alto_vida))
        elif vidas == 2:
            screen.blit(image_vida, (0, height - alto_vida))
            screen.blit(image_vida, (0 + ancho_vida + 5, height - alto_vida))
        elif vidas == 1:
            screen.blit(image_vida, (0, height - alto_vida))
        if mejora_activa:
            mostrar_texto(screen, "Mejora", fuente_juego_pequeña, (width // 2, height - 50), verde, None)
        dibujar_enemigos(screen, enemigos)
        if validacion_mejora_poder:
            screen.blit(mejora['img'], mejora['rect'])
        mostrar_texto(screen, f'Tiempo {int(mostrar_tiempo)}', fuente_juego_pequeña , superior_pantalla_mas, negro, None)
        mostrar_texto_abajo_derecha(screen, f'Puntos {puntaje}', fuente_juego_pequeña , (width, height), amarillo, None)
        pygame.display.flip()

    disparo = False
    pygame.mouse.set_visible(1)
    pygame.mixer.music.stop()
    mover_abajo = False
    mover_izquierda = False
    mover_derecha = False
    mover_arriba = False
pygame.quit()
exit()



