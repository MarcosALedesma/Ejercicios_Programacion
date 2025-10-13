#combate.py
import random
from  dashborad import menu
from clear_cli import clear  

def dado_ascii(tirada):
    if tirada < 10:
        number_str = f"  {tirada}   "
    else:
        number_str = f" {tirada}   "

    print(f"""
            ,:::,
       ,,,:;  :  ;:,,, 
   ,,,:       :       :,,, 
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ; {number_str};    ;    ;
;     ;  ;         ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::' 
""")
def tirar_d20():
    return random.randint(1, 20)

def interpretar_tirada(tirada):
    if tirada == 1:
        return "critico_fallo"
    elif tirada == 20:
        return "critico_exito"
    elif tirada >= 10:
        return "exito"
    else:
        return "fallo"

def combate(jugador, enemigo):
    print("╔"+("═" * 57)+"╗")
    print(f"║ ¡Un {enemigo.nombre} aparece!".ljust(58)+"║")
    print("╚" + ("═" * 57) + "╝")
    #menu(jugador, enemigo) 

    while jugador.vida > 0 and enemigo.vida > 0:
        menu(jugador, enemigo) 
        #print("╔"+("═" * 57)+"╗")
        #print("║ Tu turno:".ljust(58)+"║")
        #print("║ 1. Atacar".ljust(58)+"║")
        #print("║ 2. Esquivar".ljust(58)+"║")
        #print("║ 3. Bloquear".ljust(58)+"║")
        #print("╚" + ("═" * 57) + "╝")
        accion = input("> ")

        tirada = tirar_d20()
        resultado = interpretar_tirada(tirada)
        clear()
        #dado_ascii(tirada)
        print( "╔"+("═" * 57)+"╗")
        print("║"+f"Tirada de d20 de {jugador.nombre} : {tirada} → {resultado.replace('_', ' ').capitalize()}".center(57)+"║")
        if accion == "1":  # Atacar
            atributo = getattr(jugador, jugador.atributo_ataque)
            if resultado == "critico_exito":
                dano = atributo * 2
            elif resultado == "exito":
                dano = atributo
            elif resultado == "fallo":
                dano = int(atributo / 2)
            else:
                dano = 0
            enemigo.vida -= dano
            print("║"+f"Atacas al {enemigo.nombre} e infliges {dano} de daño.".center(57)+"║")
            print( "╚" + ("═" * 57) + "╝")
        elif accion == "2":  # Esquivar
            esquiva = jugador.destreza
            if resultado == "critico_exito":
                print("║"+"¡Esquiva perfecta! No recibes daño".center(57)+"║")
                print( "╚" + ("═" * 57) + "╝")
                continue  # evitar el turno enemigo
            elif resultado == "exito":
                print("║"+"Esquivaste parcialmente, recibes daño reducido.".center(57)+"║")
                jugador.vida -= max(0, enemigo.fuerza - jugador.destreza)
            elif resultado == "fallo":
                print("║"+"Fallaste al esquivar. Recibes daño completo.".center(57)+"║")
                print( "╚" + ("═" * 57) + "╝")
                jugador.vida -= enemigo.fuerza
            else:
                print("║"+"Tropiezas al esquivar y quedas vulnerable.".center(57)+"║")
                print( "╚" + ("═" * 57) + "╝")
                jugador.vida -= enemigo.fuerza + 5

        elif accion == "3":  # Bloquear
            if resultado == "critico_exito":
                print("║"+"¡Bloqueo perfecto! Reduces todo el daño.".center(57)+"║")
                print( "╚" + ("═" * 57) + "╝")
                jugador.vida -= 0
            elif resultado == "exito":
                print("║"+"Bloqueas parte del daño.".center(57)+"║")
                print( "╚" + ("═" * 57) + "╝")
                jugador.vida -= max(0, enemigo.fuerza - jugador.defensa)
            elif resultado == "fallo":
                print("║"+"Bloqueas poco. Recibes casi todo el daño.".center(57)+"║")
                print( "╚" + ("═" * 57) + "╝")
                jugador.vida -= int(enemigo.fuerza * 0.75)
            else:
                print("║"+"Fallas el bloqueo. Recibes daño crítico.".center(57)+"║")
                print( "╚" + ("═" * 57) + "╝")
                jugador.vida -= enemigo.fuerza + 5

        else:
            print( "╔"+("═" * 57)+"╗")
            print("║"+" Acción inválida. Pierdes el turno. ".center(57)+"║")
            print("║"+f"{enemigo.nombre} te ataca e inflige {enemigo.fuerza} de daño.".center(57)+"║")
            print( "╚" + ("═" * 57) + "╝")
            jugador.vida -= enemigo.fuerza
        # Turno enemigo (solo ataca)
        if enemigo.vida > 0 and accion == "1":  
            tirada = tirar_d20()
            resultado = interpretar_tirada(tirada)
            atributo = getattr(enemigo, "fuerza")            
            if resultado == "critico_exito":
                daño = atributo * 2
            elif resultado == "exito":
                daño = atributo
            elif resultado == "fallo":
                daño = int(atributo / 2)
            else:
                daño = 0
            print("╔"+("═" * 57)+"╗")   
            print("║"+f"Turno del {enemigo.nombre}:".center(57)+"║")
            print("║"+f"Tirada de d20 del monstruo: {tirada} → {resultado.replace('_', ' ').capitalize()}".center(57)+"║")
            print("║"+f"{enemigo.nombre} te ataca e inflige {daño} de daño.".center(57)+"║")
            jugador.vida -= daño
            print("╚" + ("═" * 57) + "╝")

        #print(f"\nTu vida: {jugador.vida} | Vida del enemigo: {enemigo.vida}")

    # Resultado del combate
    if jugador.vida > 0:
        print("╔"+("═" * 57)+"╗") 
        print("║"+f"¡Has derrotado al {enemigo.nombre} y ganas {enemigo.xp} XP!".center(57)+"║")
        print("╚" + ("═" * 57) + "╝")
        jugador.xp += enemigo.xp
        if jugador.max_xp():
            jugador.level_up()
    else:
        clear()
        print("╔"+("═" * 57)+"╗") 
        print("║"+f"¡Has sido derrotado por el {enemigo.nombre}...!".center(57)+"║")
        print("╚" + ("═" * 57) + "╝")
