import sys
import os
import pandas as pd
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.hechizos import obtener_hechizos, obtener_detalle_hechizo

def test_todos_los_datos_hechizos():
    """Test que muestra TODOS los datos que retorna hechizos.py"""
    
    print("=" * 80)
    print("=== LISTA COMPLETA DE HECHIZOS ===")
    print("=" * 80)
    
    # Obtener lista completa de hechizos
    hechizos = obtener_hechizos()
    df_hechizos = pd.DataFrame(hechizos)
    print(f"Total de hechizos: {len(hechizos)}")
    print("\nPrimeros 20 hechizos:")
    print(df_hechizos.head(20))
    
    print("\n" + "=" * 80)
    print("=== DETALLE COMPLETO DE HECHIZOS DE EJEMPLO ===")
    print("=" * 80)
    
    # Hechizos de ejemplo para mostrar detalle completo
    ejemplos = ['fireball', 'magic-missile', 'cure-wounds', 'shield', 'wish']
    
    for ejemplo in ejemplos:
        try:
            print(f"\n{'#' * 60}")
            print(f"### DETALLE COMPLETO DE HECHIZO: {ejemplo.upper()}")
            print(f"{'#' * 60}")
            
            detalle = obtener_detalle_hechizo(ejemplo)
            
            # 1. INFORMACIÓN BÁSICA
            print("\n--- INFORMACIÓN BÁSICA ---")
            info_basica = {
                'Campo': ['nombre', 'nivel', 'escuela', 'tiempo_de_lanzamiento', 'alcance', 'duracion'],
                'Valor': [
                    detalle['nombre'],
                    detalle['nivel'],
                    detalle['escuela'],
                    detalle['tiempo_de_lanzamiento'],
                    detalle['alcance'],
                    detalle['duracion']
                ]
            }
            df_basico = pd.DataFrame(info_basica)
            print(df_basico.to_string(index=False))
            
            # 2. COMPONENTES
            print("\n--- COMPONENTES ---")
            componentes = detalle['componentes']
            if componentes:
                df_componentes = pd.DataFrame({'Componentes': componentes})
                print(df_componentes.to_string(index=False))
            else:
                print("No tiene componentes")
            
            # 3. MATERIALES
            print(f"\n--- MATERIALES ---")
            materiales = detalle['materiales']
            if materiales:
                # Mostrar materiales en partes si es muy largo
                if len(materiales) > 150:
                    print(f"{materiales[:150]}...")
                    print(f"...{materiales[150:300]}..." if len(materiales) > 300 else "")
                else:
                    print(materiales)
            else:
                print("No requiere materiales")
            
            # 4. CLASES QUE PUEDEN USARLO
            print(f"\n--- CLASES ({len(detalle['clases'])}) ---")
            clases = detalle['clases']
            if clases:
                df_clases = pd.DataFrame({'Clases': clases})
                print(df_clases.to_string(index=False))
            else:
                print("No hay clases específicas")
            
            # 5. DESCRIPCIÓN
            print(f"\n--- DESCRIPCIÓN ---")
            descripcion = detalle['descripcion']
            if descripcion:
                if len(descripcion) > 300:
                    print(f"{descripcion[:300]}...")
                    print(f"...{descripcion[300:600]}..." if len(descripcion) > 600 else "")
                else:
                    print(descripcion)
            else:
                print("No tiene descripción")
            
            # 6. ESTRUCTURA COMPLETA EN JSON
            print(f"\n--- ESTRUCTURA COMPLETA (JSON) ---")
            print(json.dumps(detalle, indent=2, ensure_ascii=False))
            
        except Exception as e:
            print(f"❌ Error con {ejemplo}: {e}")

def test_estructura_completa_hechizos():
    """Test que muestra la estructura completa de hechizos en detalle"""
    
    print("\n" + "=" * 80)
    print("=== ESTRUCTURA COMPLETA DE HECHIZOS ===")
    print("=" * 80)
    
    try:
        print("\n📋 CAMPOS DISPONIBLES EN HECHIZOS:")
        print("-" * 50)
        
        detalle = obtener_detalle_hechizo('magic-missile')
        
        for campo, valor in detalle.items():
            tipo = type(valor).__name__
            print(f"• {campo}: {tipo}")
            if campo == 'componentes':
                print(f"  └── Valores: {valor}")
            elif campo == 'clases':
                print(f"  └── Cantidad: {len(valor)} clases")
            elif campo == 'descripcion':
                print(f"  └── Longitud: {len(valor)} caracteres")
            else:
                print(f"  └── Valor: {str(valor)[:80]}{'...' if len(str(valor)) > 80 else ''}")
        
        # Mostrar tabla resumen completa
        print("\n📊 RESUMEN COMPLETO EN TABLAS:")
        
        # Tabla de información principal
        info_principal = {
            'Campo': list(detalle.keys()),
            'Tipo': [type(detalle[campo]).__name__ for campo in detalle.keys()],
            'Valor Ejemplo': [str(detalle[campo])[:50] + '...' if len(str(detalle[campo])) > 50 else str(detalle[campo]) for campo in detalle.keys()]
        }
        df_principal = pd.DataFrame(info_principal)
        print(df_principal.to_string(index=False))
        
    except Exception as e:
        print(f"Error: {e}")

def test_comparativo_hechizos_por_nivel():
    """Test que compara hechizos de diferentes niveles"""
    
    print("\n" + "=" * 80)
    print("=== COMPARACIÓN DE HECHIZOS POR NIVEL ===")
    print("=" * 80)
    
    hechizos_por_nivel = [
        ('magic-missile', 1),
        ('fireball', 3),
        ('cone-of-cold', 5),
        ('wish', 9)
    ]
    
    resultados = []
    
    for spell_index, nivel_esperado in hechizos_por_nivel:
        try:
            detalle = obtener_detalle_hechizo(spell_index)
            
            resultados.append({
                'Hechizo': detalle['nombre'],
                'Nivel': detalle['nivel'],
                'Escuela': detalle['escuela'],
                'Tiempo Lanzamiento': detalle['tiempo_de_lanzamiento'],
                'Alcance': detalle['alcance'],
                'Componentes': len(detalle['componentes']),
                'Tiene Materiales': 'Sí' if detalle['materiales'] else 'No',
                'Duración': detalle['duracion'],
                'Clases': len(detalle['clases']),
                'Descripción (caracteres)': len(detalle['descripcion'])
            })
                
        except Exception as e:
            print(f"Error con {spell_index}: {e}")
    
    if resultados:
        df_comparativo = pd.DataFrame(resultados)
        print("\n📊 COMPARATIVA DE HECHIZOS POR NIVEL:")
        print(df_comparativo.to_string(index=False))

def test_hechizos_por_escuela():
    """Test que agrupa hechizos por escuela de magia"""
    
    print("\n" + "=" * 80)
    print("=== HECHIZOS POR ESCUELA DE MAGIA ===")
    print("=" * 80)
    
    hechizos_muestra = [
        ('fireball', 'Evocation'),
        ('mage-armor', 'Abjuration'),
        ('charm-person', 'Enchantment'),
        ('invisibility', 'Illusion'),
        ('animate-dead', 'Necromancy'),
        ('teleport', 'Conjuration'),
        ('identify', 'Divination'),
        ('slow', 'Transmutation')
    ]
    
    datos_escuelas = []
    
    for spell_index, escuela_esperada in hechizos_muestra:
        try:
            detalle = obtener_detalle_hechizo(spell_index)
            
            datos_escuelas.append({
                'Hechizo': detalle['nombre'],
                'Escuela': detalle['escuela'],
                'Nivel': detalle['nivel'],
                'Tiempo Lanzamiento': detalle['tiempo_de_lanzamiento'],
                'Alcance': detalle['alcance']
            })
                
        except Exception as e:
            print(f"Error con {spell_index}: {e}")
    
    if datos_escuelas:
        df_escuelas = pd.DataFrame(datos_escuelas)
        print("\n🎓 HECHIZOS POR ESCUELA DE MAGIA:")
        print(df_escuelas.to_string(index=False))
        
        # Agrupar por escuela
        print(f"\n📈 RESUMEN POR ESCUELA:")
        resumen_escuelas = df_escuelas.groupby('Escuela').agg({
            'Hechizo': 'count',
            'Nivel': 'mean'
        }).round(2)
        print(resumen_escuelas)

if __name__ == "__main__":
    test_todos_los_datos_hechizos()
    test_estructura_completa_hechizos()
    test_comparativo_hechizos_por_nivel()
    test_hechizos_por_escuela()
