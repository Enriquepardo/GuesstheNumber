import random

MIN = 0
# menu del juego 
def bienvenida():
    print('Bienvenido al juego de adivinar un número.')
    print(nombre= input('Introduce tu nombre para empezar a jugar: '))
bienvenida()
    
def mostrar_menu(opciones):
    print('Selecione una opcion:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')
        
def leer_opciones(opciones):
    print('Has elegido', opciones) 
    
def funcionamiento_menu(opciones, opcion_salir):
    opcion = None
    while opcion != opcion_salir:
        mostrar_menu(opciones)
        opcion= leer_opciones(opciones)
        funcionamiento_menu(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Nivel facil (entre 0 y 100).', opcion1),
        '2': ('Nivel intermedio (entre 0 y 1.000).', opcion2),
        '3': ('Nivel avanzado (entre 0 y 1.000.000)', opcion3),
        '4': ('Nivel experto (entre 0 y 1.000.000.000.000).', opcion4),
        '5': ('Salir', salir)
    }

    funcionamiento_menu(opciones, '5')

def opcion1():
    print('Has elegido el nivel fácil (entre 0 y 100).')
def opcion2():
    print('Has elegido el nivel intermedio (entre 0 y 1.000).')
def opcion3():
    print('Has elegido el nivel fácil (entre 0 y 1.000.000).')
def opcion4():
    print('Has elegido el nivel fácil (entre 0 y 1.000.000.000.000).')
def salir():
    print('Saliendo...')
    
#juego 

from entrada import (pedir_entrada_numero, pedir_entrada_numero_delimitado,
                     pedir_entrada_si_o_no)

# Seccion de definicion de variables

# estructura del codigo 
def jugar_una_vez(numero, minimo, maximo):
    intento = pedir_entrada_numero_delimitado("Adivine el numero", minimo, maximo)

    # Se comprueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        victoria = False
    else:
        print("¡Ha ganado!")
        victoria = True
        minimo = maximo = intento
    return victoria, minimo, maximo


def pedir_entrada_del_numero_incognita(minimo, maximo):
    return pedir_entrada_numero_delimitado("Introduzca el número a adivinar",
                                        minimo, maximo)


def jugar_una_partida(numero, minimo, maximo):
    while True:
        # Se entra en un bucle infinito
        # que permite jugar varias veces

        victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)

        if (victoria):
            return


def decidir_limites():
    while True:
        minimo = pedir_entrada_numero("Quelle est la borne minimale ?")
        maximo = pedir_entrada_numero("Quelle est la borne maximale ?")
        if maximo > minimo:
            return minimo, maximo


def jugar():
    minimo, maximo = decidir_limites()
    while True:
        numero = pedir_entrada_del_numero_incognita(minimo, maximo)
        jugar_una_partida(numero, minimo, maximo)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return
