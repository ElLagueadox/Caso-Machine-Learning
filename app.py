from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Carga el modelo preentrenado
model = joblib.load('modelo.pkl')

# Definir el orden de los features que el modelo espera
EXPECTED_FEATURES = ['Cuentas', 'TC', 'TxsDebAtm', 'FacDebAtm', 'CUPO',
                     'TxsDebCom', 'FacDebCom', 'Ctacte', 'Debito',
                     'ColL2T0', 'Hipotecario', 'Fac', 'FacCN',
                     'ColL2CC', 'FacCCPC', 'Internauta', 'Col',
                     'PagoNac', 'FacCCOT', 'ColMx']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Extraer los features en el orden adecuado
    try:
        features = [data[feature] for feature in EXPECTED_FEATURES]
    except KeyError as e:
        return jsonify({'error': f'Falta el feature {e} en la solicitud'}), 400

    # Realizar la predicción
    prediction = model.predict([features])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
