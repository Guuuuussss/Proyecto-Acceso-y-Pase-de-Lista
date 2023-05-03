import tkinter as tk
from tkinter import END, ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
import mysql.connector


class MasterPanel:

    def conectar_bd(self):
    # Conectar a la base de datos
        conexion = mysql.connector.connect(
            host='192.168.100.9',
            user='remote',
            password='Briza_3121',
            database='proyecto_accesos'
        )

        return conexion

    def agregar_usuario(self):

        identificador_agregar = self.identificador.get()
        nombre_agregar = self.nombre.get()
        apellido_p_agregar = self.apellido_p.get()
        apellido_m_agregar = self.apellido_m.get()
        matricula_agregar = self.matricula.get()
        tipo_usuario_agregar = self.tipo_usuario.get()
        contrasena_agregar = self.contrasena.get()

        # Verificar si los campos de entrada están vacíos //Faltaria mandar un mensaje de error al escribir en el entry un identificador igual a uno ya existente, porque lanza error.
        if not identificador_agregar or not nombre_agregar or not apellido_p_agregar or not apellido_m_agregar or not matricula_agregar or not tipo_usuario_agregar or not contrasena_agregar:
            messagebox.showerror(
                message="Por favor ingrese la información requerida", title="Error")
            return

        conexion = self.conectar_bd()
        cursor = conexion.cursor()

        query = "INSERT INTO proyecto_accesos.usuarios(identificador,nombre,apellido_p,apellido_m,matricula,tipo_usuario,contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (identificador_agregar, nombre_agregar, apellido_p_agregar,apellido_m_agregar, matricula_agregar, tipo_usuario_agregar, contrasena_agregar))

        if cursor.rowcount > 0:
            mensaje = "Registro agregado con éxito"
        else:
            mensaje = "No se ha podido agregar el registro"
        messagebox.showinfo(title="Agregado de registro", message=mensaje)

        # Limpiar los entrys después de agregar los datos a la base de datos
        self.identificador.delete(0, END)
        self.nombre.delete(0, END)
        self.apellido_p.delete(0, END)
        self.apellido_m.delete(0, END)
        self.matricula.delete(0, END)
        self.tipo_usuario.delete(0, END)
        self.contrasena.delete(0, END)

        conexion.commit()
        cursor.close()
        conexion.close()

        self.eliminar_celdas()

        self.celdas = []
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute(
            'SELECT * FROM proyecto_accesos.usuarios ORDER BY nombre')
        registros = cursor.fetchall()

        for i, fila in enumerate(registros):
            for j, valor in enumerate(fila):
                celda = tk.Label(self.frame_contenido, text=str(
                    valor), font=('Times', 14), fg="black", bg='#fcfcfc')
                celda.grid(row=i, column=j, padx=55, pady=10)
                self.celdas.append(celda)

        conexion.commit()  # si deja de funcionar eliminar esta linea
        cursor.close()
        conexion.close()

    def eliminar_usuario(self):
        identificador_eliminar = self.identificador.get()

        if not identificador_eliminar:
            messagebox.showerror(
                message="Por favor ingrese el identificador que desea eliminar.", title="Error")
            return

        conexion = self.conectar_bd()
        cursor = conexion.cursor()

        query = "DELETE FROM proyecto_accesos.usuarios WHERE identificador = %s"
        cursor.execute(query, (identificador_eliminar,))

        if cursor.rowcount > 0:
            mensaje = "Registro eliminado con éxito"
        else:
            mensaje = "No se ha encontrado ningún registro con el identificador especificado"
        messagebox.showinfo(title="Eliminación de registro", message=mensaje)

        # Limpiar los entrys después de agregar los datos a la base de datos
        self.identificador.delete(0, END)
        self.nombre.delete(0, END)
        self.apellido_p.delete(0, END)
        self.apellido_m.delete(0, END)
        self.matricula.delete(0, END)
        self.tipo_usuario.delete(0, END)
        self.contrasena.delete(0, END)

        conexion.commit()
        cursor.close()
        conexion.close()

        self.eliminar_celdas()

        self.celdas = []
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute(
            'SELECT * FROM proyecto_accesos.usuarios ORDER BY nombre')
        registros = cursor.fetchall()

        for i, fila in enumerate(registros):
            for j, valor in enumerate(fila):
                celda = tk.Label(self.frame_contenido, text=str(
                    valor), font=('Times', 14), fg="black", bg='#fcfcfc')
                celda.grid(row=i, column=j, padx=55, pady=10)
                self.celdas.append(celda)

        conexion.commit()  # si deja de funcionar eliminar esta linea
        cursor.close()
        conexion.close()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Administración de Usuarios')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=True, height=True)

        # frame admin
        frame_admin = tk.Frame(self.ventana, bd=0, width=500,relief=tk.SOLID, padx=10, pady=10, bg='#fa5c5c')
        frame_admin.pack(side="left", expand=tk.NO, fill=tk.Y)

        title = tk.Label(frame_admin, text="Administración de Usuarios", font=(
            'Times', 20), fg="white", bg='#fa5c5c', pady=20, padx=120)
        title.pack(side="top", expand=tk.YES, fill=tk.X, anchor="n")

        # etiquetas, entrys en el form admin

        # identificador
        etiqueta_identificador = tk.Label(frame_admin, text="Identificador:", font=(
            'Times', 14), fg="white", bg='#fa5c5c', anchor="w")
        etiqueta_identificador.pack(fill=tk.X, padx=20, pady=10)
        self.identificador = ttk.Entry(
            frame_admin, font=('Times', 14), width=20)
        self.identificador.pack(fill=None, padx=20, pady=10, anchor="w")

        # nombre
        etiqueta_nombre = tk.Label(frame_admin, text="Nombre:", font=(
            'Times', 14), fg="white", bg='#fa5c5c', anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20, pady=10)
        self.nombre = ttk.Entry(frame_admin, font=('Times', 14), width=20)
        self.nombre.pack(fill=None, padx=20, pady=10, anchor="w")

        # apellido_p
        etiqueta_apellido_p = tk.Label(frame_admin, text="Apellido Paterno:", font=(
            'Times', 14), fg="white", bg='#fa5c5c', anchor="w")
        etiqueta_apellido_p.pack(fill=tk.X, padx=20, pady=10)
        self.apellido_p = ttk.Entry(frame_admin, font=('Times', 14), width=20)
        self.apellido_p.pack(fill=None, padx=20, pady=10, anchor="w")

        # apellido_m
        etiqueta_apellido_m = tk.Label(frame_admin, text="Apellido Materno:", font=(
            'Times', 14), fg="white", bg='#fa5c5c', anchor="w")
        etiqueta_apellido_m.pack(fill=tk.X, padx=20, pady=10)
        self.apellido_m = ttk.Entry(frame_admin, font=('Times', 14), width=20)
        self.apellido_m.pack(fill=None, padx=20, pady=10, anchor="w")

        # matricula o numero de cuenta
        etiqueta_matricula = tk.Label(frame_admin, text="Número de cuenta:", font=(
            'Times', 14), fg="white", bg='#fa5c5c', anchor="w")
        etiqueta_matricula.pack(fill=tk.X, padx=20, pady=10)
        self.matricula = ttk.Entry(frame_admin, font=('Times', 14), width=20)
        self.matricula.pack(fill=None, padx=20, pady=10, anchor="w")

        # tipo_usuario
        etiqueta_tipo_usuario = tk.Label(frame_admin, text="Tipo de Usuario:", font=(
            'Times', 14), fg="white", bg='#fa5c5c', anchor="w")
        etiqueta_tipo_usuario.pack(fill=tk.X, padx=20, pady=10)
        self.tipo_usuario = ttk.Entry(
            frame_admin, font=('Times', 14), width=20)
        self.tipo_usuario.pack(fill=None, padx=20, pady=10, anchor="w")

        # contraseña
        etiqueta_contrasena = tk.Label(frame_admin, text="Contraseña:", font=(
            'Times', 14), fg="white", bg='#fa5c5c', anchor="w")
        etiqueta_contrasena.pack(fill=tk.X, padx=20, pady=10)
        self.contrasena = ttk.Entry(frame_admin, font=('Times', 14), width=20)
        self.contrasena.pack(fill=None, padx=20, pady=10, anchor="w")

        # boton Agregar
        agregar = tk.Button(frame_admin, text="Agregar", font=(
            'Times', 15), bd=0, bg='#fcfcfc', width=15, command=self.agregar_usuario)
        agregar.pack(side=tk.LEFT, fill=None, padx=15, pady=100)
        agregar.bind("<Return>", (lambda event: self.agregar_usuario()))

        # boton eliminar
        eliminar = tk.Button(frame_admin, text="Eliminar", font=(
            'Times', 15), bd=0, bg='#fcfcfc', width=15, command=self.eliminar_usuario)
        eliminar.pack(side=tk.RIGHT, fill=None, padx=15, pady=100)

        # frame_tabla
        frame_tabla = tk.Frame(
            self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_tabla.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        # frame_tabla_top
        frame_tabla_top = tk.Frame(
            frame_tabla, height=50, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_tabla_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_tabla_top, text="Registros", font=(
            'Times', 25), fg="black", bg='#fcfcfc', pady=20)
        title.grid(row=0, column=3, padx=20, pady=5)

        # frame_tabla_buttom
        frame_tabla_buttom = tk.Frame(
            frame_tabla, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_tabla_buttom.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        # Crear la tabla para mostrar los registros
        self.tabla_db = tk.Frame(frame_tabla_buttom, bg='#fcfcfc')
        self.tabla_db.pack(fill=tk.BOTH, expand=tk.YES)

        # Crear un canvas para permitir el desplazamiento de los registros de la tabla
        self.canvas_tabla = tk.Canvas(self.tabla_db, bg="#FFFFFF")
        self.canvas_tabla.pack(side="left", fill="both", expand=True)

        # Crear un scrollbar vertical para el canvas
        self.scrollbar_tabla = tk.Scrollbar(
            self.tabla_db, orient="vertical", command=self.canvas_tabla.yview)
        self.scrollbar_tabla.pack(side="right", fill="y")

        # Configurar el canvas para vincularlo al scrollbar
        self.canvas_tabla.configure(yscrollcommand=self.scrollbar_tabla.set)
        self.canvas_tabla.bind("<Configure>", lambda e: self.canvas_tabla.configure(
            scrollregion=self.canvas_tabla.bbox("all")))

        # Crear un frame dentro del canvas para contener los labels de la tabla
        self.frame_contenido = tk.Frame(self.canvas_tabla, bg="#FFFFFF")
        self.canvas_tabla.create_window(
            (0, 0), window=self.frame_contenido, anchor="nw")

        ### HEADER TABLA ###

        # Crear etiquetas para la cabecera de la tabla
        cabecera_identificador = tk.Label(frame_tabla_top, text="Identificador", font=(
            'Times', 14, 'bold'), fg="black", bg='#fcfcfc')
        cabecera_nombre = tk.Label(frame_tabla_top, text="Nombre", font=(
            'Times', 14, 'bold'), fg="black", bg='#fcfcfc')
        cabecera_apellido_p = tk.Label(frame_tabla_top, text="Apellido Paterno", font=(
            'Times', 14, 'bold'), fg="black", bg='#fcfcfc')
        cabecera_apellido_m = tk.Label(frame_tabla_top, text="Apellido Materno", font=(
            'Times', 14, 'bold'), fg="black", bg='#fcfcfc')
        cabecera_matricula = tk.Label(frame_tabla_top, text="Número de Cuenta", font=(
            'Times', 14, 'bold'), fg="black", bg='#fcfcfc')
        cabecera_tipo_usuario = tk.Label(frame_tabla_top, text="Tipo de usuario", font=(
            'Times', 14, 'bold'), fg="black", bg='#fcfcfc')
        cabecera_contrasena = tk.Label(frame_tabla_top, text="Contraseña", font=(
            'Times', 14, 'bold'), fg="black", bg='#fcfcfc')

        cabecera_identificador.grid(row=1, column=0, padx=55, pady=5,)
        cabecera_nombre.grid(row=1, column=1, padx=55, pady=5)
        cabecera_apellido_p.grid(row=1, column=2, padx=30, pady=5)
        cabecera_apellido_m.grid(row=1, column=3, padx=0, pady=5)
        cabecera_matricula.grid(row=1, column=4, padx=5, pady=5)
        cabecera_tipo_usuario.grid(row=1, column=5, padx=0, pady=5)
        cabecera_contrasena.grid(row=1, column=6, padx=45, pady=5)

        # Obtener los registros de la tabla
        self.celdas = []
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute(
            'SELECT * FROM proyecto_accesos.usuarios ORDER BY nombre')
        registros = cursor.fetchall()

        for i, fila in enumerate(registros):
            for j, valor in enumerate(fila):
                celda = tk.Label(self.frame_contenido, text=str(
                    valor), font=('Times', 14), fg="black", bg='#fcfcfc')
                celda.grid(row=i+1, column=j, padx=55, pady=10)
                self.celdas.append(celda)

        cursor.close()
        conexion.close()

        self.ventana.mainloop()

    # Crear una función para eliminar las celdas
    def eliminar_celdas(self):
        for celda in self.celdas:
            celda.destroy()




        

