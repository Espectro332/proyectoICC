from flask import Flask
from flask import jsonify
from flask import render_template

from formcheck import generar_casos

app = Flask(__name__)


@app.route("/")
def inicio():

    return render_template(
        "index.html"
    )


@app.route("/generar")
def generar():

    datos = generar_casos()

    return jsonify(datos)


if __name__ == "__main__":

    app.run(debug=True)