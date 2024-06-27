### English
![Portada del Script](logo.png)
# WiFi Brute Force Script - Protection and Security

This Python script performs a brute force attack to gain access to a WiFi network using common passwords and character combinations. You can adjust the character length range in the script to suit your needs. Please note that the process may take time to find the password, depending on its complexity and length.

**Note:** Avoid being connected to any network before or during script execution.

## Requirements

- Python 3
- Operating system compatible with Windows `netsh` commands (for network configuration)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Matias-Paz/brute_force_script.git
   cd brute_force_script
   ```

#### The script uses standard Python libraries. No additional installation is required.

## Usage

The script is executed from the command line by providing the WiFi network name as an argument:

```bash
python main.py <network_name>
```

Replace <network_name> with the exact and correct name of the WiFi network you wish to connect to. This modification ensures double quotes are used around the network name and emphasizes the importance of providing the exact name for the script to function correctly.

## Script Operation

### 1. Obtaining Original MAC and IP Addresses:

The script retrieves the current MAC address and IP address of the machine.

```bash
original_mac = get_original_mac()
my_ip = get_ip_address()
print("Original MAC address:   ", original_mac)
print("Original IP address:    ", my_ip)
```

### 2. Brute Force Attack with Common Passwords

It uses a list of common passwords from a text file (10-million-password-list.txt) to attempt to connect to the network.

```bash
def force_brute_txt(txt_file, wifiName):
    DB_PASSWORD = wifiCommonPassword(txt_file)
    for index, password in enumerate(DB_PASSWORD):
        outPut(password, index, wifiName)
```

### 3. Brute Force Attack with Character Combinations
It generates alphanumeric character combinations to attempt to find the network password.

```bash
def guess_password(wifiName):
    chars = string.digits + string.ascii_lowercase
    index = 0
    for password_length in range(6, 13):
        for guess in itertools.product(chars, repeat=password_length):
            index += 1
            guess = ''.join(guess)
            outPut(guess, index, wifiName)
```

## Security and Precautions

**Caution:** This script is intended solely for educational and testing purposes in controlled environments. Unauthorized access to WiFi networks is illegal and may have legal consequences.

**Responsibility:** Misuse of this script is the responsibility of the user.

### Using VPN Safely

To protect your privacy when using a VPN, consider the following steps:

1. **Use a trusted VPN:** Choose a VPN known for its security and privacy. Configure the VPN with secure protocols like OpenVPN.
2. **Set up firewall:** Ensure the firewall allows only connections through the VPN to prevent data leaks.
3. **Avoid geolocation:** Use VPN features to change your geographic location and protect your online identity.

### Hiding MAC Address

To protect your MAC address and avoid identification:

1. **Change MAC address:** Research how to change or spoof the MAC address of your network adapter using specific tools or commands for your operating system.
2. **Advanced tools and settings:** Use third-party applications or system commands to effectively modify your MAC address.
3. **Continuous evaluation:** Conduct periodic tests to ensure both the VPN and MAC address are properly hidden and protected.

It is important to use these techniques responsibly and legally, always respecting terms of use and local laws.

## Contribution

If you wish to contribute improvements or corrections, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
#### Español
# WiFi Brute Force Script - Protección y Seguridad

Este script en Python realiza un ataque de fuerza bruta para obtener acceso a una red WiFi utilizando contraseñas comunes y combinaciones de caracteres. Puedes ajustar el rango de longitud de caracteres en el script para adaptarlo a tus necesidades. Ten en cuenta que el proceso puede demorar en encontrar la contraseña, dependiendo de la complejidad y longitud de la misma.

**Nota:** Evita estar conectado a cualquier red antes o durante la ejecución del script.

## Requisitos

- Python 3
- Sistema operativo compatible con los comandos `netsh` de Windows (para la configuración de red)

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Matias-Paz/brute_force_script.git
   cd brute_force_script
   ```

#### El script utiliza bibliotecas estándar de Python. No se requiere ninguna instalación adicional.

# Uso

El script se ejecuta desde la línea de comandos proporcionando el nombre de la red WiFi como argumento:
   ```bash
    python main.py <nombre_red>
   ```

Reemplaza <nombre_red> con el nombre exacto y correcto de la red WiFi a la que deseas conectarte.
Esta modificación asegura que se utilicen comillas dobles alrededor del nombre de red y se enfatiza la importancia de proporcionar el nombre exacto para que el script funcione correctamente.

## Funcionamiento del script

### 1. Obtención de direcciones MAC e IP originales:

El script obtiene la dirección MAC y la dirección IP actual de la máquina.

   ```bash
original_mac = get_original_mac()
my_ip = get_ip_address()
print("Original MAC address:   ", original_mac)
print("Original IP address:    ", my_ip)
   ```

###  2. Ataque de fuerza bruta con contraseñas comunes

Utiliza una lista de contraseñas comunes desde un archivo de texto (10-million-password-list.txt) para intentar conectarse a la red.

```bash
def force_brute_txt(txt_file, wifiName):
    DB_PASSWORD = wifiCommonPassword(txt_file)
    for index, password in enumerate(DB_PASSWORD):
        outPut(password, index, wifiName)
```

### 3. Ataque de fuerza bruta con combinaciones de caracteres
Genera combinaciones de caracteres alfanuméricos para intentar encontrar la contraseña de la red.

```bash
def guess_password(wifiName):
    chars = string.digits + string.ascii_lowercase
    index = 0
    for password_length in range(6, 13):
        for guess in itertools.product(chars, repeat=password_length):
            index += 1
            guess = ''.join(guess)
            outPut(guess, index, wifiName)
```

## Seguridad y precauciones

**Precaución:** Este script está diseñado únicamente para fines educativos y de prueba en entornos controlados. El acceso no autorizado a redes WiFi es ilegal y puede tener consecuencias legales.

**Responsabilidad:** El uso indebido de este script es responsabilidad del usuario.

### Ocultar la VPN

Para proteger tu privacidad al utilizar una VPN, considera los siguientes pasos:

1. **Utilizar VPN de confianza:** Escoge una VPN reconocida por su seguridad y privacidad. Configura la VPN con protocolos seguros como OpenVPN.
2. **Configurar el firewall:** Asegúrate de que el firewall permita solo conexiones a través de la VPN para evitar fugas de datos.
3. **Evitar la geolocalización:** Utiliza funciones de la VPN para cambiar tu ubicación geográfica y proteger tu identidad en línea.

### Ocultar el MAC address

Para proteger tu dirección MAC y evitar la identificación:

1. **Cambiar el MAC address:** Investiga cómo cambiar o spoofear el MAC address de tu adaptador de red usando herramientas específicas o comandos según tu sistema operativo.
2. **Herramientas y configuraciones avanzadas:** Utiliza aplicaciones de terceros o comandos de sistema para modificar tu dirección MAC de forma efectiva.
3. **Evaluación continua:** Realiza pruebas periódicas para asegurarte de que tanto la VPN como el MAC address estén correctamente ocultos y protegidos.

Es importante utilizar estas técnicas de manera responsable y legal, respetando siempre los términos de uso y las leyes locales.

## Contribución

Si deseas contribuir con mejoras o correcciones, siéntete libre de hacer un fork del repositorio y enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
