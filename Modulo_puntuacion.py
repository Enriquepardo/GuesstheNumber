from Modulo_menu import nombre
from Modulo_juego import intentos



# aqui defino la tabla de puntuaciones que se muestra al final del juego 

def tabla_de_puntuacion(nivel_elegido):
    if nivel_elegido == 1:
        puntos = 100 - (intentos -1)*2
        print(f'{nombre} has obtenido {puntos} puntos.')
    elif nivel_elegido == 2:
        puntos = 500 - (intentos -1)*3
        print(f'{nombre} has obtenido {puntos} puntos.')
    elif nivel_elegido == 3:
        puntos = 1000 - (intentos -1)*4
        print(f'{nombre} has obtenido {puntos} puntos.')
    elif nivel_elegido == 4:
        puntos = 1000 - (intentos -1)*5
        print(f'{nombre} has obtenido {puntos} puntos.')
    

