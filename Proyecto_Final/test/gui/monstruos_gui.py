import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Importar tu módulo de monstruos
from core import monstruos  # Ajusta según la ruta de tu proyecto

class MonsterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monstruos D&D")
        self.setGeometry(100, 100, 1200, 600)  # Ventana más ancha

        # Layout principal
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Lista de monstruos
        self.list_widget = QListWidget()
        self.list_widget.setMinimumWidth(200)
        main_layout.addWidget(self.list_widget)

        # Panel de información con dos bloques
        info_panel_layout = QHBoxLayout()
        main_layout.addLayout(info_panel_layout)

        # Bloque 1 (izquierda)
        self.block1 = self.crear_bloque_monstruo("Bloque 1")
        info_panel_layout.addWidget(self.block1)

        # Bloque 2 (derecha)
        self.block2 = self.crear_bloque_monstruo("Bloque 2")
        info_panel_layout.addWidget(self.block2)

        # Lista de índices de monstruos
        self.monsters_list = []
        self.monster_blocks = {1: None, 2: None}  # Para rastrear qué monstruo está en cada bloque
        self.cargar_monstruos()

        # Conectar selección
        self.list_widget.currentRowChanged.connect(self.mostrar_detalle)

    def crear_bloque_monstruo(self, titulo):
        """Crea un bloque para mostrar información de un monstruo"""
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box)
        frame.setLineWidth(2)

        layout = QVBoxLayout()
        frame.setLayout(layout)

        # Título del bloque
        title_label = QLabel(titulo)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title_label)

        # Label para la imagen
        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setFixedSize(300, 300)
        layout.addWidget(image_label)

        # TextEdit para la información
        info_text = QTextEdit()
        info_text.setReadOnly(True)
        layout.addWidget(info_text)

        # Guardar referencias a los componentes
        if titulo == "Bloque 1":
            self.image_label1 = image_label
            self.info_text1 = info_text
        else:
            self.image_label2 = image_label
            self.info_text2 = info_text

        return frame

    def cargar_monstruos(self):
        data = monstruos.obtener_monstruos()
        for monster in data:
            self.monsters_list.append(monster['index'])
            self.list_widget.addItem(monster['nombre'])

    def mostrar_detalle(self, row):
        if row < 0:
            return

        monster_index = self.monsters_list[row]

        # Si el monstruo ya está en algún bloque, no hacer nada
        if monster_index in self.monster_blocks.values():
            return

        # Desplazar monstruos entre bloques
        self.desplazar_monstruos(monster_index)

    def desplazar_monstruos(self, nuevo_monstruo_index):
        """Desplaza los monstruos entre bloques y añade el nuevo"""
        # Mover monstruo del bloque 1 al bloque 2
        if self.monster_blocks[1] is not None:
            self.monster_blocks[2] = self.monster_blocks[1]
            self.actualizar_bloque(2, self.monster_blocks[2])

        # Poner el nuevo monstruo en el bloque 1
        self.monster_blocks[1] = nuevo_monstruo_index
        self.actualizar_bloque(1, nuevo_monstruo_index)

    def actualizar_bloque(self, bloque_num, monster_index):
        """Actualiza un bloque específico con la información del monstruo"""
        detalle = monstruos.obtener_detalle_monstruo(monster_index)
        
        # Determinar qué componentes usar según el bloque
        if bloque_num == 1:
            image_label = self.image_label1
            info_text = self.info_text1
        else:
            image_label = self.image_label2
            info_text = self.info_text2
        
        # Cargar imagen
        image_url = detalle.get('imagen')
        if image_url:
            try:
                response = requests.get(image_url, stream=True, timeout=10)
                response.raise_for_status()
                pixmap = QPixmap()
                if pixmap.loadFromData(response.content):
                    image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                else:
                    print("Error: No se pudo cargar la imagen desde los datos")
                    image_label.clear()
            except Exception as e:
                print(f"Error cargando imagen desde {image_url}: {e}")
                image_label.clear()
        else:
            print("No hay URL de imagen disponible")
            image_label.clear()

        # Mostrar información textual CON títulos en negrito
        info = f"<b>Nombre:</b> {detalle.get('nombre', '')}<br>"
        info += f"<b>Tamaño:</b> {detalle.get('tamaño', '')}<br>"
        info += f"<b>Tipo:</b> {detalle.get('tipo', '')}<br>"
        info += f"<b>Alineamiento:</b> {detalle.get('alineamiento', '')}<br>"
        info += f"<b>Clase de Armadura:</b> {detalle.get('clase_de_armadura', '')}<br>"
        info += f"<b>Puntos de Golpe:</b> {detalle.get('puntos_de_golpe', '')}<br>"
        
        # Mejorar la visualización de la velocidad
        speed = detalle.get('desplazamiento', {})
        speed_str = ", ".join([f"{k}: {v}" for k, v in speed.items()])
        info += f"<b>Velocidad:</b> {speed_str}<br>"
        
        info += "<b>Características:</b><br>"
        for key, value in detalle.get('caracteristicas', {}).items():
            info += f"  <b>{key.capitalize()}:</b> {value}<br>"
        
        info += "<b>Acciones:</b><br>"
        for action in detalle.get('acciones', []):
            desc = action.get('descripcion', '')
            info += f"  <b>{action.get('nombre', '')}:</b> {desc}<br>"

        # Configurar el QTextEdit para aceptar HTML
        info_text.setHtml(info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MonsterApp()
    window.show()
    sys.exit(app.exec_())
