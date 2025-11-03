def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32


def tabla_multiplicar(numero: int):
    """Muestra la tabla de multiplicar del 1 al 10"""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1) Conversión de temperatura")
        print("2) Tabla de multiplicar")
        print("3) Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                celsius = float(input("Introduce grados Celsius: "))
                fahrenheit = celsius_a_fahrenheit(celsius)
                print(f"{celsius} ºC = {fahrenheit:.2f} ºF")
            except ValueError:
                print("Valor no válido. Debes introducir un número.")
        
        elif opcion == "2":
            try:
                numero = int(input("Introduce un número entero: "))
                tabla_multiplicar(numero)
            except ValueError:
                print("Valor no válido. Debes introducir un número entero.")
        
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")


# Programa principal
if __name__ == "__main__":
    menu()
