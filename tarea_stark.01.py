from stark import lista_personajes
import os

heroe_masc_mas_bajo = ''
heroe_fem_mas_bajo = ''
heroe_masc_mas_alto = ''
heroe_fem_mas_alto = ''
altura_minima_masc = 0
altura_minima_fem = 0
altura_maxima_masc = 0
altura_maxima_fem = 0

def mostrar_nombres_masculinos(lista):
    nombres = []
    alturas = []
    for i in lista:
        if i["genero"] == "M":
            nombre  = i.get("nombre")
            nombres.append(nombre)
            altura = i.get("altura")
            altura = float(altura)
            alturas.append(altura)

    return nombres, alturas
nombres_masculinos, alturas_genero_masculinos = mostrar_nombres_masculinos(lista_personajes)

def mostrar_nombres_femenino(lista):
    nombres = []
    alturas = []
    for i in lista:
        if i["genero"] == "F":
            nombre  = i.get("nombre")
            nombres.append(nombre)
            altura = i.get("altura")
            altura = float(altura)
            alturas.append(altura)

    return nombres, alturas
nombres_femeninos, alturas_genero_femenino = mostrar_nombres_femenino(lista_personajes)

def color_ojos(lista):
    ojos_por_color = {
        "brown": [],
        "blue": [],
        "green": [],
        "hazel": [],
        "yellow": [],
        "silver": [],
        "red": [],
        "yellow (without irises)": []
        }

    for i in lista:
        color_ojos = i["color_ojos"].lower()
        nombre = i["nombre"]
        if color_ojos in ojos_por_color:
            ojos_por_color[color_ojos].append(nombre)
    return ojos_por_color

def color_pelo(lista):
    pelo_por_color ={
        "yellow" : [],
        "blond": [],
        "brown" : [],
        "brown / white": [],
        "white" : [],
        "black" : [],
        "green" : [],
        "auburn" : [],
        "red / orange" : [],
        "red" : [],
        }
    for i in lista:
        color_pelo = i["color_pelo"].lower()
        nombre = i["nombre"]
        
        if color_pelo in pelo_por_color:
            pelo_por_color[color_pelo].append(nombre)

    return pelo_por_color

def tipo_inteligencia(lista):
    tipos_de_inteligencia = {
        "average" : [],
        "good" : [],
        "high" : [],
        "" : [],
    }
    for i in lista:
        inteligencia = i["inteligencia"].lower()
        nombre = i["nombre"]
        
        if inteligencia in tipos_de_inteligencia:
            tipos_de_inteligencia[inteligencia].append(nombre)
    return tipos_de_inteligencia

def traductor_colores(lista):
    cambio_palabras={
        "yellow" : "amarillo",
        "blond" : "rubio",
        "brown" : "marron",
        "brown / white": "marron/blanco",
        "white" : "blanco",
        "black" : "negro",
        "green" : "verde",
        "auburn" : "castaño",
        "red / orange" : "rojo/naranja",
        "red" : "rojo",
        "blue": "azul",
        "hazel": "avellana",
        "silver": "plata",
        "yellow (without irises)": "amarillo (sin iris)",
    }
    return cambio_palabras.get(color, color)

def traductor(lista):
        cambio ={
        "average" : "promedio",
        "good" : "buena",
        "high" : "alta",
        "" : "no tiene",
        }
        return cambio.get(inteligencia, inteligencia)
for altura, nombre in zip(alturas_genero_masculinos, nombres_masculinos):
    if altura > altura_maxima_masc:
        altura_maxima_masc = altura
        heroe_masc_mas_alto = nombre
    if altura_minima_masc == 0 or altura_minima_masc > altura:
        altura_minima_masc = altura
        heroe_masc_mas_bajo = nombre

for altura, nombre in zip(alturas_genero_femenino, nombres_femeninos):
    if altura > altura_maxima_fem:
        altura_maxima_fem = altura
        heroe_fem_mas_alto = nombre
    if altura_minima_fem == 0 or altura_minima_fem > altura:
        altura_minima_fem = altura
        heroe_fem_mas_bajo = nombre


    


promedio_altura_masc = sum(alturas_genero_masculinos) / len(alturas_genero_masculinos)
promedio_altura_fem = sum(alturas_genero_femenino) / len(alturas_genero_femenino)

def limpiar_consola():
    os.system('cls')

while True:
    limpiar_consola()

    print('Menu de opciones.\nA. Mostrar de todos los heroes de genero masculino.\nB. Mostrar de todos los heroes de genero femenino.\nC. Mostrar el heroe mas alto y su altura.\nD. Mostrar la heroína mas alta y su altura.\nE. Mostrar el heroe mas bajo y su altura.\nF. Mostrar la heroínas mas baja y su altura.\nG. Calcular la altura promedio de los heroes.\nH. Calcular la altura promedio de las heroínas.\nI. Mostrar el nombre del heroe mas altos y mas bajo, y el nombre de la heroína mas alta y la mas baja.\nJ. Mostrar cuantos heroes tienen cada tipo de color de ojo.\nK. Mostrar cuantos heroes tienen cada tipo de color de pelo.\nL. Mostrar cuantos heroes tiene cada tipo de inteligencia.\nM. Mostrar todos los heroes agrupados por color de ojos.\nN. Mostrar todos los heroes agrupados por color de pelo.\nÑ. Mostrar todos los heroes agrupados por su inteligencia.')

    opcion = input('Ingrese la opcion que quiera que se muestre(del A al O):  ').upper()
    
    if opcion == 'A':
        for i in nombres_masculinos:
            print(i)
    elif opcion == 'B':
        for i in nombres_femeninos:
            print(i)
    elif opcion == 'C':
        print(f'El heroe mas alto es {heroe_masc_mas_alto} con {altura_maxima_masc:.2f} centimetros.')
    elif opcion == 'D':
        print(f'La heroína mas alto es {heroe_fem_mas_alto} con {altura_maxima_fem:.2f} centimetros.')
    elif opcion == 'E':
        print(f'El heroe mas bajo es {heroe_masc_mas_bajo} con {altura_minima_masc:.2f} centimetros.')
    elif opcion == 'F':
        print(f'La heroína mas bajo es {heroe_fem_mas_bajo} con {altura_minima_fem:.2f} centimetros.')
    elif opcion == 'G':
        print(f'El promedio de alturas de los heroes es de {promedio_altura_masc}.')
    elif opcion == 'H':
        print(f'El promedio de alturas de las heroínas es de {promedio_altura_fem}.')
    elif opcion == 'I':
        print(f'El heroe mas alto es {heroe_masc_mas_alto}, la heroína mas alto es {heroe_fem_mas_alto}, el heroe mas bajo es {heroe_masc_mas_bajo}, la heroína mas bajo es {heroe_fem_mas_bajo}.')
    elif opcion == 'J':
        print(f'{len(color_ojos(lista_personajes)["brown"])} tienen ojos marrones, {len(color_ojos(lista_personajes)["blue"])} tienen ojos azules, {len(color_ojos(lista_personajes)["green"])} tienen ojos verdes, {len(color_ojos(lista_personajes)["brown"])} tienen ojos avellanas, {len(color_ojos(lista_personajes)["yellow"])} tienen ojos amarillos, {len(color_ojos(lista_personajes)["silver"])} tienen ojos plateados, {len(color_ojos(lista_personajes)["red"])} tienen ojos rojos, y {len(color_ojos(lista_personajes)["yellow (without irises)"])} tienen amarillos sin iris.')
    elif opcion == 'K':
        print(f'{len(color_pelo(lista_personajes)["yellow"])} tienen pelo amarillo, {len(color_pelo(lista_personajes)["blond"])} tienen pelo rubio,  {len(color_pelo(lista_personajes)["brown"])} tienen pelo marron, {len(color_pelo(lista_personajes)["black"])} tienen pelo negro, {len(color_pelo(lista_personajes)["white"])} tienen pelo blanco, {len(color_pelo(lista_personajes)["green"])} tienen pelo verde, {len(color_pelo(lista_personajes)["auburn"])} tienen pelo castaño, {len(color_pelo(lista_personajes)["red / orange"])} tienen rojo/naranja, {len(color_pelo(lista_personajes)["red"])} tienen pelo rojo, y {len(color_pelo(lista_personajes)["brown / white"])} tienen marron/white.')
    elif opcion == 'L':
        print(f'{len(tipo_inteligencia(lista_personajes)["good"])} tienen buena inteligencia, {len(tipo_inteligencia(lista_personajes)["average"])} tienen una inteligencia promedio, {len(tipo_inteligencia(lista_personajes)["good"])} tienen buena inteligencia, y {len(tipo_inteligencia(lista_personajes)[""])} no tiene inteligencia.')
    elif opcion == 'M':
        for color, nombres in color_ojos(lista_personajes).items():
            print(f'Los heroes con ojos {traductor_colores(lista_personajes)} son: ')
            for nombre in nombres:
                print(f'   *{nombre}')
    elif opcion == 'N':
        for color, nombres in color_pelo(lista_personajes).items():
            print(f'Los heroes con pelo color {traductor_colores(lista_personajes)} son: ')
            for nombre in nombres:
                print(f'   *{nombre}')
    elif opcion == 'Ñ':
        for inteligencia, nombres in tipo_inteligencia(lista_personajes).items():
            print(f'Los heroes con inteligencia {traductor(lista_personajes)} son: ')
            for nombre in nombres:
                print(f'   *{nombre}')
    input('Presione Enter para continuar...')


