import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Importar tu módulo de monstruos
from core import monstruos  # Ajusta según la ruta de tu proyecto

class MonsterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monstruos D&D")
        self.setGeometry(100, 100, 800, 400)

        # Layout principal
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Lista de monstruos
        self.list_widget = QListWidget()
        self.list_widget.setMinimumWidth(200)
        main_layout.addWidget(self.list_widget)

        # Panel de información
        info_layout = QVBoxLayout()
        main_layout.addLayout(info_layout)

        # Label para la imagen
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(300, 300)
        info_layout.addWidget(self.image_label)

        # TextEdit para la información
        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        info_layout.addWidget(self.info_text)

        # Lista de índices de monstruos
        self.monsters_list = []
        self.cargar_monstruos()

        # Conectar selección
        self.list_widget.currentRowChanged.connect(self.mostrar_detalle)

    def cargar_monstruos(self):
        data = monstruos.obtener_monstruos()
        for monster in data:
            self.monsters_list.append(monster['index'])
            self.list_widget.addItem(monster['nombre'])

    def mostrar_detalle(self, row):
        if row < 0:
            return

        monster_index = self.monsters_list[row]
        detalle = monstruos.obtener_detalle_monstruo(monster_index)

        # Cargar imagen 
        image_url = detalle.get('imagen')
        if image_url:
            try:
                response = requests.get(image_url, stream=True, timeout=10)  # Agregar timeout
                response.raise_for_status()
                pixmap = QPixmap()
                if pixmap.loadFromData(response.content):
                    self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                else:
                    print("Error: No se pudo cargar la imagen desde los datos")
                    self.image_label.clear()
            except Exception as e:
                print(f"Error cargando imagen desde {image_url}: {e}")
                self.image_label.clear()
        else:
            print("No hay URL de imagen disponible")
            self.image_label.clear()

        # Mostrar información textual (tu código existente)
        info = f"Nombre: {detalle.get('nombre', '')}\n"
        info += f"Tamaño: {detalle.get('tamaño', '')}\n"
        info += f"Tipo: {detalle.get('tipo', '')}\n"
        info += f"Alineamiento: {detalle.get('alineamiento', '')}\n"
        info += f"Clase de Armadura: {detalle.get('clase_de_armadura', '')}\n"
        info += f"Puntos de Golpe: {detalle.get('puntos_de_golpe', '')}\n"
        
        # Mejorar la visualización de la velocidad
        speed = detalle.get('desplazamiento', {})
        speed_str = ", ".join([f"{k}: {v}" for k, v in speed.items()])
        info += f"Velocidad: {speed_str}\n"
        
        info += "Características:\n"
        for key, value in detalle.get('caracteristicas', {}).items():
            info += f"  {key.capitalize()}: {value}\n"
        
        info += "Acciones:\n"
        for action in detalle.get('acciones', []):
            # Limitar la descripción para que no sea demasiado larga
            desc = action.get('descripcion', '')
            if len(desc) > 200:
                desc = desc[:200] + "..."
            info += f"  {action.get('nombre', '')}: {desc}\n"

        self.info_text.setText(info)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MonsterApp()
    window.show()
    sys.exit(app.exec_())
