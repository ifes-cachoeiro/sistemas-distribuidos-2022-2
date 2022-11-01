from flask import Flask, jsonify, request

app = Flask(__name__)

lista_contato = []

@app.route("/")
def inicio():
    return "<h1> OLA MUNDO </h1>"


@app.route("/inicio")
def inicio2():
    return "<h1> OLA MUNDO 2</h1>"


@app.route("/api/v1/contato", methods=["POST", "GET"])
@app.route("/api/v1/contato/<int:id_contato>", methods=["GET", "PUT", "DELETE"])
def get_contato(id_contato=None):
    if request.method == "GET":
        if id_contato is not None:
            return jsonify({"id_contato": id_contato, "nome": "teste"}), 200
        else:
            return jsonify(lista_contato), 200
    elif request.method == "POST":
        contato = request.json
        lista_contato.append(contato)
        return "", 201


app.run(host="0.0.0.0", port=8080, debug=True)
