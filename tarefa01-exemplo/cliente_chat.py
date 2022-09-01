import socket
import sys
import _thread
import json
import time

HOST = ""  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
IP_SERVIDOR = "10.0.1.10"
NICKNAME = None
ID_SALA = None
ID_MSG = 1
ENTROU_SALA = False

def server(udp):
    orig = ("", PORT)
    udp.bind(orig)
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode('utf-8')
        string_dict = json.loads(msg_decoded)
        if string_dict["acao"] == 1:
            if string_dict["id_sala"] == ID_SALA:
                if string_dict["status"] == 1:
                    ENTROU_SALA = True
        elif string_dict["acao"] == 2:
            pass
        elif string_dict["acao"] == 3:
            pass
        print(f"-> #{cliente}# {string_dict}")


def client():
    print(f"Starting UDP Server on port {PORT}")
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _thread.start_new_thread(server, (udp,))
    print("Type q to exit")
    message = None
    dest = (IP_SERVIDOR, PORT)
    nome = input("Informe o seu nickname-> ")
    try:
        sala = int(input("Informe o nome da sala que deseja entrar-> "))
        ID_SALA = sala
        entrar_sala = { 
            "acao": 1, 
            "nome": nome,
            "id_sala": sala
        }
        string_json = json.dumps(entrar_sala)
        udp.sendto(string_json.encode('utf-8'), dest)
    except Exception as ex:
        sys.exit(0)
    
    count = 0
    print("Aguardando confirmacao.")
    while True:
        if not ENTROU_SALA:
            count += 1
        else:
            break
        if count == 10:
            sys.exit(0)
        time.sleep(1)

    while message != "q":
        message = input("-> ")
        msg = {
            "acao": 3,
            "nome": NICKNAME,
            "id_sala": ID_SALA,
            "id_msg": ID_MSG,
            "msg": message
        }
        string_json = json.dumps(msg)
        udp.sendto(string_json.encode('utf-8'), dest)
        ID_MSG += 1
    udp.close()

if __name__ == "__main__":
    client()
