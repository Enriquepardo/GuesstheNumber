from Modulo_menu import *
from Modulo_juego import *      # me da fallo aqui 
from Modulo_puntuacion import *


# aqui importo todos los modulos para que se unan y se ejecute el juego completo
def jugar_juego_completo():
    bienvenida()
    eleccion_menu()
    jugar_nivel_elegido()
    juego()
    tabla_de_puntuacion()
    
    
if __name__ == '__main__':
    print("Se ha ejecutado el juego")
    jugar_juego_completo()
