#escribir una funcion que 8)_calcule el area de un circulo, el parametro: radio,
#luego escribir otra funcion que calcule elvolumen de un cilindro usando la
#primera funcion, parametro:radio y alto

import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    
    Parámetros:
    radio (float): El radio del círculo.
    
    Retorna:
    float: El área del círculo.
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * (radio ** 2)

def calcular_volumen_cilindro(radio, alto):
    """
    Calcula el volumen de un cilindro dado su radio y alto.
    
    Parámetros:
    radio (float): El radio del cilindro.
    alto (float): El alto del cilindro.
    
    Retorna:
    float: El volumen del cilindro.
    """
    if radio < 0 or alto < 0:
        raise ValueError("El radio y el alto no pueden ser negativos")
    area_base = calcular_area_circulo(radio)
    return area_base * alto

def obtener_datos_usuario():
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            if radio < 0:
                print("El radio no puede ser negativo. Por favor, ingrese un valor válido.")
            else:
                break
        except ValueError:
            print("Valor inválido. Por favor, ingrese un número.")

    while True:
        try:
            alto = float(input("Ingrese el alto del cilindro: "))
            if alto < 0:
                print("El alto no puede ser negativo. Por favor, ingrese un valor válido.")
            else:
                break
        except ValueError:
            print("Valor inválido. Por favor, ingrese un número.")

    return radio, alto

def main():
    radio, alto = obtener_datos_usuario()
    area_circulo = calcular_area_circulo(radio)
    volumen_cilindro = calcular_volumen_cilindro(radio, alto)

    print(f"Área del círculo: {area_circulo:.2f}")
    print(f"Volumen del cilindro: {volumen_cilindro:.2f}")

main()
print()
print("final del programa,gracias por utilizar mi codigo")
