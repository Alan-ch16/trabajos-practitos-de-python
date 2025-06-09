#Ejercicio 2) adivina el número 
#Diseñar un programa que genere un número 
#aleatorio entre 1 y 20
#El jugador tiene 6 intentos para adivinar
#el número. En cada intento indicar si el 
#número secreto es mayor o menor al ingresado, 
#si es igual el jugador gana

import random

# Generar el numero secreto entre 1 y 20
numero_secreto = random.randint(1, 20)

# indico los intentos iniciales
intentos = 6

print("¡Bienvenido al juego 'Adivina el número'!")
print()
print("Tienes 6 intentos para adivinar el número secreto entre 1 y 20.")
print()
while intentos > 0:
    # Pido al usuario que ingrese un número
    numero_ingresado = int(input("Ingrese un número: "))

    # Verificar si el número ingresado es válido
    if numero_ingresado < 1 or numero_ingresado > 20:
        print("El número ingresado debe estar entre 1 y 20.")
        continue
    #continue salta a la sigiente interaccion del bucle
    # Verificar si el número ingresado es igual al número secreto
    if numero_ingresado == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto")
        break
    #break sale del bucle inmediatamente
    # Indicar si el número secreto es mayor o menor al ingresado
    elif numero_ingresado < numero_secreto:
        print("El número secreto es mayor que", numero_ingresado)
    else:
        print("El número secreto es menor que", numero_ingresado)

    # Decrementar el número de intentos
    intentos -= 1
    #-= resta un valor de una variable y asigna el resultado a la misma variable
    print("Te quedan", intentos, "intentos.")

# Verificar si el jugador ha agotado todos los intentos
if intentos == 0:
    print("¡Lo siento! Has agotado todos los intentos.")
    print("El número secreto era", numero_secreto)