import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.dnd_api import *
from core.traductor import traductora

def obtener_tipos_daño():
    damage_data = api_obtener_damage()
    tipos = []
    for damage in damage_data['results']:
        tipos.append({
            'index': damage['index'],
            'nombre': traductora(damage['name'])
        })
    return tipos

def obtener_detalle_daño(damage_index):
    detalle = api_obtener_damage_detalle(damage_index)
    return {
        'nombre': traductora(detalle.get('name', '')),
        'descripcion': traductora(', '.join(detalle.get('desc', [])))
    }