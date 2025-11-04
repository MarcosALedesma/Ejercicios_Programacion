import sys
import os
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.items import (
    obtener_equipo, 
    obtener_detalle_equipo, 
    obtener_objetos_magicos, 
    obtener_detalle_objeto_magico
)

def test_resumen_completo_items():
    """Test resumen que muestra todos los datos de items.py de forma organizada"""
    
    print("🎒 TEST COMPLETO - TODOS LOS DATOS DE ITEMS.PY")
    print("=" * 70)
    
    # 1. EQUIPO NORMAL
    print("\n📦 EQUIPO NORMAL")
    print("-" * 40)
    
    equipo = obtener_equipo()
    print(f"Total de items de equipo: {len(equipo)}")
    
    # Mostrar algunos items de equipo con detalles
    equipo_ejemplos = ['dagger', 'chain-mail', 'longbow', 'potion']
    
    datos_equipo = []
    for ejemplo in equipo_ejemplos:
        try:
            detalle = obtener_detalle_equipo(ejemplo)
            
            datos_equipo.append({
                'Nombre': detalle['nombre'],
                'Categoría': detalle['categoria'],
                'Peso': detalle['peso'],
                'Costo': f"{detalle['costo'].get('quantity', '')} {detalle['costo'].get('unit', '')}" if detalle['costo'] else 'N/A',
                'Descripción (caracteres)': len(detalle['descripcion'])
            })
            
        except Exception as e:
            print(f"❌ Error con {ejemplo}: {e}")
    
    if datos_equipo:
        df_equipo = pd.DataFrame(datos_equipo)
        print(df_equipo.to_string(index=False))
    
    # 2. OBJETOS MÁGICOS
    print("\n✨ OBJETOS MÁGICOS")
    print("-" * 40)
    
    objetos_magicos = obtener_objetos_magicos()
    print(f"Total de objetos mágicos: {len(objetos_magicos)}")
    
    # Mostrar algunos objetos mágicos con detalles
    magicos_ejemplos = ['potion-of-healing', 'wand-of-fireballs', 'vorpal-sword', 'armor-of-invulnerability']
    
    datos_magicos = []
    for ejemplo in magicos_ejemplos:
        try:
            detalle = obtener_detalle_objeto_magico(ejemplo)
            
            datos_magicos.append({
                'Nombre': detalle['nombre'],
                'Tipo': detalle['tipo'],
                'Rareza': detalle['rareza'],
                'Descripción (caracteres)': len(detalle['descripcion'])
            })
            
        except Exception as e:
            print(f"❌ Error con {ejemplo}: {e}")
    
    if datos_magicos:
        df_magicos = pd.DataFrame(datos_magicos)
        print(df_magicos.to_string(index=False))
    
    # 3. ESTADÍSTICAS FINALES
    print("\n📈 ESTADÍSTICAS FINALES")
    print("-" * 40)
    
    stats = {
        'Tipo': ['Equipo Normal', 'Objetos Mágicos'],
        'Total Items': [len(equipo), len(objetos_magicos)],
        'Ejemplos Mostrados': [len(datos_equipo), len(datos_magicos)]
    }
    
    df_stats = pd.DataFrame(stats)
    print(df_stats.to_string(index=False))

def test_detalles_extendidos():
    """Test con detalles extendidos de items específicos"""
    
    print("\n🔍 DETALLES EXTENDIDOS DE ITEMS ESPECÍFICOS")
    print("=" * 70)
    
    items_especiales = [
        ('dagger', 'equipo'),
        ('potion-of-healing', 'magico'),
        ('vorpal-sword', 'magico')
    ]
    
    for item_index, tipo in items_especiales:
        print(f"\n🎯 {item_index.upper()} ({tipo})")
        print("-" * 30)
        
        try:
            if tipo == 'equipo':
                detalle = obtener_detalle_equipo(item_index)
                
                print(f"Nombre: {detalle['nombre']}")
                print(f"Categoría: {detalle['categoria']}")
                print(f"Peso: {detalle['peso']}")
                if detalle['costo']:
                    print(f"Costo: {detalle['costo'].get('quantity', '')} {detalle['costo'].get('unit', '')}")
                print(f"Descripción: {detalle['descripcion'][:150]}..." if len(detalle['descripcion']) > 150 else f"Descripción: {detalle['descripcion']}")
                
            else:
                detalle = obtener_detalle_objeto_magico(item_index)
                
                print(f"Nombre: {detalle['nombre']}")
                print(f"Tipo: {detalle['tipo']}")
                print(f"Rareza: {detalle['rareza']}")
                print(f"Descripción: {detalle['descripcion'][:150]}..." if len(detalle['descripcion']) > 150 else f"Descripción: {detalle['descripcion']}")
                
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_resumen_completo_items()
    test_detalles_extendidos()
