import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
from Conexion_Mysql import Comunicacion


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

        # Cargar la interfaz gráfica desde el archivo .ui
        loadUi('C:\\Users\\Joselo\\Desktop\\Barras\\Lector\\Diseño.ui', self)

        # Configurar eventos y funcionalidad aquí
        
        

       
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = VentanaPrincipal()
        window.show()
        sys.exit(app.exec_())

        



             






