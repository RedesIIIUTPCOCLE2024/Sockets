import xmlrpc.client

# Direccion y puerto del servidor XML-RPC
direccion_servidor = 'http://172.30.154.169:12345'  # Cambia localhost al nombre o dirección IP del servidor si es necesario

# Creamos un cliente XML-RPC
cliente = xmlrpc.client.ServerProxy(direccion_servidor)

# Funcion para solicitar y mostrar el nombre asociado a una cedula ingresada
def obtener_nombre_por_cedula():
    cedula = input("Ingrese el número de cédula: ")
    # Llamamos a la funcion "entregar_cedulas" del servidor y pasamos el numero de cedula
    nombre = cliente.entregar_cedulas(cedula)
    print("El nombre asociado a la cédula {} es: {}".format(cedula, nombre))

# Ejecutamos la funcion para interactuar con el servidor
obtener_nombre_por_cedula()
