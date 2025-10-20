#ejercicio 18
#adaptar el programa "Adivina el numero" con interfaz grafica, una vez probado convertirlo a un archivo ejecutable.

import tkinter as tk
from tkinter import messagebox
import random

class AdivinaNumeroGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el Número")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Variables del juego
        self.numero_secreto = 0
        self.intentos = 6
        
        # Crear elementos de la interfaz
        self.crear_interfaz()
        
        # Iniciar un nuevo juego
        self.nuevo_juego()
    
    def crear_interfaz(self):
        # Título
        self.titulo_label = tk.Label(self.root, text="Adivina el Número", font=("Arial", 16, "bold"))
        self.titulo_label.pack(pady=10)
        
        # Instrucciones
        self.instrucciones_label = tk.Label(self.root, text="Adivina el número secreto entre 1 y 20")
        self.instrucciones_label.pack(pady=5)
        
        # Frame para los intentos
        self.intentos_frame = tk.Frame(self.root)
        self.intentos_frame.pack(pady=10)
        
        self.intentos_label = tk.Label(self.intentos_frame, text="Vidas restantes: ", font=("Arial", 12))
        self.intentos_label.pack(side=tk.LEFT)
        
        self.vidas_label = tk.Label(self.intentos_frame, text="6", font=("Arial", 12, "bold"), fg="green")
        self.vidas_label.pack(side=tk.LEFT)
        
        # Frame para la entrada
        self.entrada_frame = tk.Frame(self.root)
        self.entrada_frame.pack(pady=10)
        
        self.numero_label = tk.Label(self.entrada_frame, text="Ingresa un Número: ")
        self.numero_label.pack(side=tk.LEFT)
        
        self.numero_entry = tk.Entry(self.entrada_frame, width=10)
        self.numero_entry.pack(side=tk.LEFT, padx=5)
        self.numero_entry.bind("<Return>", lambda event: self.verificar_numero())
        
        # Botón para verificar
        self.verificar_button = tk.Button(self.root, text="Comprobar", command=self.verificar_numero)
        self.verificar_button.pack(pady=5)
        
        # Mensaje
        self.mensaje_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.mensaje_label.pack(pady=10)
        
        # Botón para nuevo juego
        self.nuevo_juego_button = tk.Button(self.root, text="Jugar otras ves", command=self.nuevo_juego)
        self.nuevo_juego_button.pack(pady=5)
    
    def nuevo_juego(self):
        # Generar nuevo número secreto
        self.numero_secreto = random.randint(1, 20)
        
        # Reiniciar intentos
        self.intentos = 6
        self.vidas_label.config(text=str(self.intentos), fg="green")
        
        # Limpiar entrada y mensaje
        self.numero_entry.delete(0, tk.END)
        self.mensaje_label.config(text="")
        
        # Habilitar entrada y botón
        self.numero_entry.config(state=tk.NORMAL)
        self.verificar_button.config(state=tk.NORMAL)
        
        # Poner foco en la entrada
        self.numero_entry.focus()
    
    def verificar_numero(self):
        try:
            # Obtener número ingresado
            numero_ingresado = int(self.numero_entry.get())
            
            # Verificar si el número está en el rango válido
            if numero_ingresado < 1 or numero_ingresado > 20:
                self.mensaje_label.config(text="El número debe estar entre 1 y 20", fg="red")
                return
            
            # Verificar si adivinó el número
            if numero_ingresado == self.numero_secreto:
                self.mensaje_label.config(text=f"¡Felicidades! Adivinaste el número {self.numero_secreto}", fg="green")
                self.numero_entry.config(state=tk.DISABLED)
                self.verificar_button.config(state=tk.DISABLED)
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades! Adivinaste el número {self.numero_secreto}")
            else:
                # Indicar si el número es mayor o menor
                if numero_ingresado < self.numero_secreto:
                    self.mensaje_label.config(text=f"El número secreto es mayor que {numero_ingresado}", fg="blue")
                else:
                    self.mensaje_label.config(text=f"El número secreto es menor que {numero_ingresado}", fg="blue")
                
                # Reducir intentos
                self.intentos -= 1
                self.vidas_label.config(text=str(self.intentos))
                
                # Cambiar color según los intentos restantes
                if self.intentos <= 2:
                    self.vidas_label.config(fg="red")
                elif self.intentos <= 4:
                    self.vidas_label.config(fg="orange")
                
                # Verificar si se agotaron los intentos
                if self.intentos == 0:
                    self.mensaje_label.config(text=f"¡Perdiste! El número secreto era {self.numero_secreto}", fg="red")
                    self.numero_entry.config(state=tk.DISABLED)
                    self.verificar_button.config(state=tk.DISABLED)
                    messagebox.showinfo("¡Perdiste!", f"¡Lo siento! Has agotado todos los intentos. El número secreto era {self.numero_secreto}")
            
            # Limpiar entrada
            self.numero_entry.delete(0, tk.END)
            self.numero_entry.focus()
            
        except ValueError:
            self.mensaje_label.config(text="Por favor ingresa un número válido", fg="red")
            self.numero_entry.delete(0, tk.END)
            self.numero_entry.focus()

# Crear la ventana principal
root = tk.Tk()
app = AdivinaNumeroGUI(root)
root.mainloop()