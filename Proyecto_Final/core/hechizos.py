import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.dnd_api import *

def obtener_hechizos():
    spells_data = api_obtener_spells()
    spells = []
    for spell in spells_data['results']:
        spells.append({
            'index': spell['index'],
            'nombre': spell['name']  
        })
    return spells

def obtener_detalle_hechizo(spell_index):
    detalle = api_obtener_spell_detalle(spell_index)
    return {
        'nombre': detalle.get('name', ''),
        'nivel': detalle.get('level', ''),
        'escuela': detalle.get('school', {}).get('name', ''),
        'tiempo_de_lanzamiento': detalle.get('casting_time', ''),
        'alcance': detalle.get('range', ''),
        'componentes': detalle.get('components', []),
        'materiales': detalle.get('material', ''),
        'duracion': detalle.get('duration', ''),
        'descripcion': ', '.join(detalle.get('desc', [])),
        'clases': [clase['name'] for clase in detalle.get('classes', [])]
    }
