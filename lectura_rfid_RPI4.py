import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

lector = SimpleMFRC522()

####Conexion a base de datos 
try: 
    conexion = mysql.connector.connect(
        host='database-1.ccolsljrufdk.us-east-2.rds.amazonaws.com',
        port='3306',
        user='admin',
        password='admin',
        db='rfid_read'
    )

    if conexion.is_connected():
        print("Conexion exitosa.")
        while True:
            id=lector.read()
            #registro = str(data)
            #print(registro)
            #print(len(registro))
            #registro1 = registro[7:18]
            #print(registro1)
            print(id)
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO rfid_data (Member_ID) VALUES (%s)", [(id)])
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

