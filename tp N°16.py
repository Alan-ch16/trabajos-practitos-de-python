# ejercicio 15
# importar en python una imagen y almacenarla en una matriz.implementar una funcion para rotar la imagen.
# preguntar al usuario si quiere rotar 90 grados hacia la izquierda o hacia la derecha a 180 grados mostrar
# la imagen original y la rotada

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

# la ruta de la imagen
ruta = r"C:\Users\NET USO ESCOLAR 136\Pictures\imagen de prueba\imagen de robot.jpeg"

# Cargo la imagen y la convierto a escala de grises si se desea (opcional)
# Si quieres conservar colores, comenta .convert("L")
try:
    imagen = Image.open(ruta).convert("L")  # "L" = escala de grises
except FileNotFoundError:
    raise SystemExit(f"No se encontró la imagen en la ruta: {ruta}")
except PermissionError:
    raise SystemExit("Permisos denegados para abrir la imagen.")
except Exception as e:
    raise SystemExit(f"Error al abrir la imagen: {e}")

# Convierto a matriz NumPy
matriz_original = np.array(imagen)

# funcion para rotar la imagen 
def rotar_matriz(matriz, angulo_grados):
    if angulo_grados % 90 != 0:
        raise ValueError("Este rotador soporta sólo rotaciones en múltiplos de 90 grados.")
    k = (angulo_grados // 90) % 4
    # Usamos NumPy para rotar: rot90 rota counterclockwise; para clockwise invertimos signo
    # rot90 con k=1 => 90° CCW; para obtener CW, usamos -k
    rotada = np.rot90(matriz, k=-k)
    return rotada

# Pido al usuario el tipo de rotación
print("Elige rotación:")
print("  1) 90° a la izquierda ")
print("  2) 90° a la derecha ")
print("  3) 180°")
opcion = input("Ingresa 1, 2 o 3: ").strip()

end_action = None
if opcion == "1":
    angulo = -90  # 90° a la izquierda es CCW
elif opcion == "2":
    angulo = 90   # 90° a la derecha es CW
elif opcion == "3":
    angulo = 180
else:
    raise SystemExit("Entrada no válida. Ingresa 1, 2 o 3.")

# Realizo la rotación
matriz_rotada = rotar_matriz(matriz_original, angulo)

# Muestro la imágenes: original y rotada
plt.figure(figsize=(8, 4))

# imagen original
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(matriz_original, cmap="gray", vmin=0, vmax=255)
plt.axis("off")

# imagen rotada
plt.subplot(1, 2, 2)
plt.title(f"Rotada ({'90° Izquierda' if angulo==-90 else '90° derecha' if angulo==90 else '180°'})")
plt.imshow(matriz_rotada, cmap="gray", vmin=0, vmax=255)
plt.axis("off")

plt.tight_layout()
plt.show()