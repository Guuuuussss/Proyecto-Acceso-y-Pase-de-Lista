import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pyodbc

lector = SimpleMFRC522()

####Conexion a base de datos 
try: 
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.100.7,1433;DATABASE=rfid_read;UID=sa;PWD=Briza_3121')

    if conexion.is_connected():
        print("Conexion exitosa.")
        while True:
            id=lector.read()
            registro = str(id)
            registro1 = registro[1:13]
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO rfid_data (Members_ID) VALUES (%s)", [(registro1)])
            conexion.commit()
            cursor.close()
            print("Registro insertado con exito.")
except Error as ex:
    print("Error durante la conexion.", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        GPIO.cleanup()
        print("La conexion ha finalizado")

