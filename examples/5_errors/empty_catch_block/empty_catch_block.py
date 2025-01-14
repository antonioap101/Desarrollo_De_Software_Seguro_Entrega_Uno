import os

def insecure_error_handling(file_path):
    """
    Manejo inseguro: Bloque de captura vacío.
    """
    try:
        # Intentar leer un archivo inexistente
        with open(file_path, 'r') as file:
            print(file.read())
    except Exception as e:
        # Bloque vacío: No se maneja el error
        pass

def secure_error_handling(file_path):
    """
    Manejo seguro: Gestión explícita de errores.
    """
    try:
        # Intentar leer un archivo inexistente
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError as e:
        print(f"Error: El archivo '{file_path}' no existe. Detalles: {e}")
    except PermissionError as e:
        print(f"Error: No tienes permisos para leer '{file_path}'. Detalles: {e}")
    except Exception as e:
        print(f"Error inesperado al acceder al archivo. Detalles: {e}")

if __name__ == "__main__":
    # Archivo inexistente
    file_path = "non_existent_file.txt"

    # Manejo seguro de errores
    print("\nEjemplo con manejo seguro:")
    secure_error_handling(file_path)

    # Manejo inseguro de errores
    print("Ejemplo con manejo inseguro:")
    insecure_error_handling(file_path)

