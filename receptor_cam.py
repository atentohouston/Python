# Utilice protocolo TCP (script de prueba..)
import cv2
import socket
import struct
import numpy as np
from datetime import datetime

HOST = "0.0.0.0" # No cambie (ANY).
PORT = 9999 # Cambie según sus requerimientos..

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"📡 Esperando conexión en {HOST}:{PORT}...")
conn, addr = server_socket.accept()
print(f"✅ Conectado con {addr}")

data = b""
payload_size = struct.calcsize(">L")

# Crear ventana ajustable
cv2.namedWindow("Servidor - Video recibido", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Servidor - Video recibido", 800, 600)

while True:
    # Recibir tamaño del frame
    while len(data) < payload_size:
        packet = conn.recv(4096)
        if not packet:
            break
        data += packet
    
    if not data:
        break

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]

    # Recibir frame completo
    while len(data) < msg_size:
        data += conn.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Reconstruir frame desde JPEG
    frame = cv2.imdecode(np.frombuffer(frame_data, dtype=np.uint8), cv2.IMREAD_COLOR)

    # Redimensionar frame a tamaño más grande
    frame = cv2.resize(frame, (800, 600))

    # Obtener fecha y hora actuales
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Dibujar texto con contorno negro
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (10, 30)
    font_scale = 0.7   # tamaño más pequeño
    thickness = 1      # grosor de la letra principal

    # Primero contorno negro más grueso
    cv2.putText(frame, timestamp, org, font, font_scale, (0, 0, 0), thickness + 2, cv2.LINE_AA)
    # Luego texto verde encima
    cv2.putText(frame, timestamp, org, font, font_scale, (0, 255, 0), thickness, cv2.LINE_AA)

    cv2.imshow("Servidor - Video recibido", frame)
    
    # Salir con ESC
    if cv2.waitKey(1) == 27:
        break

conn.close()
cv2.destroyAllWindows()
