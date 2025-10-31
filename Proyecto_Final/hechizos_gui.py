import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget, QLabel, 
                             QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit,
                             QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt

# Importar tu módulo de hechizos
from core import hechizos  # Ajusta según la ruta de tu proyecto

class SpellsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hechizos D&D")
        self.setGeometry(100, 100, 900, 600)

        # Lista completa de hechizos (para el buscador)
        self.todos_hechizos = []
        self.spells_list = []  # Índices de hechizos mostrados actualmente
        
        self.setup_ui()
        self.cargar_hechizos()

    def setup_ui(self):
        # Layout principal
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Panel izquierdo
        left_panel = QVBoxLayout()
        main_layout.addLayout(left_panel)

        # Barra de búsqueda
        search_layout = QHBoxLayout()
        left_panel.addLayout(search_layout)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar hechizos...")
        self.search_input.textChanged.connect(self.buscar_hechizos)
        search_layout.addWidget(self.search_input)

        # Botón para limpiar búsqueda
        self.clear_button = QPushButton("X")
        self.clear_button.setFixedWidth(30)
        self.clear_button.clicked.connect(self.limpiar_busqueda)
        self.clear_button.setToolTip("Limpiar búsqueda")
        search_layout.addWidget(self.clear_button)

        # Lista de hechizos
        self.list_widget = QListWidget()
        self.list_widget.setMinimumWidth(250)
        left_panel.addWidget(self.list_widget)

        # Panel de información
        info_layout = QVBoxLayout()
        main_layout.addLayout(info_layout)

        # TextEdit para la información
        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        info_layout.addWidget(self.info_text)

        # Conectar selección
        self.list_widget.currentRowChanged.connect(self.mostrar_detalle)

    def cargar_hechizos(self):
        data = hechizos.obtener_hechizos()
        self.todos_hechizos = data  # Guardar todos los hechizos para búsqueda
        
        for spell in data:
            self.spells_list.append(spell['index'])
            self.list_widget.addItem(spell['nombre'])

    def buscar_hechizos(self):
        texto_busqueda = self.search_input.text().lower().strip()
        
        # Limpiar la lista actual
        self.list_widget.clear()
        self.spells_list.clear()
        
        if not texto_busqueda:
            # Si no hay texto, mostrar todos los hechizos
            for spell in self.todos_hechizos:
                self.spells_list.append(spell['index'])
                self.list_widget.addItem(spell['nombre'])
        else:
            # Filtrar hechizos que coincidan con la búsqueda
            for spell in self.todos_hechizos:
                if texto_busqueda in spell['nombre'].lower():
                    self.spells_list.append(spell['index'])
                    self.list_widget.addItem(spell['nombre'])
        
        # Mostrar resultado de búsqueda
        if self.list_widget.count() == 0:
            self.list_widget.addItem("No se encontraron hechizos")
            self.info_text.setText("No se encontraron hechizos que coincidan con tu búsqueda.")
        else:
            # Seleccionar el primer resultado si hay coincidencias
            self.list_widget.setCurrentRow(0)

    def limpiar_busqueda(self):
        self.search_input.clear()
        # Esto automáticamente disparará buscar_hechizos() y mostrará todos

    def mostrar_detalle(self, row):
        if row < 0 or row >= len(self.spells_list):
            return

        spell_index = self.spells_list[row]
        detalle = hechizos.obtener_detalle_hechizo(spell_index)

        # Mostrar información del hechizo
        info = self.formatear_info_hechizo(detalle)
        self.info_text.setText(info)

    def formatear_info_hechizo(self, detalle):
        # Determinar el nivel del hechizo para el emoji
        nivel = detalle.get('nivel', 0)
        if nivel == 0:
            nivel_emoji = "🪄"
            nivel_texto = "Truco"
        else:
            nivel_emoji = "✨"
            nivel_texto = f"Nivel {nivel}"
        
        info = f"<h2>{nivel_emoji} {detalle.get('nombre', '')}</h2>"
        info += f"<p><b>{nivel_texto}</b> • <b>{detalle.get('escuela', '')}</b></p>"
        
        info += "<hr>"
        
        # Información básica en formato tabla
        info += "<table width='100%'>"
        info += f"<tr><td><b>Tiempo de lanzamiento:</b></td><td>{detalle.get('tiempo_de_lanzamiento', '')}</td></tr>"
        info += f"<tr><td><b>Alcance:</b></td><td>{detalle.get('alcance', '')}</td></tr>"
        info += f"<tr><td><b>Duración:</b></td><td>{detalle.get('duracion', '')}</td></tr>"
        info += "</table>"
        
        info += "<hr>"
        
        # Componentes
        componentes = detalle.get('componentes', [])
        componentes_texto = ', '.join(componentes)
        info += f"<p><b>Componentes:</b> {componentes_texto}</p>"
        
        materiales = detalle.get('materiales', '')
        if materiales:
            info += f"<p><b>Materiales:</b> {materiales}</p>"
        
        info += "<hr>"
        
        # Descripción
        descripcion = detalle.get('descripcion', '')
        info += f"<p><b>Descripción:</b></p>"
        info += f"<p style='text-align: justify;'>{descripcion}</p>"
        
        # Clases que pueden usar el hechizo
        clases = detalle.get('clases', [])
        if clases:
            info += "<hr>"
            info += f"<p><b>Clases que pueden usar este hechizo:</b><br>"
            info += f"{', '.join(clases)}</p>"
        
        return info


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpellsApp()
    window.show()
    sys.exit(app.exec_())
