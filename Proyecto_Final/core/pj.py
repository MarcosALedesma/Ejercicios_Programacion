import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from api.dnd_api import *
from core.traductor import traductora

def obtener_razas():
    razas_data = api_obtener_races()
    razas = []
    for raza in razas_data['results']:
        razas.append({
            'index': raza['index'],
            'nombre': traductora(raza['name'])
        })
    return razas

def obtener_detalle_raza(race_index):
    detalle = api_obtener_race_detalle(race_index)
    return {
        'nombre': traductora(detalle.get('name', '')),
        'edad': traductora(detalle.get('age', '')),
        'alineamiento': traductora(detalle.get('alignment', '')),
        'tamaño': traductora(detalle.get('size_description', '')),
        'descripcion': traductora(', '.join(detalle.get('language_desc', ''))),
        'rasgos': [traductora(trait['name']) for trait in detalle.get('traits', [])]
    }

def obtener_clases():
    clases_data = api_obtener_classes()
    clases = []
    for clase in clases_data['results']:
        clases.append({
            'index': clase['index'],
            'nombre': traductora(clase['name'])
        })
    return clases

def obtener_detalle_clase(class_index):
    detalle = api_obtener_class_detalle(class_index)
    return {
        'nombre': traductora(detalle.get('name', '')),
        'dado_de_golpe': detalle.get('hit_die', ''),
        'competencias': [traductora(prof['name']) for prof in detalle.get('proficiencies', [])],
        'competencias_elegibles': detalle.get('proficiency_choices', []),
        'salvaciones': [traductora(st['name']) for st in detalle.get('saving_throws', [])]
    }

def obtener_ability_scores():
    abilities_data = api_obtener_ability_scores()
    abilities = []
    for ability in abilities_data['results']:
        abilities.append({
            'index': ability['index'],
            'nombre': traductora(ability['name'])
        })
    return abilities

def obtener_detalle_ability_score(score_index):
    detalle = api_obtener_ability_score_detalle(score_index)
    return {
        'nombre': traductora(detalle.get('name', '')),
        'nombre_completo': traductora(detalle.get('full_name', '')),
        'descripcion': traductora(', '.join(detalle.get('desc', [])))
    }
