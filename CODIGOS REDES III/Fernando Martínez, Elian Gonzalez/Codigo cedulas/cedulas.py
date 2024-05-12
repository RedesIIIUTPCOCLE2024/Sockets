import socket

def buscar_cedula(cedula):
    try:
        with open("registro.txt") as file: 
            return next(line.split("=")[1].strip() for line in file if cedula in line)
    except StopIteration:
        return "Cédula no encontrada"
#aqui mandamos al programa que busque el archivo donde tenemos el ejecutable del programa.
HOST = '0.0.0.0' #el host tcp en este caso es 0.0.0.0 para que indentifique la maquina
PORT = 12345 #abrimos el puerto

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #sentencia para habilitar la comunicacion con el socket
    s.bind((HOST, PORT)) #
    s.listen(1) #en forma de escuha
    print("Esperando conexión...")
    conn, addr = s.accept() 
    with conn:
        print('Conectado a', addr) #envia un mensaje a la consola que la ip "x.x.x.x" se conecto
        while True:
            data = conn.recv(1024)
            if not data:
                break
            cedula = data.decode("utf-8", "strict") #se intento que ambos programas soportaran utf-8 pero no lo logramos
            respuesta = buscar_cedula(cedula) # le envia la cedula al cliente
            conn.sendall(respuesta.encode('utf-8')) #envia la respuesta, es decir el cliente da la cedula y le envia el nombre
