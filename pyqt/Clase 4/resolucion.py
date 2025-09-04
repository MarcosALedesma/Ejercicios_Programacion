# Práctico PyQt5: Editor de Texto con Menús y Diálogos
# ------------------------------------------------
#
# Objetivo: Crear un editor de texto completo integrando todos los conceptos aprendidos:
# menús, diálogos, gestión de archivos, barras de estado y shortcuts de teclado.
#
# Este ejercicio te guiará para construir una aplicación profesional paso a paso.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Ventana principal con área de texto
# -----------------------------------------------------------------------------
# Teoría:
# - QMainWindow es la base para aplicaciones con menús y barras de herramientas.
# - QTextEdit permite editar texto con formato básico.
# - setCentralWidget() define el widget principal de la ventana.
#
# Consigna:
# - Crear ventana principal (QMainWindow) de 800x600, título "Editor de Texto".
# - Agregar QTextEdit como widget central.
# - Configurar texto inicial: "Escribe aquí tu texto..."

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenuBar, 
                             QAction, QFileDialog, QMessageBox, QStatusBar,
                             QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from theme import * 

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Texto Open source")
        self.setGeometry(100, 100, 800, 600)
        
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setPlaceholderText("Escribe aquí tu texto...")
        # Complementos
        self.crear_menus()
        self.crear_barra_estado()

# -----------------------------------------------------------------------------
# Ejercicio 2: Crear la barra de menús
# -----------------------------------------------------------------------------
# Teoría:
# - menuBar() devuelve la barra de menús de QMainWindow.
# - addMenu() crea un menú nuevo.
# - QAction representa una acción que puede estar en menús o barras de herramientas.
#
# Consigna:
# - Crear menú "Archivo" con opciones: "Nuevo", "Abrir", "Guardar", "Salir".
# - Crear menú "Editar" con opciones: "Cortar", "Copiar", "Pegar".
# - Crear menú "Ayuda" con opción: "Acerca de".

    def crear_menus(self):
        bar_menu = self.menuBar()
        
        #=== TEXT MENU ===#
        menu_file = bar_menu.addMenu('&Archivo')
        
        # New file 
        new_file = QAction('&Nuevo', self)
        new_file.setShortcut(QKeySequence.New)  # Ctrl+N 
        new_file.triggered.connect(self.nuevo_archivo)
        new_file.setShortcutContext(Qt.ApplicationShortcut)
        menu_file.addAction(new_file)
        menu_file.addSeparator()
        # OPEN FILE 
        open_file =QAction('&Abrir',self)
        open_file.setShortcut(QKeySequence.Open)
        open_file.triggered.connect(self.abrir_archivo)
        open_file.setShortcutContext(Qt.ApplicationShortcut)
        menu_file.addAction(open_file)
        menu_file.addSeparator()
        #SAVE FILE 
        save_file =QAction('&Guardar',self)
        save_file.setShortcut(QKeySequence.Save)
        save_file.triggered.connect(self.guardar_archivo)
        save_file.setShortcutContext(Qt.ApplicationShortcut)
        menu_file.addAction(save_file)
        menu_file.addSeparator()
        #SAVEAS FILE
        saveas_file =QAction('&Guardar Como',self)
        saveas_file.setShortcut(QKeySequence.SaveAs)
        saveas_file.triggered.connect(self.guardar_como)
        saveas_file.setShortcutContext(Qt.ApplicationShortcut)
        menu_file.addAction(saveas_file)
        menu_file.addSeparator()
        #CLOSE FILE 
        close_file =QAction('&Salir',self)
        close_file.setShortcut(QKeySequence.Quit)
        close_file.triggered.connect(self.salir)
        close_file.setShortcutContext(Qt.ApplicationShortcut)
        menu_file.addAction(close_file)
        menu_file.addSeparator()
        

        # === HELP MENU ===#
        help_menu = bar_menu.addMenu('A&yuda')
        
        about_this = QAction('&Acerca de...', self)
        about_this.setShortcut(QKeySequence.HelpContents)
        about_this.triggered.connect(self.acerca_de)
        help_menu.addAction(about_this)
        pass

# -----------------------------------------------------------------------------
# Ejercicio 3: Implementar funciones de archivo
# -----------------------------------------------------------------------------

    def nuevo_archivo(self):
        # NEW FILE
        if self.editor.document().isModified():
            respuesta = QMessageBox.question(self, 'Nuevo archivo',
                                           '¿Desea guardar los cambios?',
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if respuesta == QMessageBox.Yes:
                self.guardar_archivo()
            elif respuesta == QMessageBox.Cancel:
                return
        
        self.editor.clear()
        self.archivo_actual = None
        self.setWindowTitle("Editor - Nuevo documento")
        self.statusBar().showMessage("Nuevo documento creado", 2000)
    
    def abrir_archivo(self):
        # OPEN FILE
        archivo, _ = QFileDialog.getOpenFileName(
            self,                           # Ventana padre
            'Abrir archivo',               # Título del diálogo
            '',                           # Directorio inicial (vacío = último usado)
            'Archivos de texto (*.txt);;Todos los archivos (*.*)'  # Filtros
        )
        
        if archivo:  # Si el usuario seleccionó un archivo
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.editor.setPlainText(contenido)
                
                self.archivo_actual = archivo
                self.setWindowTitle(f"Editor - {archivo}")
                self.statusBar().showMessage(f"Archivo abierto: {archivo}", 3000)
                
            except Exception as e:
                QMessageBox.critical(self, 'Error',
                                   f'No se pudo abrir el archivo:\n{str(e)}')
    
    def guardar_archivo(self):
        # SAVE FILE
        if self.archivo_actual:
            self._escribir_archivo(self.archivo_actual)
        else:
            self.guardar_como()
    
    def guardar_como(self):
        #SAVEAS FILE
        archivo, _ = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo como',
            '',
            'Archivos de texto (*.txt);;Todos los archivos (*.*)'
        )
        if archivo:
            if not archivo.lower().endswith(".txt"):
                archivo += ".txt"
            self._escribir_archivo(archivo) 
    
    def _escribir_archivo(self, archivo):
        # WRITE FILE
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(self.editor.toPlainText())
            
            self.archivo_actual = archivo
            self.setWindowTitle(f"Editor - {archivo}")
            self.statusBar().showMessage(f"Archivo guardado: {archivo}", 3000)
            self.editor.document().setModified(False)
            
        except Exception as e:
            QMessageBox.critical(self, 'Error al guardar',
                               f'No se pudo guardar el archivo:\n{str(e)}')# -----------------------------------------------------------------------------
# Ejercicio 4: Agregar diálogos informativos
# -----------------------------------------------------------------------------
# Teoría:
# - QMessageBox permite mostrar mensajes, advertencias y preguntas al usuario.
# - QMessageBox.information() muestra información.
# - QMessageBox.question() hace preguntas con botones Sí/No.
#
# Consigna:
# - Implementar acerca_de(): mostrar información del programa.
# - Modificar salir(): preguntar si desea guardar antes de cerrar.

    def acerca_de(self):
        # HELP
        QMessageBox.about(self, 'Acerca de Editor',
                         '''<h3>Aplicacion Open source</h3>
                         <p>Creado por Marcos Ledesma y Agustin Lahthier</p>
                         <p>DE TUP1 de UTNFRVT</p>
                         <p>Es open source no apto para windwos</p>''')
        pass
    
    def salir(self):
        # QUIT
        respuesta = QMessageBox.question(self, 'Salir', 
                                         '¿Desea guardar los cambios antes de salir?',
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if respuesta == QMessageBox.Yes:
            self.guardar_archivo()
        elif respuesta == QMessageBox.No:
            self.close()
        pass

# -----------------------------------------------------------------------------
# Ejercicio 5: Agregar barra de estado
# -----------------------------------------------------------------------------
# Teoría:
# - QStatusBar muestra información en la parte inferior de la ventana.
# - statusBar() devuelve la barra de estado de QMainWindow.
# - showMessage() muestra un mensaje temporal.
#
# Consigna:
# - Agregar barra de estado que muestre "Listo" al inicio.
# - Actualizar mensaje cuando se realizan acciones (abrir, guardar, etc.).

    def crear_barra_estado(self):
        self.statusBar().showMessage('Listo')
        self.editor.cursorPositionChanged.connect(self.actualizar_cursor)

    def actualizar_cursor(self):
        cursor = self.editor.textCursor() 
        linea = cursor.blockNumber() + 1   
        columna = cursor.columnNumber() + 1 
        self.statusBar().showMessage(f'Línea: {linea}, Columna: {columna}')

# -----------------------------------------------------------------------------
# Ejercicio 6: Integración completa
# -----------------------------------------------------------------------------
# Consigna:
# - Llamar todos los métodos de configuración en __init__.
# - Probar todas las funcionalidades del editor.
# - Personalizar colores, fuentes o agregar más opciones de menú.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = EditorTexto() 
    app.setStyleSheet(chaca_theme) 
    editor.show()
    sys.exit(app.exec_())

# -----------------------------------------------------------------------------
# Ejercicio Extra: Mejoras opcionales
# -----------------------------------------------------------------------------
# - Agregar función "Buscar y reemplazar".
# - Implementar vista previa de impresión.
# - Añadir formato de texto (negrita, cursiva).
# - Crear diálogo de configuración de fuente.
# - Implementar funcionalidad de "Archivos recientes".
