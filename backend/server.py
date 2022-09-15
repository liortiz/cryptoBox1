from flask import Flask, jsonify

from classCryptosystems.desplazamiento import desplazamiento

app = Flask(__name__)

@app.route('/desplazamiento/encript/<data>&<k>', methods=['GET'])
def desplazamineto_encript(data,k):
    data = str(data)
    k = int(k)
    textEncrypt =  desplazamiento(data,k).encrypt()
    response = jsonify({'TextoEncriptado': textEncrypt})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/desplazamiento/desencript/<data>&<k>', methods=['GET'])
def desplazamineto_desencript(data,k):
    data = str(data)
    k = int(k)
    textDesncrypt =  desplazamiento(data,k).desencrypt()
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

if __name__ == "__main__":
    app.run(debug=True)