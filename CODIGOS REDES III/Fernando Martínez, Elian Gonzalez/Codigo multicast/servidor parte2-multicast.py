import socket
import threading

# Función para manejar las conexiones de clientes
def handle_client(client_socket, client_address):
    while True:
        try:
            # Recibir el mensaje del cliente
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Mensaje recibido de {client_address}: {message}")

            # Reenviar el mensaje a todos los clientes conectados
            for client in connected_clients:
                if client != client_socket:
                    client.send(message.encode("utf-8"))
        except Exception as e:
            print(f"Error: {e}")
            break

    # Cerrar la conexión con el cliente
    client_socket.close()
    connected_clients.remove(client_socket)

# Configuración del servidor
HOST = '172.30.154.163'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Servidor escuchando en {HOST}:{PORT}")

connected_clients = []

# Esperar conexiones de clientes
while True:
    client_socket, client_address = server.accept()
    print(f"Conexión establecida con {client_address}")
    connected_clients.append(client_socket)

    # Iniciar un hilo para manejar al cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()