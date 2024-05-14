from flask import Flask, request, jsonify

app = Flask(__name__)

# Diccionario con los datos de la cedula que ingresemos, de no ser asi dara un mensaje de error
datos_personales = {
    "2-752-1787": {
        "nombre": "Elian Gonzalez",
        "fecha_nacimiento": "2003-10-14"
    },
    "2-100-1234": {
        "nombre": "Juan Tapia",
        "fecha_nacimiento": "1996-11-12"
    },
    "2-752-681": {
        "nombre": "Kevin Santamaria",
        "fecha_nacimiento": "2003-08-27"
    },
    "2-753-614": {
        "nombre": "Nicolas Pineda",
        "fecha_nacimiento": "2003-03-04"
    },
    "2-123-1234": {
        "nombre": "Mario Jaen",
        "fecha_nacimiento": "1993-02-18"
    }
}

# Ruta para manejar las solicitudes GET
@app.route('/info-personal', methods=['GET'])
def obtener_info_personal():
    # Obtener el número de cédula del parámetro de la solicitud
    cedula = request.args.get('cedula')
    # Verificar si la cédula está en los datos personales
    if cedula in datos_personales:
        # Obtener la información asociada a la cédula
        info = datos_personales[cedula]
        # Devolver la información en formato JSON
        return jsonify(info)
    else:
        # Si la cédula no está en los datos personales, devolver un mensaje de error
        return jsonify({'error': 'Información no encontrada'}), 404

if __name__ == '__main__':
    # Ejecutar el servidor en la IP y puerto especificados
    app.run(host='19---', port=12345)
