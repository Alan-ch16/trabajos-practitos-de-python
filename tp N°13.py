#ejercicio 13
#declarar una matriz de 4 filas y 4 columnas con numeros enteros sucesivos a partir de 1 en cada celda. calcular la suma y la multiplicacion de los elementos de la diagonal principal y la contra diagonal. mostrar en pantalla estos balores y los elementos de la matriz

# Crear matriz 4x4 con números consecutivos automáticamente
matriz = [] # la lista vacia para guardar la matriz
contador = 1 # numero principal que lo usare para llenar las columnas

for i in range(4):          # recorre las filas
    fila = []
    for j in range(4):      # recorre las columnas
        fila.append(contador)   # Coloco el numero actual
        contador += 1           # le sumo 1 para el numero siguiente
    matriz.append(fila)     # agrego la fila a la matriz

# muestro la matriz de 4x4
print("Matriz 4x4 generada automáticamente:")
for fila in matriz:# recoro las filas
    print(fila)

# en estas variables almaceno los resultados de las diagonales
suma_diagonal_principal = 0# la suma empieza en 0 porque sumamos
prod_diagonal_principal = 1# el producto empieza en 1 porque multiplicamos
suma_diagonal_contra = 0
prod_diagonal_contra = 1
# Calcular diagonales
for i in range(4):# usamos el for que recorre las 4 posiciones diagonales.
    suma_diagonal_principal += matriz[i][i]# fila = columna → matriz[i][i]
    prod_diagonal_principal *= matriz[i][i]
    suma_diagonal_contra += matriz[i][3-i]# fila + columna = tamaño - 1 → matriz[i][3-i]
    prod_diagonal_contra *= matriz[i][3-i]

# muestro los resultados
print("\nDiagonal principal:")# \n sirve para dejar una línea en blanco.
#Se muestran los resultados finales de suma y producto
print("Suma =", suma_diagonal_principal)
print("Producto =", prod_diagonal_principal)
#Se muestran los resultados finales de suma y producto
print("\nContra diagonal:")
print("Suma =", suma_diagonal_contra)
print("Producto =", prod_diagonal_contra)

