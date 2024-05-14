# cliente.py
from xmlrpc.client import ServerProxy

# Crea un proxy para el servidor XML-RPC
proxy = ServerProxy("http://172.30.154.163:12345")

# Llama a las funciones en el servidor y muestra los resultados
resultado_suma = proxy.suma(10, 5)
resultado_resta = proxy.resta(20, 8)
resultado_multiplicacion = proxy.multiplicacion(4, 8)
resultado_division = proxy.division(40, 8)

print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)
print("Resultado de la multiplicación:", resultado_multiplicacion)
print("Resultado de la división:", resultado_division)
