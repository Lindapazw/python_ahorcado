import random

from palabras import palabras

def obtener_palabra(palabras):
    # seleccionar una palabra de la lista de palabras válidas
    palabra = random.choice(palabras)

def ahorcado():

    print("****************")
    print("***bienvenido***")
    print("****************")

    palabra = obtener_palabra(palabras)