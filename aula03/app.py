from flask import Flask, jsonify, request

app = Flask(__name__)

lista_contatos = []
lista_clientes = []


@app.route("/")
def inicio():
    return "<h1> OLA MUNDO </h1>", 200


@app.route("/inicio")
@app.route("/begin")
def inicio2():
    return "<h1> OLA MUNDO 2</h1>"


@app.route("/api/v1/contatos", methods=["POST", "GET"])
@app.route(
    "/api/v1/contatos/<int:id_contato>", methods=["GET", "PUT", "PATCH", "DELETE"]
)
def contato(id_contato=None):
    if request.method == "GET":
        if id_contato is not None:
            return jsonify({"id_contato": id_contato, "nome": "teste"}), 200
        else:
            return jsonify(lista_contatos), 200
    elif request.method == "POST":
        contato = request.json
        lista_contatos.append(contato)
        return "", 201


@app.route("/api/v1/clientes", methods=["POST", "GET"])
@app.route(
    "/api/v1/clientes/<int:id_cliente>", methods=["GET", "PUT", "PATCH", "DELETE"]
)
def cliente(id_cliente):
    if request.method == "GET":
        if id_cliente is not None:
            return jsonify({"id_cliente": id_cliente, "nome": "teste"}), 200
        else:
            return jsonify(lista_clientes), 200
    elif request.method == "POST":
        cliente = request.json
        lista_clientes.append(cliente)
        return "", 201


app.run(host="0.0.0.0", port=8080, debug=True)
