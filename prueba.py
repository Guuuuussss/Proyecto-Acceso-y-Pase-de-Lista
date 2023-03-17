import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "usuario" and password == "contraseña":
        message_label.config(text="Inicio de sesión exitoso!")
    else:
        message_label.config(text="Nombre de usuario o contraseña incorrectos")

root = tk.Tk()
root.title("Inicio de sesión")

# Etiqueta de nombre de usuario
username_label = tk.Label(root, text="Nombre de usuario:")
username_label.pack()

# Cuadro de entrada de nombre de usuario
username_entry = tk.Entry(root)
username_entry.pack()

# Etiqueta de contraseña
password_label = tk.Label(root, text="Contraseña:")
password_label.pack()

# Cuadro de entrada de contraseña
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Botón de inicio de sesión
login_button = tk.Button(root, text="Iniciar sesión", command=login)
login_button.pack()

# Etiqueta de mensaje
message_label = tk.Label(root, text="")
message_label.pack()

root.mainloop()
