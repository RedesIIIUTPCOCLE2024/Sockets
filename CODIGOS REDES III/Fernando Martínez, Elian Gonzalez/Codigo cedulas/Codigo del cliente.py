import socket

HOST = '172.30.154.169'  # El servidor está en la misma máquina
PORT = 12345  # Puerto en el que el servidor está escuchando

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Crear un socket TCP
    s.connect((HOST, PORT))  # Conectar al servidor en el puerto especificado
    while True:  # Bucle infinito
        # Solicitar al usuario que ingrese la cédula en el formato x-xxx-xxxx
        cedula = input("Ingrese la cédula (en formato x-xxx-xxxx): ")
       
        # Enviar la cédula al servidor
        s.sendall(cedula.encode('utf-8'))
        
        # Recibir la respuesta del servidor (hasta 1024 bytes)
        respuesta = s.recv(1024)
        
        # Imprimir la respuesta del servidor
        print("Respuesta del servidor:", respuesta.decode('utf-8'))
