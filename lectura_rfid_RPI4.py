import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pyodbc

lector = SimpleMFRC522()




def conectar_bd():
    # Conectar a la base de datos
        conexion = mysql.connector.connect(
            host='192.168.100.10',
            user='remote',
            password='Briza_3121',
            database='accesos'
        )
    
        return conexion

def registrar_acceso():

    if tipo_usuario == "P":
        cursor=conexion.cursor()
        query = "INSERT INTO accesos.accesos(identificador) VALUES(%s) "
        cursor.execute(query,(identificador))
        conexion.commit()
        cursor.close()

try: 
    conexion = conectar_bd()

    if conexion.is_connected():
        print("Conexion exitosa.")
        while True:
            id=lector.read()
            registro = str(id)
            identificador = registro[1:13]
            cursor=conexion.cursor()
            query = "SELECT * FROM accesos.usuarios WHERE identificador = %s;"
            
            try:
                cursor.execute(query, (identificador,))
                resultado = cursor.fetchone()
                identificador = resultado[0]
                nombre = resultado[1]
                apellido_p = resultado[2]
                apellido_m = resultado[3]
                matricula = resultado[4]
                tipo_usuario = resultado[5]
                contrasena = resultado[6]
                # aquí puedes hacer lo que quieras con las variables obtenidas

                registrar_acceso()

            except Exception as e:
                print("Error", f"No se pudo ejecutar el query: {e}")
            
            conexion.commit()
            cursor.close()
           
            

            
except Error as ex:
    print("Error durante la conexion.", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        GPIO.cleanup()
        print("La conexion ha finalizado")






