#include <iostream>

int main() {
    int *ptr = nullptr; // Puntero nulo

    std::cout << "Intentando desreferenciar un puntero nulo..." << std::endl;
    std::cout << *ptr << std::endl; // Provocará un fallo de segmentación

    return 0;
}
