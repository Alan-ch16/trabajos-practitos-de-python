#10)_uncion que devuelva el factorial de el numero entero 
#ingresado como parametro diseñar una funcio

def factorial(n):
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Pedir al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Calcular y imprimir el factorial
try:
    print(f"El factorial de {n} es: {factorial(n)}")
except ValueError as e:
    print(e)