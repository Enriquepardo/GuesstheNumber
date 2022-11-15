import random

MAX = 1000000000000
MIN = 0
intentos = MAX
nombre = input('Bienvenido, introduce tu nombre para empezar a jugar: ')
menu = """ahora elige un nivel de dificultad para comenzar a jugar:
    [1] Nivel fácil (entre 0 y 100)
    [2] Nivel intermedio (entre 0 y 1.000)
    [3] Nivel avanzado (entre 0 y 1.000.000)
    [4] Nivel experto (entre 0 y 1.000.000.000.000)
    [5] Salir del juego
"""
eleccion_menu = True
intentos = 0
intentoslim = {}


def menu_principal():
    print("Genial", nombre, menu)

menu_principal()

def elecion_menu():
    while eleccion_menu:
        nivel_elegido = int(input('¿Qué nivel vas a jugar?: '))
        intentos += 1
        if nivel_elegido == 1:
            print('Has elegido el nivel fácil, tienes 15 intentos.')
            numero = random.randint (0,100)
            intentoslim <= 15
        
        elif nivel_elegido == 2:
            print('Has elegido el nivel intermedio, tienes 10 intentos.')
            numero = random.randint (0,1000)
            intentos <= 10
            
        elif nivel_elegido == 3:
            print('Has elegido el nivel dificil, tienes 5 intentos.')
            numero = random.randint (0, 1000000)
            intentos <= 5
            
        elif nivel_elegido == 4:
            print('Has elegido el nivel experto,, tienes 3 intentos.')
            numero = random.randint (0, 1000000000000)
            intentos <= 3
            
        elif nivel_elegido == 5:
            print('Saliendo...')
            
            
        else: 
            print('No has elegido ningun nivel, intentalo otra vez.')
        




while juego:
    
    if intentos <= intentoslim:
        eleccion= input("Introduce un número entre 0 y 99: ")
        
        if eleccion.isdigit():
            
                try:
                    intentos = int(intentos)
                except:
                    print ("Escribe un numero entero.")
                    
                    if eleccion == numero:
                        print("Has acertado, lo has adivinado en", intentos, "intentos.")
                        juego = False
                        
                    elif eleccion > numero:
                        print("Demasiado alto, llevas", intentos, "intentos.")
                        
                    elif eleccion < numero:
                        print("Demasiado bajo, llevas", intentos, "intentos.") 
                                
    else:
        print("Has perdido, te has quedado sin intentos.")
        juego = False 
