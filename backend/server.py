from flask import Flask, jsonify


from classCryptosystems.desplazamiento import desplazamiento
from classCryptosystems.permutacion import permutacion

app = Flask(__name__)

# AFIN 
# DESPLAZAMIENTO 

@app.route('/desplazamiento/encript/<data>&<p>', methods=['GET'])
def desplazamineto_encript(data,p):
    data = str(data)
    p = int(p)
    textEncrypt =  desplazamiento(data,p).encrypt()
    response = jsonify({'TextoEncriptado': textEncrypt})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/desplazamiento/desencript/<data>&<p>', methods=['GET'])
def desplazamineto_desencript(data,p):
    data = str(data)
    p = int(p)
    textDesncrypt =  desplazamiento(data,p).desencrypt()
    response = jsonify({'TextoDesencriptado': textDesncrypt})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/desplazamiento/analisis/<data>', methods=['GET'])
def desplazamineto_analisis(data):
    data = str(data)
    analisis =  desplazamiento(data,1).cryptanalysis()
    response = jsonify({'Analisis': analisis})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# HILL 
# PERMUTACION 
@app.route('/permutacion/encript/<data>&<p>', methods=['GET'])
def permutacion_encript(data,p):
    textEncrypt =  permutacion(data,p).encrypt()
    response = jsonify({'TextoEncriptado': textEncrypt})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/permutacion/desencript/<data>&<p>', methods=['GET'])
def permutacion_desencript(data,p):
    textDesncrypt =  permutacion(data,p).desencrypt()
    response = jsonify({'TextoDesencriptado': textDesncrypt})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/permutacion/analisis/<data>', methods=['GET'])
def permutacion_analisis(data):
    analisis =  permutacion(data,[]).cryptanalysis()
    response = jsonify({'Analisis': analisis})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# SUSTITUCION 
# VIGENERE



if __name__ == "__main__":
    app.run(debug=True)