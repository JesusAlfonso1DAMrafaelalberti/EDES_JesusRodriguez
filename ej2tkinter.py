import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk   # pip install pillow
import cv2
import threading

# --- Funciones de lógica ---
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

def mostrar_imagen():
    try:
        img = Image.open("rafaelalberti.jpg")   # pon aquí tu archivo
        img = img.resize((300, 200))     # opcional: redimensionar
        img_tk = ImageTk.PhotoImage(img)
        ventana = tk.Toplevel(root)
        ventana.title("Imagen")
        lbl = tk.Label(ventana, image=img_tk)
        lbl.image = img_tk  # evitar que se borre de memoria
        lbl.pack()
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró la imagen.")

def reproducir_video():
    def run_video():
        cap = cv2.VideoCapture("intro anime.mp4")  # pon aquí tu archivo
        if not cap.isOpened():
            messagebox.showerror("Error", "No se pudo abrir el vídeo.")
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Reproducción de video (cierra con Q)", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    # Ejecutar en un hilo aparte para no congelar Tkinter
    threading.Thread(target=run_video).start()

# --- Interfaz gráfica ---
root = tk.Tk()
root.title("Ejercicio 2 - Tkinter con Imagen y Video")

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

# Imagen
frame3 = tk.LabelFrame(root, text="Imagen")
frame3.pack(padx=10, pady=10, fill="x")
tk.Button(frame3, text="Mostrar imagen", command=mostrar_imagen).pack(pady=5)

# Vídeo
frame4 = tk.LabelFrame(root, text="Vídeo")
frame4.pack(padx=10, pady=10, fill="x")
tk.Button(frame4, text="Reproducir vídeo", command=reproducir_video).pack(pady=5)

# Salir
tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

root.mainloop()
