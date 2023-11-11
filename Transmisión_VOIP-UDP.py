import socket
import pyaudio

# Configuración de la dirección IP y el puerto del host receptor
host = '193.161.193.99'
port = 36312

# Configuración de PyAudio
chunk_size = 1024
sample_format = pyaudio.paInt16
channels = 2
rate = 44100

# Inicialización de PyAudio
audio = pyaudio.PyAudio()

# Apertura del flujo de grabación desde el micrófono
stream = audio.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk_size)

# Creación del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Transmitiendo audio por UDP...")

try:
    while True:
        # Lectura de los datos del flujo de grabación
        data = stream.read(chunk_size)
        
        # Envío de los datos al host receptor
        sock.sendto(data, (host, port))
except KeyboardInterrupt:
    pass

print("Transmisión finalizada.")

# Cierre del flujo de grabación y del socket
stream.stop_stream()
stream.close()
audio.terminate()
sock.close()
