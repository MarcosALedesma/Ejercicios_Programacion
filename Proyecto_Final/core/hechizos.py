import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.dnd_api import *
from core.traductor import traductora

def obtener_hechizos():
    spells_data = api_obtener_spells()
    spells = []
    for spell in spells_data['results']:
        spells.append({
            'index': spell['index'],
            'nombre': traductora(spell['name'])
        })
    return spells

def obtener_detalle_hechizo(spell_index):
    detalle = api_obtener_spell_detalle(spell_index)
    return {
        'nombre': traductora(detalle.get('name', '')),
        'nivel': detalle.get('level', ''),
        'escuela': traductora(detalle.get('school', {}).get('name', '')),
        'tiempo_de_lanzamiento': detalle.get('casting_time', ''),
        'alcance': detalle.get('range', ''),
        'componentes': detalle.get('components', []),
        'materiales': traductora(detalle.get('material', '')),
        'duracion': detalle.get('duration', ''),
        'descripcion': traductora(', '.join(detalle.get('desc', []))),
        'clases': [traductora(clase['name']) for clase in detalle.get('classes', [])]
    }