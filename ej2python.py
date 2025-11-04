import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import webbrowser
import vlc
import time

def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def tabla_multiplicar(numero: int):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def mostrar_imagen():
    try:
        img = mpimg.imread("rafaelalberti.jpg")
        plt.imshow(img)
        plt.axis("off")
        plt.show()
    except FileNotFoundError:
        print("No se encontró la imagen.")

def reproducir_video_externo():
    """Abrir vídeo con el reproductor predeterminado (con sonido)."""
    try:
        webbrowser.open("intro anime slayers.mp4")
    except Exception as e:
        print(f"Error al abrir el vídeo: {e}")

def reproducir_video_vlc():
    """Reproducir vídeo con VLC (con sonido)."""
    try:
        player = vlc.MediaPlayer("video.mp4")
        player.play()
        # Mantener el programa vivo mientras se reproduce
        time.sleep(90)  # ajusta según la duración del vídeo
    except Exception as e:
        print(f"Error al reproducir con VLC: {e}")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1) Conversión de temperatura")
        print("2) Tabla de multiplicar")
        print("3) Mostrar imagen")
        print("4) Reproducir vídeo (reproductor externo)")
        print("5) Reproducir vídeo (VLC)")
        print("6) Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                celsius = float(input("Introduce grados Celsius: "))
                fahrenheit = celsius_a_fahrenheit(celsius)
                print(f"{celsius} ºC = {fahrenheit:.2f} ºF")
            except ValueError:
                print("Valor no válido.")
        
        elif opcion == "2":
            try:
                numero = int(input("Introduce un número entero: "))
                tabla_multiplicar(numero)
            except ValueError:
                print("Valor no válido.")
        
        elif opcion == "3":
            mostrar_imagen()
        
        elif opcion == "4":
            reproducir_video_externo()
        
        elif opcion == "5":
            reproducir_video_vlc()
        
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
