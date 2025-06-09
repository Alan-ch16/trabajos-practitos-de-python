#CONVERTIR EN DECIMAL_BINARIO_HEXADECIMAL
#Diseñar un programa que muestre el numero ingresado por el
#usuario en sistema decimal, binerio y hexadecimal

def convertir_numero(numero):
    print(f"Decimal: {numero}")
    print(f"Binario: {bin(numero)}")
    print(f"Hexadecimal: {hex(numero)}")

numero = int(input("Ingrese un número: "))
convertir_numero(numero)
