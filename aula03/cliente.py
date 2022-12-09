from requests import post, get
from pprint import pprint

url = "http://127.0.0.1:8080"

contatos = [
    {"id_contato": 1, "nome": "Amanda", "endereco": "Rua 456"},
    {"id_contato": 2, "nome": "Carolina", "endereco": "Rua asd"},
    {"id_contato": 3, "nome": "Daniel", "endereco": "Rua dfg"},
    {"id_contato": 4, "nome": "Viviane", "endereco": "Rua 4d"},
    {"id_contato": 5, "nome": "Theo", "endereco": "Rua dfgg6"},
    {"id_contato": 6, "nome": "Ricardo", "endereco": "Rua dfgg"},
    {"id_contato": 7, "nome": "Antonio", "endereco": "Rua dfggd"},
]

for contato in contatos:
    post(f"{url}/api/v1/contato", json=contato)

r = get(f"{url}/api/v1/contato")
pprint(r.json())
