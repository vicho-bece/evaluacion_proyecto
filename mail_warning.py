import datetime
from email.message import EmailMessage
import smtplib

def get_Fecha():
    dt = datetime.datetime.now()

    mes = str(dt.month)
    dia = str(dt.day)

    if(dt.month < 10):
        mes = "0" + str(dt.month)

    if(dt.day < 10):
        dia = "0" + str(dt.day)


    fecha = str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second) + " , " + dia + "-" + mes + "-" + str(dt.year)

    return(fecha)

def mandarEmail(encabezado, contenido):

    # Las siguientes lineas, se debe ingresar su correo y contrasena para enviar los correos a los alumnos
    # Ingrese su correo electronico
    
    origen = "vicentebecerra72@gmail.com"
    destinatario = "vbecerra@miramar.cl"
    contrasena = "zwrw uotk kczr ievf"


    correo = EmailMessage()
    correo["From"] = f"Automatización de Evaluación de Proyecto<{origen}>"
    correo["To"] = f"<Vicente Becerra R.>  <{destinatario}>"
    correo["Subject"] = str(encabezado) + " [ " + get_Fecha() + " ]"

    correo.set_content(str(contenido))
    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.starttls()
        mail.login(origen, contrasena)
        mail.sendmail(origen, destinatario, correo.as_string())
        print("Correo enviado exitosamente.")
    except Exception as error:
        print(f"Error al enviar el correo: {error}. Favor contactarse con el desarrollador")
    finally:
        mail.quit()