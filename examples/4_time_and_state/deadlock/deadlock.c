#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Recursos compartidos
pthread_mutex_t resource_a;
pthread_mutex_t resource_b;

void *thread_1(void *arg) {
    printf("Thread 1: intentando adquirir Resource A...\n");
    pthread_mutex_lock(&resource_a);
    printf("Thread 1: Resource A adquirido.\n");
    sleep(1);

    printf("Thread 1: intentando adquirir Resource B...\n");
    pthread_mutex_lock(&resource_b);
    printf("Thread 1: Resource B adquirido.\n");

    // Liberar recursos
    pthread_mutex_unlock(&resource_b);
    pthread_mutex_unlock(&resource_a);
    printf("Thread 1: recursos liberados.\n");

    return NULL;
}

void *thread_2(void *arg) {
    printf("Thread 2: intentando adquirir Resource B...\n");
    pthread_mutex_lock(&resource_b);
    printf("Thread 2: Resource B adquirido.\n");
    sleep(1);

    printf("Thread 2: intentando adquirir Resource A...\n");
    pthread_mutex_lock(&resource_a);
    printf("Thread 2: Resource A adquirido.\n");

    // Liberar recursos
    pthread_mutex_unlock(&resource_a);
    pthread_mutex_unlock(&resource_b);
    printf("Thread 2: recursos liberados.\n");

    return NULL;
}

int main() {
    pthread_t t1, t2;

    // Inicializar los mutex
    pthread_mutex_init(&resource_a, NULL);
    pthread_mutex_init(&resource_b, NULL);

    // Crear hilos
    pthread_create(&t1, NULL, thread_1, NULL);
    pthread_create(&t2, NULL, thread_2, NULL);

    // Esperar a que los hilos terminen
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    // Destruir los mutex
    pthread_mutex_destroy(&resource_a);
    pthread_mutex_destroy(&resource_b);

    printf("Programa finalizado.\n");

    return 0;
}
