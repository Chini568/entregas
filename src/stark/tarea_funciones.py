#1

def area_circulo(radio : float) -> float:
    """Culacular area circulo

    Args:
        radio (float): Radio dado por usuario.

    Returns:
        float: Area del circulo en base al radio.
    """
    PI = 3.14
    area = PI * radio ** 2
    return area

print(area_circulo(10))

#2

def numero_par(numero : int) -> str :
    """Calcular si el numero es par o impar

    Args:
        numero (int): numero dado por usuario

    Returns:
        str: Confirmacion de si es o no un numero par
    """
    if numero % 2 == 0:
        mensaje = 'par'
    else:
        mensaje = "impar"
    return print(f'El numero es {mensaje}')

numero_par(15)

#3

def suma_lista_numero(numeros : list) -> float :
    """Suma los numeros de una lista

    Args:
        numeros (float): Son los numeros asociados a la lista

    Returns:
        float: Resultado de la suma 
    """
    suma = 0 
    for numero in numeros:
        suma += numero 
    return suma 
lista_numeros = [1, 5, 200.5, 1255.275]
resultado = suma_lista_numero(lista_numeros)
print(f'La suma de la lista es de {resultado}')

#4

def numero_mayor(numero_a : float, numero_b : float, numero_c : float) -> float:
    """Saca numero mayor entre 3 numeros 

    Args:
        numero_a (float): Primer numero a ingresar
        numero_b (float): segundo numero a ingresar
        numero_c (float): tercer numero a ingresar

    Returns:
        float: El numero mayor entre los 3 
    """
    maximo_numero = max(numero_a, numero_b, numero_c)
    return maximo_numero

print(f'El numero mayor es {numero_mayor(2, 200, 5)}')

#5

def invertir_cadena(cadena : str) -> str:
    """Invierte cadena de palabras

    Args:
        cadena (str): oracion a invertir 


    Returns:
        str: oracion invertida 
    """
    cadena_invertida = cadena[:: -1 ]
    return cadena_invertida
texto = "estoy programando"
cadena_invertida = invertir_cadena(texto)
print(f"{cadena_invertida}")

#6

def ordenar_palabras_alfabeticamente(lista_palabras : list) -> list:
    """Ordena las palabras por orden alfabetico

    Args:
        lista_palabras (list): Lista de las palabras a ordenar

    Returns:
        list: Lista ya ordenada
    """
    palabras_ordenadas = sorted(lista_palabras)
    return palabras_ordenadas
lista_palabras = ['auto', 'programador', 'python', 'funcion']
resultado_orden_alfabetico = ordenar_palabras_alfabeticamente(lista_palabras)
print(f'{resultado_orden_alfabetico}')

#7

def calcular_potencia(numero : float, potencia : float) -> float:
    """Calcular la potencia de un numero

    Args:
        numero (float): Base a elevar
        potencia (float): Exponente 

    Returns:
        float: Resultado de la potenciacion
    """
    resultado = numero ** potencia
    return resultado
print(calcular_potencia(2, 4))

#8

def lista_numeros_pares(lista_numeros : list) -> list:
    """Crear lista de numeros pares

    Args:
        lista_numeros (list): Lista de numeros

    Returns:
        list: Nueva lista de numeros pares
    """
    lista_numeros_pares = []
    for i in lista_numeros:
        if i % 2 == 0:
            lista_numeros_pares.append(i)
        else:
            pass
    return lista_numeros_pares
lista_numeros_2 = [1, 5, 200, 125, 150]
print(lista_numeros_pares(lista_numeros_2))

#9

def multiplicar_lista_numeros(lista_numeros : list) -> float:
    """Multiplica una lista de numeros entre si

    Args:
        lista_numeros (list): Lista de numeros a multiplicar

    Returns:
        float: Resultado de la multiplicacion
    """
    producto = 1 
    for i in lista_numeros:
        producto = producto * i 
    return producto
lista_numeros_a_multiplicar = [2, 4, 5, 5]
print(multiplicar_lista_numeros(lista_numeros_a_multiplicar))

#10

def detector_palindromos(cadena : str) -> str:
    """Detecta si la cadena dada es un palindromo

    Args:
        cadena (str): Cadena a analizar

    Returns:
        str: Resultado de si es o no un palindromo
    """
    cadena_invertida = cadena.upper()[:: -1 ]
    if cadena.upper() == cadena_invertida:
        resultado = 'Es un palindromo'
    else:
        resultado = 'No es un palindromo'
    return resultado
print(detector_palindromos('Neuquen'))
