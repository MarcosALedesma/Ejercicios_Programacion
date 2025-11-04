import sys
import os
import pandas as pd
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.monstruos import obtener_monstruos, obtener_detalle_monstruo

def test_todos_los_datos_monstruos():
    """Test que muestra TODOS los datos que retorna monstruos.py"""
    
    print("=" * 80)
    print("=== LISTA COMPLETA DE MONSTRUOS ===")
    print("=" * 80)
    
    # Obtener lista completa de monstruos
    monstruos = obtener_monstruos()
    df_monstruos = pd.DataFrame(monstruos)
    print(f"Total de monstruos: {len(monstruos)}")
    print("\nPrimeros 15 monstruos:")
    print(df_monstruos.head(15))
    
    print("\n" + "=" * 80)
    print("=== DETALLE COMPLETO DE MONSTRUOS DE EJEMPLO ===")
    print("=" * 80)
    
    # Monstruos de ejemplo para mostrar detalle completo
    ejemplos = ['goblin', 'zombie', 'dragon']
    
    for ejemplo in ejemplos:
        try:
            print(f"\n{'#' * 60}")
            print(f"### DETALLE COMPLETO DE: {ejemplo.upper()}")
            print(f"{'#' * 60}")
            
            detalle = obtener_detalle_monstruo(ejemplo)
            
            # 1. INFORMACIÓN BÁSICA
            print("\n--- INFORMACIÓN BÁSICA ---")
            info_basica = {
                'Campo': ['nombre', 'tamaño', 'tipo', 'alineamiento', 'clase_de_armadura', 'puntos_de_golpe', 'cr'],
                'Valor': [
                    detalle['nombre'],
                    detalle['tamaño'],
                    detalle['tipo'],
                    detalle['alineamiento'],
                    detalle['clase_de_armadura'],
                    detalle['puntos_de_golpe'],
                    detalle.get('cr', 'N/A')
                ]
            }
            df_basico = pd.DataFrame(info_basica)
            print(df_basico.to_string(index=False))
            
            # 2. CARACTERÍSTICAS (Atributos)
            print("\n--- CARACTERÍSTICAS ---")
            caracteristicas = detalle['caracteristicas']
            df_caracteristicas = pd.DataFrame([caracteristicas])
            print(df_caracteristicas)
            
            # 3. DESPLAZAMIENTO
            print("\n--- DESPLAZAMIENTO ---")
            desplazamiento = detalle['desplazamiento']
            if desplazamiento:
                datos_desplazamiento = []
                for tipo, valor in desplazamiento.items():
                    if isinstance(valor, dict):
                        datos_desplazamiento.append({
                            'Tipo': tipo,
                            'Velocidad': valor.get('value', ''),
                            'Condición': valor.get('condition', 'N/A')
                        })
                    else:
                        datos_desplazamiento.append({
                            'Tipo': tipo,
                            'Velocidad': valor,
                            'Condición': 'N/A'
                        })
                
                if datos_desplazamiento:
                    df_desplazamiento = pd.DataFrame(datos_desplazamiento)
                    print(df_desplazamiento.to_string(index=False))
                else:
                    print("No hay datos de desplazamiento")
            else:
                print("No hay datos de desplazamiento")
            
            # 4. ACCIONES
            print(f"\n--- ACCIONES ({len(detalle['acciones'])}) ---")
            acciones = detalle['acciones']
            if acciones:
                df_acciones = pd.DataFrame(acciones)
                # Mostrar todas las acciones con nombre y descripción
                for i, accion in enumerate(acciones, 1):
                    print(f"\n{i}. {accion['nombre']}")
                    print(f"   Descripción: {accion['descripcion'][:100]}..." if len(accion['descripcion']) > 100 else f"   Descripción: {accion['descripcion']}")
            else:
                print("No tiene acciones")
            
            # 5. IMAGEN
            print(f"\n--- IMAGEN ---")
            print(f"URL: {detalle['imagen'] if detalle['imagen'] else 'No tiene imagen'}")
            
            # 6. ESTRUCTURA COMPLETA EN JSON (para ver todos los campos)
            print(f"\n--- ESTRUCTURA COMPLETA (JSON) ---")
            print(json.dumps(detalle, indent=2, ensure_ascii=False))
            
        except Exception as e:
            print(f"❌ Error con {ejemplo}: {e}")

def test_estructura_completa_uno():
    """Test que muestra la estructura completa de un solo monstruo en detalle"""
    
    print("\n" + "=" * 80)
    print("=== ESTRUCTURA COMPLETA DE UN MONSTRUO (Goblin) ===")
    print("=" * 80)
    
    try:
        detalle = obtener_detalle_monstruo('goblin')
        
        # Mostrar todos los campos y sus tipos
        print("\n📋 CAMPOS DISPONIBLES Y SUS VALORES:")
        print("-" * 50)
        
        for campo, valor in detalle.items():
            tipo = type(valor).__name__
            print(f"• {campo}: {tipo}")
            if campo == 'caracteristicas':
                print("  └── Subcampos:", list(valor.keys()))
            elif campo == 'acciones':
                print(f"  └── Cantidad: {len(valor)} acciones")
            elif campo == 'desplazamiento':
                print(f"  └── Tipos: {list(valor.keys())}")
            else:
                print(f"  └── Valor: {valor}")
        
        # Mostrar tabla resumen completa
        print("\n📊 RESUMEN COMPLETO EN TABLAS:")
        
        # Tabla de información principal
        info_principal = {
            'Campo': list(detalle.keys())[:7],  # primeros 7 campos
            'Tipo': [type(detalle[campo]).__name__ for campo in list(detalle.keys())[:7]],
            'Valor Ejemplo': [str(detalle[campo])[:50] + '...' if len(str(detalle[campo])) > 50 else str(detalle[campo]) for campo in list(detalle.keys())[:7]]
        }
        df_principal = pd.DataFrame(info_principal)
        print(df_principal.to_string(index=False))
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_todos_los_datos_monstruos()
    test_estructura_completa_uno()
