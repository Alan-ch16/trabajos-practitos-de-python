#6)_Un cajero automatico entrega solo billetes de 
#1000 y de 200. Ingresar la cantidad que desea 
#extraer el usuario, y luego indicar cuantos 
#billetes de 1000 y de 200 se le entregan al 
#cliente.indicar ademas el saldoque no se pudo 
#extraer por que no hay billetes



# Pedir al usuario que ingrese la cantidad que desea extraer
cantidad = int(input("Ingrese la cantidad que desea extraer de plata: "))

# Calcular el número de billetes de 1000
billetes_1000 = cantidad // 1000

# Calcular el resto después de entregar billetes de 1000
resto = cantidad % 1000

# Calcular el número de billetes de 200
billetes_200 = resto // 200

# Calcular el resto después de entregar billetes de 200 (saldo no extraído)
saldo_no_extraido = resto % 200

# Imprimir los resultados
print()
print(f"Billetes de 1000: {billetes_1000}")
print()
print(f"Billetes de 200: {billetes_200}")
print()
print(f"Saldo no extraído: {saldo_no_extraido}")