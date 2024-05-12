import socket


SERVER_IP = '172.30.154.164'  # IP del primer servidor
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, PORT))
    print("Conexión establecida con el servidor")

    # Enviar un mensaje al servidor
    message = input("Ingrese un mensaje: ")
    s.sendall(message.encode())
    print("Mensaje enviado al servidor")