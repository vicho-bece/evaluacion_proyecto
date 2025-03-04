# Bibliotecas para crear las Interfaces
from customtkinter import *
import CTkMessagebox
# Importa las funciones del siguiente Python
import read_csv

# ----------------------------------------------------------
# SECCION DE CLASES DE COMPONENTES Y CONFIGURACION DE ESTILO
# ----------------------------------------------------------

# 1 - CLASE DE BUTTON
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

# 2 - CLASE DE TEXT
class CustomText(CTkTextbox):
    def __init__(self, master, **kwargs):
        default_config = {
            "fg_color": "#000000",
            "width": 300,
            "height": 100
        }
        default_config.update(kwargs)
        super().__init__(master, **default_config)


# 3 - CLASE DE LABEL
class CustomLabel(CTkLabel):
    def __init__(self, master, **kwargs):
        default_config = {
            "fg_color": "#222222",
            "font": ("Arial",13, "bold")
        }
        default_config.update(kwargs)
        super().__init__(master, **default_config)

# 4 - CLASE DE ENTRY
class CustomEntry(CTkEntry):
    def __init__(self, master, **kwargs):
        default_config = {
            "fg_color": "#000000",
            "width": 100
        }
        default_config.update(kwargs)
        super().__init__(master, **default_config)

# 5 - CLASE DE FRAME
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




# --------------------
# SECCION DE FUNCIONES
# --------------------

# 1 - ACTUALIZACION, MUESTRA EL RESULTADO SEGUN LA FUNCION QUE SE LLAMA
def respuesta_refrescar():
    CTkMessagebox.CTkMessagebox(title = "Resultado", message = read_csv.actualiza())

# 2 - LAS SIGUIENTES 2 FUNCIONES, REVISA QUE LOS CAMPOS OBLIGATORIOS TENGAN DATOS DE ENTRADA PARA LUEGO VALIDAR SU CONTENIDO Y FORMATO

def validacion(recu, constr, tipo_dcto, cc, rut, dcto, fecha, exento, neto, iva, ceec, otros, files, nota, centro, cta, obs):

    warn = ""

    if len(constr) < 1: warn += "Tiene que seleccionar una constructora\n"
    if len(dcto) == 0: warn += "Indique el número de documento\n"
    
    if len(rut) == 0: warn += "Tiene que colocar el rut\n"
    if len(fecha) == 0: warn += "Indique la fecha y/o siga el formato dd-mm-yyyy\n"
    if len(iva) == 0: warn += "Indique el valor IVA"

    if len(centro) < 1 : warn += "Indique el Centro de Costo"
    if len(cta) == 0 : warn += "Indique la Cuenta Contable"


    if len(warn) > 10:
        CTkMessagebox.CTkMessagebox("Error", icon="cancel", message=warn)
    else:
        CTkMessagebox.CTkMessagebox("Informacion", message=read_csv.insertarFila( recu, constr,  tipo_dcto, cc,  rut,  dcto, fecha, exento, neto, iva, ceec, otros, files, nota, centro, cta, obs))

def hayTexto(constr, dcto, rut, total, edificio):
    warn = ""

    if len(constr) < 1: warn += "Tiene que seleccionar una constructora\n"
    if len(dcto) == 0: warn += "Indique el número de documento\n"
    if len(rut) == 0: warn += "Tiene que colocar el rut\n"
    if len(total) == 0: warn += "Tiene que colocar monto total\n"
    if len(edificio) < 1: warn += "Tiene que seleccionar el centro de costo\n"

    if len(warn) > 1:
        CTkMessagebox.CTkMessagebox("Error", icon="cancel", message=warn)
    else:
        CTkMessagebox.CTkMessagebox("Informacion", message=read_csv.eliminarFila(constr, dcto, rut, total, edificio))

# 3 - REVISA QUE EXISTA DATOS DE ENTRADA 
def contacto(asunto, msg):

    if len(asunto) > 0:
        if len(msg) > 0:
            CTkMessagebox.CTkMessagebox(title = "Resultado", message = read_csv.correoAsistencia(asunto, msg))
        else:
            CTkMessagebox.CTkMessagebox(title = "Advertencia", icon="cancel", message = "Necesitamos que describas los detalles para enviar el correo")
    else:
        CTkMessagebox.CTkMessagebox(title = "Advertencia", icon="cancel", message = "Necesitamos que indiques el encabezado")


# ------------------------------------
# SECCION DE VENTANAS SEGUN SU FUNCION
# ------------------------------------

# 1 - INSERTAR FACTURA

def ventana_insertar():
    insertar = CTkToplevel()
    insertar.title("Insertar una fila")
    insertar.geometry("1000x600")
    insertar.config(background="#000000")

    insertar.grid_rowconfigure(0, weight=1)
    insertar.grid_rowconfigure(1, weight=1)
    insertar.grid_rowconfigure(2, weight=1)
    insertar.grid_rowconfigure(3, weight=1)
    insertar.grid_rowconfigure(4, weight=1)
    insertar.grid_columnconfigure(0, weight=1)

    seccion1 = CustomFrame(insertar, fg_color="#000000", bg_color= "#000000")
    seccion2 = CustomFrame(insertar, width = 775, height = 225)
    seccion3 = CustomFrame(insertar, width = 775, height = 225)
    seccion4 = CustomFrame(insertar, fg_color="#000000", bg_color= "#000000")
    seccion5 = CustomFrame(insertar, fg_color="#000000", bg_color= "#000000")

    seccion1.grid(row=0, column=0)
    seccion2.grid(row=1, column=0)
    seccion3.grid(row=2, column=0)
    seccion4.grid(row=3, column=0)
    seccion5.grid(row=4, column=0)

    insert_msg = "Aqui puedes agregar una factura en el Resumen de Acuse. Complete los campos de la seccion OBLIGATORIOS y pulse Insertar.\nEn la seccion de ADICIONALES es opcional completar los campos."
    info_insert = CustomLabel(seccion1, text=insert_msg, fg_color="#000000")
    info_insert.pack()

    mandatory = "SECCION OBLIGATORIOS"
    obligatorio = CustomLabel(seccion2, text=mandatory).place(x=10,y=5)

    constructora = CustomLabel(seccion2, text="Constructora").place(x=10,y=40)
    campo_constructora = CTkComboBox(
        seccion2, 
        values=["CONSTRUCTORA DIEZ SPA", "CONSTRUCTORA VYV LIMITADA", "Constructora e Inmobiliaria VYV"],
        width=250
    )
    campo_constructora.place(x=10, y=65)

    rut_proveedor = CustomLabel(seccion2, text="Rut Proveedor (ej: 12354678-9)").place(x=300,y=40)
    campo_rut_proveedor = CustomEntry(seccion2)
    campo_rut_proveedor.place(x=300, y=65)

    folio = CustomLabel(seccion2, text="Folio").place(x=550,y=40)
    campo_folio = CustomEntry(seccion2)
    campo_folio.place(x=550, y=65)

    centro_costo = CustomLabel(seccion2, text="Centro Costo").place(x=10,y=100)
    campo_centro_costo = CTkComboBox(
        seccion2, 
        values=["DISTRITO CAVANCHA 1", "DISTRITO CAVANCHA 2", "EDIFICIO MUELLE", "EDIFICIO BRAVA"],
        width=250
    )
    campo_centro_costo.place(x=10, y=125)

    cta = CustomLabel(seccion2, text="Cuenta contable (ej: 1.1.1)").place(x=300,y=100)
    campo_cta = CustomEntry(seccion2)
    campo_cta.place(x=300, y=125)

    fecha = CustomLabel(seccion2, text="Fecha Documento (ej: 21-02-2025)").place(x=550,y=100)
    campo_fecha = CustomEntry(seccion2)
    campo_fecha.place(x=550, y=125)

    exento = CustomLabel(seccion2, text="Exento").place(x=10,y=160)
    campo_exento = CustomEntry(seccion2)
    campo_exento.place(x=10, y=185)

    neto = CustomLabel(seccion2, text="Neto").place(x=175,y=160)
    campo_neto = CustomEntry(seccion2)
    campo_neto.place(x=175, y=185)

    iva = CustomLabel(seccion2, text="IVA").place(x=350,y=160)
    campo_iva = CustomEntry(seccion2)
    campo_iva.place(x=350, y=185)

    otros = CustomLabel(seccion2, text="Otros").place(x=550,y=160)
    campo_otros = CustomEntry(seccion2)
    campo_otros.place(x=550, y=185)


    op = "SECCION ADICIONALES"
    opcional = CustomLabel(seccion3, text=op).place(x=10,y=5)


    recuperable = CustomLabel(seccion3, text="IVA Recuperable").place(x=10,y=40)
    campo_recuperable = CTkComboBox(
        seccion3, 
        values=["SI", "NO"],
        width=75
    )
    campo_recuperable.place(x=10,y=65)

    tipo_dcto = CustomLabel(seccion3, text="Tipo de Documento").place(x=300,y=40)
    campo_tipo_dcto = CTkComboBox(
        seccion3, 
        values=["FACTURA EXENTA", "FACTURA AFECTA", "NOTA DE CREDITO"],
        width=150
    )
    campo_tipo_dcto.place(x=300, y=65)

    cc = CustomLabel(seccion3, text="CC").place(x=550,y=40)
    campo_cc = CustomEntry(seccion3)
    campo_cc.place(x=550, y=65)

    archivos = CustomLabel(seccion3, text="Archivos Anteriores").place(x=10,y=100)
    campo_archivos = CTkComboBox(
        seccion3, 
        values=["SI", "NO"],
        width=75
    )
    campo_archivos.place(x=10,y=125)

    notas = CustomLabel(seccion3, text="Notas").place(x=300,y=100)
    campo_notas = CustomEntry(seccion3)
    campo_notas.place(x=300, y=125)

    ceec = CustomLabel(seccion3, text="CEEC").place(x=550,y=100)
    campo_ceec = CustomEntry(seccion3)
    campo_ceec.place(x=550, y=125)


    obs = CustomLabel(seccion3, text="Observaciones").place(x=10,y=160)
    campo_obs = CustomEntry(seccion3, width=700, height=30)
    campo_obs.place(x=10, y=185)


    info_adicional = "INFORMACION\nSi ud. dejo en blanco en los campos de Exento, Neto y/u Otros, favor de completarlos con ceros (0)\nLa factura que ud. va a ingresar, se guardara en el Excel ACUSES INGRESADOS en la carpeta donde ud. deposito los Excel de Acuse"
    label_adicional = CustomLabel(seccion4, text=info_adicional, fg_color="#000000").pack()

    boton_cerrar = CustomButton(seccion5, text="Volver al Menú Principal", cursor="hand2", command=insertar.destroy)
    boton_cerrar.pack(padx = 30, side="left")

    boton_INSERT = CustomButton(
        seccion5, 
        text="Insertar", cursor="hand2", 
        command=lambda: validacion(
             campo_recuperable.get(), campo_constructora.get(),
             campo_tipo_dcto.get(), campo_cc.get(), 
            campo_rut_proveedor.get(),  campo_folio.get(), campo_fecha.get(), campo_exento.get(),
            campo_neto.get(), campo_iva.get(), campo_ceec.get(), campo_otros.get(), campo_archivos.get(),
            campo_notas.get(),  campo_centro_costo.get(), campo_cta.get(),
             campo_obs.get()
        )
    )

    boton_INSERT.pack(padx = 40, side="right")

    insertar.mainloop()

# 2 - ELIMINAR FACTURA

def eliminarFila():
    eliminar = CTkToplevel()
    eliminar.title("Eliminar una fila")
    eliminar.geometry("450x600")
    eliminar.config(background="#000000")

    eliminar.grid_rowconfigure(0, weight=1)
    eliminar.grid_rowconfigure(1, weight=1)
    eliminar.grid_rowconfigure(2, weight=1)
    eliminar.grid_rowconfigure(3, weight=1)
    eliminar.grid_columnconfigure(0, weight=1)

    seccion1 = CustomFrame(eliminar, fg_color="#000000", bg_color= "#000000")
    seccion2 = CustomFrame(eliminar)
    seccion3 = CustomFrame(eliminar, fg_color="#000000", bg_color= "#000000")
    seccion4 = CustomFrame(eliminar, fg_color="#000000", bg_color= "#000000")

    seccion1.grid(row=0, column=0)
    seccion2.grid(row=1, column=0)
    seccion3.grid(row=2, column=0)
    seccion4.grid(row=3, column=0)

    eliminar_msg = "Te encuentras en esta ventana para ELIMINAR\nuna factura del Resumen de Acuse que se encuentra en\nla Base de Datos y del Excel de origen.\n\nComplete todos los campos y pulse Eliminar"
    info_delete = CustomLabel(seccion1, text=eliminar_msg, fg_color="#000000").pack()

    info_tabla = CustomLabel(seccion2, text="Constructora").pack() 
    constructora = CTkComboBox(
        seccion2, 
        values=["CONSTRUCTORA DIEZ SPA", "CONSTRUCTORA VYV LIMITADA", "Constructora e Inmobiliaria VYV"],
        width=250
    )
    constructora.pack() 

    documento = CustomLabel(seccion2, text="Número Documento").pack() 
    campo_documento = CustomEntry(seccion2)
    campo_documento.pack() 

    rut = CustomLabel(seccion2, text="Rut Proveedor (ej: 12345678-9)").pack() 
    campo_rut = CustomEntry(seccion2)
    campo_rut.pack() 

    total = CustomLabel(seccion2, text="Monto total (no utilizar puntos)").pack() 
    campo_total = CustomEntry(seccion2)
    campo_total.pack() 

    info_centro = CustomLabel(seccion2, text="Centro de Costo").pack() 
    centro_cost = CTkComboBox(
        seccion2, 
        values=["DISTRITO CAVANCHA 1", "DISTRITO CAVANCHA 2", "EDIFICIO MUELLE", "EDIFICIO BRAVA"],
        width=250
    )
    centro_cost.pack(pady=(0,10), padx=50)  

    info_adicional = "INFORMACION\nQueremos insistir de que ud. esta en la ventana\npara ELIMINAR una factura de la Base de datos\ny del Excel de origen\n Dicha factura no se podra recuperar."
    label_adicional = CustomLabel(seccion3, text=info_adicional, fg_color="#000000").pack()

    boton_cerrar = CustomButton(seccion4, text="Volver al Menú Principal", command=eliminar.destroy)
    boton_cerrar.pack(padx = 30, side="left")

    boton_DELETE = CustomButton(
        seccion4, 
        text="Eliminar",
        command=lambda: hayTexto(
            constructora.get(),
            campo_documento.get(),
            campo_rut.get(),
            campo_total.get(),
            centro_cost.get()
        )
    )

    boton_DELETE.pack(padx = 40, side="right")

    eliminar.mainloop()

# 3 - ENVIAR CORREO AL DESARROLLADOR

def ventana_mensaje():
    mensaje = CTkToplevel()
    mensaje.title("Enviar un correo")
    mensaje.geometry("400x400")
    mensaje.config(background="#000000")

    mensaje.grid_rowconfigure(0, weight=1)
    mensaje.grid_rowconfigure(1, weight=1)
    mensaje.grid_rowconfigure(2, weight=1)
    mensaje.grid_columnconfigure(0, weight=1)

    seccion1 = CustomFrame(mensaje, fg_color="#000000", bg_color= "#000000")
    seccion2 = CustomFrame(mensaje)
    seccion3 = CustomFrame(mensaje, fg_color="#000000", bg_color= "#000000")

    seccion1.grid(row=0, column=0)
    seccion2.grid(row=1, column=0)
    seccion3.grid(row=2, column=0)

    titulo = "Complete el siguiente formulario para enviar\nun correo al desarrollador de la Interfaz"
    info_titulo = CustomLabel(seccion1, text=titulo, font=("Ariel", 15, "bold"), fg_color="#000000")
    info_titulo.pack()

    asunto = CustomLabel(seccion2, text="Asunto").pack(padx = 15, pady = (5, 0), anchor = 'w')
    campo_asunto = CustomText(seccion2)
    campo_asunto.pack(pady=(0,20), padx=15)

    detalles = CustomLabel(seccion2, text="Mensaje").pack(padx = 15, anchor = 'w')
    campo_dt = CustomText(
        seccion2
    )
    campo_dt.pack(pady=(0,10), padx=15)
    
    boton_cerrar = CustomButton(
        seccion3, 
        text="Volver al Menú Principal", 
        command=mensaje.destroy                        
    )
    boton_cerrar.pack(padx = 30, side="left")


    boton_enviar = CustomButton(
        seccion3,
        text="Enviar",
        command=lambda: contacto(
            str(campo_asunto.get("1.0", "end-1c")),
            str(campo_dt.get("1.0", "end-1c"))
        )
    )

    boton_enviar.pack(padx = 40,side="right")

    mensaje.mainloop()