import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl 
from forms.form_master import MasterPanel


class App:

    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()

        # Conectar con la base de datos MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Briza_3121",
            database="accesos"
        )

        # Ejecutar una consulta SQL para validar el usuario y contraseña
        mycursor = mydb.cursor()
        sql = "SELECT * FROM accesos.usuarios WHERE matricula = %s AND contraseña = %s AND tipo_usuario = 'A'"
        val = (usu, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")
        


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Sistema de Acceso')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0,height=0)
        utl.centrar_ventana(self.ventana,800,500)

        logo = utl.leer_imagen("Proyecto-Acceso-y-Pase-de-Lista/Interfaz/images/logo.png", (200,200))

        # Frame_logo

        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#EC3F45')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo,bg='#EC3F45')
        label.place(x=0,y=0,relwidth=1,relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        # frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top,text="Inicio de sesión", font=('Times',30), fg="black",bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        # frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        # etiquetas, entrys y boton
        etiqueta_usuario = tk.Label(frame_form_fill, text="Número de cuenta", font=('Times',14), fg="black",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=10)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times',14),width=20)
        self.usuario.pack(fill=None, padx=20,pady=10,anchor="w")

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times',14), fg="black",bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=10)
        self.password = ttk.Entry(frame_form_fill, font=('Times',14),width=20)
        self.password.pack(fill=None, padx=20,pady=10,anchor="w")
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Iniciar sesión", font=('Times', 15), bd=0,bg='red',width=20,command=self.verificar)
        inicio.pack(fill=None, padx=20, pady=20)
        inicio.bind("<Return>",(lambda event: self.verificar()))

    
        self.ventana.mainloop()
