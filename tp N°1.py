#Utilice la función input y print
#para preguntar el nombre el usuario 
#saludar y luego preguntar el año de 
#nacimiento calcular la edad del usuario

nombre=""
edad=0
edadf=0
año_naci=0
cumplido=""

import datetime

año_actual=datetime.datetime.now().year

print("cual es tu nombre")
nombre=input()

print("cual es su año de nacimiento")
año_naci=int(input())

print("¿ya cumplio años si o no?")
cumplido=input()

if(cumplido=="si"):
    edad=año_actual-año_naci
    print("Hola ",nombre," su edad es: ",edad)

else:
    edad=año_actual-año_naci
    edadf=edad-1
    print("Hola ",nombre," su edad es: ",edadf)