import sys
import os

# Configurar el path para importar desde la raíz del proyecto
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Importar todas las funciones de los módulos core
from core.pj import (
    obtener_razas, 
    obtener_detalle_raza,
    obtener_clases,
    obtener_detalle_clase,
    obtener_ability_scores,
    obtener_detalle_ability_score
)

from core.items import (
    obtener_equipo,
    obtener_detalle_equipo,
    obtener_objetos_magicos,
    obtener_detalle_objeto_magico
)

from core.hechizos import (
    obtener_hechizos,
    obtener_detalle_hechizo
)

from core.monstruo import (
    obtener_monstruos,
    obtener_detalle_monstruo
)

from core.daño import (
    obtener_tipos_daño,
    obtener_detalle_daño
)

def test_pj():
    print("=== TEST PERSONAJES (PJ) ===")
    
    # Test razas
    print("\n1. Obteniendo razas...")
    razas = obtener_razas()
    print(f"Razas encontradas: {len(razas)}")
    for i, raza in enumerate(razas[:3]):  # Mostrar solo 3
        print(f"  {i+1}. {raza['nombre']} (index: {raza['index']})")
    
    # Test detalle de raza
    if razas:
        print(f"\n2. Obteniendo detalle de '{razas[0]['index']}'...")
        detalle = obtener_detalle_raza(razas[0]['index'])
        print(f"  Nombre: {detalle['nombre']}")
        print(f"  Edad: {detalle['edad'][:50]}...")  # Mostrar solo primeros 50 caracteres
        print(f"  Rasgos: {detalle['rasgos'][:3]}")  # Mostrar solo 3 rasgos
    
    # Test clases
    print("\n3. Obteniendo clases...")
    clases = obtener_clases()
    print(f"Clases encontradas: {len(clases)}")
    for i, clase in enumerate(clases[:3]):
        print(f"  {i+1}. {clase['nombre']} (index: {clase['index']})")
    
    # Test detalle de clase
    if clases:
        print(f"\n4. Obteniendo detalle de '{clases[0]['index']}'...")
        detalle = obtener_detalle_clase(clases[0]['index'])
        print(f"  Nombre: {detalle['nombre']}")
        print(f"  Dado de golpe: {detalle['dado_de_golpe']}")
        print(f"  Competencias: {detalle['competencias'][:3]}")  # Mostrar solo 3
    
    # Test ability scores
    print("\n5. Obteniendo ability scores...")
    abilities = obtener_ability_scores()
    print(f"Ability scores encontrados: {len(abilities)}")
    for ability in abilities:
        print(f"  - {ability['nombre']} (index: {ability['index']})")
    
    # Test detalle ability score
    if abilities:
        print(f"\n6. Obteniendo detalle de '{abilities[0]['index']}'...")
        detalle = obtener_detalle_ability_score(abilities[0]['index'])
        print(f"  Nombre: {detalle['nombre']}")
        print(f"  Descripción: {detalle['descripcion'][:100]}...")

def test_items():
    print("\n\n=== TEST ITEMS ===")
    
    # Test equipo
    print("\n1. Obteniendo equipo...")
    equipo = obtener_equipo()
    print(f"Equipos encontrados: {len(equipo)}")
    for i, item in enumerate(equipo[:3]):
        print(f"  {i+1}. {item['nombre']} (index: {item['index']})")
    
    # Test detalle equipo
    if equipo:
        print(f"\n2. Obteniendo detalle de '{equipo[0]['index']}'...")
        detalle = obtener_detalle_equipo(equipo[0]['index'])
        print(f"  Nombre: {detalle['nombre']}")
        print(f"  Categoría: {detalle['categoria']}")
        print(f"  Peso: {detalle['peso']}")
    
    # Test objetos mágicos
    print("\n3. Obteniendo objetos mágicos...")
    objetos_magicos = obtener_objetos_magicos()
    print(f"Objetos mágicos encontrados: {len(objetos_magicos)}")
    for i, item in enumerate(objetos_magicos[:3]):
        print(f"  {i+1}. {item['nombre']} (index: {item['index']})")
    
    # Test detalle objeto mágico
    if objetos_magicos:
        print(f"\n4. Obteniendo detalle de '{objetos_magicos[0]['index']}'...")
        detalle = obtener_detalle_objeto_magico(objetos_magicos[0]['index'])
        print(f"  Nombre: {detalle['nombre']}")
        print(f"  Rareza: {detalle['rareza']}")

def test_hechizos():
    print("\n\n=== TEST HECHIZOS ===")
    
    # Test hechizos
    print("\n1. Obteniendo hechizos...")
    hechizos = obtener_hechizos()
    print(f"Hechizos encontrados: {len(hechizos)}")
    for i, hechizo in enumerate(hechizos[:3]):
        print(f"  {i+1}. {hechizo['nombre']} (index: {hechizo['index']})")
    
    # Test detalle hechizo
    if hechizos:
        print(f"\n2. Obteniendo detalle de '{hechizos[0]['index']}'...")
        detalle = obtener_detalle_hechizo(hechizos[0]['index'])
        print(f"  Nombre: {detalle['nombre']}")
        print(f"  Nivel: {detalle['nivel']}")
        print(f"  Escuela: {detalle['escuela']}")
        print(f"  Descripción: {detalle['descripcion'][:100]}...")

def test_monstruos():
    print("\n\n=== TEST MONSTRUOS ===")
    
    # Test monstruos
    print("\n1. Obteniendo monstruos...")
    monstruos = obtener_monstruos()
    print(f"Monstruos encontrados: {len(monstruos)}")
    for i, monstruo in enumerate(monstruos[:3]):
        print(f"  {i+1}. {monstruo['nombre']} (index: {monstruo['index']})")
    
    # Test detalle monstruo
    if monstruos:
        print(f"\n2. Obteniendo detalle de '{monstruos[0]['index']}'...")
        detalle = obtener_detalle_monstruo(monstruos[0]['index'])
        print(f"  Nombre: {detalle['nombre']}")
        print(f"  Tamaño: {detalle['tamaño']}")
        print(f"  Tipo: {detalle['tipo']}")
        print(f"  CA: {detalle['clase_de_armadura']}")
        print(f"  PG: {detalle['puntos_de_golpe']}")

def test_daño():
    print("\n=== TEST DAÑO ===")
    
    # Test tipos de daño
    print("\n1. Obteniendo tipos de daño...")
    tipos_daño = obtener_tipos_daño()
    print(f"Tipos de daño encontrados: {len(tipos_daño)}")
    for tipo in tipos_daño:
        print(f"  - {tipo['nombre']} (index: {tipo['index']})")
    
    # Test detalle daño
    if tipos_daño:
        print(f"\n2. Obteniendo detalle de '{tipos_daño[0]['index']}'...")
        detalle = obtener_detalle_daño(tipos_daño[0]['index'])
        print(f"  Nombre: {detalle['nombre']}")
        print(f"  Descripción: {detalle['descripcion'][:100]}...")

def main():
    print("INICIANDO PRUEBAS DE LA API DE DUNGEONS & DRAGONS")
    print("=" * 60)
    
    try:
        #test_pj()
        #test_items()
        #test_hechizos()
        #test_monstruos()
        test_daño()
        
        print("\n" + "=" * 60)
        print("¡TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE!")
        
    except Exception as e:
        print(f"ERROR durante las pruebas: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()