import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QComboBox, QSpinBox, QTextEdit,
                             QPushButton, QGroupBox, QFormLayout, QMessageBox,
                             QTabWidget, QListWidget, QSplitter)
from PyQt5.QtCore import Qt

from core import pj
from core.database import DatabaseManager

class CharacterCreatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.setup_ui()
        self.cargar_datos_api()
        
    def setup_ui(self):
        self.setWindowTitle("Creador de Personajes D&D")
        self.setGeometry(100, 100, 1000, 700)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Crear pestañas
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Pestaña de creación
        self.crear_tab_creacion()
        
        # Pestaña de personajes guardados
        self.crear_tab_lista()
        
    def crear_tab_creacion(self):
        tab_creacion = QWidget()
        layout = QVBoxLayout()
        tab_creacion.setLayout(layout)
        
        # Splitter para dividir la ventana
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)
        
        # Panel izquierdo - Información básica
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)
        
        # Grupo de información básica
        basic_group = QGroupBox("Información Básica")
        basic_layout = QFormLayout()
        basic_group.setLayout(basic_layout)
        
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre del personaje")
        basic_layout.addRow("Nombre:", self.nombre_input)
        
        self.raza_combo = QComboBox()
        basic_layout.addRow("Raza:", self.raza_combo)
        
        self.clase_combo = QComboBox()
        basic_layout.addRow("Clase:", self.clase_combo)
        
        self.nivel_spin = QSpinBox()
        self.nivel_spin.setRange(1, 20)
        self.nivel_spin.setValue(1)
        basic_layout.addRow("Nivel:", self.nivel_spin)
        
        left_layout.addWidget(basic_group)
        
        # Grupo de habilidades
        abilities_group = QGroupBox("Habilidades")
        abilities_layout = QFormLayout()
        abilities_group.setLayout(abilities_layout)
        
        self.fuerza_spin = QSpinBox()
        self.fuerza_spin.setRange(1, 20)
        self.fuerza_spin.setValue(10)
        abilities_layout.addRow("Fuerza:", self.fuerza_spin)
        
        self.destreza_spin = QSpinBox()
        self.destreza_spin.setRange(1, 20)
        self.destreza_spin.setValue(10)
        abilities_layout.addRow("Destreza:", self.destreza_spin)
        
        self.constitucion_spin = QSpinBox()
        self.constitucion_spin.setRange(1, 20)
        self.constitucion_spin.setValue(10)
        abilities_layout.addRow("Constitución:", self.constitucion_spin)
        
        self.inteligencia_spin = QSpinBox()
        self.inteligencia_spin.setRange(1, 20)
        self.inteligencia_spin.setValue(10)
        abilities_layout.addRow("Inteligencia:", self.inteligencia_spin)
        
        self.sabiduria_spin = QSpinBox()
        self.sabiduria_spin.setRange(1, 20)
        self.sabiduria_spin.setValue(10)
        abilities_layout.addRow("Sabiduría:", self.sabiduria_spin)
        
        self.carisma_spin = QSpinBox()
        self.carisma_spin.setRange(1, 20)
        self.carisma_spin.setValue(10)
        abilities_layout.addRow("Carisma:", self.carisma_spin)
        
        left_layout.addWidget(abilities_group)
        
        # Trasfondo
        self.trasfondo_text = QTextEdit()
        self.trasfondo_text.setPlaceholderText("Historia y trasfondo del personaje...")
        left_layout.addWidget(QLabel("Trasfondo:"))
        left_layout.addWidget(self.trasfondo_text)
        
        # Botón guardar
        self.guardar_btn = QPushButton("Guardar Personaje")
        self.guardar_btn.clicked.connect(self.guardar_personaje)
        self.guardar_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; padding: 10px; }")
        left_layout.addWidget(self.guardar_btn)
        
        # Panel derecho - Detalles de raza/clase
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)
        
        self.detalles_text = QTextEdit()
        self.detalles_text.setReadOnly(True)
        right_layout.addWidget(QLabel("Detalles:"))
        right_layout.addWidget(self.detalles_text)
        
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([500, 500])
        
        self.tabs.addTab(tab_creacion, "🧙 Crear Personaje")
        
        # Conectar signals
        self.raza_combo.currentTextChanged.connect(self.mostrar_detalle_raza)
        self.clase_combo.currentTextChanged.connect(self.mostrar_detalle_clase)
        
    def crear_tab_lista(self):
        tab_lista = QWidget()
        layout = QVBoxLayout()
        tab_lista.setLayout(layout)
        
        # Botón actualizar
        actualizar_btn = QPushButton("Actualizar Lista")
        actualizar_btn.clicked.connect(self.cargar_personajes_guardados)
        layout.addWidget(actualizar_btn)
        
        # Lista de personajes
        self.lista_personajes = QListWidget()
        self.lista_personajes.itemClicked.connect(self.mostrar_personaje_detalle)
        layout.addWidget(self.lista_personajes)
        
        # Detalles del personaje seleccionado
        self.detalle_personaje_text = QTextEdit()
        self.detalle_personaje_text.setReadOnly(True)
        layout.addWidget(self.detalle_personaje_text)
        
        self.tabs.addTab(tab_lista, "📚 Personajes Guardados")
        
    def cargar_datos_api(self):
        # Cargar razas
        razas = pj.obtener_razas()
        for raza in razas:
            self.raza_combo.addItem(raza['nombre'], raza['index'])
        
        # Cargar clases
        clases = pj.obtener_clases()
        for clase in clases:
            self.clase_combo.addItem(clase['nombre'], clase['index'])
        
        # Cargar personajes guardados
        self.cargar_personajes_guardados()
    
    def cargar_personajes_guardados(self):
        self.lista_personajes.clear()
        personajes = self.db.obtener_personajes()
        for pj in personajes:
            self.lista_personajes.addItem(f"{pj['nombre_personaje']} - {pj['raza']} {pj['clase']} (Nivel {pj['nivel']})")
    
    def mostrar_detalle_raza(self):
        raza_index = self.raza_combo.currentData()
        if raza_index:
            detalle = pj.obtener_detalle_raza(raza_index)
            info = self.formatear_info_raza(detalle)
            self.detalles_text.setText(info)
    
    def mostrar_detalle_clase(self):
        clase_index = self.clase_combo.currentData()
        if clase_index:
            detalle = pj.obtener_detalle_clase(clase_index)
            info = self.formatear_info_clase(detalle)
            self.detalles_text.setText(info)
    
    def formatear_info_raza(self, detalle):
        info = f"<h2>🏹 {detalle['nombre']}</h2>"
        info += f"<p><b>Edad:</b> {detalle.get('edad', 'N/A')}</p>"
        info += f"<p><b>Alineamiento:</b> {detalle.get('alineamiento', 'N/A')}</p>"
        info += f"<p><b>Tamaño:</b> {detalle.get('tamaño', 'N/A')}</p>"
        info += f"<p><b>Idiomas:</b> {detalle.get('descripcion', 'N/A')}</p>"
        
        rasgos = detalle.get('rasgos', [])
        if rasgos:
            info += "<p><b>Rasgos raciales:</b><br>"
            info += "<br>".join([f"• {rasgo}" for rasgo in rasgos])
            info += "</p>"
        
        return info
    
    def formatear_info_clase(self, detalle):
        info = f"<h2>⚔️ {detalle['nombre']}</h2>"
        info += f"<p><b>Dado de Golpe:</b> d{detalle.get('dado_de_golpe', 'N/A')}</p>"
        
        salvaciones = detalle.get('salvaciones', [])
        if salvaciones:
            info += f"<p><b>Salvaciones:</b> {', '.join(salvaciones)}</p>"
        
        competencias = detalle.get('competencias', [])
        if competencias:
            info += "<p><b>Competencias:</b><br>"
            info += "<br>".join([f"• {comp}" for comp in competencias[:10]])  # Mostrar solo 10 
            if len(competencias) > 10:
                info += f"<br>• ... y {len(competencias) - 10} más"
            info += "</p>"
        
        return info
    
    def guardar_personaje(self):
        # Validar datos
        if not self.nombre_input.text().strip():
            QMessageBox.warning(self, "Error", "Por favor ingresa un nombre para el personaje")
            return
        
        personaje = {
            'nombre': self.nombre_input.text().strip(),
            'raza': self.raza_combo.currentText(),
            'clase': self.clase_combo.currentText(),
            'nivel': self.nivel_spin.value(),
            'fuerza': self.fuerza_spin.value(),
            'destreza': self.destreza_spin.value(),
            'constitucion': self.constitucion_spin.value(),
            'inteligencia': self.inteligencia_spin.value(),
            'sabiduria': self.sabiduria_spin.value(),
            'carisma': self.carisma_spin.value(),
            'trasfondo': self.trasfondo_text.toPlainText()
        }
        
        if self.db.guardar_personaje(personaje):
            QMessageBox.information(self, "Éxito", "Personaje guardado correctamente")
            self.limpiar_formulario()
            self.cargar_personajes_guardados()
            self.tabs.setCurrentIndex(1)  # Cambiar a pestaña de lista
        else:
            QMessageBox.critical(self, "Error", "Error al guardar el personaje")
    
    def limpiar_formulario(self):
        self.nombre_input.clear()
        self.nivel_spin.setValue(1)
        self.fuerza_spin.setValue(10)
        self.destreza_spin.setValue(10)
        self.constitucion_spin.setValue(10)
        self.inteligencia_spin.setValue(10)
        self.sabiduria_spin.setValue(10)
        self.carisma_spin.setValue(10)
        self.trasfondo_text.clear()
    
    def mostrar_personaje_detalle(self, item):
        texto = item.text()
        nombre_pj = texto.split(' - ')[0]
        
        personajes = self.db.obtener_personajes()
        for pj in personajes:
            if pj['nombre_personaje'] == nombre_pj:
                info = self.formatear_detalle_personaje(pj)
                self.detalle_personaje_text.setText(info)
                break
    
    def formatear_detalle_personaje(self, personaje):
        info = f"<h1>{personaje['nombre_personaje']}</h1>"
        info += f"<h2>{personaje['raza']} {personaje['clase']} (Nivel {personaje['nivel']})</h2>"
        info += "<hr>"
        
        info += "<h3>🎯 Habilidades</h3>"
        info += "<table width='100%'>"
        info += f"<tr><td><b>Fuerza:</b></td><td>{personaje['fuerza']} (+{(personaje['fuerza']-10)//2})</td>"
        info += f"<td><b>Destreza:</b></td><td>{personaje['destreza']} (+{(personaje['destreza']-10)//2})</td></tr>"
        info += f"<tr><td><b>Constitución:</b></td><td>{personaje['constitucion']} (+{(personaje['constitucion']-10)//2})</td>"
        info += f"<td><b>Inteligencia:</b></td><td>{personaje['inteligencia']} (+{(personaje['inteligencia']-10)//2})</td></tr>"
        info += f"<tr><td><b>Sabiduría:</b></td><td>{personaje['sabiduria']} (+{(personaje['sabiduria']-10)//2})</td>"
        info += f"<td><b>Carisma:</b></td><td>{personaje['carisma']} (+{(personaje['carisma']-10)//2})</td></tr>"
        info += "</table>"
        
        if personaje['trasfondo']:
            info += "<hr>"
            info += f"<h3>📖 Trasfondo</h3>"
            info += f"<p>{personaje['trasfondo']}</p>"
        
        info += f"<hr><p><i>Creado: {personaje['created_at']}</i></p>"
        
        return info

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CharacterCreatorApp()
    window.show()
    sys.exit(app.exec_())
