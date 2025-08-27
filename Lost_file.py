####################################################
## Encontrar archivos perdidos en Windows y Linux ##
####################################################

import os
import sys
from colorama import init, Fore, Style

# Inicializar colorama para que funcione en Windows
init(autoreset=True)

# Colores
COLOR_VERDE = Fore.GREEN
COLOR_ROJO = Fore.RED
COLOR_RESET = Style.RESET_ALL

def buscar_archivo(nombre_archivo, directorio_raiz):
    """
    Busca un archivo específico dentro de un directorio y sus subdirectorios.
    """
    rutas_archivos = []
    for ruta_actual, _, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            if archivo == nombre_archivo:
                rutas_archivos.append(os.path.join(ruta_actual, archivo))
    return rutas_archivos

# Verificar si se proporcionó el nombre del archivo como argumento
if len(sys.argv) != 2:
    print(f"{COLOR_ROJO}Uso: python {sys.argv[0]} <nombre_del_archivo>{COLOR_RESET}")
    sys.exit(1)

nombre_archivo = sys.argv[1]

# Determinar el directorio raíz según el sistema operativo
directorio_raiz = os.path.abspath(os.sep)  # '/' en Linux, 'C:\\' en Windows

# Buscar el archivo
rutas_archivos = buscar_archivo(nombre_archivo, directorio_raiz)

# Mostrar resultados
if rutas_archivos:
    print("\n")
    print(f"[{COLOR_VERDE}+{COLOR_RESET}] {COLOR_VERDE}Éxito -> {COLOR_ROJO}{nombre_archivo}{COLOR_RESET} {COLOR_VERDE}se encontró en:{COLOR_RESET}\n")
    for ruta_archivo in rutas_archivos:
        print(f"-> {COLOR_VERDE}{ruta_archivo}{COLOR_RESET}")
    print("\n")
else:
    print(f"{COLOR_ROJO}No se encontró el archivo {nombre_archivo} en el directorio raíz.{COLOR_RESET}")
