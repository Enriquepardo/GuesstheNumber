import sys

nombre = input('Bienvenido, introduce tu nombre para empezar a jugar: ')
menu = """ahora elige un nivel de dificultad para comenzar a jugar:
    [1] Nivel fácil (entre 0 y 100)
    [2] Nivel intermedio (entre 0 y 1.000)
    [3] Nivel avanzado (entre 0 y 1.000.000)
    [4] Nivel experto (entre 0 y 1.000.000.000.000)
    [5] Salir del juego
"""
maximo = 0
numintentos_max = 15

# definicion de bienvenida a mi juego 
def bienvenida():
    print("Genial", nombre, menu)



# aqui defino el menu y hago una mini expliacion antes de jugar el nivel elegido
def eleccion_menu():        
    while True:
            nivel_elegido = input('¿Qué nivel vas a jugar?: ')           # se introduce el nivel que va jugar 
            if nivel_elegido.isdigit():
                try:
                    nivel_elegido = int(nivel_elegido)                  # compruebo que la cadena introducida es un entero
                        
                    if nivel_elegido <= 1:
                        maximo = maximo + 100
                        intentoslim = 15
                        break
                    elif nivel_elegido <= 2:
                        maximo = maximo + 1000
                        intentoslim = 10
                        break
                    elif nivel_elegido <= 3:
                        maximo = maximo + 1000000
                        intentoslim = 5
                        break
                    elif nivel_elegido <= 4:
                        maximo = maximo + 1000000000000
                        intentoslim = 3
                        break

                except ValueError:
                    print ("La entrada es incorrecta.")

                while not 0 < nivel_elegido < 5:
                    print('No has elegido ningun nivel, intentalo otra vez.\n')
                    break

            else:
                print('No has elegido ningun nivel, intentalo otra vez.\n')
