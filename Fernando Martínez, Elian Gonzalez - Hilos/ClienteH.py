import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('172.30.154.169', 12345)
    client_socket.connect(server_address)

    try:
        while True:
            operacion = input("Selecciona 'suma' o 'resta': ")
            client_socket.sendall(operacion.encode())

            mensaje = client_socket.recv(1024).decode()
            print(mensaje)

            numeros = input("Ingresa dos números, separados por espacio")
            client_socket.sendall(numeros.encode())

            resultado = client_socket.recv(1024).decode()
            print(resultado)
    except KeyboardInterrupt:
        print("Cliente desconectado.")
        client_socket.close()

if _name_ == "_main_":
    main()