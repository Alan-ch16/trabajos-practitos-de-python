#5)_El profe tiene X caramelos para repartir entre Y 
#de estudiantes.Los estudiantes deben recibir un 
#número entero de caramelo.Preguntar al usuario 
#cuántos caramelos se reparten entre cuantos 
#estudiantes y luego indicar cuantos le tocan a 
#cada estudiante y cuantos sobran en la bolsa

# Pedir al usuario que ingrese el número de caramelos y estudiantes
caramelos = int(input("Ingrese el número que quiere repartir de caramelos: "))
print()
estudiantes = int(input("Ingrese el número de estudiantes a los que se le repartiran los caramelos: "))

# Calcular el número de caramelos que le tocan a cada estudiante
caramelos_por_estudiante = caramelos // estudiantes

# Calcular el número de caramelos que sobran
caramelos_sobrantes = caramelos % estudiantes

# Imprimir los resultados
print()
print(f"Cada estudiante recibe {caramelos_por_estudiante} caramelos.")
print()
print(f"Sobran {caramelos_sobrantes} caramelos en la bolsa.")