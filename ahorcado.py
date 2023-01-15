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

        # mostrado estado del ahorado
        print(vidas_diccionario_visual[vidas])

        # mostrar las letras separadas por un espacio
        print(f"Palabra:{' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        # Si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras 
        #que ya se han ingredaso, se añade la letra al conjunto de letras ingresadas.

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.ad(letra_usuario)

        # si la letra esta en la palabra
        # quitar la letra del conjunto de letras pendientes por adivinar 
        # si no esta en la letra quitar una vida.

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\n Tu letra, {letra_usuario} no esta en la palabra")

            # Si la letra es escogida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\n Ya escogista esa letra. Por favor escoge una letra nueva.")
        else:
            print("\n Esta letra no es válida.")

    # El juego llega a esta lénea cuando se avidinan todas las letras de la palabra o cuando se agotan las vidas del jugador. 
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Los siento perdiste. La palabra era {palabra}")
    else: 
        print(f"excelente adivinaste la palabra {palabra}!")

        

