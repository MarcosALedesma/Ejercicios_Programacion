import requests

BASE_URL = "https://www.dnd5eapi.co/api"


#===== JUGADOR / CLASES =====#

def api_obtener_races():
    return requests.get(f"{BASE_URL}/races").json()

def api_obtener_race_detalle(race_index):
    return requests.get(f"{BASE_URL}/races/{race_index}").json()

def api_obtener_classes():
    return requests.get(f"{BASE_URL}/classes").json()

def api_obtener_class_detalle(class_index):
    return requests.get(f"{BASE_URL}/classes/{class_index}").json()

def api_obtener_ability_scores():
    return requests.get(f"{BASE_URL}/ability-scores").json()

def api_obtener_ability_score_detalle(score_index):
    return requests.get(f"{BASE_URL}/ability-scores/{score_index}").json()

def api_obtener_equip_ini(class_index):
    return requests.get(f"{BASE_URL}/classes/{class_index}/starting-equipment").json()



#===== ITEMS / EQUIPO =====#

def api_obtener_equipment():
    return requests.get(f"{BASE_URL}/equipment").json()

def api_obtener_equipment_detalle(equip_index):
    return requests.get(f"{BASE_URL}/equipment/{equip_index}").json()

def api_obtener_magic_items():
    return requests.get(f"{BASE_URL}/magic-items").json()

def api_obtener_magic_item_detalle(item_index):
    return requests.get(f"{BASE_URL}/magic-items/{item_index}").json()

def api_obtener_weapon_properties():
    return requests.get(f"{BASE_URL}/weapon-properties").json()



#===== DAÑO =====#

def api_obtener_damage():
    return requests.get(f"{BASE_URL}/damage-types").json()

def api_obtener_damage_detalle(damage_index):
    return requests.get(f"{BASE_URL}/damage-types/{damage_index}").json()



#===== HECHIZOS =====#

def api_obtener_spells():
    return requests.get(f"{BASE_URL}/spells").json()

def api_obtener_spell_detalle(spell_index):
    return requests.get(f"{BASE_URL}/spells/{spell_index}").json()

def api_obtener_magic_schools():
    return requests.get(f"{BASE_URL}/magic-schools").json()



#===== MONSTRUOS =====#

def api_obtener_monsters():
    return requests.get(f"{BASE_URL}/monsters").json()

def api_obtener_monster_detalle(monster_index):
    return requests.get(f"{BASE_URL}/monsters/{monster_index}").json()
