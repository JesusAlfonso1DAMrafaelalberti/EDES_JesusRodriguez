import tkinter as tk
from tkinter import messagebox


def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32


def convertir_temperatura():
    try:
        celsius = float(entry_temp.get())
        fahrenheit = celsius_a_fahrenheit(celsius)
        messagebox.showinfo("Resultado", f"{celsius} ºC = {fahrenheit:.2f} ºF")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido.")


def mostrar_tabla():
    try:
        numero = int(entry_tabla.get())
        resultado = "\n".join([f"{numero} x {i} = {numero * i}" for i in range(1, 11)])
        messagebox.showinfo("Tabla de multiplicar", resultado)
    except ValueError:
        messagebox.showerror("Error", "Introduce un número entero válido.")


# Ventana principal
root = tk.Tk()
root.title("Ejercicio Python - Menú")

# Conversión de temperatura
frame1 = tk.LabelFrame(root, text="Conversión de temperatura")
frame1.pack(padx=10, pady=10, fill="x")

tk.Label(frame1, text="Grados Celsius:").pack(side="left", padx=5)
entry_temp = tk.Entry(frame1)
entry_temp.pack(side="left", padx=5)
tk.Button(frame1, text="Convertir", command=convertir_temperatura).pack(side="left", padx=5)

# Tabla de multiplicar
frame2 = tk.LabelFrame(root, text="Tabla de multiplicar")
frame2.pack(padx=10, pady=10, fill="x")

tk.Label(frame2, text="Número:").pack(side="left", padx=5)
entry_tabla = tk.Entry(frame2)
entry_tabla.pack(side="left", padx=5)
tk.Button(frame2, text="Mostrar tabla", command=mostrar_tabla).pack(side="left", padx=5)

# Botón salir
tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

root.mainloop()
