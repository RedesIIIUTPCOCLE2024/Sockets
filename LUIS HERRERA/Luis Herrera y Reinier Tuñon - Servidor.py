import socket

# Creamos un diccionario con las cedulas y las asociamos a nombres
datos_personas = {
    "7-714-237": "Luis Herrera",
    "1": "Barzoom220pty",
    "2": "famp03", 
    "3": "ya comiste ya te vas"
}
    # Creamos la funcion para verificar la cedula
def verif_cedula(cedula):
    if cedula in datos_personas:
        return "El nombre asociado a la cédula especificada es: " + datos_personas[cedula]
    else:
        return "Cédula no encontrada"

def main():
    # Configurar el servidor
    host = '172.30.154.162'
    port = 12345

    # Crear el socket del servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(5)  # Permitir hasta 5 conexiones en cola

    print("Servidor de Datos iniciado.")

    while True:
        # Esperar por una conexión
        cliente, direccion = servidor.accept()
        print("Conexión establecida desde:", direccion)

        # Recibir la cédula del cliente
        cedula = cliente.recv(1024).decode('utf-8')

        # Procesar la cédula y obtener el nombre asociado
        nombre = verif_cedula(cedula)

        # Enviar el nombre al cliente
        cliente.send(nombre.encode('utf-8'))
        

if __name__ == "__main__":
    main()
