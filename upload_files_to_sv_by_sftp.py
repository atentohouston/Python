import os
import paramiko
from paramiko.ssh_exception import SSHException, NoValidConnectionsError
import socket

host = "192.168.1.144" # cambie el host
port = 22 
username = "mi_usuario"
password = "mi_contraseña"

local_path = r"C:\Users\pepe\Desktop"
remote_path = "/ruta/a_mi/servidor/"

def upload_dir(sftp, local_dir, remote_dir):
    """Sube un directorio completo recursivamente con SFTP."""
    try:
        sftp.mkdir(remote_dir)
    except IOError:
        # Ya existe
        pass

    for item in os.listdir(local_dir):
        local_item = os.path.join(local_dir, item)
        remote_item = remote_dir + "/" + item
        if os.path.isfile(local_item):
            try:
                print(f"⬆️ Subiendo archivo: {local_item} -> {remote_item}")
                sftp.put(local_item, remote_item)
            except Exception as e:
                print(f"⚠ No se pudo subir el archivo {local_item}: {e}")
        else:
            # Carpeta, subimos recursivamente
            upload_dir(sftp, local_item, remote_item)

# Conexión SSH con manejo de errores
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"🔌 Conectando a {host}:{port}...")
    ssh.connect(host, port, username, password, timeout=10)
except (TimeoutError, socket.timeout):
    print(f"⛔ Timeout: no se pudo conectar a {host}:{port}")
    ssh = None
except NoValidConnectionsError as e:
    print(f"⛔ Conexión fallida: {e}")
    ssh = None
except SSHException as e:
    print(f"⛔ Error SSH: {e}")
    ssh = None
except Exception as e:
    print(f"⛔ Error inesperado: {e}")
    ssh = None

# Solo intentar SFTP si la conexión fue exitosa
if ssh:
    try:
        sftp = ssh.open_sftp()
        upload_dir(sftp, local_path, remote_path)
        sftp.close()
        print("✅ Transferencia completa.")
    except Exception as e:
        print(f"⚠ Error durante la transferencia SFTP: {e}")
    finally:
        ssh.close()
else:
    print("⚠ Se saltó la transferencia SFTP porque no se pudo conectar.")
