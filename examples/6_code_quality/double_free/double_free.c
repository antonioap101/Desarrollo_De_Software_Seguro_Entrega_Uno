#include <stdlib.h>
#include <stdio.h>

int main() {
    char *buffer = (char *)malloc(10 * sizeof(char));
    if (buffer == NULL) {
        perror("Error al asignar memoria");
        return 1;
    }

    free(buffer); // Liberación inicial
    free(buffer); // Liberación duplicada

    printf("Programa finalizado.\n");
    return 0;
}
