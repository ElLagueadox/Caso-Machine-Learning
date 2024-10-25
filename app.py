from flask import Flask, request, jsonify, render_template
import pickle

# Cargar el modelo
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

# Ruta para la página web
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Recibir las características del formulario
        cuentas = float(request.form["Cuentas"])
        tc = float(request.form["TC"])
        txs_deb_atm = float(request.form["TxsDebAtm"])
        fac_deb_atm = float(request.form["FacDebAtm"])
        cupo = float(request.form["CUPO"])
        txs_deb_com = float(request.form["TxsDebCom"])
        fac_deb_com = float(request.form["FacDebCom"])
        ctacte = float(request.form["Ctacte"])
        debito = float(request.form["Debito"])
        col_l2t0 = float(request.form["ColL2T0"])
        hipotecario = float(request.form["Hipotecario"])
        fac = float(request.form["Fac"])
        fac_cn = float(request.form["FacCN"])
        col_l2cc = float(request.form["ColL2CC"])
        fac_ccpc = float(request.form["FacCCPC"])
        internauta = float(request.form["Internauta"])
        col = float(request.form["Col"])
        pago_nac = float(request.form["PagoNac"])
        fac_ccot = float(request.form["FacCCOT"])
        col_mx = float(request.form["ColMx"])

        # Crear lista de características para la predicción
        features = [cuentas, tc, txs_deb_atm, fac_deb_atm, cupo,
                    txs_deb_com, fac_deb_com, ctacte, debito,
                    col_l2t0, hipotecario, fac, fac_cn,
                    col_l2cc, fac_ccpc, internauta, col,
                    pago_nac, fac_ccot, col_mx]

        # Realizar la predicción
        prediction = model.predict([features])[0]

        # Convertir la predicción numérica en "sí" o "no"
        prediction = "Dualidad: Sí" if prediction == 1 else "Dualidad: No"

        # Renderizar el resultado en la misma página
        return render_template("index.html", prediction=prediction)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)