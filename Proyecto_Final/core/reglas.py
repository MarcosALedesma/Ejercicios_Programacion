import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.dnd_api import *

def obtener_categorias_reglas():
    """Obtiene las categorías principales de reglas"""
    categorias_data = api_obtener_categorias_reglas()
    categorias = []
    for categoria in categorias_data['results']:
        categorias.append({
            'index': categoria['index'],
            'nombre': categoria['name']
        })
    return categorias

def obtener_secciones_reglas():
    """Obtiene las secciones de reglas disponibles"""
    secciones_data = api_obtener_reglas()
    secciones = []
    for seccion in secciones_data['results']:
        secciones.append({
            'index': seccion['index'],
            'nombre': seccion['name']
        })
    return secciones

def obtener_detalle_regla(rule_index):
    """Obtiene el detalle completo de una regla"""
    detalle = api_obtener_regla_detalle(rule_index)
    
    return {
        'nombre': detalle.get('name', ''),
        'indice': detalle.get('index', ''),
        'descripcion': detalle.get('desc', ''),
        'url': detalle.get('url', '')
    }

def obtener_reglas_basicas():
    """Obtiene reglas básicas importantes para nuevos jugadores"""
    reglas_basicas = [
        'ability-checks',
        'saving-throws', 
        'advantage-and-disadvantage',
        'proficiency-bonus',
        'combat',
        'movement',
        'actions-in-combat',
        'cover'
    ]
    
    reglas = []
    for regla_index in reglas_basicas:
        try:
            detalle = obtener_detalle_regla(regla_index)
            reglas.append(detalle)
       except:
            continue
            
    return reglas
