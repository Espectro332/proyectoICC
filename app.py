from flask import Flask, render_template, jsonify
from formcheck import generar_casos

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/generar")
def generar():
    resultados = generar_casos()
    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)