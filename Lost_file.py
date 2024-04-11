####################################################
## Encontrar archivos perdidos en Windows y Linux ##
####################################################

import os
import sys

# Códigos de colores ANSI para texto
COLOR_VERDE = '\033[92m'  # Verde
COLOR_ROJO = '\033[91m'   # Rojo
COLOR_RESET = '\033[0m'   # Resetear el color

def buscar_archivo(nombre_archivo, directorio_raiz):
    rutas_archivos = []
    for ruta_actual, _, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            if archivo == nombre_archivo:
                rutas_archivos.append(os.path.join(ruta_actual, archivo))
    return rutas_archivos

# Verificar si se proporcionó el nombre del archivo como argumento
if len(sys.argv) != 2:
    print(f"{COLOR_ROJO}Uso: python script.py <nombre_del_archivo>{COLOR_RESET}")
    sys.exit(1)

nombre_archivo = sys.argv[1]

# Buscar el archivo desde el directorio raíz
directorio_raiz = '/'  # Cambia este directorio raíz según tus necesidades
rutas_archivos = buscar_archivo(nombre_archivo, directorio_raiz)

if rutas_archivos:
    print("\n")
    print(f"{COLOR_ROJO}[{COLOR_RESET}{COLOR_VERDE}+{COLOR_RESET}{COLOR_ROJO}]{COLOR_RESET}{COLOR_VERDE} Exito -> {COLOR_ROJO}{nombre_archivo}{COLOR_RESET} {COLOR_VERDE}se encontró en{COLOR_RESET}")
    print("\n")
    for ruta_archivo in rutas_archivos:
        print(f"-> {COLOR_VERDE}{ruta_archivo}{COLOR_RESET}")
    print("\n")
        
else:
    print(f"{COLOR_ROJO}No se encontró el archivo {nombre_archivo} en el directorio raíz.{COLOR_RESET}")
