import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'dm_data'
        self.user = 'root'  # Cambiar
        self.password = ''  # Cambiar
    
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
    
    def guardar_personaje(self, personaje):
        connection = self.get_connection()
        if connection is None:
            return False
        
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO personajes 
                (nombre_personaje, raza, clase, nivel, fuerza, destreza, constitucion, 
                 inteligencia, sabiduria, carisma, trasfondo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                personaje['nombre'],
                personaje['raza'],
                personaje['clase'],
                personaje['nivel'],
                personaje['fuerza'],
                personaje['destreza'],
                personaje['constitucion'],
                personaje['inteligencia'],
                personaje['sabiduria'],
                personaje['carisma'],
                personaje['trasfondo']
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
    
    def obtener_personajes(self):
        connection = self.get_connection()
        if connection is None:
            return []
        
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM personajes ORDER BY created_at DESC"
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error obteniendo personajes: {e}")
            return []
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
