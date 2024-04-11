import paramiko
import glob

def scp_transfer(source, destination, hostname, port, username, password=None, private_key=None):
    # Establecer la conexión SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Autenticación
        if password:
            ssh_client.connect(hostname, port=port, username=username, password=password)
        elif private_key:
            ssh_client.connect(hostname, port=port, username=username, key_filename=private_key)
        else:
            raise ValueError("Se debe proporcionar una contraseña o una clave privada para la autenticación SSH.")

        # Crear un canal SCP
        with ssh_client.open_sftp() as sftp:
            # Transferir los archivos con extensión .png
            for file_path in glob.glob(source):
                file_name = file_path.split("\\")[-1]
                sftp.put(file_path, f"{destination}/{file_name}")
                print(f"Archivo {file_name} transferido exitosamente.")
    except Exception as e:
        print(f"Error al transferir los archivos: {e}")
    finally:
        # Cerrar la conexión SSH
        ssh_client.close()

def main():
    # Solicitar la ruta del archivo al usuario
    source_path = input("Ingrese la ruta del archivo o el patrón de archivo (wildcard): ")

    # Solicitar la dirección IP del servidor
    hostname = input("Ingrese la dirección IP del servidor: ")

    # Solicitar el puerto del servidor
    port = int(input("Ingrese el puerto del servidor (predeterminado 22): ") or "22")

    # Solicitar la ruta de destino en el servidor
    destination_path = input("Ingrese la ruta de destino en el servidor: ")

    # Credenciales de la máquina remota
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")  # Puedes implementar una lógica más segura aquí

    # Realizar la transferencia
    scp_transfer(source_path, destination_path, hostname, port, username, password=password)

if __name__ == "__main__":
    main()
