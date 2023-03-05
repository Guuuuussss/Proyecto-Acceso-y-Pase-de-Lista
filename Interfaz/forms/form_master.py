import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
import mysql.connector

class MasterPanel: 
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Master Panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w,h))
        self.ventana.config(bg = '#fcfcfc')
        self.ventana.resizable(width=True, height=True)

        logo = utl.leer_imagen("Proyecto-Acceso-y-Pase-de-Lista/Interfaz/images/logo.png", (200,200))

        label = tk.Label(self.ventana, image=logo,bg='#EC3F45')
        label.place(x=0,y=0,relwidth=1,relheight=1)
        
        # Conectar a la base de datos
        self.conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Briza_3121',
            database='accesos'
        )
        
        # Obtener los registros de la tabla
        cursor = self.conexion.cursor()
        cursor.execute('SELECT * FROM accesos.usuarios LEFT JOIN accesos ON usuarios.identificador = accesos.identificador LEFT JOIN clases ON usuarios.identificador = clases.id_profesor WHERE usuarios.identificador = 374203472;')
        registros = cursor.fetchall()
        
        # Crear la tabla para mostrar los registros
        self.tabla = tk.Frame(self.ventana)
        self.tabla.pack(fill=tk.BOTH, expand=True)
        
        for i, fila in enumerate(registros):
            for j, valor in enumerate(fila):
                celda = tk.Label(self.tabla, text=str(valor))
                celda.grid(row=i, column=j)
        
        self.ventana.mainloop()
