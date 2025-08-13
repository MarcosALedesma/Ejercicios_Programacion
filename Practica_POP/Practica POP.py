import random

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
        dados = [random.randint(1, 6) for _ in range(6)] #tirar 6 dados de 6 caras
        dados.remove(min(dados))
        return sum(dados)

    def show_stats(self):
        print("=" * 20)
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"XP: {self.xp}")
        print("--------------------")
        print(f"Fuerza: {self.fuerza}")
        print(f"Destreza: {self.destreza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        if hasattr(self, "clase"): # "hasattr" verifica si una clase tiene un atributo  
            print(f"Clase: {self.clase}")
        print("=" * 20)


## Xp ## 
    def max_xp(self):    
        return self.xp >= 100

    def cheat_xp(self): #test de xp
        self.xp += 100 
    
    def level_up(self):
        if self.max_xp():
            self.nivel += 1
            self.xp -= 100 
        print("Felicidades", self.nombre,"haz subido al nivel", self.nivel)
        self.fuerza = self.fuerza + 1
        self.destreza = self.destreza + 1
        self.inteligencia = self.inteligencia + 1
        self.defensa = self.defensa + 1

class Guerrero(Personaje):
    def __init__(self, base):
         #se le pasa el "diccionario" ya que "super()" da un "error" que genera las stats al inico y remplaza luego de elegir .
        self.__dict__.update(base.__dict__)
        self.clase = "Guerrero"
        self.fuerza += 3
        self.defensa += 2
        self.atributo_ataque = "fuerza"

    #def habilidad_especial(self):
    #    print(f"{self.nombre} usa Golpe Poderoso!")  #Mejora a futuro

class Mago(Personaje):
    def __init__(self, base):
        self.__dict__.update(base.__dict__)
        self.clase = "Mago"
        self.inteligencia += 4
        self.vida -= 10
        self.atributo_ataque = "inteligencia"

    #def habilidad_especial(self):
    #    print(f"{self.nombre} lanza Bola de Fuego!") #Mejora a futuro

class Picaro(Personaje):
    def __init__(self, base):
        self.__dict__.update(base.__dict__)
        self.clase = "Pícaro"
        self.destreza += 4
        self.fuerza -= 1
        self.atributo_ataque = "destreza"

    #def habilidad_especial(self):
    #    print(f"{self.nombre} usa Ataque Sorpresa!") #Mejora a futuro

def crear_personaje():
    nombre = input("Ingresa el nombre de tu personaje: ")
    base = Personaje(nombre)
    base.show_stats()

    print("Elige una clase:")
    print("1 - Guerrero (Fuerza +3, Defensa +2, habilidad: Golpe Poderoso)")
    print("2 - Mago (Inteligencia +4, Vida -10, habilidad: Bola de Fuego)")
    print("3 - Pícaro (Destreza +4, Fuerza -1, habilidad: Ataque Sorpresa)")
    while True:
        opcion = input("Número de clase: ")
        if opcion == "1":
            return Guerrero(base)
            break
        elif opcion == "2":
            break
            return Mago(base)
        elif opcion == "3":
            break
            return Picaro(base)
        else:
            print("Opción inválida, intente de nuevo")
        

pj = crear_personaje()
pj.show_stats()
#pj.habilidad_especial()

