#include <iostream>

void memoryLeakExample() {
    int *leakedArray = new int[10]; // Memoria asignada pero nunca liberada
    for (int i = 0; i < 10; i++) {
        leakedArray[i] = i;
    }

    std::cout << "Memoria asignada pero no liberada." << std::endl;
}

int main() {
    memoryLeakExample();
    std::cout << "Fin del programa sin liberar memoria." << std::endl;
    return 0;
}
