import requests

BASE_URL = "https://www.dnd5eapi.co"

def obtener_races():
    response = requests.get(f"{BASE_URL}/api/races")
    return response.json()

def obtener_race_detalle(race_index):
    response = requests.get(f"{BASE_URL}/api/races/{race_index}")
    return response.json()

def obtener_classes():
    response = requests.get(f"{BASE_URL}/api/classes")
    return response.json()

def obtener_class_detalle(class_index):
    response = requests.get(f"{BASE_URL}/api/classes/{class_index}")
    return response.json()

def obtener_ability_scores():
    response = requests.get(f"{BASE_URL}/api/ability-scores")
    return response.json()
