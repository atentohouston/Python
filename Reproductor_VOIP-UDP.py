import socket
import pyaudio

# Configuración de la dirección IP y el puerto para recibir audio
host = '0.0.0.0'  # Escucha en todas las interfaces de red
port = 1234

# Configuración de PyAudio
chunk_size = 1024
sample_format = pyaudio.paInt16
channels = 2
rate = 44100

# Inicialización de PyAudio
audio = pyaudio.PyAudio()

# Configuración del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print("Esperando conexión...")

# Inicialización del flujo de reproducción de audio
stream = audio.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    output=True,
                    frames_per_buffer=chunk_size)

print("Reproduciendo audio...")

while True:
    data, addr = sock.recvfrom(chunk_size)
    stream.write(data)  # Reproducir los datos de audio recibidos

# Cierre del flujo de reproducción y del socket
stream.stop_stream()
stream.close()
audio.terminate()
sock.close()
