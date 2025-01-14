public class UncheckedReturnValueExample {

    public static void main(String[] args) {
        System.out.println("\nEjecución con manejo seguro:");
        checkedReturnValue(10, 0);

        System.out.println("Ejecución con manejo inseguro:");
        unCheckedReturnValue(10, 0);
    }

    private static boolean isValidDivision(int numerator, int denominator) {
        return denominator != 0;
    }

    private static void unCheckedReturnValue(int numerator, int denominator) {
        isValidDivision(numerator, denominator);
        // Ignorar el retorno de isValidDivision
        System.out.println("Resultado: " + (numerator / denominator));
    }

    private static void checkedReturnValue(int numerator, int denominator) {
        // Verificar el retorno de isValidDivision
        if (!isValidDivision(numerator, denominator)) {
            System.out.println("Error: División por cero.");
            return;
        }

        System.out.println("Resultado: " + (numerator / denominator));
    }
}
