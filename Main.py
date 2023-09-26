import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar la interfaz gráfica desde el archivo .ui
        loadUi('C:\\Users\\Joselo\\Desktop\\Barras\\Lector\\Diseño.ui', self)

        # Configurar eventos y funcionalidad aquí

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self)._init_()
        
         loadUi('Diseño.ui',self)

         self.bt_menu.clicked.connect(self.mover_menu)
         self.base_datos = Comunicacion()
        
         self.bt_restaurar.hide()

         self.bt_refrescar.clicked.connect(self.mostrar_empledos)
         self.bt_agregar.clicked.connect(self.registrar_empledos)
         self.bt_borrar.clicked.connect(self.eliminar_empledos)
         self.bt_actualizar_tabla.clicked.connect(self.modificar_empledos)
         self.bt_actualizar_buscar.clicked.connect(self.buscar_por_nombre_actualiza)
         self.bt_buscar_borrar.clicked.connect(self.buscar_por_nombre_eliminar)
        
         self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
         self.bt_restaurar.clicked.connect(self.control_bt_normal)
         self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
         self.bt_cerrar.clicked.connect(lambda: self.close())
        
         self.setWindowFlag(QtCore.Qt.FramelesWindowHit)
        self.setWindowOpacity(1)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        self.frame_superior.mouseMoveEvent = self.mover_ventana

        self.bt_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_datos))
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        self.bt_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        self.bt_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))

        self.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_empleados.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        def control_bt_minimizar(self):
            self.showMinimized()

        def control_bt_normal(self):
            self.showNormal()
            self.bt_restaurar.hide()
            self.bt_maximizar.show()
            
        def control_bt_maximizar(self):
            self.showMaximized()
            self.bt_maximizar.hide()
            self.bt_restaurar.show()

        def resizeEvent(self, event):
            rect = self.rect()
            self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

       
        def mousePressEvent(self, event):
            self.click_position = event.globalPos()

        def mover_ventana(self, event):
            if self.isMaximized() == False:
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.click_position)
                    self.click_position = event.globalPos()
                    event.accept()
                    if event.globalPos().y()<=10:
                        self.showMaximezed()
                        self.bt_maximizar.hide()
                        self.bt_restaurar.show()

                    else:
                        self.showNormal()
                        self.bt_restaurar.hide()
                        self.bt_maximizar.show()

        def mover_menu(self):
            if True:
                width = self.frame_control.width()
                normal = 0
                if width==0:
                    extender = 200
                else:
                    extender = normal
                    self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
                    self.animacion.setDuration(300)
                    self.animacion.setStartValue(width)
                    self.animacion.setEndValue(extender)
                    self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                    self.animacion.start()

                    
        def mostrar_empleados(self):
            datos = self.base_datos.mostrar_empleados()
            i = len(datos)
            self.tabla_empleados.setRowCount(i)
            tablerow = 0
            for row in datos:
                self.Id = row[0]
                self.table.empleados.setItem(tablerow,0,QWidget.QTableWidgetItem(row[1]))
                self.table.empleados.setItem(tablerow,1,QWidget.QTableWidgetItem(row[2]))
                self.table.empleados.setItem(tablerow,2,QWidget.QTableWidgetItem(row[3]))
                self.table.empleados.setItem(tablerow,3,QWidget.QTableWidgetItem(row[4]))
                self.table.empleados.setItem(tablerow,4,QWidget.QTableWidgetItem(row[5]))
                tablerow +=1
                self.signal_actualizar.setText("")
                self.signal_registrar.setText("")
                self.signal_eliminacion.setText("")

        def registrar_empleados(self):
            numero = self.reg_numero.text().upper()
            nombre = self.reg_nombre.text().upper()
            app = self.reg_app.text().upper()
            apm = self.reg_apm.text().upper()
            unidad = self.reg_unidad.text().upper()
            puesto = self.reg_puesto.text().upper()

            if numero != '' and nombre !='' and app !='' and apm !='' and unidad !='' and puesto !='':
                self.base_datos.insertar_empleado(numero,nombre,app.apm,unidad,puesto)
                self.signal_registrar.setText('Empleados Registrados')
                self.reg_numero.clear()
                self.reg_nombre.clear()
                self.reg_app.clear()
                self.reg_apm.clear()
                self.reg_unidad.clear()
                self.reg_puesto.clear()
            else:



             






