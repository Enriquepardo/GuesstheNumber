import random
import sys
from Modulo_menu import numintentos_max


intentos = 0

# con esta funcion hago que el jugador entre en un bucle hasta que elija un nivel valido del juego.

def jugar_nivel_elegido():
    eleccion_nivel = int(input('Elige el nivel que quieres jugar: '))
    while eleccion_nivel != [1, 2, 3, 4, 5]:
        print('No has elegido ningun nivel, prueba a introducir otra vez.')
        return eleccion_nivel
        

# defino el corazon del juego

def juego(nivel_elegido):
    num_minimo = 0
    if nivel_elegido == 1:
        numero = random.randint (0, 100)
        maximo = 100 
        numintentos_max = 15
        orden = 'Elige un número entre 0 y 100.'
        diferencia = numero - 10
    elif nivel_elegido == 2:
        numero = random.randint (0, 1000)
        maximo = 1000
        numintentos_max = 10
        orden = 'Elige un número entre 0 y 1.000.'
        diferencia = numero - 100
    elif nivel_elegido == 3:
        numero = random.randint (0, 1000000)
        maximo = 1000000
        intentos_max = 5
        orden = 'Elige un número entre 0 y 1.000.000. '  
        diferencia = numero - 1000
    elif nivel_elegido == 4:
        numero = random.randint (0, 1000000000000)
        maximo = 1000000000000
        numintentos_max = 3
        orden = 'Elige un número entre 0 y 1.000.000.000.000.'
        diferencia = numero - 1000000
    while intentos < intentos_max:
        
        numero_jugador = int(input(orden))
        if abs(numero_jugador)>0:
            if numero_jugador!=numero:
                if (abs(numero_jugador))< diferencia:
                    print("Vas muy bien, te estas acercando.")
                else:
                    print("Vas muy bien, te esats acercando.")
                    repeticiones = 1
            else:
                repesticiones += 1
                print("HAS INTRODUCIDO EL MISMO NÚMERO ",repeticiones," VECES SEGUIDAS...")
                
    intentos += 1
    if intentos < intentos_max:
        if numero == numero_jugador:
            print(f'¡¡¡Felicidades, has ganado!!! has necesitado ', intentos, ' intetnos')

        elif numero < numero_jugador:
            print(f'Has fallado, demasiado grande vuelve a intentarlo.\n Llevas ',intentos,' intentos.')
        elif numero > numero_jugador:
            print(f'Has fallado, demasiado pequeño vuelve a intentarlo.\n Llevas ',intentos,' intentos.')
        else: 
            print()


