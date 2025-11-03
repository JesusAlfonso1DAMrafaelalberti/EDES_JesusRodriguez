import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

def tabla_multiplicar(numero: int):
    """Muestra la tabla de multiplicar del 1 al 10"""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def mostrar_imagen():
    """Muestra una imagen en una ventana usando matplotlib"""
    try:
        img = mpimg.imread("rafaelalberti.jpg")  # pon aquí tu archivo
        plt.imshow(img)
        plt.axis("off")
        plt.show()
    except FileNotFoundError:
        print("No se encontró la imagen. Asegúrate de que está en la misma carpeta que el programa.")

def reproducir_video():
    """Reproduce un vídeo en una ventana usando OpenCV"""
    try:
        cap = cv2.VideoCapture("intro anime.mp4")  # pon aquí tu archivo

        if not cap.isOpened():
            print("No se pudo abrir el vídeo.")
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Reproducción de video", frame)

            # salir con la tecla q
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error al reproducir el vídeo: {e}")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1) Conversión de temperatura")
        print("2) Tabla de multiplicar")
        print("3) Mostrar imagen")
        print("4) Reproducir vídeo")
        print("5) Salir")

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
            reproducir_video()
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
