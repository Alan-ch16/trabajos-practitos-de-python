#Ejercicio 11_Sorteo
#Los estudiantes deben pasar al frente a exponer, pero nadie quiere pasar primero.
#Diseñar un programa con una lista con los nombres de los estudiantes, y de formaaleatoria generar otra lista que indique
#el orden en el que deben pasar a exponer.
#Ayuda:Usar bucle for in range(len(estudiantes)):
#Ayuda:Para añadir un elemento a una lista se puede usar el metodo append().
#no se puede usar la funcion shuffle() pq realiza todo lo que pide el programa.


import random

#La lista de estudiantes
estudiantes = ["juan", "antonio", "gabriela", "liliana", "lucila", "alan"]

#orden hecho manualmente con append
orden = []
usados = [False] * len(estudiantes)

for _ in range(len(estudiantes)):
    # Elege el índice alazar entre los que no an sido usados
    while True:
        idx = random.randrange(len(estudiantes))
        if not usados[idx]:
            break
    orden.append(estudiantes[idx])
    usados[idx] = True

print("Orden para exponer:", orden)