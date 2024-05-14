import socket

def main():
    # Configurar el cliente
    host = '172.30.154.162'
    port = 12345

    # Crear el socket del cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    cliente.connect((host, port))

    # Solicitar al usuario que ingrese la cédula
    cedula = input("Ingrese el número de cédula: ")

    # Enviar la cédula al servidor
    cliente.send(cedula.encode('utf-8'))

    # Recibir la respuesta del servidor
    nombre = cliente.recv(1024).decode('utf-8')

    # Mostrar el nombre recibido
    print("Nombre:", nombre)

    # Cerrar la conexión con el servidor
    cliente.close()

if __name__ == "__main__":
    main()
