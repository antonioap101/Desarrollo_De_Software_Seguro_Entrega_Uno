import threading
import time

# Recursos compartidos
resource_a = threading.Lock()
resource_b = threading.Lock()

def thread_1():
    print("Thread 1: intentando adquirir Resource A...")
    resource_a.acquire()
    print("Thread 1: Resource A adquirido.")
    time.sleep(1)

    print("Thread 1: intentando adquirir Resource B...")
    resource_b.acquire()
    print("Thread 1: Resource B adquirido.")

    # Liberar recursos
    resource_b.release()
    resource_a.release()
    print("Thread 1: recursos liberados.")

def thread_2():
    print("Thread 2: intentando adquirir Resource B...")
    resource_b.acquire()
    print("Thread 2: Resource B adquirido.")
    time.sleep(1)

    print("Thread 2: intentando adquirir Resource A...")
    resource_a.acquire()
    print("Thread 2: Resource A adquirido.")

    # Liberar recursos
    resource_a.release()
    resource_b.release()
    print("Thread 2: recursos liberados.")
if __name__ == "__main__":
    # Creación de hilos
    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)

    # Iniciar hilos
    t1.start()
    t2.start()

    # Esperar a que los hilos terminen
    t1.join()
    t2.join()

    print("Programa finalizado.")
