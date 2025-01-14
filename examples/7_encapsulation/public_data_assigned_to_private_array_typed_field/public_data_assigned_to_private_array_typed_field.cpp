#include <iostream>
#include <string>

class SecureClass {
private:
    std::string* sensitiveData;

public:
    // Constructor para inicializar el puntero a nullptr
    SecureClass() : sensitiveData(nullptr) {}

    // Método público que permite asignar un array externo al array privado (por referencia)
    void setSensitiveData(std::string* externalData) {
        sensitiveData = externalData; // Se almacena la referencia al array externo
    }

    void printSensitiveData() const {
        std::cout << "Contenido del array privado (referencia al externo):" << std::endl;
        for (int i = 0; i < 3; i++) {
            std::cout << sensitiveData[i] << std::endl;
        }
    }
};

int main() {
    SecureClass secure;

    // Datos externos públicos
    std::string publicData[3] = {"expuesto1", "expuesto2", "expuesto3"};

    // Asignamos los datos públicos al array privado
    secure.setSensitiveData(publicData);

    // Modificamos los datos públicos
    publicData[0] = "modificado";

    // El array privado también refleja los cambios
    secure.printSensitiveData();

    return 0;
}
