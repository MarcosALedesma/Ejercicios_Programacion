import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.dnd_api import *

BASE_IMAGE_URL = "https://www.dnd5eapi.co"  # imagenes

def obtener_monstruos():
    monsters_data = api_obtener_monsters()
    monsters = []
    for monster in monsters_data['results']:
        monsters.append({
            'index': monster['index'],
            'nombre': monster['name']
        })
    return monsters

def obtener_detalle_monstruo(monster_index):
    detalle = api_obtener_monster_detalle(monster_index)

    imagen_url = detalle.get('image')
    if imagen_url and imagen_url.startswith("/"):
        imagen_url = BASE_IMAGE_URL + imagen_url

    return {
        'nombre': detalle.get('name', ''),
        'tamaño': detalle.get('size', ''),
        'tipo': detalle.get('type', ''),
        'alineamiento': detalle.get('alignment', ''),
        'clase_de_armadura': detalle.get('armor_class', [{}])[0].get('value', ''),
        'puntos_de_golpe': detalle.get('hit_points', ''),
        'cr': detalle.get('challenge_rating', ''), 
        'desplazamiento': detalle.get('speed', {}),
        'caracteristicas': {
            'fuerza': detalle.get('strength', ''),
            'destreza': detalle.get('dexterity', ''),
            'constitucion': detalle.get('constitution', ''),
            'inteligencia': detalle.get('intelligence', ''),
            'sabiduria': detalle.get('wisdom', ''),
            'carisma': detalle.get('charisma', '')
        },
        'acciones': [{
            'nombre': action.get('name', ''),
            'descripcion': action.get('desc', '')
        } for action in detalle.get('actions', [])],
        'imagen': imagen_url 
    }
