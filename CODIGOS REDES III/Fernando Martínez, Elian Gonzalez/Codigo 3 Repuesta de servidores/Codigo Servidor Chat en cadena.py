import socket
HOST = '172.30.154.163'  # Escucha en todas las interfaces de red disponibles
PORT = 12345
# Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)  # Escuchar hasta 5 conexiones entrantes

    print("Servidor escuchando en", HOST, "en el puerto", PORT)

    # Aceptar conexiones entrantes
    conn, addr = s.accept()

    with conn:
        print('Conexión establecida por:', addr)
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Mensaje recibido:', data.decode())
            
            # Enviar el mensaje a otros servidores
            for server_address in ['172.30.154.162']:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
                    s2.connect((server_address, PORT))
                    s2.sendall(data)