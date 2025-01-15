import json
import bcrypt
from abc import ABC, abstractmethod

# Archivo JSON para almacenar los usuarios
DB_FILE = "db_users.json"

# Clase base Hasher
class Hasher(ABC):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass

    @abstractmethod
    def verify_password(self, password: str, hashed: str) -> bool:
        pass

# Implementación NoHash (Insegura)
class NoHash(Hasher):
    def hash_password(self, password: str) -> str:
        return password  # Sin protección

    def verify_password(self, password: str, hashed: str) -> bool:
        return password == hashed

# Implementación Hash (Segura)
class Hash(Hasher):
    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode())

# Función para cargar/guardar usuarios
def load_users():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"insecure_users": {}, "secure_users": {}}

def save_users(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Registro de usuarios
def register_user(username, password, hasher: Hasher, user_type: str):
    users = load_users()
    if username in users[user_type]:
        print(f"El usuario '{username}' ya existe.")
        return
    hashed_password = hasher.hash_password(password)
    users[user_type][username] = hashed_password
    save_users(users)
    print(f"Usuario '{username}' registrado con exito.")

# Autenticación de usuarios
def authenticate_user(username, password, hasher: Hasher, user_type: str):
    users = load_users()
    if username not in users[user_type]:
        print(f"Usuario '{username}' no encontrado.")
        return
    hashed_password = users[user_type][username]
    if hasher.verify_password(password, hashed_password):
        print(f"Usuario '{username}' autenticado correctamente.")
    else:
        print(f"Fallo de autenticacion para el usuario '{username}'.")

# Eliminación de usuarios
def delete_user(username, user_type: str):
    users = load_users()
    if username in users[user_type]:
        del users[user_type][username]
        save_users(users)
        print(f"Usuario '{username}' eliminado con exito.")
    else:
        print(f"Usuario '{username}' no encontrado.")

# Ejecución de ejemplos
if __name__ == "__main__":
    # Instancias de Hashers
    insecure_hasher = NoHash()
    secure_hasher = Hash()

    # Registro
    print("Registro Inseguro:")
    register_user("user1", "password123", insecure_hasher, "insecure_users")
    print("\nRegistro Seguro:")
    register_user("user2", "password123", secure_hasher, "secure_users")

    # Autenticación
    print("\nAutenticacion Insegura:")
    authenticate_user("user1", "password123", insecure_hasher, "insecure_users")
    print("\nAutenticacion Segura:")
    authenticate_user("user2", "password123", secure_hasher, "secure_users")

    # Eliminación
    print("\nEliminacion de los usuarios creados :")
    # delete_user("user1", "insecure_users")
    # delete_user("user2", "secure_users")
