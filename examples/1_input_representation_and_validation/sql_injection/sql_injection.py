import sqlite3

def create_demo_db():
    """
    Crea una base de datos de demostración con una tabla de usuarios.
    """
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'user123')")
    connection.commit()
    connection.close()


def insecure_authenticate(username, password):
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    # Consulta insegura
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Ejecutando consulta insegura:", query)
    cursor.execute(query)
    result = cursor.fetchall()
    print("Resultado de la consulta:", result)
    connection.close()
    if result:
        print("Autenticación exitosa (consulta insegura).")
    else:
        print("Autenticación fallida (consulta insegura).")


def secure_authenticate(username, password):
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    # Consulta segura
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print("Ejecutando consulta segura:", query)
    cursor.execute(query, (username, password))
    result = cursor.fetchall()
    print("Resultado de la consulta:", result)
    connection.close()
    if result:
        print("Autenticación exitosa (consulta segura).")
    else:
        print("Autenticación fallida (consulta segura).")


if __name__ == "__main__":
    create_demo_db()
    print("-----------------------Consulta insegura-----------------------")
    insecure_authenticate("admin'--", "irrelevant_password")
    print("-----------------------Consulta segura-----------------------")
    secure_authenticate("admin'--", "irrelevant_password")
