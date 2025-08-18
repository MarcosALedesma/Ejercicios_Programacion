from dado import tirar_dados, imprimir_dado

# Diccionario de efectos especiales
efectos_tablero = {
    3: +2,
    5: -1,
    7: -2,
    9: +1
}

def tirar_jugador(jugador):
    print(f"\nTirando dado para {jugador.nombre}...")
    resultado = tirar_dados()
    print(f"{jugador.nombre} obtuvo un {resultado}")
    return resultado

def decidir_turno(jugador1, resultado1, jugador2, resultado2, criterio):
    if criterio == "mayor":
        if resultado1 > resultado2:
            return jugador1, jugador2
        elif resultado2 > resultado1:
            return jugador2, jugador1
    elif criterio == "menor":
        if resultado1 < resultado2:
            return jugador1, jugador2
        elif resultado2 < resultado1:
            return jugador2, jugador1
    return None, None  # empate

def mostrar_dados_finales(jugador1, resultado1, jugador2, resultado2):
    print("\n=== RESULTADOS FINALES ===\n")
    print(f"{jugador1.nombre}:")
    imprimir_dado(resultado1)
    print(f"{jugador2.nombre}:")
    imprimir_dado(resultado2)

def aplicar_efecto(jugador):
    if jugador.posicion in efectos_tablero:
        efecto = efectos_tablero[jugador.posicion]
        if efecto > 0:
            print(f"{jugador.nombre} cayó en la casilla {jugador.posicion} y avanza {efecto} más!")
        else:
            print(f"{jugador.nombre} cayó en la casilla {jugador.posicion} y retrocede {abs(efecto)}!")
            '''
            la funciona abs devuelve el valor absoluto de un número
            numero1 = -10
            numero2 = 5
            numero3 = -3.7
            print(abs(numero1))  # Salida: 10
            print(abs(numero2))  # Salida: 5
            print(abs(numero3))  # Salida: 3.7
            '''
        jugador.avanzar(efecto)

def jugar_tablero(jugador1, jugador2):
    ganador = None
    while not ganador:
        for jugador in [jugador1, jugador2]:
            input(f"{jugador.nombre}, presiona Enter para tirar el dado")
            tirada = tirar_dados()
            jugador.avanzar(tirada)
            imprimir_dado(tirada)
            #jugador.mostrar_estado()

            aplicar_efecto(jugador)
            jugador.mostrar_estado()
            
            print(f"{jugador1.nombre}: " + "=== " * jugador1.posicion)
            print(f"{jugador2.nombre}: " + "=== " * jugador2.posicion)


            if jugador.posicion >= 10:
                ganador = jugador
                break
    print(f"{ganador.nombre} ha llegado a la meta y gana el juego!")

