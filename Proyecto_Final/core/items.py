import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.dnd_api import *
from core.traductor import traductora

def obtener_equipo():
    equipo_data = api_obtener_equipment()
    equipo = []
    for item in equipo_data['results']:
        equipo.append({
            'index': item['index'],
            'nombre': traductora(item['name'])
        })
    return equipo

def obtener_detalle_equipo(equip_index):
    detalle = api_obtener_equipment_detalle(equip_index)
    return {
        'nombre': traductora(detalle.get('name', '')),
        'categoria': traductora(detalle.get('equipment_category', {}).get('name', '')),
        'costo': detalle.get('cost', {}),
        'peso': detalle.get('weight', ''),
        'descripcion': traductora(', '.join(detalle.get('desc', []))) if detalle.get('desc') else ''
    }

def obtener_objetos_magicos():
    items_data = api_obtener_magic_items()
    items = []
    for item in items_data['results']:
        items.append({
            'index': item['index'],
            'nombre': traductora(item['name'])
        })
    return items

def obtener_detalle_objeto_magico(item_index):
    detalle = api_obtener_magic_item_detalle(item_index)
    return {
        'nombre': traductora(detalle.get('name', '')),
        'tipo': traductora(detalle.get('equipment_category', {}).get('name', '')),
        'rareza': traductora(detalle.get('rarity', {}).get('name', '')),
        'descripcion': traductora(', '.join(detalle.get('desc', []))) if detalle.get('desc') else ''
    }