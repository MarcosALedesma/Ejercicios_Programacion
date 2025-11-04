import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.dnd_api import *

def obtener_tipos_daño():
    damage_data = api_obtener_damage()
    tipos = []
    for damage in damage_data['results']:
        tipos.append({
            'index': damage['index'],
            'nombre': damage['name'] 
        })
    return tipos

def obtener_detalle_daño(damage_index):
    detalle = api_obtener_damage_detalle(damage_index)
    return {
        'nombre': detalle.get('name', ''),
        'descripcion': ', '.join(detalle.get('desc', []))
    }
