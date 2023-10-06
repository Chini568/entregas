from stark import lista_personajes
import os

def mostrar_nombres(lista):
    nombres = []
    for i in lista:
        nombre  = i.get("nombre")
        nombres.append(nombre)
    return nombres


def mostrar_altura(lista):
    alturas = []
    for i in lista:
        altura = i.get("altura")
        altura = float(altura)
        alturas.append(altura)
    return alturas 

def promedio_alturas(lista):
    alturas = mostrar_altura(lista_personajes)
    promedio = sum(alturas) / len(alturas)
    return promedio

def calcular_heroe_mas_alto_y_bajo(lista):
    altura_maxima = 0
    altura_minima = 0
    heroe_mas_bajo = ''
    heroe_mas_alto = ''
    for i in lista:
        nombre = i.get("nombre")
        altura = i.get("altura")
        altura = float(altura)
        if altura > altura_maxima:
            altura_maxima = altura
            heroe_mas_alto = nombre
        if altura_minima == 0 or altura < altura_minima:
            altura_minima = altura
            heroe_mas_bajo = nombre
    return altura_maxima, heroe_mas_alto, altura_minima, heroe_mas_bajo
altura_maxima, heroe_mas_alto , altura_minima, heroe_mas_bajo  = calcular_heroe_mas_alto_y_bajo(lista_personajes)

def heroe_mas_y_menos_pesado(lista):
    peso_maximo = 0
    peso_minimo = 0
    heroe_peso_maximo = ''
    heroe_peso_minimo = ''
    for i in lista:
        nombre = i.get("nombre")
        peso = i.get("peso")
        peso = float(peso)
        if peso > peso_maximo:
            peso_maximo = peso
            heroe_peso_maximo = nombre
        if peso_minimo == 0 or peso_minimo > peso:
            peso_minimo = peso
            heroe_peso_minimo = nombre
    return peso_maximo, heroe_peso_maximo, peso_minimo, heroe_peso_minimo
peso_maximo, heroe_peso_maximo, peso_minimo, heroe_peso_minimo = heroe_mas_y_menos_pesado(lista_personajes)

def limpiar_consola():
    os.system('cls')

while True:
    limpiar_consola()

    print('Menu de opciones:\n1. Mostrar heroes.\n2. Mostrar heroes con sus alturas.\n3. Mostrar promedio de altura.\n4. Mostrar heroes mas alto y mas bajo.\n5. Mostrar heroes mas y menos pesado.\n6. Salir')

    opcion = input('Ingrese la opcion que quiera que se muestre(del 1 al 6):  ')
    if opcion == '1':
        for nombre in mostrar_nombres(lista_personajes):
            print(f'{nombre}')
    elif opcion == '2':
        for nombre, altura in zip(mostrar_nombres(lista_personajes), mostrar_altura(lista_personajes)):
            print(f'{nombre} mide {altura:.2f}')
    elif opcion == '3':
        print(f'El promedio de altura es de : {promedio_alturas(lista_personajes):.2f}')
    elif opcion == '4':
        print(f'El heroe mas alto es {heroe_mas_alto} con {altura_maxima} centimetros, y el mas bajo es {heroe_mas_bajo} con {altura_minima} centrimetros.')
    elif opcion == '5':
        print(f'El heroe mas pesado es {heroe_peso_maximo} con {peso_maximo} kilos, y el menos pesado es {heroe_peso_minimo} con {peso_minimo} kilos.')
    elif opcion == '6':
        break
    else:
        print('Caracter invalido elija un numero de 1 a 6')
        print('Menu de opciones:\n1. Mostrar heroes.\n2. Mostrar heroes con sus alturas.\n3. Mostrar promedio de altura.\n4. Mostrar heroes mas alto y mas bajo.\n5. Mostrar heroes mas y menos pesado.\n6. Salir')

    input('Presione Enter para continuar...')
        
