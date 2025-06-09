#7)_Diseñar un programa que pida la fecha de 
#nacimiento del usuario y indicar en 2 formatos: 
#edad total en dias y edad en año, meses y dias


from datetime import datetime

# Pedir al usuario que ingrese su fecha de nacimiento
fecha_nacimiento = input("Ingrese su fecha de nacimiento (en forma dd/mm/aaaa): ")
dia, mes, anio = map(int, fecha_nacimiento.split('/'))

# Convertir la fecha de nacimiento a un objeto datetime
fecha_nacimiento = datetime(anio, mes, dia)

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular la edad en días
edad_dias = (fecha_actual - fecha_nacimiento).days

# Calcular la edad en años, meses y días
edad_anos = edad_dias // 365
edad_meses = (edad_dias % 365) // 30
edad_dias_restantes = (edad_dias % 365) % 30

# Imprimir los resultados
print()
print(f"Edad total en días: {edad_dias} días")
print()
print(f"Edad en años, meses y días: {edad_anos} años, {edad_meses} meses y {edad_dias_restantes} días")