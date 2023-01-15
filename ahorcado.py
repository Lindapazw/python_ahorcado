import random
import string

from palabras import palabras
from vidas import vidas_diccionario_visual

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

    vidas = 7 

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        # mostrar el estado actual de la palabra
        # H - L A
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]  # list comprehension
        print(vidas_diccionario_visual[vidas])
