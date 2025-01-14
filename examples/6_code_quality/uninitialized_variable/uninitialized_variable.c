#include <stdio.h>

int main() {
    int uninitializedVar; // Variable no inicializada

    printf("El valor de la variable no inicializada es: %d\n", uninitializedVar); // Valor impredecible

    return 0;
}
