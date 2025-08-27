# Use protocolo UDP.
import socket
import pyaudio
import numpy as np

host = '0.0.0.0' # Mantenga (ANY).
port = 8080 # Ajsute Port segun necesidades.

chunk_size = 1024
sample_format = pyaudio.paInt16
channels = 1 # Ajustar en caso de que las máquinas lo requieran (emisor, Receptor).
rate = 21050
AMPLIFY = 3.6

audio = pyaudio.PyAudio()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

stream = audio.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    output=True,
                    frames_per_buffer=chunk_size)

while True:
    data, addr = sock.recvfrom(4096) 
    audio_data = np.frombuffer(data, dtype=np.int16)
    amplified = np.clip(audio_data * AMPLIFY, -32768, 32767).astype(np.int16)
    stream.write(amplified.tobytes())
