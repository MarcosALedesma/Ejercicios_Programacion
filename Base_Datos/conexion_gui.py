# Proyecto PyQt5 + MySQL
# Todo en un solo archivo

import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel,
    QTableWidget, QTableWidgetItem, QTextEdit, QMessageBox, QGroupBox, QFormLayout, QToolButton, QApplication
)
from PyQt5.QtCore import Qt

# -----------------------------
# CSS / Theme
# -----------------------------
THEME_STYLESHEET = """
QWidget {
    font-family: Arial;
    font-size: 14px;
}
QLineEdit, QTextEdit {
    border: 1px solid #555;
    border-radius: 5px;
    padding: 5px;
}
QPushButton {
    background-color: #3498db;
    color: white;
    border-radius: 5px;
    padding: 5px 10px;
}
QPushButton:hover {
    background-color: #2980b9;
}
QGroupBox {
    border: 1px solid #555;
    border-radius: 5px;
    margin-top: 10px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 3px;
}
QTableWidget {
    border: 1px solid #555;
    gridline-color: #bbb;
}
"""

# -----------------------------
# Función de conexión a MySQL
# -----------------------------
def conectar_mysql(host, database, user, password):
    try:
        conexion = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if conexion.is_connected():
            return conexion
        return None
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# -----------------------------
# Clase principal GUI
# -----------------------------
class AppMySQL(QWidget):
    def __init__(self):
        super().__init__()
        self.conexion = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Usuarios - PyQt5 + MySQL")
        self.setGeometry(200, 200, 900, 700)

        main_layout = QVBoxLayout()

        # Credenciales
        self.cred_group = QGroupBox("Credenciales MySQL")
        form_cred = QFormLayout()
        self.input_host = QLineEdit("127.0.0.1")
        self.input_user = QLineEdit("root")
        self.input_pass = QLineEdit(""); self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_db = QLineEdit("")
        
        form_cred.addRow("Host:", self.input_host)
        form_cred.addRow("Usuario:", self.input_user)
        form_cred.addRow("Contraseña:", self.input_pass)
        form_cred.addRow("Base de datos:", self.input_db)
        self.btn_conectar = QPushButton("Conectar"); self.btn_conectar.clicked.connect(self.conectar_mysql)
        form_cred.addRow(self.btn_conectar)
        self.cred_group.setLayout(form_cred)

        self.toggle_btn = QToolButton()
        self.toggle_btn.setText("Mostrar/Ocultar Credenciales")
        self.toggle_btn.setCheckable(True)
        self.toggle_btn.setChecked(True)
        self.toggle_btn.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.toggle_btn.clicked.connect(self.toggle_credentials)

        # Inputs de usuario y botones en HBox
        input_btn_layout = QHBoxLayout()
        self.input_nombre = QLineEdit(); self.input_nombre.setPlaceholderText("Nombre")
        self.input_email = QLineEdit(); self.input_email.setPlaceholderText("Email")
        self.input_edad = QLineEdit(); self.input_edad.setPlaceholderText("Edad")
        input_btn_layout.addWidget(self.input_nombre)
        input_btn_layout.addWidget(self.input_email)
        input_btn_layout.addWidget(self.input_edad)

        self.btn_insertar = QPushButton("Agregar Usuario"); self.btn_insertar.clicked.connect(self.insertar_usuario)
        self.btn_cargar = QPushButton("Mostrar Usuarios"); self.btn_cargar.clicked.connect(self.cargar_usuarios)
        self.btn_eliminar = QPushButton("Eliminar Usuario (por Email)"); self.btn_eliminar.clicked.connect(self.eliminar_usuario)
        input_btn_layout.addWidget(self.btn_insertar)
        input_btn_layout.addWidget(self.btn_cargar)
        input_btn_layout.addWidget(self.btn_eliminar)

        # Tabla y query en VBox
        self.tabla = QTableWidget(); self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Email", "Edad", "Fecha Creación"])
        self.query_text = QTextEdit(); self.query_text.setReadOnly(True)

        # Agregar al main layout
        main_layout.addWidget(self.toggle_btn)
        main_layout.addWidget(self.cred_group)
        main_layout.addLayout(input_btn_layout)
        main_layout.addWidget(QLabel("Usuarios:"))
        main_layout.addWidget(self.tabla)
        main_layout.addWidget(QLabel("Última Query ejecutada:"))
        main_layout.addWidget(self.query_text)

        self.setLayout(main_layout)

    def conectar_mysql(self):
        self.conexion = conectar_mysql(
            self.input_host.text().strip(),
            self.input_db.text().strip(),
            self.input_user.text().strip(),
            self.input_pass.text().strip()
        )
        if self.conexion: QMessageBox.information(self,"Conexión","Conexión exitosa a MySQL")
        else: QMessageBox.warning(self,"Error","No se pudo conectar")

    def insertar_usuario(self):
        if not self.conexion: QMessageBox.warning(self,"Error","No hay conexión activa"); return
        nombre=self.input_nombre.text().strip(); email=self.input_email.text().strip(); edad=self.input_edad.text().strip()
        if not nombre or not email or not edad: QMessageBox.warning(self,"Error","Todos los campos son obligatorios"); return
        try:
            cursor=self.conexion.cursor(); sql="INSERT INTO usuarios (nombre,email,edad) VALUES (%s,%s,%s)"
            cursor.execute(sql,(nombre,email,int(edad))); self.conexion.commit(); self.query_text.setText(cursor.statement)
            QMessageBox.information(self,"Éxito",f"Usuario '{nombre}' insertado correctamente")
            self.input_nombre.clear(); self.input_email.clear(); self.input_edad.clear()
        except Exception as e: QMessageBox.critical(self,"Error",str(e))

    def cargar_usuarios(self):
        if not self.conexion: QMessageBox.warning(self,"Error","No hay conexión activa"); return
        try:
            cursor=self.conexion.cursor(); sql="SELECT id,nombre,email,edad,fecha_creacion FROM usuarios"
            cursor.execute(sql); usuarios=cursor.fetchall(); self.tabla.setRowCount(len(usuarios))
            for i,fila in enumerate(usuarios):
                for j,valor in enumerate(fila): self.tabla.setItem(i,j,QTableWidgetItem(str(valor)))
            self.query_text.setText(cursor.statement)
        except Exception as e: QMessageBox.critical(self,"Error",str(e))

    def eliminar_usuario(self):
        if not self.conexion: QMessageBox.warning(self,"Error","No hay conexión activa"); return
        email=self.input_email.text().strip()
        if not email: QMessageBox.warning(self,"Error","Debe ingresar un email para eliminar"); return
        try:
            cursor=self.conexion.cursor(); sql="DELETE FROM usuarios WHERE email=%s"
            cursor.execute(sql,(email,)); self.conexion.commit(); self.query_text.setText(cursor.statement)
            if cursor.rowcount>0: QMessageBox.information(self,"Éxito",f"Usuario con email '{email}' eliminado")
            else: QMessageBox.warning(self,"Aviso",f"No existe usuario con email '{email}'")
        except Exception as e: QMessageBox.critical(self,"Error",str(e))

    def toggle_credentials(self):
        self.cred_group.setVisible(self.toggle_btn.isChecked())

# -----------------------------
# Main
# -----------------------------
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(THEME_STYLESHEET)
    ventana=AppMySQL(); ventana.show()
    sys.exit(app.exec_())