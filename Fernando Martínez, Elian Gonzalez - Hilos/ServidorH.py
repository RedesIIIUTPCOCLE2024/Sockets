import socket
import threading

# Función para manejar la conexión con cada cliente
def manejar_cliente(client_socket):
    try:
        while True:
            # Recibe la operación seleccionada por el cliente
            operacion = client_socket.recv(1024).decode()

            # Verifica la operación seleccionada y realiza la operación correspondiente
            if operacion.lower() == 'suma':
                client_socket.sendall("Ingresa dos números para sumar: ".encode())
                numeros = client_socket.recv(1024).decode().split()
                resultado = float(numeros[0]) + float(numeros[1])
                client_socket.sendall(f"Resultado de la suma: {resultado}".encode())
            elif operacion.lower() == 'resta':
                client_socket.sendall("Ingresa dos numeros para restar: ".encode())
                numeros = client_socket.recv(1024).decode().split()
                resultado = float(numeros[0]) - float(numeros[1])
                client_socket.sendall(f"Resultado de la resta: {resultado}".encode())
            else:
                client_socket.sendall("Operación no válida. Por favor, selecciona 'suma' o 'resta'.".encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    # Crea un socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Especifica la dirección IP y el puerto para el servidor
    server_address = ('172.30.154.169', 12345)
    print(f"Iniciando servidor en {server_address[0]} puerto {server_address[1]}")

    # Enlaza el socket al puerto
    server_socket.bind(server_address)

    # Escucha por conexiones entrantes
    server_socket.listen(5)

    try:
        while True:
            # Espera por una conexión entrante
            client_socket, client_address = server_socket.accept()
            print(f"Conexión entrante de {client_address}")

            # Inicia un nuevo hilo para manejar la conexión con el cliente
            cliente_thread = threading.Thread(target=manejar_cliente, args=(client_socket,))
            cliente_thread.start()
    except KeyboardInterrupt:
        print("Servidor detenido.")
        server_socket.close()

if _name_ == "_main_":
    main()