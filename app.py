from flask import Flask, jsonify, render_template
import random
import socket
from pokeneas import POKENEAS

app = Flask(__name__)

@app.route('/api/pokenea', methods=['GET'])
def get_random_pokenea():
    pokenea = random.choice(POKENEAS)
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": socket.gethostname()
    }
    return jsonify(response)

@app.route('/pokenea', methods=['GET'])
def show_pokeneas():
    return render_template('pokenea.html', pokeneas=POKENEAS, contenedor_id=socket.gethostname())

if __name__ == '__main__':
    app.run(debug=True)