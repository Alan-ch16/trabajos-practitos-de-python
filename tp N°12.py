#ejercicio 12
#inplementar en python una funcion para aplicar sifrado cesar a una cadena. Debe pasar el mensaje y el desplamiento como parametros.
#La misma funcion debe decifrar el mensaje si se aplica un desplazamiento negativo. ayuda:Usar la funcion ord() y chr

def cifrado_cesar_sencillo(mensaje: str, desplazamiento: int) -> str:
    
    resultado = []

    for ch in mensaje:
        if 'A' <= ch <= 'Z':
            base = ord('A')
            nuevo_orden = (ord(ch) - base + desplazamiento) % 26
            resultado.append(chr(base + nuevo_orden))
        elif 'a' <= ch <= 'z':
            base = ord('a')
            nuevo_orden = (ord(ch) - base + desplazamiento) % 26
            resultado.append(chr(base + nuevo_orden))
        else:
            resultado.append(ch)

    return ''.join(resultado)

# Interfaz simple para el usuario
if __name__ == "__main__":
    texto = input("Escribe el texto a cifrar/descifrar: ")
    try:
        despl = int(input("Desplazamiento (positivo para cifrar, negativo para descifrar): "))
    except ValueError:
        print("Debes ingresar un número entero para el desplazamiento.")
        raise SystemExit(1)

    resultado = cifrado_cesar_sencillo(texto, despl)
    print("Resultado:", resultado)