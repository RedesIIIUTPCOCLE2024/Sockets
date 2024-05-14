import requests

def obtener_info(cedula):
    url = f'http://172.30.154.169:12345/info-personal?cedula={cedula}'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        info = respuesta.json()
        nombre = info.get('nombre')
        fecha_nacimiento = info.get('fecha_nacimiento')
        print(f"Nombre: {nombre}")
        print(f"Fecha de Nacimiento: {fecha_nacimiento}")
    else:
        print("Error: No se pudo obtener la información")

def main():
    cedula = input("Ingrese el número de cédula: ")
    obtener_info(cedula)

if __name__ == "__main__":
    main()

