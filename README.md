![Portada del Script](logo.png)
#### Español
## WiFi Brute Force Script - Protección y Seguridad

Este script en Python realiza un ataque de fuerza bruta para obtener acceso a una red WiFi utilizando contraseñas comunes y combinaciones de caracteres. Puedes ajustar el rango de longitud de caracteres en el script para adaptarlo a tus necesidades. Ten en cuenta que el proceso puede demorar en encontrar la contraseña, dependiendo de la complejidad y longitud de la misma.

**Nota:** Evita estar conectado a cualquier red antes o durante la ejecución del script.

## Requisitos

- Python 3
- Sistema operativo compatible con los comandos `netsh` de Windows (para la configuración de red)

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/repo.git
   cd repo
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
