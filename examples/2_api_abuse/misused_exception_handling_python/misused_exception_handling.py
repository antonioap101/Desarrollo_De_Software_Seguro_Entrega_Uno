import os


def read_file_without_proper_handling(filename):
    """
    Ejemplo de manejo incorrecto de excepciones.
    """
    with open(filename, 'r') as file:
        content = file.read()
        print("Contenido del archivo:\n", content)


def read_file_with_proper_handling(filename):
    """
    Ejemplo de manejo adecuado de excepciones.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"El archivo '{filename}' no existe.")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Contenido del archivo:\n", content)
    except FileNotFoundError as e:
        print("Error: Archivo no encontrado.", e)
        # Se puede tomar una acción específica aquí, como registrar el error.
    except PermissionError as e:
        print("Error: No tienes permisos para leer el archivo.", e)
    except Exception as e:
        print("Error inesperado:", e)
        # Se podría registrar el error o tomar otra acción según sea necesario.


# Ejecución del ejemplo
if __name__ == "__main__":
    # Ejemplo con manejo incorrecto
    print("\nEjemplo: Manejo Adecuado de Excepciones")
    try:
        read_file_with_proper_handling("archivo_inexistente.txt")
    except FileNotFoundError as e:
        print("El archivo no existe y no se gestionó la excepción en la función.")


    print("Ejemplo: Manejo Incorrecto de Excepciones")
    read_file_without_proper_handling("archivo_inexistente.txt")

