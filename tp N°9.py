#9)_escribir una funcion  que calcule el total de una 
#factura tras aplicarle la IVA. Funcion debe recibir el 
#importe sin IVA y el porcentaje de IVA a aplicar. 
#Si se invoca la funcion sin pasar el porcentaje del IVA, 
#debera aplicar el 21%

def calcular_total(importe, iva=21):
 return importe + (importe * iva / 100)

# funcion para validar que sea numero lo ingresado por el usuario
def obtener_numero(mensaje):
 while True:
     try:
         return float(input(mensaje))
         except ValueError:
             print("Por favor, ingrese un número válido.")

# Pido al usuario que ingrese el importe sin IVA
importe = obtener_numero("Ingrese el importe sin IVA: ")

# Calculo y mostrar el total con IVA (por defecto 21%)
print(f"Total con IVA (21%): {calcular_total(importe):.2f}")

# pido al usuario que ingrese el porcentaje de IVA
iva = obtener_numero("Ingrese el porcentaje de IVA (opcional, ingrese 0 para terminar): ")

# Si el usuario ingresa un porcentaje de IVA, calculo y muestro el total con el IVA que ingreso
if iva != 0:
 print(f"Total con IVA ({iva}%): {calcular_total(importe, iva):.2f}")