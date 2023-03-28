from PIL import ImageTk, Image

def leer_imagen (path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

'''def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho/2)-(aplicacion_ancho/2))
    y = int((pantalla_largo/2)-(aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")'''

def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    # Obtener las dimensiones de la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    
    # Calcular las proporciones de la ventana
    proporcion_ancho = aplicacion_ancho / pantalla_ancho
    proporcion_largo = aplicacion_largo / pantalla_largo
    
    # Ajustar las proporciones de la ventana según el tamaño de la pantalla
    if proporcion_ancho > 1:
        aplicacion_ancho = int(pantalla_ancho * 0.9)
    if proporcion_largo > 1:
        aplicacion_largo = int(pantalla_largo * 0.9)
    
    # Calcular la posición central de la ventana
    x = int((pantalla_ancho / 2) - (aplicacion_ancho / 2))
    y = int((pantalla_largo / 2) - (aplicacion_largo / 2))
    
    # Configurar la geometría de la ventana
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")

