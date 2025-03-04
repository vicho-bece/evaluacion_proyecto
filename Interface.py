from customtkinter import *

import funcionesInterfaz as fInter


class CustomButton(CTkButton):
    def __init__(self, master, **kwargs):
        default_config = {
            "fg_color": "#000080",
            "hover_color": "#5757ff",
            "cursor": "hand2",
            "font": ("Arial", 11, "bold"),
            "border_width": 0
        }
        default_config.update(kwargs)
        super().__init__(master, **default_config)

class CustomLabel(CTkLabel):
    def __init__(self, master, **kwargs):
        default_config = {
            "fg_color": "#222222",
            "font": ("Arial",13, "bold")
        }
        default_config.update(kwargs)
        super().__init__(master, **default_config)

class CustomFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        default_config = {
            "fg_color": "#222222",
            "bg_color": "#000000",
            "border_width": 0,
            "corner_radius": 20 
        }
        default_config.update(kwargs)
        super().__init__(master, **default_config)

root = CTk()
root.title("Interfaz de Base de Datos PostgreSQL")
root.geometry("400x500")
root.config(background="#000000")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

seccion1 = CustomFrame(master=root)
seccion2 = CustomFrame(master=root)
seccion3 = CustomFrame(master=root)
seccion4 = CustomFrame(master=root)

seccion1.grid(row=0, column=0)
seccion2.grid(row=1, column=0)
seccion3.grid(row=2, column=0)
seccion4.grid(row=3, column=0)

# Sección 1 - Actualizar la Base de Datos
mensaje_1 = "Presiona el boton de Refrescar\npara actualizar la Base de Datos"
CustomLabel(seccion1, text=mensaje_1).pack(pady=(10,0), padx=85)
boton1 = CustomButton(seccion1,
          text="Refrescar",
          command=fInter.respuesta_refrescar)

boton1.pack(pady=10)


# Sección 2 - Insertar una Factura
mensaje_2 = "¿Quieres agregar una factura\nen el Resumen de Acuse?\nPulse Insertar"
CustomLabel(seccion2, text=mensaje_2).pack(pady=(10,0), padx=95)
boton2 = CustomButton(seccion2, 
                   text="Insertar", 
                   command=fInter.ventana_insertar,
)
boton2.pack(pady=10)

# Sección 3 - Eliminar una Factura
mensaje_3 = "Si quieres eliminar una factuar del\nResumen de Acuse, Pulse Eliminar"
CustomLabel(seccion3, text=mensaje_3).pack(pady=(10,0), padx=75)
boton3 = CustomButton(seccion3, 
                   text="Eliminar", 
                   command=fInter.eliminarFila)
boton3.pack(pady=10)


# Sección 4 - Asistencia por Correo
mensaje_4 = "¿Necesitas asistencia?, Presione el boton de Contactar\npara enviar un correo al desarrollador"
CustomLabel(seccion4, text=mensaje_4).pack(pady=(10,0), padx=15)
boton4 = CustomButton(seccion4, 
                  text="Contactar", 
                  command=fInter.ventana_mensaje)
boton4.pack(pady=10)

root.mainloop()