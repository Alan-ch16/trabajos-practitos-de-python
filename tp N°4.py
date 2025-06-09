#3)_Una bacteria se reproduce en un lapso de 1 hora,
#luego de cada hora pasa, cada bacteria se reproduce
#en otra representado en python el usuario ingresa
#las horas que pasan


# Inicializar el número de bacterias
bacterias = 1
#indico el motivo y como funciona
print("Hola estimado usuario, tendra que ingresar una sierta cantidad de hora para saber cuantas bacterias abria, ya que las bacterias se reproducen cada 1 hora")
print()
# Pedir al usuario que ingrese el número de horas
horas = int(input("Ingrese el número de horas: "))

# Simular la reproducción de bacterias durante el número de horas ingresado
for hora in range(1, horas + 1):
    bacterias *= 2  # Cada bacteria se reproduce en otra
    #*=Es un operador de asignacion que se utiliza para multiplicar una variable por un valor y asignar el resultado a la misma variable
    print(f"Hora {hora}: {bacterias} bacterias")

print(f"Después de {horas} horas, hay {bacterias} bacterias.")