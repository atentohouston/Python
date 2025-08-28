import pyaudio, wave, paramiko, os, argparse, sys

print("")

# --- Argumentos ---
parser = argparse.ArgumentParser(
    description="Captura audio y envía a un servidor SSH/SFTP",
    usage="%(prog)s --host <ip> --port <puerto> --username <usuario> --password <clave> --duration <segundos>\n\nLlame a python en caso de ejecutar el script en raw.",
    add_help=False
)

parser.add_argument("--host", required=True)
parser.add_argument("--port", type=int, default=22)
parser.add_argument("--username", required=True)
parser.add_argument("--password", required=True)
parser.add_argument("--duration", type=int, required=True)

try:
    args = parser.parse_args()
except SystemExit:
    print("\nIncorrect parameter.\n")
    parser.print_help()
    sys.exit(1)

# --- Verificación de conexión ---
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(args.host, args.port, args.username, args.password, timeout=10)
    ssh.close()
    print("\nConexión establecida con el servidor.")
except Exception:
    print("\nNo se pudo conectar con el servidor. Cerrando programa...")
    sys.exit(1)

# --- Configuración de grabación ---
OUTPUT_FILENAME = "grabacion.wav"
p = pyaudio.PyAudio()
try:
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    stream.close()
except Exception:
    print("\nNo se detectó ningún micrófono!")
    sys.exit(1)

# --- Grabación ---
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
print(f"Grabando {args.duration} segundos...")
frames = [stream.read(1024) for _ in range(int(44100 / 1024 * args.duration))]
stream.stop_stream()
stream.close()
p.terminate()

with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))

print(f"Captura guardada como {OUTPUT_FILENAME}")

# --- Subida con progreso ---
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(args.host, args.port, args.username, args.password, timeout=10)
    sftp = ssh.open_sftp()
    remote_file = f"/home/{args.username}/Desktop/{OUTPUT_FILENAME}"
    print(f"Subiendo archivo: {OUTPUT_FILENAME} -> {remote_file}")

    file_size = os.path.getsize(OUTPUT_FILENAME)

    def progress(transferred, total):
        percent = int(transferred / total * 100)
        sys.stdout.write(f"\rProgreso: {percent}%")
        sys.stdout.flush()

    sftp.put(OUTPUT_FILENAME, remote_file, callback=progress)
    print("\nSubida completada.")

    sftp.close()
    ssh.close()
    os.remove(OUTPUT_FILENAME)
    print("Archivo enviado y eliminado localmente.")
except Exception:
    print("No se pudo enviar el archivo al servidor. Cerrando programa...")
    sys.exit(1)
