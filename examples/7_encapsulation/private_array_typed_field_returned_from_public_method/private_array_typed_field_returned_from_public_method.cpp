#include <iostream>
#include <string>

class SecureClass {
private:
    std::string sensitiveData[3] = {"clave1", "clave2", "clave3"};

public:
    // Método público que devuelve una referencia al arreglo privado
    std::string* getSensitiveData() {
        return sensitiveData; // Devuelve el arreglo privado directamente
    }
};

int main() {
    SecureClass secure;

    // Obtenemos una referencia al arreglo privado
    std::string* data = secure.getSensitiveData();

    // Modificamos el contenido del arreglo privado desde fuera de la clase
    data[0] = "modificación-no-autorizada";

    std::cout << "Contenido modificado del array privado:" << std::endl;
    for (int i = 0; i < 3; i++) {
        std::cout << data[i] << std::endl;
    }

    return 0;
}
