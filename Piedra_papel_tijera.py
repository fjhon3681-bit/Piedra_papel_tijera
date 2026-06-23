# Importa la librería random para generar elecciones aleatorias
import random

# Se crea una lista con las opciones posibles del juego
opciones = ["piedra", "papel", "tijera"]

# Solicita al usuario que ingrese una opción
# .lower() convierte el texto a minúsculas para evitar errores
# La función input() permite que el programa reciba datos del usuario por teclado
jugador = input("Elige piedra, papel o tijera: ").lower()

# La computadora selecciona aleatoriamente una opción de la lista
computadora = random.choice(opciones)

# Muestra en pantalla la opción elegida por la computadora
print("La computadora eligió:", computadora)

# IF: Comprueba si el jugador y la computadora eligieron la misma opción
# Si la condición es verdadera, se declara un empate
if jugador == computadora:
    print("Empate")

# ELIF: Se ejecuta si la condición anterior es falsa
# Verifica todas las combinaciones en las que el jugador gana
elif (
    # OR significa "o"
    # Si cualquiera de estas condiciones es verdadera, el jugador gana

    # Piedra gana a tijera
    (jugador == "piedra" and computadora == "tijera")

    or

    # Papel gana a piedra
    (jugador == "papel" and computadora == "piedra")

    or

    # Tijera gana a papel
    (jugador == "tijera" and computadora == "papel")
):
    print("Ganaste")

# ELSE: Se ejecuta cuando ninguna de las condiciones anteriores se cumple
# Esto significa que la computadora ganó la partida
else:
    print("Perdiste")

