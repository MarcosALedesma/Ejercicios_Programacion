 import sys
import os
import pandas as pd
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.reglas import (
    obtener_categorias_reglas,
    obtener_secciones_reglas, 
    obtener_detalle_regla,
    obtener_reglas_basicas
)

def test_todas_las_reglas():
    """Test que muestra TODAS las reglas disponibles"""
    
    print("=" * 80)
    print("=== CATEGORÍAS DE REGLAS DISPONIBLES ===")
    print("=" * 80)
    
    # Obtener categorías de reglas
    categorias = obtener_categorias_reglas()
    df_categorias = pd.DataFrame(categorias)
    print(f"Total de categorías de reglas: {len(categorias)}")
    print("\nCategorías principales:")
    print(df_categorias.to_string(index=False))
    
    print("\n" + "=" * 80)
    print("=== SECCIONES DE REGLAS DISPONIBLES ===")
    print("=" * 80)
    
    # Obtener secciones de reglas
    secciones = obtener_secciones_reglas()
    df_secciones = pd.DataFrame(secciones)
    print(f"Total de secciones de reglas: {len(secciones)}")
    print("\nPrimeras 20 secciones:")
    print(df_secciones.head(20).to_string(index=False))

def test_reglas_basicas_detalladas():
    """Test que muestra las reglas básicas más importantes"""
    
    print("\n" + "=" * 80)
    print("=== REGLAS BÁSICAS (Para nuevos jugadores) ===")
    print("=" * 80)
    
    reglas_basicas = obtener_reglas_basicas()
    
    for i, regla in enumerate(reglas_basicas, 1):
        print(f"\n{'#' * 60}")
        print(f"### REGLA BÁSICA {i}: {regla['nombre'].upper()}")
        print(f"{'#' * 60}")
        
        # Mostrar información básica
        print(f"\n📋 INFORMACIÓN:")
        print(f"• Nombre: {regla['nombre']}")
        print(f"• Índice: {regla['indice']}")
        
        # Mostrar descripción
        print(f"\n📖 DESCRIPCIÓN:")
        descripcion = regla['descripcion']
        if descripcion:
            # Mostrar en partes si es muy larga
            if len(descripcion) > 500:
                lineas = descripcion.split('. ')
                for j, linea in enumerate(lineas[:8]):  # Mostrar primeras 8 líneas
                    if linea.strip():
                        print(f"  {linea.strip()}.")
                if len(lineas) > 8:
                    print(f"  ... y {len(lineas) - 8} líneas más")
            else:
                print(f"  {descripcion}")
        else:
            print("  No hay descripción disponible")

def test_reglas_combate():
    """Test enfocado en reglas de combate"""
    
    print("\n" + "=" * 80)
    print("=== REGLAS DE COMBATE ===")
    print("=" * 80)
    
    reglas_combate = [
        'actions-in-combat',
        'movement',
        'cover',
        'damage-and-healing',
        'making-an-attack'
    ]
    
    for regla_index in reglas_combate:
        try:
            print(f"\n⚔️  {regla_index.upper()}")
            print("-" * 40)
            
            detalle = obtener_detalle_regla(regla_index)
            print(f"Nombre: {detalle['nombre']}")
            
            descripcion = detalle['descripcion']
            if descripcion:
                # Mostrar resumen de la descripción
                lineas = descripcion.split('. ')
                for linea in lineas[:3]:  # Mostrar primeras 3 líneas
                    if linea.strip():
                        print(f"• {linea.strip()}.")
                if len(lineas) > 3:
                    print(f"• ... ({len(lineas) - 3} líneas más)")
                    
        except Exception as e:
            print(f"❌ Error con {regla_index}: {e}")

def test_estructura_reglas():
    """Test que muestra la estructura de las reglas"""
    
    print("\n" + "=" * 80)
    print("=== ESTRUCTURA DE LAS REGLAS ===")
    print("=" * 80)
    
    # Probar con una regla específica
    try:
        detalle = obtener_detalle_regla('ability-checks')
        
        print("\n📋 ESTRUCTURA DE UNA REGLA:")
        print("-" * 50)
        
        for campo, valor in detalle.items():
            tipo = type(valor).__name__
            print(f"• {campo}: {tipo}")
            if campo == 'descripcion':
                print(f"  └── Longitud: {len(valor)} caracteres")
                print(f"  └── Preview: {valor[:100]}...")
            else:
                print(f"  └── Valor: {valor}")
                
    except Exception as e:
        print(f"Error: {e}")

def test_resumen_reglas_esenciales():
    """Test con resumen de reglas esenciales para nuevos jugadores"""
    
    print("\n" + "=" * 80)
    print("=== RESUMEN DE REGLAS ESENCIALES ===")
    print("=" * 80)
    
    reglas_esenciales = {
        'ability-checks': 'Tiradas de habilidad',
        'saving-throws': 'Tiradas de salvación', 
        'advantage-and-disadvantage': 'Ventaja y desventaja',
        'proficiency-bonus': 'Bonificación por competencia',
        'actions-in-combat': 'Acciones en combate',
        'movement': 'Movimiento',
        'spellcasting': 'Lanzamiento de hechizos'
    }
    
    datos_resumen = []
    
    for regla_index, nombre_español in reglas_esenciales.items():
        try:
            detalle = obtener_detalle_regla(regla_index)
            
            datos_resumen.append({
                'Regla': nombre_español,
                'Índice': detalle['indice'],
                'Descripción (caracteres)': len(detalle['descripcion']),
                'Resumen': detalle['descripcion'][:100] + '...' if len(detalle['descripcion']) > 100 else detalle['descripcion']
            })
            
        except Exception as e:
            print(f"❌ Error con {regla_index}: {e}")
    
    if datos_resumen:
        df_resumen = pd.DataFrame(datos_resumen)
        print("\n📊 REGLAS ESENCIALES:")
        print(df_resumen.to_string(index=False))

if __name__ == "__main__":
    test_todas_las_reglas()
    test_reglas_basicas_detalladas()
    test_reglas_combate()
    test_estructura_reglas()
    test_resumen_reglas_esenciales()
