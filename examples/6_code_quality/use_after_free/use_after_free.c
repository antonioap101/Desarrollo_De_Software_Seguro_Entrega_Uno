#include <stdio.h>
#include <stdlib.h>

int main() {
    int *data = (int *)malloc(sizeof(int));
    if (data == NULL) {
        perror("Error al asignar memoria");
        return 1;
    }

    *data = 42;
    free(data); // Liberación de memoria

    printf("Intentando acceder a la memoria liberada: %d\n", *data); // Uso después de liberar

    return 0;
}
