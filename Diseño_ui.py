# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Joselo\Desktop\Barras\Lector\Diseño.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 706)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: rgb(242, 233, 216);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_Superior = QtWidgets.QFrame(self.frame)
        self.frame_Superior.setEnabled(True)
        self.frame_Superior.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_Superior.setStyleSheet("QFrame{\n"
"\n"
"    background-color: rgb(218, 198, 161);\n"
"        }\n"
"\n"
"QPushButton{\n"
"\n"
"background-color:#000000ff;\n"
" border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #118C4B;\n"
" border-radius: 20px;\n"
"}")
        self.frame_Superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Superior.setObjectName("frame_Superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_Superior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Menu = QtWidgets.QPushButton(self.frame_Superior)
        self.Menu.setEnabled(True)
        self.Menu.setMinimumSize(QtCore.QSize(40, 40))
        self.Menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Joselo\\Desktop\\Barras\\Lector\\Iconos/icons8-menú-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Menu.setIcon(icon)
        self.Menu.setIconSize(QtCore.QSize(41, 38))
        self.Menu.setObjectName("Menu")
        self.horizontalLayout.addWidget(self.Menu)
        spacerItem1 = QtWidgets.QSpacerItem(790, 27, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Minimizar = QtWidgets.QPushButton(self.frame_Superior)
        self.Minimizar.setEnabled(True)
        self.Minimizar.setMinimumSize(QtCore.QSize(40, 40))
        self.Minimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Joselo\\Desktop\\Barras\\Lector\\Iconos/icons8-línea-horizontal-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minimizar.setIcon(icon1)
        self.Minimizar.setIconSize(QtCore.QSize(41, 50))
        self.Minimizar.setObjectName("Minimizar")
        self.horizontalLayout.addWidget(self.Minimizar)
        self.Expandir = QtWidgets.QPushButton(self.frame_Superior)
        self.Expandir.setEnabled(True)
        self.Expandir.setMinimumSize(QtCore.QSize(40, 40))
        self.Expandir.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Joselo\\Desktop\\Barras\\Lector\\Iconos/icons8-cambiar-tamaño-cuatro-direcciones-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Expandir.setIcon(icon2)
        self.Expandir.setIconSize(QtCore.QSize(44, 44))
        self.Expandir.setObjectName("Expandir")
        self.horizontalLayout.addWidget(self.Expandir)
        self.Cerrar = QtWidgets.QPushButton(self.frame_Superior)
        self.Cerrar.setEnabled(True)
        self.Cerrar.setMinimumSize(QtCore.QSize(40, 40))
        self.Cerrar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Joselo\\Desktop\\Barras\\Lector\\Iconos/icons8-eliminar-100-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cerrar.setIcon(icon3)
        self.Cerrar.setIconSize(QtCore.QSize(38, 38))
        self.Cerrar.setObjectName("Cerrar")
        self.horizontalLayout.addWidget(self.Cerrar)
        self.verticalLayout_2.addWidget(self.frame_Superior)
        self.frame_Contenido = QtWidgets.QFrame(self.frame)
        self.frame_Contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Contenido.setObjectName("frame_Contenido")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_Contenido)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Desp = QtWidgets.QFrame(self.frame_Contenido)
        self.Desp.setMinimumSize(QtCore.QSize(300, 0))
        self.Desp.setMaximumSize(QtCore.QSize(0, 16777215))
        self.Desp.setStyleSheet("    QFrame{\n"
"background-color: rgb(34, 92, 80);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(61, 61, 61);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    font: 77 10pt \"Arial Black\";\n"
"}\n"
"")
        self.Desp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Desp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Desp.setObjectName("Desp")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Desp)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Buscar = QtWidgets.QPushButton(self.Desp)
        self.Buscar.setMinimumSize(QtCore.QSize(40, 40))
        self.Buscar.setObjectName("Buscar")
        self.verticalLayout_3.addWidget(self.Buscar)
        self.Registrar = QtWidgets.QPushButton(self.Desp)
        self.Registrar.setMinimumSize(QtCore.QSize(40, 40))
        self.Registrar.setObjectName("Registrar")
        self.verticalLayout_3.addWidget(self.Registrar)
        self.Actualizar = QtWidgets.QPushButton(self.Desp)
        self.Actualizar.setMinimumSize(QtCore.QSize(40, 40))
        self.Actualizar.setObjectName("Actualizar")
        self.verticalLayout_3.addWidget(self.Actualizar)
        self.Eliminar = QtWidgets.QPushButton(self.Desp)
        self.Eliminar.setMinimumSize(QtCore.QSize(40, 40))
        self.Eliminar.setObjectName("Eliminar")
        self.verticalLayout_3.addWidget(self.Eliminar)
        self.Ajustes = QtWidgets.QPushButton(self.Desp)
        self.Ajustes.setMinimumSize(QtCore.QSize(40, 40))
        self.Ajustes.setObjectName("Ajustes")
        self.verticalLayout_3.addWidget(self.Ajustes)
        self.horizontalLayout_2.addWidget(self.Desp)
        self.Paginas = QtWidgets.QFrame(self.frame_Contenido)
        self.Paginas.setMinimumSize(QtCore.QSize(0, 40))
        self.Paginas.setStyleSheet("QFrame {\n"
"    background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 87 16pt \"Arial Black\";\n"
"    background-color: #000000ff;\n"
"    color: rgb(34, 92, 80);\n"
"    border: 0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px;\n"
"    border-bottom: 2px solid rgb(61, 61, 61);\n"
"    font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(61, 61, 61);\n"
"    font: 77 10pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 77 10pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"  gridline-color: rgb(0,206,151);  \n"
"   font-size: 12pt;\n"
"    color: #000000;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(34, 92, 80);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(34, 92, 80);\n"
"}")
        self.Paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Paginas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Paginas.setObjectName("Paginas")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Paginas)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Paginas)
        self.stackedWidget.setMinimumSize(QtCore.QSize(100, 30))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Page_Error = QtWidgets.QWidget()
        self.Page_Error.setObjectName("Page_Error")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Page_Error)
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget.addWidget(self.Page_Error)
        self.page_Buscar = QtWidgets.QWidget()
        self.page_Buscar.setObjectName("page_Buscar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_Buscar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.page_Buscar)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.TablEmpleados = QtWidgets.QTableWidget(self.page_Buscar)
        self.TablEmpleados.setObjectName("TablEmpleados")
        self.TablEmpleados.setColumnCount(4)
        self.TablEmpleados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablEmpleados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablEmpleados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablEmpleados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablEmpleados.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.TablEmpleados)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(378, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.ButtoActualizar = QtWidgets.QPushButton(self.page_Buscar)
        self.ButtoActualizar.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        self.ButtoActualizar.setFont(font)
        self.ButtoActualizar.setObjectName("ButtoActualizar")
        self.horizontalLayout_4.addWidget(self.ButtoActualizar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.page_Buscar)
        self.Page_Registrar = QtWidgets.QWidget()
        self.Page_Registrar.setObjectName("Page_Registrar")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Page_Registrar)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.Page_Registrar)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 105, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(40)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.Page_Registrar)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.Page_Registrar)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.Page_Registrar)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.Page_Registrar)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(10, -1, 30, 0)
        self.verticalLayout_7.setSpacing(40)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit = QtWidgets.QLineEdit(self.Page_Registrar)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_7.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Page_Registrar)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_7.addWidget(self.lineEdit_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Page_Registrar)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_7.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.Page_Registrar)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_7.addWidget(self.lineEdit_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 105, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.Page_Registrar)
        self.label_8.setMinimumSize(QtCore.QSize(200, 40))
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        spacerItem5 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.Page_Registrar)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.Page_Registrar)
        self.Page_Actualizar = QtWidgets.QWidget()
        self.Page_Actualizar.setObjectName("Page_Actualizar")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Page_Actualizar)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.Page_Actualizar)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 31))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.label_9)
        spacerItem6 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.Page_Actualizar)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.Page_Actualizar)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.Page_Actualizar)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        spacerItem7 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(30)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.Page_Actualizar)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.Page_Actualizar)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.label_13 = QtWidgets.QLabel(self.Page_Actualizar)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.Page_Actualizar)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(10, 0, 30, 0)
        self.verticalLayout_11.setSpacing(40)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.Page_Actualizar)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_11.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.Page_Actualizar)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_11.addWidget(self.lineEdit_8)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.Page_Actualizar)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_11.addWidget(self.lineEdit_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.Page_Actualizar)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_11.addWidget(self.lineEdit_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.Page_Actualizar)
        self.label_16.setMinimumSize(QtCore.QSize(200, 30))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.pushButton_2 = QtWidgets.QPushButton(self.Page_Actualizar)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.stackedWidget.addWidget(self.Page_Actualizar)
        self.Page_Eliminar = QtWidgets.QWidget()
        self.Page_Eliminar.setObjectName("Page_Eliminar")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Page_Eliminar)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.Page_Eliminar)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_13.addWidget(self.label_17)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_18 = QtWidgets.QLabel(self.Page_Eliminar)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_10.addWidget(self.label_18)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.Page_Eliminar)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_10.addWidget(self.lineEdit_12)
        self.pushButton_4 = QtWidgets.QPushButton(self.Page_Eliminar)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_10.addWidget(self.pushButton_4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.tableWidget = QtWidgets.QTableWidget(self.Page_Eliminar)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_13.addWidget(self.tableWidget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_19 = QtWidgets.QLabel(self.Page_Eliminar)
        self.label_19.setMinimumSize(QtCore.QSize(200, 30))
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_9.addWidget(self.label_19)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.pushButton_5 = QtWidgets.QPushButton(self.Page_Eliminar)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_9.addWidget(self.pushButton_5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.stackedWidget.addWidget(self.Page_Eliminar)
        self.Page_Ajustes = QtWidgets.QWidget()
        self.Page_Ajustes.setObjectName("Page_Ajustes")
        self.stackedWidget.addWidget(self.Page_Ajustes)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.Paginas)
        self.verticalLayout_2.addWidget(self.frame_Contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 12)
        self.verticalLayout_8.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Buscar.setText(_translate("MainWindow", "Buscar"))
        self.Registrar.setText(_translate("MainWindow", "Registrar"))
        self.Actualizar.setText(_translate("MainWindow", "Actualizar"))
        self.Eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.Ajustes.setText(_translate("MainWindow", "Ajustes"))
        self.label.setText(_translate("MainWindow", "Empleados"))
        item = self.TablEmpleados.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Numero de empleado"))
        item = self.TablEmpleados.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.TablEmpleados.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Unidad"))
        item = self.TablEmpleados.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Puesto"))
        self.ButtoActualizar.setText(_translate("MainWindow", "Actualizar"))
        self.label_7.setText(_translate("MainWindow", "Registrar Empleados"))
        self.label_2.setText(_translate("MainWindow", "Numero Empleado"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.label_5.setText(_translate("MainWindow", "Unidad"))
        self.label_6.setText(_translate("MainWindow", "Puesto"))
        self.pushButton.setText(_translate("MainWindow", "Registrar"))
        self.label_9.setText(_translate("MainWindow", "Actualizar"))
        self.label_15.setText(_translate("MainWindow", "Numero Empleado"))
        self.pushButton_3.setText(_translate("MainWindow", "Buscar"))
        self.label_10.setText(_translate("MainWindow", "Numero empleado"))
        self.label_11.setText(_translate("MainWindow", "Nombre"))
        self.label_13.setText(_translate("MainWindow", "Unidad"))
        self.label_14.setText(_translate("MainWindow", "Puesto"))
        self.pushButton_2.setText(_translate("MainWindow", "Actualizar"))
        self.label_17.setText(_translate("MainWindow", "Eliminar Empleados"))
        self.label_18.setText(_translate("MainWindow", "Numero Empleado"))
        self.pushButton_4.setText(_translate("MainWindow", "Buscar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Numero de empleado"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Unidad"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Puesto"))
        self.pushButton_5.setText(_translate("MainWindow", "Eliminar"))
