class Personaje:
    def __init__(self, turno, nombre=None):
        if nombre is None:
            nombre = input("Ingrese su nombre: ")
        self.nombre = nombre
        self.turno = turno
        self.posicion = 0

    def avanzar(self, cantidad):
        self.posicion += cantidad
        if self.posicion > 10:
            self.posicion = 10

    def mostrar_estado(self):
        print(f"{self.nombre} está en la casilla {self.posicion}")