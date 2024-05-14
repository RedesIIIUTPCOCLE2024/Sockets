# Importamos la clase SimpleXMLRPCServer del módulo xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
# Definimos un diccionario con cédulas y nombres
cedulas = {
    "2-752-1786": "Elian Gonzalez",
    "2-100-1234": "Juan Tapia",
    "2-752-681": "Kevin Santamaria",
    "2-752-1787": "Elian Gonzalez",
    "2-123-1234": "Mario Jaen"
}
# Definimos una función que toma una cédula como entrada y devuelve el nombre asociado si la encuentra en el diccionario
# de lo contrario devuelve un mensaje indicando que la cédula no se encontró
def entregar_cedulas(cedula):
    return cedulas.get(cedula, "La cedula no se encontró")
# Creamos una instancia del servidor XML-RPC en localhost y en el puerto 12345
with SimpleXMLRPCServer(('localhost', 12345)) as server:
    # Imprimimos un mensaje indicando que el servidor está escuchando en el puerto 12345
    print("El servidor XML-RPC está escuchando en el puerto 12345")
    # Registramos la función "entregar_cedulas" para que esté disponible a través del servidor con el mismo nombre
    server.register_function(entregar_cedulas, "entregar_cedulas")
    # Mantenemos el servidor en funcionamiento indefinidamente
    server.serve_forever()
