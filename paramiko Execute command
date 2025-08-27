import paramiko

# Crear cliente SSH
ssh = paramiko.SSHClient()

# Aceptar automÃ¡ticamente llaves de host desconocidas
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Conectar
ssh.connect(hostname="200.28.162.248", username="kali", password="kali")

# Definir el comando a ejecutar
cmd_to_execute = "pkill python  ; ./script2.sh&>/dev/null & ; ./script.sh&>/dev/null &"

# Ejecutar comando
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)

# Mostrar salida
print(ssh_stdout.read().decode())
print(ssh_stderr.read().decode())

# Cerrar conexiÃ³n
ssh.close()
