import random
import string

from palabras import palabras

def obtener_palabra(palabras):
    # seleccionar una palabra de la lista de palabras válidas
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra: 
        palabra = random.choice(palabras)
    
    return palabra.upper()

def ahorcado():

    print("****************")
    print("***bienvenido***")
    print("****************")

    palabra = obtener_palabra(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set() 
    abecedario = set(string.ascii_uppercase)