import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'dm_data'
        self.user = 'root'  # Cambiar por tu usuario
        self.password = 'miau123'  # Cambiar por tu contraseña
    
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return connection
        except Error as e:
            print(f"Error conectando a MySQL: {e}")
            return None
    
    # ===== JUGADORES =====
    def guardar_jugador(self, jugador):
        connection = self.get_connection()
        if connection is None:
            return False
        
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO jugadores 
                (nombre_jugador, email, telefono)
                VALUES (%s, %s, %s)
            """
            values = (
                jugador['nombre'],
                jugador['email'],
                jugador['telefono']
            )
            
            cursor.execute(query, values)
            connection.commit()
            return cursor.lastrowid  # ID JUGADOR
            
        except Error as e:
            print(f"Error guardando jugador: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def obtener_jugadores(self):
        connection = self.get_connection()
        if connection is None:
            return []
        
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM jugadores ORDER BY nombre_jugador"
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error obteniendo jugadores: {e}")
            return []
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def buscar_jugador_por_nombre(self, nombre):
        connection = self.get_connection()
        if connection is None:
            return None
        
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM jugadores WHERE nombre_jugador = %s"
            cursor.execute(query, (nombre,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error buscando jugador: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    # ===== PERSONAJES =====
    def guardar_personaje(self, personaje):
        connection = self.get_connection()
        if connection is None:
            return False
        
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO personajes 
                (nombre_personaje, raza, clase, nivel, fuerza, destreza, constitucion, 
                 inteligencia, sabiduria, carisma, puntos_golpe_max, puntos_golpe_actuales, jugador_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                personaje['nombre_personaje'],
                personaje['raza'],
                personaje['clase'],
                personaje['nivel'],
                personaje['fuerza'],
                personaje['destreza'],
                personaje['constitucion'],
                personaje['inteligencia'],
                personaje['sabiduria'],
                personaje['carisma'],
                personaje['puntos_golpe_max'],
                personaje['puntos_golpe_actuales'],
                personaje['jugador_id']
            )
            
            cursor.execute(query, values)
            connection.commit()
            return True
            
        except Error as e:
            print(f"Error guardando personaje: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def obtener_personajes_por_jugador(self, jugador_id):
        connection = self.get_connection()
        if connection is None:
            return []
        
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT p.*, j.nombre_jugador 
                FROM personajes p 
                JOIN jugadores j ON p.jugador_id = j.id 
                WHERE p.jugador_id = %s 
                ORDER BY p.nivel DESC, p.nombre_personaje
            """
            cursor.execute(query, (jugador_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error obteniendo personajes: {e}")
            return []
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def obtener_todos_personajes(self):
        connection = self.get_connection()
        if connection is None:
            return []
        
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT p.*, j.nombre_jugador 
                FROM personajes p 
                JOIN jugadores j ON p.jugador_id = j.id 
                ORDER BY j.nombre_jugador, p.nivel DESC
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error obteniendo todos los personajes: {e}")
            return []
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def eliminar_personaje(self, personaje_id):
        connection = self.get_connection()
        if connection is None:
            return False
        
        try:
            cursor = connection.cursor()
            query = "DELETE FROM personajes WHERE id = %s"
            cursor.execute(query, (personaje_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error eliminando personaje: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
