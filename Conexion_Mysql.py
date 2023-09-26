import Conexion_Mysql

class Comunicacion():
    def __init__(self):
        self.conexion= Conexion_Mysql.connect('base_datos.bd')
    
    def inserta_empleado (self, numero_empleado, nombre, ap_paterno, ap_materno, unidad, puesto):
        cursor =self.conexion.cursor
        bd= '''INSERT INTO tabla_empleados SET NUMERO_EMPLEADO = '{}', NOMBRE = '{}', AP_PATERNO = '{}', AP_MATERNO = '{}', UNIDAD = '{}', PUESTO = '{}' WHERE NUMERO_EMPLEADO = '{}' '''.format(numero_empleado, nombre, ap_paterno, ap_materno, unidad, puesto)
        cursor.execute(bd)
        a= cursor.rowcount
        self.conexion.commit()
        cursor.close()

    def mostrar_empleados(self):
        cursor= self.conexion.cursor()
        bd=  "SELECT * FROM tabla_empleados"
        cursor.execute(bd)    
        registro =cursor.fetchall()
        return registro
    
    def busca_empleado(self, numero_empleado):
        cursor = self.conexion.cursor()
        bd= '''SELECT * FROM tabla_empleados WHERE NUMERO_EMPLEADO = {}'''.frmat(numero_empleado)
        cursor.execute(bd)    
        registro =cursor.fetchall()
        cursor.close()
        return registro

    def eliminar_empleados(self, numero_empleado):
        cursor = self.conexion.cursor()
        bd= '''DELETE FROM tabla_empleados WHERE NUMERO_EMPLEADO = {}'''.frmat(numero_empleado)
        self.conexion.commit()
        cursor.close()

    def actualizar_empleados (self, numero_empleado, nombre, ap_paterno, ap_materno, unidad, puesto):
        cursor = self.conexion.cursor()
        bd= '''UPDATE FROM tabla_empleados SET NUMERO_EMPLEADO = '{}', NOMBRE = '{}', AP_PATERNO = '{}', AP_MATERNO = '{}', UNIDAD = '{}', PUESTO = '{}' WHERE NUMERO_EMPLEADO = '{}' '''.format(numero_empleado, nombre, ap_paterno, ap_materno, unidad, puesto)
        cursor.execute(bd)
        a= cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a









