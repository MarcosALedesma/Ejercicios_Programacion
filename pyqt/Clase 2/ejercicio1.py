# trabajo realizado por Marcos Ledesma y Agustin Lanthier
# version de Marcos Ledesma
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)

        layout = QGridLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color: lightgrey;")

        # Título
        titulo = QLabel("Formulario de Registro")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-family: Arial; font-size: 24px; font-weight: bold; color: navy;")

        # Campos de texto
        nombre = QLabel("Nombre:")
        nombre.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.input_nombre = QLineEdit()
        self.input_nombre.setStyleSheet("font-family: Verdana; font-size: 12px;")

        email = QLabel("Email:")
        email.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.input_email = QLineEdit()
        self.input_email.setStyleSheet("font-family: Verdana; font-size: 12px;")

        password = QLabel("Password:")
        password.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setStyleSheet("font-family: Verdana; font-size: 12px;")

        # Género
        tituloG = QLabel("Género:") 
        tituloG.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.masculino = QRadioButton("Masculino")
        self.masculino.setStyleSheet("font-family: Verdana; font-size: 12px;")
        self.femenino = QRadioButton("Femenino")
        self.femenino.setStyleSheet("font-family: Verdana; font-size: 12px;")
        self.generos = QButtonGroup()
        self.generos.addButton(self.masculino)
        self.generos.addButton(self.femenino)

        # País
        tituloP = QLabel("País:")
        tituloP.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.paises = QComboBox()
        self.paises.setStyleSheet("font-family: Verdana; font-size: 12px;")
        self.paises.addItems(["Argentina", "Uruguay", "Chile", "Brasil", "Colombia"])

        # Checkbox
        self.terminos = QCheckBox("Acepto los términos y condiciones")
        self.terminos.setStyleSheet("font-family: Verdana; font-size: 12px;")

        # Botón
        boton_registro = QPushButton("Registrarse")
        boton_registro.setStyleSheet("""
            font-family: Verdana; 
            font-size: 14px; 
            font-weight: bold; 
            background-color: darkblue; 
            color: white; 
            border-radius: 5px; 
            padding: 5px;
        """)
        boton_registro.clicked.connect(self.valida_formulario)

        # Layout
        layout.addWidget(titulo, 0, 0, 1, 2)
        layout.addWidget(nombre, 1, 0)
        layout.addWidget(self.input_nombre, 1, 1)
        layout.addWidget(email, 2, 0)
        layout.addWidget(self.input_email, 2, 1)
        layout.addWidget(password, 3, 0)
        layout.addWidget(self.input_password, 3, 1)
        layout.addWidget(tituloG, 4, 0)
        layout.addWidget(self.masculino, 4, 1)
        layout.addWidget(self.femenino, 4, 2)
        layout.addWidget(tituloP, 5, 0)
        layout.addWidget(self.paises, 5, 1)
        layout.addWidget(self.terminos, 6, 0, 1, 2)
        layout.addWidget(boton_registro, 7, 0, 1, 2)

    def valida_formulario(self):
        if not self.input_nombre.text() or not self.input_email.text() or not self.input_password.text():
            QMessageBox.warning(self, "Error", "Todos los campos deben ser completados")
            return

        if not (self.masculino.isChecked() or self.femenino.isChecked()):
            QMessageBox.warning(self, "Error", "Debe seleccionar un género")
            return

        if not self.paises.currentText():
            QMessageBox.warning(self, "Error", "Debe seleccionar un país")
            return

        if not self.terminos.isChecked():
            QMessageBox.warning(self, "Error", "Debe aceptar los términos y condiciones")
            return

        QMessageBox.information(self, "Registro Exitoso", "¡Te has registrado correctamente!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

