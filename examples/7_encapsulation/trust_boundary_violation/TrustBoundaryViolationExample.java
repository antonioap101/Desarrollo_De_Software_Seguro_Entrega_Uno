import java.util.HashMap;
import java.util.Map;

public class TrustBoundaryViolationExample {

    public static void main(String[] args) {
        Map<String, String> userData = new HashMap<>();

        // Datos confiables: Validados por el sistema
        userData.put("username", "secure_user");
        userData.put("role", "admin");

        // Datos no confiables: Proporcionados por el usuario (potencialmente maliciosos)
        String untrustedInput = "<script>alert('Hacked!');</script>";
        userData.put("bio", untrustedInput);

        // Procesar y mostrar los datos del usuario
        displayUserProfile(userData);
    }

    private static void displayUserProfile(Map<String, String> userData) {
        System.out.println("Mostrando perfil del usuario...");

        // Simulamos el renderizado de un perfil en un sistema web
        String profileHtml = "<html>" +
                "<body>" +
                "<h1>Usuario: " + userData.get("username") + "</h1>" +
                "<p>Rol: " + userData.get("role") + "</p>" +
                "<p>Biografía: " + userData.get("bio") + "</p>" +
                "</body>" +
                "</html>";

        // Aquí se mezcla contenido confiable (username, role) con no confiable (bio)
        System.out.println("Renderizando perfil...");
        System.out.println(profileHtml);

        // Si el código HTML se interpreta (por ejemplo, en un navegador), el script malicioso se ejecutará
    }
}
