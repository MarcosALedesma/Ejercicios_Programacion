# Práctico PyQt5: Formulario de compra de pasaje de avión
# --------------------------------------------------------
#
# En este práctico, construirás paso a paso un formulario de compra de pasaje aéreo.
# Cada ejercicio suma widgets y lógica, guiando el aprendizaje de PyQt5 y QGridLayout.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Estructura básica y datos del pasajero
# -----------------------------------------------------------------------------
# Teoría:
# - QLabel muestra texto en la interfaz.
# - QLineEdit permite ingresar texto.
# - QGridLayout organiza los widgets en filas y columnas.
#
# Consigna:
# - Ventana 500x350, título “Compra de Pasaje Aéreo”.
# - QLabel grande y centrado: “Formulario de Compra”.
# - QLabel “Nombre:” y QLineEdit al lado.
# - QLabel “Apellido:” y QLineEdit al lado.
# - QLabel “DNI:” y QLineEdit al lado.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compra de Pasaje Aéreo")
        self.setGeometry(100, 100, 500, 350)
        layout = QGridLayout()
        self.setLayout(layout)

        # Título
        titulo = QLabel("Formulario de Compra")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-family: Arial; font-size: 24px; font-weight: bold; color: green;")

        # Campos de texto
        nombre = QLabel("Nombre:")
        nombre.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.input_nombre = QLineEdit()
        self.input_nombre.setStyleSheet("font-family: Verdana; font-size: 12px;")

        email = QLabel("Email:")
        email.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.input_email = QLineEdit()
        self.input_email.setStyleSheet("font-family: Verdana; font-size: 12px;")

        apellido = QLabel("Apellido:")
        apellido.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.input_apellido = QLineEdit()
        self.input_apellido.setEchoMode(QLineEdit.Password)
        self.input_apellido.setStyleSheet("font-family: Verdana; font-size: 12px;")

        # COMPLETAR: Crear QLabel grande y centrado ("Formulario de Compra")
        # COMPLETAR: Crear QLabel y QLineEdit para Nombre, Apellido y DNI
        # layout.addWidget(...)
                # Layout
        layout.addWidget(titulo, 0, 0, 1, 2)
        layout.addWidget(nombre, 1, 0)
        layout.addWidget(self.input_nombre, 1, 1)
        layout.addWidget(apellido, 2, 0)
        layout.addWidget(self.input_email, 2, 1)
        layout.addWidget(email, 3, 0)
        layout.addWidget(self.input_apellido, 3, 1)
        
# -----------------------------------------------------------------------------
# Ejercicio 2: Selección de vuelo
# -----------------------------------------------------------------------------
# Teoría:
# - QComboBox permite elegir una opción de una lista desplegable.
# - QDateEdit permite seleccionar una fecha.
#
# Consigna:
# - Agregar QLabel “Origen:” y QComboBox con al menos 3 ciudades.
# - Agregar QLabel “Destino:” y QComboBox con al menos 3 ciudades.
# - Agregar QLabel “Fecha de vuelo:” y QDateEdit.

# -----------------------------------------------------------------------------
# Ejercicio 3: Clase y cantidad de pasajeros
# -----------------------------------------------------------------------------
# Teoría:
# - QRadioButton permite seleccionar una opción (Ej: clase turista o ejecutiva).
# - QSpinBox permite elegir un número (Ej: cantidad de pasajeros).
#
# Consigna:
# - Agregar QRadioButton para “Turista” y “Ejecutiva”.
# - Agregar QLabel “Cantidad de pasajeros:” y QSpinBox (mínimo 1, máximo 10).

# -----------------------------------------------------------------------------
# Ejercicio 4: Confirmación y resumen
# -----------------------------------------------------------------------------
# Teoría:
# - QPushButton ejecuta una función al hacer clic.
# - QMessageBox muestra mensajes emergentes.
#
# Consigna:
# - Agregar QPushButton “Comprar”.
# - Al hacer clic, mostrar un resumen de la compra en un QMessageBox.

# -----------------------------------------------------------------------------
# Ejercicio 5: Personalización visual
# -----------------------------------------------------------------------------
# Consigna:
# - Cambiar colores, fuentes y tamaño de los widgets para una interfaz moderna.
# - Centrar el formulario en la ventana.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
