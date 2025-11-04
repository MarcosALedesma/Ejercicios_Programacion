import sys
import os

# Agregar el directorio actual al path para que Python encuentre los módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QComboBox, QSpinBox, QTextEdit,
                             QPushButton, QGroupBox, QFormLayout, QMessageBox,
                             QTabWidget, QListWidget, QSplitter, QMainWindow,
                             QDialog, QDialogButtonBox, QTableWidget, QTableWidgetItem,
                             QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Importar desde core (que está en la misma raíz que pj_gui.py)
from core import pj
from core.database import DatabaseManager

class JugadorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nuevo Jugador")
        self.setModal(True)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        form_layout = QFormLayout()
        
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre del jugador")
        form_layout.addRow("Nombre:", self.nombre_input)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("email@ejemplo.com")
        form_layout.addRow("Email:", self.email_input)
        
        self.telefono_input = QLineEdit()
        self.telefono_input.setPlaceholderText("+54 11 1234-5678")
        form_layout.addRow("Teléfono:", self.telefono_input)
        
        layout.addLayout(form_layout)
        
        # Botones
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
    
    def get_datos(self):
        return {
            'nombre': self.nombre_input.text().strip(),
            'email': self.email_input.text().strip(),
            'telefono': self.telefono_input.text().strip()
        }

class CharacterManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.jugador_actual = None
        self.setup_ui()
        self.cargar_datos_iniciales()
        
    def setup_ui(self):
        self.setWindowTitle("Gestor de Jugadores y Personajes D&D")
        self.setGeometry(100, 100, 1200, 800)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Título
        title = QLabel("🎮 GESTOR DE JUGADORES Y PERSONAJES")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #8B4513; margin: 10px;")
        layout.addWidget(title)
        
        # Crear pestañas
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Pestaña de gestión de jugadores
        self.crear_tab_jugadores()
        
        # Pestaña de creación de personajes
        self.crear_tab_creacion_personaje()
        
        # Pestaña de lista de personajes
        self.crear_tab_lista_personajes()
    
    def crear_tab_jugadores(self):
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Botones superiores
        button_layout = QHBoxLayout()
        
        btn_nuevo_jugador = QPushButton("➕ Nuevo Jugador")
        btn_nuevo_jugador.clicked.connect(self.agregar_jugador)
        btn_nuevo_jugador.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; padding: 8px; }")
        button_layout.addWidget(btn_nuevo_jugador)
        
        btn_actualizar = QPushButton("🔄 Actualizar Lista")
        btn_actualizar.clicked.connect(self.cargar_jugadores)
        button_layout.addWidget(btn_actualizar)
        
        layout.addLayout(button_layout)
        
        # Lista de jugadores
        self.jugadores_list = QListWidget()
        self.jugadores_list.itemClicked.connect(self.seleccionar_jugador)
        layout.addWidget(QLabel("Jugadores:"))
        layout.addWidget(self.jugadores_list)
        
        # Información del jugador seleccionado
        self.jugador_info = QTextEdit()
        self.jugador_info.setReadOnly(True)
        self.jugador_info.setMaximumHeight(150)
        layout.addWidget(QLabel("Información del Jugador:"))
        layout.addWidget(self.jugador_info)
        
        self.tabs.addTab(tab, "👥 Jugadores")
    
    def crear_tab_creacion_personaje(self):
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Mensaje si no hay jugador seleccionado
        self.mensaje_jugador = QLabel("⚠️ Selecciona un jugador en la pestaña 'Jugadores' para crear un personaje")
        self.mensaje_jugador.setStyleSheet("color: #FF6B6B; font-weight: bold; padding: 10px; border: 1px solid #FF6B6B; border-radius: 5px;")
        self.mensaje_jugador.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.mensaje_jugador)
        
        # Formulario de personaje (inicialmente deshabilitado)
        self.form_personaje = QWidget()
        form_layout = QVBoxLayout()
        self.form_personaje.setLayout(form_layout)
        
        # Información del jugador actual
        self.jugador_actual_label = QLabel()
        self.jugador_actual_label.setStyleSheet("font-weight: bold; color: #2E8B57; font-size: 14px;")
        form_layout.addWidget(self.jugador_actual_label)
        
        # Splitter para el formulario
        splitter = QSplitter(Qt.Horizontal)
        form_layout.addWidget(splitter)
        
        # Panel izquierdo - Información básica
        left_panel = QVBoxLayout()
        left_widget = QWidget()
        left_widget.setLayout(left_panel)
        
        # Grupo de información básica
        basic_group = QGroupBox("Información Básica del Personaje")
        basic_layout = QFormLayout()
        basic_group.setLayout(basic_layout)
        
        self.nombre_personaje_input = QLineEdit()
        self.nombre_personaje_input.setPlaceholderText("Nombre del personaje")
        basic_layout.addRow("Nombre:", self.nombre_personaje_input)
        
        self.raza_combo = QComboBox()
        basic_layout.addRow("Raza:", self.raza_combo)
        
        self.clase_combo = QComboBox()
        basic_layout.addRow("Clase:", self.clase_combo)
        
        self.nivel_spin = QSpinBox()
        self.nivel_spin.setRange(1, 20)
        self.nivel_spin.setValue(1)
        self.nivel_spin.valueChanged.connect(self.actualizar_puntos_golpe)
        basic_layout.addRow("Nivel:", self.nivel_spin)
        
        left_panel.addWidget(basic_group)
        
        # Grupo de puntos de golpe
        hp_group = QGroupBox("Puntos de Golpe")
        hp_layout = QFormLayout()
        hp_group.setLayout(hp_layout)
        
        self.pg_max_spin = QSpinBox()
        self.pg_max_spin.setRange(1, 500)
        self.pg_max_spin.setValue(10)
        hp_layout.addRow("PG Máximos:", self.pg_max_spin)
        
        self.pg_actuales_spin = QSpinBox()
        self.pg_actuales_spin.setRange(0, 500)
        self.pg_actuales_spin.setValue(10)
        hp_layout.addRow("PG Actuales:", self.pg_actuales_spin)
        
        left_panel.addWidget(hp_group)
        
        # Panel derecho - Habilidades
        right_panel = QVBoxLayout()
        right_widget = QWidget()
        right_widget.setLayout(right_panel)
        
        abilities_group = QGroupBox("Habilidades")
        abilities_layout = QFormLayout()
        abilities_group.setLayout(abilities_layout)
        
        self.fuerza_spin = QSpinBox()
        self.fuerza_spin.setRange(1, 30)
        self.fuerza_spin.setValue(10)
        abilities_layout.addRow("Fuerza:", self.fuerza_spin)
        
        self.destreza_spin = QSpinBox()
        self.destreza_spin.setRange(1, 30)
        self.destreza_spin.setValue(10)
        abilities_layout.addRow("Destreza:", self.destreza_spin)
        
        self.constitucion_spin = QSpinBox()
        self.constitucion_spin.setRange(1, 30)
        self.constitucion_spin.setValue(10)
        abilities_layout.addRow("Constitución:", self.constitucion_spin)
        
        self.inteligencia_spin = QSpinBox()
        self.inteligencia_spin.setRange(1, 30)
        self.inteligencia_spin.setValue(10)
        abilities_layout.addRow("Inteligencia:", self.inteligencia_spin)
        
        self.sabiduria_spin = QSpinBox()
        self.sabiduria_spin.setRange(1, 30)
        self.sabiduria_spin.setValue(10)
        abilities_layout.addRow("Sabiduría:", self.sabiduria_spin)
        
        self.carisma_spin = QSpinBox()
        self.carisma_spin.setRange(1, 30)
        self.carisma_spin.setValue(10)
        abilities_layout.addRow("Carisma:", self.carisma_spin)
        
        right_panel.addWidget(abilities_group)
        
        # Botón guardar
        self.guardar_btn = QPushButton("💾 Guardar Personaje")
        self.guardar_btn.clicked.connect(self.guardar_personaje)
        self.guardar_btn.setStyleSheet("QPushButton { background-color: #2196F3; color: white; font-weight: bold; padding: 10px; }")
        right_panel.addWidget(self.guardar_btn)
        
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        
        layout.addWidget(self.form_personaje)
        self.form_personaje.setVisible(False)
        
        self.tabs.addTab(tab, "🧙 Crear Personaje")
    
    def crear_tab_lista_personajes(self):
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Botones
        button_layout = QHBoxLayout()
        
        btn_actualizar = QPushButton("🔄 Actualizar Lista")
        btn_actualizar.clicked.connect(self.cargar_todos_personajes)
        button_layout.addWidget(btn_actualizar)
        
        layout.addLayout(button_layout)
        
        # Tabla de personajes
        self.personajes_table = QTableWidget()
        self.personajes_table.setColumnCount(8)
        self.personajes_table.setHorizontalHeaderLabels([
            "ID", "Personaje", "Jugador", "Raza", "Clase", "Nivel", "PG", "Acciones"
        ])
        self.personajes_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.personajes_table)
        
        self.tabs.addTab(tab, "📋 Todos los Personajes")
    
    def cargar_datos_iniciales(self):
        self.cargar_jugadores()
        self.cargar_razas_clases()
    
    def cargar_jugadores(self):
        self.jugadores_list.clear()
        jugadores = self.db.obtener_jugadores()
        for jugador in jugadores:
            self.jugadores_list.addItem(f"{jugador['nombre_jugador']} (ID: {jugador['id']})")
    
    def cargar_razas_clases(self):
        # Cargar razas
        try:
            razas = pj.obtener_razas()
            self.raza_combo.clear()
            for raza in razas:
                self.raza_combo.addItem(raza['nombre'], raza['index'])
        except Exception as e:
            print(f"Error cargando razas: {e}")
            self.raza_combo.addItem("Error al cargar razas")
        
        # Cargar clases
        try:
            clases = pj.obtener_clases()
            self.clase_combo.clear()
            for clase in clases:
                self.clase_combo.addItem(clase['nombre'], clase['index'])
        except Exception as e:
            print(f"Error cargando clases: {e}")
            self.clase_combo.addItem("Error al cargar clases")
    
    def agregar_jugador(self):
        dialog = JugadorDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            datos = dialog.get_datos()
            if datos['nombre']:
                if self.db.guardar_jugador(datos):
                    QMessageBox.information(self, "Éxito", "Jugador agregado correctamente")
                    self.cargar_jugadores()
                else:
                    QMessageBox.critical(self, "Error", "Error al guardar el jugador")
    
    def seleccionar_jugador(self, item):
        texto = item.text()
        nombre_jugador = texto.split(' (ID: ')[0]
        
        jugador = self.db.buscar_jugador_por_nombre(nombre_jugador)
        if jugador:
            self.jugador_actual = jugador
            self.mostrar_info_jugador(jugador)
            self.habilitar_form_personaje(True)
    
    def mostrar_info_jugador(self, jugador):
        info = f"<h3>👤 {jugador['nombre_jugador']}</h3>"
        if jugador['email']:
            info += f"<p><b>Email:</b> {jugador['email']}</p>"
        if jugador['telefono']:
            info += f"<p><b>Teléfono:</b> {jugador['telefono']}</p>"
        
        # Cargar personajes del jugador
        personajes = self.db.obtener_personajes_por_jugador(jugador['id'])
        info += f"<p><b>Personajes:</b> {len(personajes)}</p>"
        if personajes:
            info += "<ul>"
            for pj in personajes[:3]:  # Mostrar solo los primeros 3
                info += f"<li>{pj['nombre_personaje']} - {pj['raza']} {pj['clase']} (Nvl {pj['nivel']})</li>"
            if len(personajes) > 3:
                info += f"<li>... y {len(personajes) - 3} más</li>"
            info += "</ul>"
        
        self.jugador_info.setHtml(info)
        self.jugador_actual_label.setText(f"Creando personaje para: {jugador['nombre_jugador']}")
    
    def habilitar_form_personaje(self, habilitar):
        self.mensaje_jugador.setVisible(not habilitar)
        self.form_personaje.setVisible(habilitar)
    
    def actualizar_puntos_golpe(self):
        # Lógica básica para calcular PG según nivel y constitución
        nivel = self.nivel_spin.value()
        constitucion = self.constitucion_spin.value()
        modificador_constitucion = (constitucion - 10) // 2
        
        # PG base según clase (simplificado)
        clase = self.clase_combo.currentText().lower()
        if any(x in clase for x in ['barbarian', 'barbaro']):
            pg_base = 12
        elif any(x in clase for x in ['fighter', 'paladin', 'ranger', 'guerrero', 'paladin']):
            pg_base = 10
        elif any(x in clase for x in ['cleric', 'druid', 'monk', 'rogue', 'clerigo', 'druida']):
            pg_base = 8
        else:
            pg_base = 6
        
        pg_calculado = pg_base + modificador_constitucion + (nivel - 1) * (pg_base // 2 + modificador_constitucion)
        pg_calculado = max(1, pg_calculado)  # Mínimo 1 PG
        
        self.pg_max_spin.setValue(pg_calculado)
        self.pg_actuales_spin.setValue(pg_calculado)
    
    def guardar_personaje(self):
        if not self.jugador_actual:
            QMessageBox.warning(self, "Error", "Primero selecciona un jugador")
            return
        
        if not self.nombre_personaje_input.text().strip():
            QMessageBox.warning(self, "Error", "Ingresa un nombre para el personaje")
            return
        
        personaje = {
            'nombre_personaje': self.nombre_personaje_input.text().strip(),
            'raza': self.raza_combo.currentText(),
            'clase': self.clase_combo.currentText(),
            'nivel': self.nivel_spin.value(),
            'fuerza': self.fuerza_spin.value(),
            'destreza': self.destreza_spin.value(),
            'constitucion': self.constitucion_spin.value(),
            'inteligencia': self.inteligencia_spin.value(),
            'sabiduria': self.sabiduria_spin.value(),
            'carisma': self.carisma_spin.value(),
            'puntos_golpe_max': self.pg_max_spin.value(),
            'puntos_golpe_actuales': self.pg_actuales_spin.value(),
            'jugador_id': self.jugador_actual['id']
        }
        
        if self.db.guardar_personaje(personaje):
            QMessageBox.information(self, "Éxito", "Personaje guardado correctamente")
            self.limpiar_formulario()
            self.cargar_todos_personajes()
            self.mostrar_info_jugador(self.jugador_actual)  # Actualizar info del jugador
            self.tabs.setCurrentIndex(2)  # Ir a la pestaña de lista
        else:
            QMessageBox.critical(self, "Error", "Error al guardar el personaje")
    
    def limpiar_formulario(self):
        self.nombre_personaje_input.clear()
        self.nivel_spin.setValue(1)
        self.fuerza_spin.setValue(10)
        self.destreza_spin.setValue(10)
        self.constitucion_spin.setValue(10)
        self.inteligencia_spin.setValue(10)
        self.sabiduria_spin.setValue(10)
        self.carisma_spin.setValue(10)
        self.actualizar_puntos_golpe()
    
    def cargar_todos_personajes(self):
        try:
            personajes = self.db.obtener_todos_personajes()
            self.personajes_table.setRowCount(len(personajes))
            
            for row, pj in enumerate(personajes):
                self.personajes_table.setItem(row, 0, QTableWidgetItem(str(pj['id'])))
                self.personajes_table.setItem(row, 1, QTableWidgetItem(pj['nombre_personaje']))
                self.personajes_table.setItem(row, 2, QTableWidgetItem(pj['nombre_jugador']))
                self.personajes_table.setItem(row, 3, QTableWidgetItem(pj['raza']))
                self.personajes_table.setItem(row, 4, QTableWidgetItem(pj['clase']))
                self.personajes_table.setItem(row, 5, QTableWidgetItem(str(pj['nivel'])))
                self.personajes_table.setItem(row, 6, QTableWidgetItem(f"{pj['puntos_golpe_actuales']}/{pj['puntos_golpe_max']}"))
                
                # Botón eliminar
                btn_eliminar = QPushButton("🗑️ Eliminar")
                btn_eliminar.clicked.connect(lambda checked, id=pj['id']: self.eliminar_personaje(id))
                btn_eliminar.setStyleSheet("QPushButton { background-color: #f44336; color: white; padding: 5px; }")
                self.personajes_table.setCellWidget(row, 7, btn_eliminar)
        except Exception as e:
            print(f"Error cargando personajes: {e}")
            QMessageBox.critical(self, "Error", f"Error al cargar los personajes: {e}")
    
    def eliminar_personaje(self, personaje_id):
        reply = QMessageBox.question(self, "Confirmar", 
                                   "¿Estás seguro de que quieres eliminar este personaje?",
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            if self.db.eliminar_personaje(personaje_id):
                QMessageBox.information(self, "Éxito", "Personaje eliminado correctamente")
                self.cargar_todos_personajes()
                if self.jugador_actual:
                    self.mostrar_info_jugador(self.jugador_actual)  # Actualizar info
            else:
                QMessageBox.critical(self, "Error", "Error al eliminar el personaje")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CharacterManagerApp()
    window.show()
    sys.exit(app.exec_())
