import requests

BASE_URL = "https://www.dnd5eapi.co"


#==== JUGADOR ====#
def api_obtener_races():
    respuesta = requests.get(f"{BASE_URL}/api/races")
    return respuesta.json()

def api_obtener_race_detalle(race_index):
    respuesta = requests.get(f"{BASE_URL}/api/races/{race_index}")
    return respuesta.json()
def api_obtener_classes():
    respuesta = requests.get(f"{BASE_URL}/api/classes")
    return respuesta.json()

def api_obtener_class_detalle(class_index):
    respuesta = requests.get(f"{BASE_URL}/api/classes/{class_index}")
    return respuesta.json()

def api_obtener_equip_ini(class_index):
    respuesta = requests.get(f"{BASE_URL}/api/classes/{class_index}/starting-equipment")
    return respuesta.json()

def api_obtener_ability_scores():
    respuesta = requests.get(f"{BASE_URL}/api/ability-scores")
    return respuesta.json()
#==== ITEMS ====#

#==== DAÑO ====#
def api_obtener_damage():
    respuesta = requests.get(f"{BASE_URL}/api/damage-types")
    return respuesta.json()

def api_obtener_damage_detalle(damage_index):
    respuesta = requests.get(f"{BASE_URL}/api/damage-types/{damage_index}")
    return respuesta.json()


#==== HECHIZOS ====#
#==== MONSTRUOS ====#
def api_obtener_races():
    respuesta = requests.get(f"{BASE_URL}/api/races")
    return respuesta.json()
