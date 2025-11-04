import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import vlc
import time
import threading

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
        img = Image.open("rafaelalberti.jpg")
        img = img.resize((300, 200))
        img_tk = ImageTk.PhotoImage(img)
        ventana = tk.Toplevel(root)
        ventana.title("Imagen")
        lbl = tk.Label(ventana, image=img_tk)
        lbl.image = img_tk
        lbl.pack()
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró la imagen.")

def reproducir_video_externo():
    try:
        webbrowser.open("intro anime slayers.mp4")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el vídeo: {e}")

def reproducir_video_vlc():
    def run_vlc():
        try:
            player = vlc.MediaPlayer("intro anime slayers.mp4")
            player.play()
            time.sleep(90)  # ajusta según la duración del vídeo
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo reproducir con VLC: {e}")
    threading.Thread(target=run_vlc).start()

# --- Interfaz gráfica ---
root = tk.Tk()
root.title("Ejercicio 2 - Tkinter con Imagen y Video")

# Conversión
frame1 = tk.LabelFrame(root, text="Conversión de temperatura")
frame1.pack(padx=10, pady=10, fill="x")
tk.Label(frame1, text="Grados Celsius:").pack(side="left", padx=5)
entry_temp = tk.Entry(frame1)
entry_temp.pack(side="left", padx=5)
tk.Button(frame1, text="Convertir", command=convertir_temperatura).pack(side="left", padx=5)

# Tabla
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

# Vídeo externo
frame4 = tk.LabelFrame(root, text="Vídeo (reproductor externo)")
frame4.pack(padx=10, pady=10, fill="x")
tk.Button(frame4, text="Abrir en reproductor externo", command=reproducir_video_externo).pack(pady=5)

# Vídeo VLC
frame5 = tk.LabelFrame(root, text="Vídeo (VLC)")
frame5.pack(padx=10, pady=10, fill="x")
tk.Button(frame5, text="Reproducir con VLC", command=reproducir_video_vlc).pack(pady=5)

# Salir
tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

root.mainloop()
