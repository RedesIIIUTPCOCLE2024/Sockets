mport socket

# Función para manejar la recepción de mensajes
def receive_messages(client_socket):
    print("╔═══════════════════════════════╗")
    print("║   ¡Chat multicast iniciado!    ║")
    print("║  ¡Puedes enviar mensajes ahora!║")
    print("╚═══════════════════════════════╝")
    while True:
        try:
            # Recibir mensaje del servidor y mostrarlo
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except Exception as e:
            print(f"Error: {e}")
            break

# Configurar el cliente
HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Llamar a la función para recibir mensajes del servidor
receive_messages(client)

# El cliente solo recibirá mensajes del servidor, no enviará mensajes al servidor