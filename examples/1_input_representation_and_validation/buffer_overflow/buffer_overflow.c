// buffer_overflow.c
// Ejemplo de vulnerabilidad: Buffer Overflow con gets()

#include <stdio.h>

void vulnerable_function() {
    char buffer[5]; // Buffer pequeño

    printf("Introduce un texto largo: ");
    gets(buffer); // Inseguro: no valida el tamaño de la entrada
    printf("Contenido del buffer: %s\n", buffer);
}

int main() {
    printf("Llamando a la función vulnerable...\n");
    vulnerable_function();

    return 0;
}
