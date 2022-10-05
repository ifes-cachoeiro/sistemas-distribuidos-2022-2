import socket
import _thread
import json

DEBUG = True
PORT = 5000  # Porta que o Servidor esta
LISTA_USUARIO = []

def adicionar_usuario(usuario, cliente):
    novo_usuario = {}
    novo_usuario["nome"] = usuario["nome"]
    novo_usuario["conexao"] = cliente
    novo_usuario["id_sala"] = usuario["id_sala"]
    LISTA_USUARIO.append(novo_usuario)

def chat_server(udp):
    print(f"Starting UDP Server on port {PORT}")
    orig = ("", PORT)
    udp.bind(orig)
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode('utf-8')
        if DEBUG:
            print(f"{msg_decoded}")
        try:
            string_dict = json.loads(msg_decoded)
            if string_dict["acao"] == 1:
                adicionar_usuario(string_dict, cliente)
                msg = {
                    "acao": 1,
                    "nome": string_dict["nome"],
                    "id_sala": string_dict["id_sala"],
                    "status": 1
                }
                msg_json = json.dumps(msg)
                if DEBUG:
                    print(f"{msg_json} -> {cliente}")
                udp.sendto(msg_json.encode("utf-8"), cliente)
            elif string_dict["acao"] == 2:
                pass
            elif string_dict["acao"] == 3:
                pass
        except Exception as ex:
            pass
    udp.close()

def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    chat_server(udp)

if __name__ == "__main__":
    main()
