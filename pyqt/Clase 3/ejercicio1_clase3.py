import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class GradientLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("Verdana", 28, QFont.Bold))  # Puedes cambiar la fuente aquí

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), 0) 

        gradient.setColorAt(0.0, QColor(255, 0, 0))    # Rojo 
        #gradient.setColorAt(0.5, QColor(255, 255, 255))  # Blanco
        gradient.setColorAt(1.0, QColor(0, 0, 0))      # Negro 

        painter.setFont(self.font())
        path = QPainterPath()
        path.addText(0, self.height() - 10, self.font(), self.text())
        painter.fillPath(path, gradient)

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 450)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color:darkgrey;")
        # Titul
        """
        titulo = QLabel("Formulario De Afiliados")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-family: Arial; font-size: 24px; font-weight: bold; color: darkred;")
        layout.addWidget(titulo)
        """
        titulo = GradientLabel("Formulario De Afiliados")
        fuente = QFont("Verdana", 28, QFont.Bold)  # Fuente Verdana, tamaño 28, negrita
        titulo.setFont(fuente)
        layout.addWidget(titulo)
        
        # Imagen 
        pixmap = QPixmap("logo.png")
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        image_label.setFixedHeight(150)  # Ajusta la altura de la imagen
        layout.addWidget(image_label, alignment=Qt.AlignCenter)

        # Campos de texto
        nombre = QLabel("Nombre:")
        nombre.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.input_nombre = QLineEdit()
        self.input_nombre.setStyleSheet("font-family: Verdana; font-size: 12px;")

        apellido = QLabel("Apellido:")
        apellido.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.input_apellido = QLineEdit()
        self.input_apellido.setStyleSheet("font-family: Verdana; font-size: 12px;")

        dni = QLabel("Dni:")
        dni.setStyleSheet("font-family: Verdana; font-size: 14px; font-weight: bold;")
        self.input_dni = QLineEdit()
        self.input_dni.setStyleSheet("font-family: Verdana; font-size: 12px;")

        fecha = QLabel("Fecha de nacimiento:")
        self.input_fecha = QDateEdit()
        self.input_fecha.setCalendarPopup(True)
        self.input_fecha.setDate(QDate.currentDate())

        # Layout en grid
        form_layout = QGridLayout()
        form_layout.addWidget(nombre, 0, 0)
        form_layout.addWidget(self.input_nombre, 0, 1)
        form_layout.addWidget(apellido, 1, 0)
        form_layout.addWidget(self.input_apellido, 1, 1)
        form_layout.addWidget(dni, 2, 0)
        form_layout.addWidget(self.input_dni, 2, 1)
        form_layout.addWidget(fecha, 3, 0)
        form_layout.addWidget(self.input_fecha, 3, 1)

        layout.addLayout(form_layout)

class VentanaHerramientas(QWidget):
    def __init__(self, ventana_formulario):
        super().__init__()
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        self.ventana_formulario = ventana_formulario

        layout = QVBoxLayout()
        self.setLayout(layout)

        # botones
        boton_guardar = QPushButton("Guardar")
        boton_guardar.setFixedSize(QSize(150, 50))
        boton_guardar.setStyleSheet("""
            font-family: Verdana; 
            font-size: 14px; 
            font-weight: bold; 
            background-color: darkred; 
            color: white; 
            border-radius: 5px; 
            padding: 5px;
        """)       
        boton_abrir = QPushButton("Abrir")
        boton_abrir.setFixedSize(QSize(150, 50))
        boton_abrir.setStyleSheet("""
            font-family: Verdana; 
            font-size: 14px; 
            font-weight: bold; 
            background-color: darkred; 
            color: white; 
            border-radius: 5px; 
            padding: 5px;
        """)
        boton_buscar = QPushButton("Buscar")
        boton_buscar.setFixedSize(QSize(150, 50))
        boton_buscar.setStyleSheet("""
            font-family: Verdana; 
            font-size: 14px; 
            font-weight: bold; 
            background-color: darkred; 
            color: white; 
            border-radius: 5px; 
            padding: 5px;
        """)       
        boton_salir = QPushButton("Salir")
        boton_salir.setFixedSize(QSize(150, 50))
        boton_salir.setStyleSheet("""
            font-family: Verdana; 
            font-size: 14px; 
            font-weight: bold; 
            background-color: darkred; 
            color: white; 
            border-radius: 5px; 
            padding: 5px;
        """)

        layout.addWidget(boton_guardar)
        layout.addWidget(boton_buscar)
        layout.addWidget(boton_abrir)
        layout.addWidget(boton_salir)

        layout.setAlignment(Qt.AlignCenter)

        # botones acciones
        boton_guardar.clicked.connect(self.guardar_datos)
        boton_salir.clicked.connect(self.cerrar_todo)

    def guardar_datos(self):
        nombre = self.ventana_formulario.input_nombre.text()
        apellido = self.ventana_formulario.input_apellido.text()
        dni = self.ventana_formulario.input_dni.text()

        if not nombre or not apellido or not dni:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
        else:
            QMessageBox.information(
                self, "Datos guardados",
                f"Nombre: {nombre}\nApellido: {apellido}\nDNI: {dni}"
            )

    def cerrar_todo(self):
        self.ventana_formulario.close()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_form = VentanaFormulario()
    ventana_herr = VentanaHerramientas(ventana_form)
    ventana_form.show()
    ventana_herr.show()
    sys.exit(app.exec_())

