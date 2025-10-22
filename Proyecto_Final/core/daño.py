import sys
import os
from traductor import traductora

# Agregar el directorio raíz al path para importar desde api
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from api.dnd_api import api_obtener_damage, api_obtener_damage_detalle

def obtener_daño():
    data=api_obtener_damage()
    resultado = {}

    for d in data["results"]:
        detalle = api_obtener_damage_detalle(d["index"])
        nombre = detalle['name']

        if detalle.get('desc'):
            descripcion = detalle['desc'][0]
            descripcion = traductora(descripcion)
            nombre = traductora(nombre)
        else:
            descripcion = ''

        print(f'{nombre}: "{descripcion}"')
        resultado[nombre] = descripcion

    return resultado

if __name__ == "__main__":
    daños = obtener_daño()