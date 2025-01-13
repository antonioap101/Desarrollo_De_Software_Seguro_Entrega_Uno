# Desarrollo de Software Seguro: Análisis de Vulnerabilidades

### Introducción

El desarrollo de software seguro es una disciplina esencial en la ingeniería de software moderna, especialmente en un contexto donde las aplicaciones están cada vez más expuestas a entornos diversos y potencialmente hostiles. Este trabajo tiene como objetivo principal analizar y comprender cómo se manifiestan las vulnerabilidades en el software, así como las protecciones inherentes que ofrecen los lenguajes de programación y entornos de desarrollo modernos.

A partir del estudio de los primeros temas de la asignatura y de referencias clave como "Seven Pernicious Kingdoms" y el CWE/SANS Top 25, se ha decidido enfocar este proyecto en la exploración práctica de varias vulnerabilidades comunes, como el desbordamiento de buffer, la inyección SQL y el Cross-Site Scripting (XSS). Estas vulnerabilidades han sido seleccionadas por su relevancia en el ámbito de la seguridad de software y por su representatividad dentro de distintas categorías de errores de programación.

El enfoque del trabajo no se centra en la funcionalidad de los programas desarrollados, sino en su capacidad para ilustrar y probar las vulnerabilidades seleccionadas. De este modo, se busca identificar las debilidades inherentes en los lenguajes y entornos elegidos, así como las medidas preventivas que estos ofrecen. La investigación también incluirá casos en los que las vulnerabilidades no puedan ser reproducidas debido a protecciones existentes, lo que también será objeto de análisis.

Con esta metodología, el trabajo pretende proporcionar un aprendizaje práctico y aplicado sobre las mejores prácticas en el desarrollo de software seguro, ayudando a prevenir errores comunes y a diseñar aplicaciones resilientes ante ataques y usos indebidos.

### Fundamentos Teóricos

#### Software Seguro y Resiliente
Un software seguro y resiliente se caracteriza por su capacidad para proteger la información y los recursos frente a accesos no autorizados, ataques malintencionados y errores involuntarios. Entre sus propiedades fundamentales destacan:
- **Confidencialidad**: Garantiza que la información está disponible solo para las personas autorizadas.
- **Integridad**: Protege la información contra modificaciones no autorizadas.
- **Disponibilidad**: Asegura que los recursos estén accesibles cuando se necesitan.
- **Autenticación**: Verifica la identidad de los usuarios y sistemas.
- **Autorización**: Controla el acceso a recursos en función de permisos predefinidos.
- **Auditoría**: Registra y monitorea las acciones para identificar actividades sospechosas.

#### Errores Más Comunes
Los errores más peligrosos según el **CWE/SANS Top 25** incluyen vulnerabilidades que suelen ser explotadas en aplicaciones modernas. Para 2024, de acuerdo con [MITRE](https://www.mitre.org/), el ranking de los mismos es el siguiente:

**¿Qué es MITRE?**


MITRE es una organización sin ánimo de lucro que gestiona programas de investigación y desarrollo para el beneficio público, particularmente en áreas como ciberseguridad, defensa, salud pública y tecnologías emergentes. Entre sus contribuciones destaca la gestión de bases de datos como CWE (Common Weakness Enumeration) y CVE (Common Vulnerabilities and Exposures), herramientas fundamentales para identificar, clasificar y mitigar vulnerabilidades en el desarrollo de software.

<div align="center">
    <img src="readme-assets/mitre-logo.png" alt="MITRE Logo" width="150"/>
    <p><em>Figura 1: Logo de MITRE</em></p>
</div>

A continuación, se presenta una tabla con el ranking de vulnerabilidades:


| **Rank** | **ID**     | **Name** | **Score** | **CVEs in KEV** | **Rank Change vs. 2023** |
|----------|------------|------------------------------------------------------------------------------------------|-----------|-----------------|--------------------------|
| 1        | CWE-79     | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')     | 56.92     | 3               | +1                       |
| 2        | CWE-787    | Out-of-bounds Write                                                                      | 45.20     | 18              | -1                       |
| 3        | CWE-89     | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')     | 35.88     | 4               | 0                        |
| 4        | CWE-352    | Cross-Site Request Forgery (CSRF)                                                        | 19.57     | 0               | +5                       |
| 5        | CWE-22     | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')           | 12.74     | 4               | +3                       |
| 6        | CWE-125    | Out-of-bounds Read                                                                       | 11.42     | 3               | +1                       |
| 7        | CWE-78     | Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')| 11.30     | 5               | -2                       |
| 8        | CWE-416    | Use After Free                                                                           | 10.19     | 5               | -4                       |
| 9        | CWE-862    | Missing Authorization                                                                    | 10.11     | 0               | +2                       |
| 10       | CWE-434    | Unrestricted Upload of File with Dangerous Type                                          | 10.03     | 0               | 0                        |
| 11       | CWE-94     | Improper Control of Generation of Code ('Code Injection')                                | 7.13      | 7               | +12                      |
| 12       | CWE-20     | Improper Input Validation                                                               | 6.78      | 1               | -6                       |
| 13       | CWE-77     | Improper Neutralization of Special Elements used in a Command ('Command Injection')      | 6.74      | 4               | +3                       |
| 14       | CWE-287    | Improper Authentication                                                                 | 5.94      | 4               | -1                       |
| 15       | CWE-269    | Improper Privilege Management                                                           | 5.22      | 0               | +7                       |
| 16       | CWE-502    | Deserialization of Untrusted Data                                                       | 5.07      | 5               | -1                       |
| 17       | CWE-200    | Exposure of Sensitive Information to an Unauthorized Actor                               | 5.07      | 0               | +13                      |
| 18       | CWE-863    | Incorrect Authorization                                                                 | 4.05      | 2               | +6                       |
| 19       | CWE-918    | Server-Side Request Forgery (SSRF)                                                      | 4.05      | 2               | 0                        |
| 20       | CWE-119    | Improper Restriction of Operations within the Bounds of a Memory Buffer                  | 3.69      | 2               | -3                       |
| 21       | CWE-476    | NULL Pointer Dereference                                                                | 3.58      | 0               | -9                       |
| 22       | CWE-798    | Use of Hard-coded Credentials                                                           | 3.46      | 2               | -4                       |
| 23       | CWE-190    | Integer Overflow or Wraparound                                                          | 3.37      | 3               | -9                       |
| 24       | CWE-400    | Uncontrolled Resource Consumption                                                       | 3.23      | 0               | +13                      |
| 25       | CWE-306    | Missing Authentication for Critical Function                                            | 2.73      | 5               | -5                       |


Algunos ejemplos destacados son:
1. **CWE-79**: Cross-site Scripting (XSS): Neutralización inapropiada de entradas durante la generación de páginas web.
2. **CWE-787**: Escritura fuera de los límites de memoria.
3. **CWE-89**: Inyección SQL: Neutralización incorrecta de elementos especiales en comandos SQL.
4. **CWE-352**: Cross-Site Request Forgery (CSRF): Peticiones no autorizadas realizadas desde un navegador autenticado.
5. **CWE-22**: Path Traversal: Limitación inadecuada de rutas de acceso.

Estos errores pertenecen a diferentes categorías de vulnerabilidades, como la validación de entradas, el manejo incorrecto de memoria y el abuso de APIs, que se analizan también en los "Seven Pernicious Kingdoms".

#### Vulnerabilidades Seleccionadas
En este trabajo, se ha decidido explorar las siguientes vulnerabilidades:

1. **Desbordamiento de Buffer**: Problema típico en lenguajes como C/C++ debido a la falta de verificación de límites al trabajar con memoria.
2. **Inyección SQL**: Exploits en bases de datos que permiten a un atacante alterar consultas SQL utilizando entradas maliciosas.
3. **Cross-Site Scripting (XSS)**: Ataques que aprovechan la falta de validación de entradas en aplicaciones web para ejecutar scripts maliciosos en el navegador de un usuario.
4. **Errores en Manejo de Sesiones**: Incluyen la reutilización de identificadores de sesión y la falta de controles adecuados, lo que puede conducir a ataques de hijacking.

Estas vulnerabilidades se probarán en distintos entornos y lenguajes de programación, evaluando tanto la facilidad para explotarlas como las medidas preventivas disponibles.


### Bibliografía

En esta sección se enumeran las referencias utilizadas para analizar las vulnerabilidades y conceptos tratados en el trabajo:

1. **CWE/SANS Top 25**: Publicación oficial sobre los 25 errores de software más peligrosos.
   - Fuente: [CWE/SANS 2024 Top 25](https://cwe.mitre.org/top25/archive/2024/2024_cwe_top25.html#top25list)
   - Análisis general y puntuación de las vulnerabilidades.

2. **CCN-CERT**: Resumen sobre los CWE/SANS Top 25.
   - Fuente: [CCN-CERT sobre CWE/SANS](https://www.ccn-cert.cni.es/es/soluciones-seguridad/elena.html?view=article&id=895:cwesans-publica-la-lista-de-los-25-errores-de-software-mas-peligrosos&catid=23)

3. **Seven Pernicious Kingdoms**: Taxonomía de errores de seguridad en software.
   - Fuente: [Seven Pernicious Kingdoms: Taxonomy of Software Security Errors (PDF)](https://cwe.mitre.org/documents/sources/SevenPerniciousKingdoms.pdf)

4. **Documentaciones oficiales**:
   - **C++**: [Documentación oficial de C++](https://cplusplus.com/)
   - **Python**: [Documentación oficial de Python](https://docs.python.org/3/)
   - **JavaScript**: [MDN Web Docs para JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
   - **SQL**: [Documentación oficial de SQLite](https://www.sqlite.org/docs.html)

