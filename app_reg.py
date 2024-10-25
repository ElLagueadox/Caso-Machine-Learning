from flask import Flask, request, jsonify, render_template
import pickle

# Cargar el modelo
with open("modelo_regresion.pkl", "rb") as f:
    modelo_regresion = pickle.load(f)

app = Flask(__name__)

# Ruta para la página web
@app.route("/", methods=["GET", "POST"])
def index_reg():
    if request.method == "POST":
        # Recibir las características del formulario
        eecc_nac = float(request.form["EeccNac"])
        col_l1te = float(request.form["ColL1TE"])
        col = float(request.form["Col"])
        pago_nac = float(request.form["PagoNac"])
        antiguedad = float(request.form["Antiguedad"])
        col_l1t0 = float(request.form["ColL1T0"])
        edad = float(request.form["Edad"])
        fac = float(request.form["Fac"])
        fac_cn = float(request.form["FacCN"])
        cupo = float(request.form["CUPO"])
        txs = float(request.form["Txs"])
        txs_cn = float(request.form["TxsCN"])
        tc = float(request.form["TC"])
        fac_ccpc = float(request.form["FacCCPC"])
        renta = float(request.form["Renta"])
        col_l2t0 = float(request.form["ColL2T0"])
        fac_pat = float(request.form["FacPAT"])
        col_mx = float(request.form["ColMx"])
        txs_pat = float(request.form["TxsPAT"])
        uso_li = float(request.form["UsoLI"])

        # Crear lista de características para la predicción
        features = [eecc_nac, col_l1te, col, pago_nac, antiguedad,
                    col_l1t0, edad, fac, fac_cn, cupo,
                    txs, txs_cn, tc, fac_ccpc, renta,
                    col_l2t0, fac_pat, col_mx, txs_pat, uso_li]

        # Realizar la predicción
        prediction = modelo_regresion.predict([features])[0]
        prediction = round(prediction, 2)  # Redondear el resultado a dos decimales

        # Renderizar el resultado en la misma página
        return render_template("index_reg.html", prediction=prediction)

    return render_template("index_reg.html")

if __name__ == "__main__":
    app.run(debug=True)