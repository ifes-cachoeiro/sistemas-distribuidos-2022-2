import socket
import _thread
import json

HOST = ""  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

def server(udp):
    print(f"Starting UDP Server on port {PORT}")
    orig = ("", PORT)
    udp.bind(orig)
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode('utf-8')
        string_dict = json.loads(msg_decoded)
        print(f"-> #{cliente}# {string_dict}")
    udp.close()

def client():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _thread.start_new_thread(server, (udp,))
    print("Type q to exit")
    message = None
    while message != "q":
        ip_dest = input("destino -> ")
        dest = (ip_dest, PORT)
        message = input("-> ")
        msg = {}
        msg['destino'] = ip_dest
        msg['body'] = message
        string_json = json.dumps(msg)
        udp.sendto(string_json.encode('utf-8'), dest)
    udp.close()

if __name__ == "__main__":
    client()
