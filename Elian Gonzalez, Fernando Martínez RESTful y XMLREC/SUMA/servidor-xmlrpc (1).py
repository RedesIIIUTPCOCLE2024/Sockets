
# servidor.py
from xmlrpc.server import SimpleXMLRPCServer

# Define una función para sumar dos números
def suma(a, b):
    return a + b

# Define una función para restar dos números
def resta(a, b):
    return a - b

# Define una función para multiplicar dos números
def multiplicacion(a, b):
    return a * b

# Define una función para dividir dos números
def division(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    else:
        return a / b

# Crea el servidor XML-RPC
server = SimpleXMLRPCServer(("172.30.154.169", 12345), allow_none=True)

# Registra las funciones en el servidor
server.register_function(suma, "suma")
server.register_function(resta, "resta")
server.register_function(multiplicacion, "multiplicacion")
server.register_function(division, "division")

print("Servidor XML-RPC en ejecución en 172.30.154.169:12345...")

# Inicia el servidor
server.serve_forever()
