import tkinter as tk
import time

# Logica del temporizador
def temporizador():
    try:
        segundos = int(entry.get())  # Obtener los segundos ingresados
    except ValueError:
        tiempo_restante.set("Por favor ingresa un número válido")
        return

    def actualizar_reloj():
        nonlocal segundos
        if segundos > 0:
            mins = segundos // 60
            secs = segundos % 60
            tiempo_restante.set(f"{mins:02d}:{secs:02d}")
            segundos -= 1
            ventana.after(1000, actualizar_reloj)  # Actualizar cada segundo
        else:
            tiempo_restante.set("¡Tiempo finalizado!")

    actualizar_reloj()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Temporizador Digital")
ventana.configure(bg="black")  # Fondo negro

# Estilo de la etiqueta de tiempo con un marco similar al de un reloj digital
tiempo_restante = tk.StringVar()
tiempo_restante.set("00:00")

# Crear un marco con bordes redondeados
marco_reloj = tk.Frame(ventana, bg="black", bd=10, relief="solid", padx=20, pady=20)
marco_reloj.pack(pady=50)

# Agregar el reloj dentro del marco
etiqueta = tk.Label(marco_reloj, textvariable=tiempo_restante, font=("Arial", 60, "bold"), fg="green", bg="black", width=8, height=2)
etiqueta.pack()

# Caja de entrada para ingresar los segundos con bordes redondeados
entry_label = tk.Label(ventana, text="Ingresa los segundos:", font=("Helvetica", 16), fg="white", bg="black")
entry_label.pack()

entry = tk.Entry(ventana, font=("Helvetica", 18), bd=5, relief="flat", width=10, justify="center", fg="black", bg="white")
entry.pack(pady=10)

# Botón con bordes redondeados y sombra para hacerlo más moderno
boton_iniciar = tk.Button(ventana, text="Iniciar Temporizador", font=("Helvetica", 18), command=temporizador, fg="white", bg="#8B0000", bd=0, relief="flat", padx=20, pady=10)
boton_iniciar.pack(pady=20)

# Efecto hover en el botón (cuando el ratón pasa sobre el botón)
def on_enter(event):
    boton_iniciar.config(bg="#C00B0B")

def on_leave(event):
    boton_iniciar.config(bg="#8B0000")

boton_iniciar.bind("<Enter>", on_enter)
boton_iniciar.bind("<Leave>", on_leave)

# Ejecutar la interfaz
ventana.mainloop()
