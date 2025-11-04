import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.dnd_api import api_obtener_conditions, api_obtener_condition_detalle

#===== FUNCIONES BÁSICAS DE DADOS =====#

def tirar_dado(caras=20):
    return random.randint(1, caras)

def tirar_dados(cantidad, caras):
    return sum(random.randint(1, caras) for _ in range(cantidad))

#===== CÁLCULOS DE CARACTERÍSTICAS =====#

def calcular_modificador(puntuacion_caracteristica):
    return (puntuacion_caracteristica - 10) // 2

def calcular_bonus_competencia(nivel, competencia=True):
    if not competencia:
        return 0
    return 2 + (nivel - 1) // 4

#===== CÁLCULOS DE COMBATE =====#

def calcular_golpe(bonus_ataque, ventaja=False, desventaja=False):
    if ventaja and desventaja:
        ventaja = False
        desventaja = False
    
    if ventaja:
        resultado_dado = max(tirar_dado(20), tirar_dado(20))
    elif desventaja:
        resultado_dado = min(tirar_dado(20), tirar_dado(20))
    else:
        resultado_dado = tirar_dado(20)
    
    total = resultado_dado + bonus_ataque
    impacto_critico = (resultado_dado == 20)
    
    return {
        'dado': resultado_dado,
        'bonus': bonus_ataque,
        'total': total,
        'impacto': impacto_critico or (total >= 10),
        'critico': impacto_critico
    }

def calcular_dano(dados, bonus_dano=0, critico=False):
    if isinstance(dados, str):
        cantidad, caras = map(int, dados.split('d'))
    else:
        cantidad, caras = dados
    
    if critico:
        cantidad *= 2
    
    return tirar_dados(cantidad, caras) + bonus_dano

#===== TIRADAS DE SALVACIÓN =====#

def tirar_salvacion(caracteristica, bonus_caracteristica, bonus_competencia=0, ventaja=False, desventaja=False, otros_bonos=0):
    if ventaja and desventaja:
        ventaja = False
        desventaja = False
    
    if ventaja:
        resultado_dado = max(tirar_dado(20), tirar_dado(20))
    elif desventaja:
        resultado_dado = min(tirar_dado(20), tirar_dado(20))
    else:
        resultado_dado = tirar_dado(20)
    
    bonus_total = bonus_caracteristica + bonus_competencia + otros_bonos
    total = resultado_dado + bonus_total
    
    return {
        'caracteristica': caracteristica,
        'dado': resultado_dado,
        'bonus_caracteristica': bonus_caracteristica,
        'bonus_competencia': bonus_competencia,
        'otros_bonos': otros_bonos,
        'bonus_total': bonus_total,
        'total': total,
        'exito': (resultado_dado == 20) or (resultado_dado == 1),
        'critico': (resultado_dado == 20),
        'pifia': (resultado_dado == 1)
    }

def salvacion_contra_hechizo(cd_salvacion, caracteristica, bonus_caracteristica, bonus_competencia=0, otros_bonos=0, ventaja=False, desventaja=False):
    resultado = tirar_salvacion(caracteristica, bonus_caracteristica, bonus_competencia, ventaja, desventaja, otros_bonos)
    resultado['cd_requerida'] = cd_salvacion
    resultado['exito'] = resultado['total'] >= cd_salvacion
    return resultado

#===== FUNCIONES DE CONDICIONES =====#

def obtener_condiciones():
    condiciones_data = api_obtener_conditions()
    return [{'index': cond['index'], 'nombre': cond['name']} for cond in condiciones_data['results']]

def obtener_detalle_condicion(condition_index):
    detalle = api_obtener_condition_detalle(condition_index)
    return {
        'nombre': detalle.get('name', ''),
        'indice': detalle.get('index', ''),
        'descripcion': ', '.join(detalle.get('desc', [])),
        'url': detalle.get('url', '')
    }

def obtener_condiciones_comunes():
    condiciones_comunes = [
        'blinded', 'charmed', 'frightened', 'grappled', 'incapacitated',
        'invisible', 'paralyzed', 'petrified', 'poisoned', 'prone',
        'restrained', 'stunned', 'unconscious'
    ]
    
    condiciones = []
    for condicion_index in condiciones_comunes:
        try:
            detalle = obtener_detalle_condicion(condicion_index)
            condiciones.append(detalle)
        except:
            continue
            
    return condiciones

def aplicar_condicion(condicion_index, duracion=1):
    try:
        detalle_condicion = obtener_detalle_condicion(condicion_index)
        
        efecto = {
            'condicion': detalle_condicion['nombre'],
            'indice': condicion_index,
            'descripcion': detalle_condicion['descripcion'],
            'duracion': duracion,
            'rondas_restantes': duracion
        }
        
        # Efectos automáticos de condiciones comunes
        efectos_automaticos = {
            'prone': {'ventaja_cercano': True, 'desventaja_distante': True},
            'restrained': {'desventaja_ataque': True, 'desventaja_salvacion_destreza': True},
            'frightened': {'desventaja_ataque': True, 'no_acercarse': True},
            'poisoned': {'desventaja_ataque': True, 'desventaja_habilidad': True},
            'blinded': {'automatico_fallo_vision': True, 'ventaja_contra_el': True},
            'paralyzed': {'automatico_critico_cercano': True, 'incapacitado': True},
            'stunned': {'incapacitado': True, 'automatico_fallo_salvacion_fuerza_destreza': True}
        }
        
        if condicion_index in efectos_automaticos:
            efecto.update(efectos_automaticos[condicion_index])
        
        return efecto
        
    except Exception as e:
        return None

def actualizar_condiciones(personaje):
    if 'condiciones' not in personaje:
        return personaje
    
    condiciones_activas = []
    for condicion in personaje.get('condiciones', []):
        condicion['rondas_restantes'] -= 1
        if condicion['rondas_restantes'] > 0:
            condiciones_activas.append(condicion)
    
    personaje['condiciones'] = condiciones_activas
    return personaje

def calcular_bonos_por_condiciones(condiciones, tipo='ataque'):
    ventaja = False
    desventaja = False
    
    for condicion in condiciones:
        condicion_index = condicion.get('indice', '')
        
        if tipo == 'ataque':
            if condicion_index in ['restrained', 'frightened', 'poisoned']:
                desventaja = True
                
        elif tipo == 'salvacion':
            if condicion_index == 'restrained':
                desventaja = True
                
        elif tipo == 'defensa':
            if condicion_index == 'blinded':
                ventaja = True
            elif condicion_index == 'prone':
                ventaja = True
    
    return {'ventaja': ventaja, 'desventaja': desventaja}

#===== ATAQUE COMPLETO CON ESTADOS =====#

def ataque_completo(bonus_ataque, dados_dano, bonus_dano=0, ventaja=False, desventaja=False, condiciones_atacante=None, condiciones_defensor=None):
    if condiciones_atacante:
        bonos_ataque = calcular_bonos_por_condiciones(condiciones_atacante, 'ataque')
        if bonos_ataque['ventaja']:
            ventaja = True
        if bonos_ataque['desventaja']:
            desventaja = True
    
    resultado_golpe = calcular_golpe(bonus_ataque, ventaja, desventaja)
    
    if resultado_golpe['impacto']:
        dano = calcular_dano(dados_dano, bonus_dano, resultado_golpe['critico'])
    else:
        dano = 0
    
    return {
        'golpe': resultado_golpe,
        'dano': dano,
        'impacto': resultado_golpe['impacto'],
        'critico': resultado_golpe['critico']
    }
