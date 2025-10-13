import requests

BASE_URL = "https://www.dnd5eapi.co/api"

def get_classes():
    #Obtiene la lista de clases disponibles#
    result = requests.get(f"{BASE_URL}/classes")
    result.raise_for_status()
    return result.json()["results"]

def get_class_details(class_name):
    #Obtiene los detalles de una clase específica#
    result = requests.get(f"{BASE_URL}/classes/{class_name.lower()}")
    result.raise_for_status()
    return result.json()



def get_monsters(limit=10):
    #Obtiene una lista de monstruos#
    result = requests.get(f"{BASE_URL}/monsters?limit={limit}")
    result.raise_for_status()
    return result.json()["results"]

def get_monster_details(monster_name):
    #Obtiene detalles de un monstruo específico#
    monster_id = monster_name.lower().replace(" ", "-")
    result = requests.get(f"{BASE_URL}/monsters/{monster_id}")
    result.raise_for_status()
    print(result)
    return result.json()
monster_namea=input("a")
get_monster_details(monster_namea)