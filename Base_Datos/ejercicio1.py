import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',   
            database='comercial',     
            user='root',   
            password=''
        )
        if conexion.is_connected():
            print("Conexión exitosa")
            info_servidor = conexion.get_server_info()
            print(f"Información del servidor: mysql {info_servidor}")

            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            db_actual = cursor.fetchone()
            if db_actual:
                print(f"Base de datos actual: {db_actual[0]}")

            return conexion
        else:
            return None

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def crear_tabla_usuarios(conexion):
    try:
        cursor = conexion.cursor()
        crear_tabla = """
        CREATE TABLE IF NOT EXISTS usuarios(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            edad INT,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(crear_tabla)
        print("Tabla 'usuarios' creada o verificada correctamente")

    except Error as e:
        print(f"Error al crear tabla: {e}")

def insertar_usuario(conexion, nombre, email, edad):
    try:
        cursor = conexion.cursor()
        insertar_sql = "INSERT INTO usuarios (nombre, email, edad) VALUES (%s, %s, %s)"
        datos_usuario = (nombre, email, edad)
        cursor.execute(insertar_sql, datos_usuario)
        conexion.commit()
        print(f"Usuario '{nombre}' insertado correctamente (ID: {cursor.lastrowid})")

    except Error as e:
        print(f"Error al insertar usuario: {e}")

def consultar_usuarios(conexion):
    try:
        cursor = conexion.cursor()
        consulta_sql = "SELECT id, nombre, email, edad, fecha_creacion FROM usuarios"
        cursor.execute(consulta_sql)
        usuarios = cursor.fetchall()

        print("Lista de usuarios:")
        print("." * 80)
        print(f"{'ID':<5}{'nombre':<20}{'email':<30}{'edad':<5}{'fecha_creacion'}")
        print("." * 80)

        for usuario in usuarios:
            id_usuarios, nombre, email, edad, fecha = usuario
            print(f"{id_usuarios:<5}{nombre:<20}{email:<30}{edad:<5}{fecha}")
        print(f"Total de usuarios: {len(usuarios)}")

    except Error as e:
        print(f"Error al consultar usuarios: {e}")

def buscar_usuarios_por_email(conexion, email):
    try:
        cursor = conexion.cursor()
        buscar_sql = "SELECT id, nombre, email, edad, fecha_creacion FROM usuarios WHERE email = %s"
        cursor.execute(buscar_sql, (email,))
        usuario = cursor.fetchone()

        if usuario:
            print("Usuario encontrado:")
            print(f"    id: {usuario[0]}")
            print(f"    nombre: {usuario[1]}")
            print(f"    email: {usuario[2]}")
            print(f"    edad: {usuario[3]}")
            print(f"    fecha de creación: {usuario[4]}")
        else:
            print(f"No se encontró usuario con email {email}")

    except Error as e:
        print(f"Error al buscar usuario: {e}")

def main():
    print("Ejemplo de conexión MySQL")
    print("-" * 80)

    conexion = conectar_mysql()

    if conexion:
        try:
            crear_tabla_usuarios(conexion)

            print("Insertando usuarios de ejemplo")
            insertar_usuario(conexion, "juan perez1", "juan1@gmail.com", 25)
            insertar_usuario(conexion, "juan perez2", "juan2@gmail.com", 25)
            insertar_usuario(conexion, "juan perez3", "juan3@gmail.com", 25)
            insertar_usuario(conexion, "juan perez4", "juan4@gmail.com", 25)

            consultar_usuarios(conexion)

            print("Buscando usuarios por email")
            buscar_usuarios_por_email(conexion, "juan1@gmail.com")
        except Error as e:
            print(f"Error de operación: {e}")
        finally:
            if conexion.is_connected():
                conexion.close()
                print("Conexión cerrada")
    else:
        print("No se pudo establecer conexión con MySQL")
        print("Verifique:")
        print("- que MySQL esté ejecutándose")
        print("- las credenciales de conexión")
        print("- que exista la base de datos indicada")

if __name__ == "__main__":
    main()

