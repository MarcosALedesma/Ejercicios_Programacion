import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from api.dnd_api import *

def obtener_razas():
    razas_data = api_obtener_races()
    razas = []
    for raza in razas_data['results']:
        razas.append({
            'index': raza['index'],
            'nombre': raza['name']  
        })
    return razas

def obtener_detalle_raza(race_index):
    detalle = api_obtener_race_detalle(race_index)
    return {
        'nombre': detalle.get('name', ''),
        'edad': detalle.get('age', ''),
        'alineamiento': detalle.get('alignment', ''),
        'tamaño': detalle.get('size_description', ''),
        'descripcion': detalle.get('language_desc', ''), 
        'rasgos': [trait['name'] for trait in detalle.get('traits', [])]
    }

def obtener_clases():
    clases_data = api_obtener_classes()
    clases = []
    for clase in clases_data['results']:
        clases.append({
            'index': clase['index'],
            'nombre': clase['name']  
        })
    return clases

def obtener_detalle_clase(class_index):
    detalle = api_obtener_class_detalle(class_index)
    return {
        'nombre': detalle.get('name', ''),
        'dado_de_golpe': detalle.get('hit_die', ''),
        'competencias': [prof['name'] for prof in detalle.get('proficiencies', [])],
        'competencias_elegibles': detalle.get('proficiency_choices', []),
        'salvaciones': [st['name'] for st in detalle.get('saving_throws', [])]
    }

def obtener_ability_scores():
    abilities_data = api_obtener_ability_scores()
    abilities = []
    for ability in abilities_data['results']:
        abilities.append({
            'index': ability['index'],
            'nombre': ability['name']  
        })
    return abilities

def obtener_detalle_ability_score(score_index):
    detalle = api_obtener_ability_score_detalle(score_index)
    return {
        'nombre': detalle.get('name', ''),
        'nombre_completo': detalle.get('full_name', ''),
        'descripcion': ', '.join(detalle.get('desc', []))
    }
