#pj.py
import random
from clear_cli import clear  

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.xp = 0
        self.vida = 100

        self.fuerza = self.rolear_stats()
        self.destreza = self.rolear_stats()
        self.inteligencia = self.rolear_stats()
        self.defensa = self.rolear_stats()

    def rolear_stats(self):
        dados = [random.randint(1, 6) for _ in range(6)]
        dados.remove(min(dados))
        return sum(dados)

    def show_stats(self):
        print()
        print("Statsbase".center(21))
        print("╔"+("═" * 20)+"╗")
        print(f"║Nombre: {self.nombre}".ljust(21)+"║")
        print(f"║Nivel: {self.nivel}".ljust(21)+"║")
        print(f"║XP: {self.xp}".ljust(21)+"║")
        print("║"+("═"* 20)+"║")
        print(f"║Fuerza: {self.fuerza}".ljust(21)+"║")
        print(f"║Destreza: {self.destreza}".ljust(21)+"║")
        print(f"║Inteligencia: {self.inteligencia}".ljust(21)+"║")
        print(f"║Defensa: {self.defensa}".ljust(21)+"║")
        print(f"║Vida: {self.vida}".ljust(21)+"║")
        print("╚"+("═" * 20)+"╝")

    def habilidad_especial(self):
        print(f"{self.nombre} no tiene habilidad especial.")

## Xp ## 
    def max_xp(self):    
        return self.xp >= 100

    def cheat_xp(self):
        self.xp += 100 
    
    def level_up(self):
        if self.max_xp():
            self.nivel += 1
            self.xp -= 100 
        print("╔"+("═" * 57)+"╗") 
        
        print("║"+f"Felicidades, {self.nombre},haz subido al nivel {self.nivel}".center(57)+"║")
        print("╚" + ("═" * 57) + "╝")
        self.fuerza = self.fuerza + 1
        self.destreza = self.destreza + 1
        self.inteligencia = self.inteligencia + 1
        self.defensa = self.defensa + 1

class Guerrero(Personaje):
    def __init__(self, base):
        self.__dict__.update(base.__dict__)
        self.clase = "Guerrero"
        self.fuerza += 3
        self.defensa += 2
        self.atributo_ataque = "fuerza"

    def habilidad_especial(self):
        print(f"{self.nombre} Bono de ataque en base a Fuerza")

class Mago(Personaje):
    def __init__(self, base):
        self.__dict__.update(base.__dict__)
        self.clase = "Mago"
        self.inteligencia += 4
        self.vida -= 10
        self.atributo_ataque = "inteligencia"

    def habilidad_especial(self):
        print(f"{self.nombre} Bono de ataque en base Inteligencia")

class Picaro(Personaje):
    def __init__(self, base):
        self.__dict__.update(base.__dict__)
        self.clase = "Pícaro"
        self.destreza += 4
        self.fuerza -= 1
        self.atributo_ataque = "destreza"

    def habilidad_especial(self):
        print(f"{self.nombre} Bono de ataque en base Destreza")

def crear_personaje():
    print("║"+"Ingresa el nombre de tu personaje: ".center(57)+"║")
    nombre = input("╚" + ("═" * 57) + "╝\n> ")
    base = Personaje(nombre)
    clear()
    base.show_stats()
    print("╔"+("═" * 57)+"╗")
    print(f"║Elige una clase:".ljust(58)+"║")
    #print("Elige una clase:")
    print("║"+("═" * 57)+"║")
    print("║ 1 - Guerrero (Fuerza +3, Defensa +2, Bono Fuerza)".ljust(58)+"║")
    print("║ 2 - Mago (Inteligencia +4, Vida -10, Bono Inteligencia)".ljust(58)+"║")
    print("║ 3 - Pícaro (Destreza +4, Fuerza -1, Bono Destreza)".ljust(58)+"║")

    while True:
        opcion = input("╚" + ("═" * 57) + "╝\n> ")

        if opcion == "1": 
            print("Tu opción fue Guerrero")
            return Guerrero(base)
            break
        elif opcion == "2": 
            print("Tu opción fue Mago")
            return Mago(base)
            break
        elif opcion == "3": 
            print("Tu opción fue Picaro")
            return Picaro(base)
            break
        else:
            print("Opción inválida, se crea personaje base.")
    base.show_stats()

#pj = crear_personaje()
#pj.show_stats()
#pj.habilidad_especial()

