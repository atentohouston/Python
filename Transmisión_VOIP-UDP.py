# Utilice protoclo UDP.
import cv2
import socket
import struct

SERVER_IP = "192.168.1.127" # Cambie según sus requerimientos.
PORT = 5555 # Ajuste según sus requerimientos...

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Comprimir frame a JPEG
    ret, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    data = buffer.tobytes()
    
    # Enviar tamaño y datos
    message_size = struct.pack(">L", len(data))  # ">L" = big-endian unsigned long
    client_socket.sendall(message_size + data)

cap.release()
client_socket.close()
