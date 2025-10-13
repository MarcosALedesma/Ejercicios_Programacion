'''
import requests

URL = "https://www.dnd5eapi.co/api/2014/monsters/"

datos = requests.get(URL).json()

for monstruo in datos["results"]:
    print(monstruo["index"]) 

    detalle_url = f"{URL}{monstruo['index']}"
    detalle = requests.get(detalle_url).json()

    print("Challenge Rating:", detalle["challenge_rating"])
    print("-" * 40)
'''

import requests
import json
import time

URL = "https://www.dnd5eapi.co/api/2014/monsters/"

# Descargar lista de monstruos
lista = requests.get(URL).json()["results"]

todos = []

for i, monstruo in enumerate(lista):
    detalle = requests.get(URL + monstruo["index"]).json()
    todos.append({
        "index": monstruo["index"],
        "name": detalle["name"],
        "challenge_rating": detalle["challenge_rating"]
    })
    print(f"{i+1}/{len(lista)} - {detalle['name']}")
    time.sleep(0.1)  # para no sobrecargar la API

# Guardar en archivo
print(todos)
with open("monstruos.json", "w", encoding="utf-8") as f:
    json.dump(todos, f, indent=2, ensure_ascii=False)
