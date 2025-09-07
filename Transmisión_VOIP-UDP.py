# Emisor UDP de audio
import socket
import pyaudio

# Cambia esto por la IP del receptor
dest_ip = '192.168.1.100'  # ⚠️ Cambia a la IP real del receptor
dest_port = 8080

chunk_size = 1024
sample_format = pyaudio.paInt16
channels = 1 # Ajuste Según el hardware del emisor.
rate = 21050

audio = pyaudio.PyAudio()
stream = audio.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk_size)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"[🔊] Enviando audio a {dest_ip}:{dest_port}... (Ctrl+C para salir)")

try:
    while True:
        data = stream.read(chunk_size, exception_on_overflow=False)
        sock.sendto(data, (dest_ip, dest_port))
except KeyboardInterrupt:
    print("\n[⛔] Transmisión finalizada por el usuario.")
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
    sock.close()
