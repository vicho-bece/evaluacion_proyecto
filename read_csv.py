import glob
from datetime import datetime
import psycopg2  # type: ignore
import ntpath

import pandas as pd 
import mail_warning as utl
import query_sql as qs

def conexion():
    bd = "DataBase"
    usuario = "postgres"
    password = "Miramar2025#"
    host = "localhost"
    port = "5433"

    return bd, usuario, password, host, port 

def actualiza():

    basedatos, usuario, password, host, port = conexion()

    try:
        # Conexion con la base de datos PostgreSQL
        conn = psycopg2.connect(
            dbname=basedatos,
            user=usuario,
            password=password,
            host=host,
            port=port
        )
    except:
        return "Se produjo un error en la conexion con la BASE DE DATOS."
    
    cur = conn.cursor()


    #csv_files = glob.glob('C:/Users/vicho/Desktop/data/ACUSES/*.csv')
    csv_files = glob.glob('Y:/EVALUACION DE PROYECTO/ACUSES/*.csv')


    if (csv_files == []):
        cur.close()
        conn.close()
        return "No se ha detectado algun archivo(.csv), revisar el contenido de la carpeta y formato de los Excel"
    

    # Por cada archivo(.csv), la tabla almacena su contenido
    for file in csv_files:

        archivo = ntpath.basename(file)
        # Leer CSV con pandas
        df = pd.read_csv(file, sep=";", encoding="utf-8")

        # Eliminar las últimas dos columnas
        df = df.iloc[:, :-2]

        # Eliminar el separador de Miles
        columnas_numericas = ["EXENTO", "NETO", "IVA", "TOTAL", "OTROS"]

        for col in columnas_numericas:
            df[col] = df[col].astype(str).str.replace(".", "", regex=False)
            df[col] = df[col].astype(str).str.replace(",", ".", regex=False)
            df[col] = pd.to_numeric(df[col], errors="coerce")  # Convertir a número

        # Guardar el dataframe en un archivo temporal
        temp_file = "temp.csv"
        df.to_csv(temp_file, index=False, sep=";", encoding="utf-8")
        
        try:
            with open(temp_file, 'r', encoding="utf-8") as f:
                lineas = f.readlines()  # Lee todas las líneas
                datos = [line.strip().split(';') for line in lineas]

            query = qs.resumen_libro()
            cont = 0

            for line in datos:
                if cont > 0:
                    cur.execute(query, (line[4], line[9], line[11], line[23], line[24], line[17], 
                        line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]
                        , line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17]
                        , line[18], line[19], line[20], line[21], line[22], line[23], line[24], line[25], line[26], archivo))
                    conn.commit()
                else:
                    cont += 1
        except Exception as error:
            cur.close()
            conn.close()
            print(error)
            return "Se produjo un error durante la copia del CSV hacia la base de datos. Archivo: " + str(file) + "\n\nMensaje:\n" + str(error)
        
# --------------------------------------------       
    query = qs.sin_asignar()
    cur.execute(query)
    conn.commit()

    #csv_files = glob.glob('C:/Users/vicho/Desktop/data/LIBRO DE COMPRAS DIEZ/*.csv')

    csv_files = glob.glob('Y:/EVALUACION DE PROYECTO/LIBRO DE COMPRAS DIEZ/*.csv')

    if (csv_files == []):
        cur.close()
        conn.close()
        return "No se ha detectado algun archivo(.csv), revisar el contenido de la carpeta y formato de los Excel"

    for file in csv_files:

        # Lee el CSV sin encabezado
        df = pd.read_csv(file, sep=";", encoding="utf-8", header=None)
        df = df.loc[~df.isnull().all(axis=1)]
        df = df[df[0].str.isnumeric()]
        df[4] = df[4].astype(str).str.replace(".", "", regex=False)
        name = "contador.csv"
        df.to_csv(name, index=False, sep=";", encoding="utf-8")

        try:
            with open(name, 'r', encoding="utf-8") as f:
                lineas3 = f.readlines()  # Lee todas las líneas
                datos = [line.strip().split(';') for line in lineas3]

            query1 = qs.traspaso("""Libro_compras_DIEZ""")
            cont = 0
        
            for line in datos:
                if cont > 0:
                    cur.execute(query1, (line[1], line[4], line[0], line[1], line[2], line[3],line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12]))
                    conn.commit()
                else:
                    cont += 1

        except Exception as error:
            cur.close()
            conn.close()
            return "Se produjo un error durante la copia del CSV hacia la base de datos. Archivo: " + str(file) + "\n\nMensaje:\n" + str(error)

# ---------------------------------------------------------------------------------------------------------------------------------------------

    #csv_files = glob.glob('C:/Users/vicho/Desktop/data/LIBRO CONSTRUCTORA VYV/*.csv')
    csv_files = glob.glob('Y:/EVALUACION DE PROYECTO/LIBRO CONSTRUCTORA VYV/*.csv')

    if (csv_files == []):
        cur.close()
        conn.close()
        return "No se ha detectado algun archivo(.csv), revisar el contenido de la carpeta y formato de los Excel"

    for file in csv_files:

        # Lee el CSV sin encabezado
        df = pd.read_csv(file, sep=";", encoding="utf-8", header=None)
        df = df.loc[~df.isnull().all(axis=1)]
        df = df[df[0].str.isnumeric()]
        df[4] = df[4].astype(str).str.replace(".", "", regex=False)
        name = "contador.csv"
        df.to_csv(name, index=False, sep=";", encoding="utf-8")

        try:
            with open(name, 'r', encoding="utf-8") as f:
                lineas = f.readlines()  # Lee todas las líneas
                datos = [line.strip().split(';') for line in lineas]

            query2 = qs.traspaso("""Libro_constructora_vyv""")
            cont = 0

            for line in datos:
                if cont > 0:
                    cur.execute(query2, (line[1], line[4], line[0], line[1], line[2], line[3],line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12]))
                    conn.commit()
                else:
                    cont += 1

        except Exception as error:
            cur.close()
            conn.close()
            return "Se produjo un error durante la copia del CSV hacia la base de datos. Archivo: " + str(file) + "\n\nMensaje:\n" + str(error)

# ---------------------------------------------------------------------------------------------------------------------------------------------
    #csv_files = glob.glob('C:/Users/vicho/Desktop/data/LIBRO CONSTR E INMOB VYV/*.csv')
    csv_files = glob.glob('Y:/EVALUACION DE PROYECTO/LIBRO CONSTR E INMOB VYV/*.csv')

    if (csv_files == []):
        cur.close()
        conn.close()
        return "No se ha detectado algun archivo(.csv), revisar el contenido de la carpeta y formato de los Excel"

    for file in csv_files:

        # Lee el CSV sin encabezado
        df = pd.read_csv(file, sep=";", encoding="utf-8", header=None)
        df = df.loc[~df.isnull().all(axis=1)]
        df = df[df[0].str.isnumeric()]
        df[4] = df[4].astype(str).str.replace(".", "", regex=False)
        name = "contador.csv"
        df.to_csv(name, index=False, sep=";", encoding="utf-8")

        try:
            with open(name, 'r', encoding="utf-8") as f:
                lineas = f.readlines()  # Lee todas las líneas
                datos = [line.strip().split(';') for line in lineas]

            query3 = qs.traspaso("""Libro_constr_inmob_vyv""")
            cont = 0

            for line in datos:
                if cont > 0:
                    cur.execute(query3, (line[1], line[4], line[0], line[1], line[2], line[3],line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12]))
                    conn.commit()
                else:
                    cont += 1

        except Exception as error:
            cur.close()
            conn.close()
            return "Se produjo un error durante la copia del CSV hacia la base de datos. Archivo: " + str(file) + "\n\nMensaje:\n" + str(error)

# ---------------------------------------------------------------------------------------------------------------------------------------------

    cur.execute(qs.constructora10())
    conn.commit()

    cur.execute(qs.constructoraVYV())
    conn.commit()

    cur.execute(qs.construc_inmob_VYV())
    conn.commit()

    cur.close()
    conn.close()

    return "¡La Base de Datos PostgreSQL ha sido actualizado!"

def formatoRUT(rut):
    rut = str(rut)
    rut = rut.replace(".", "")
    guion = str(rut).find("-")

    if guion >= 0:
        rut = rut.split("-")
        if rut[0].isdigit():
            return True

    return False

def insertarFila(recu, constr,  tipo_dcto, cc,  rut,  dcto, fecha, exento2, neto, iva, ceec, otros2, files, nota, centro, cta, obs):

    revision = ""
    obs_suma = ""
    formato_fecha = "%d-%m-%Y"
    proveedor = ""

    match constr:
        case "CONSTRUCTORA DIEZ SPA": rut_const = '77298664-5'
        case "CONSTRUCTORA VYV LIMITADA": rut_const = '78901770-0'
        case "Constructora e Inmobiliaria VYV": rut_const = '76680204-4'

    basedatos, usuario, password, host, port = conexion()

    try:
        # Conexion con la base de datos PostgreSQL
        conn = psycopg2.connect(
            dbname=basedatos,
            user=usuario,
            password=password,
            host=host,
            port=port
        )

        cur = conn.cursor()
        cur.execute(qs.noRepetidos())
        guardar = cur.fetchall()

        if formatoRUT(rut):
            proveedores_dict = {r: nombre for _, r, _, nombre, _ in guardar}
            proveedor = proveedores_dict.get(rut, "")
        else:
            revision += "Formato del Rut invalido\n"
    except:
        revision += "Falla en la conexion con la Base de Datos"

    cur.close()
    conn.close()

    try:
        date = datetime.strptime(fecha, formato_fecha)
    except:
        revision += "El formato de la fecha debe utilizar: dd-mm-yyyy. La entrada: " + fecha + "\n"

    if not str(neto).isdigit(): obs_suma += "El Valor Neto solo debe contener números\n"
    if not str(iva).isdigit(): obs_suma += "El Valor IVA solo debe contener números\n"
    if not str(exento2).isdigit(): obs_suma += "El Valor Exento solo debe contener números\n"
    if not str(otros2).isdigit(): obs_suma += "El Valor de Otros Impuestos solo debe contener números\n"

    mes = str(date.month)

    if(date.month < 10):
        mes = "0" + str(date.month)

    periodo = str(date.year) + mes

    total = 0
    if len(obs_suma) < 1 and len(revision) < 1:
        total = int(neto) + int(iva) + int(exento2) + int(otros2)

        #csv_files = 'C:/Users/vicho/Desktop/data/ACUSES/ACUSES INGRESADOS.csv'
        csv_files = 'Y:/EVALUACION DE PROYECTO/ACUSES/ACUSES INGRESADOS.csv'   

        df = pd.read_csv(csv_files, sep=";", encoding="utf-8")
        nueva_fila = ["", periodo, recu, constr, rut_const, 0, tipo_dcto, cc, "", rut, proveedor, dcto, fecha, exento2, neto, iva, ceec, total, otros2, files, "", nota, "", centro, cta, "", obs, "", ""]
        df.loc[len(df)] = nueva_fila

        df.to_csv(csv_files,index=False, sep=";", encoding="utf-8")   

        revision += "Esta fila fue guardado en el Excel ACUSES INGRESADOS.\nEste Excel se encuentra en la carpeta ACUSES (El mismo donde ud deposita los acuses)"         


    return revision + obs_suma

def eliminarFila(constr, dcto, rut_proveedor, total, edificio):

    obs = ""

    match constr:
        case "CONSTRUCTORA DIEZ SPA": rut_const = '77298664-5'
        case "CONSTRUCTORA VYV LIMITADA": rut_const = '78901770-0'
        case "Constructora e Inmobiliaria VYV": rut_const = '76680204-4'
        case _: obs += "Seleccione una constructora que esta dentro de las opciones" 

    basedatos, usuario, password, host, port = conexion()

    try:
        # Conexion con la base de datos PostgreSQL
        conn = psycopg2.connect(
            dbname=basedatos,
            user=usuario,
            password=password,
            host=host,
            port=port
        )

        cur = conn.cursor()
        cur.execute(qs.noRepetidos())
        guardar = cur.fetchall()

        resultado_dcto = [tupla for tupla in guardar if tupla[2] == int(dcto)]
        if resultado_dcto == []:
            obs += "El número de documento que ingreso no existe en la Base de Datos.\n"

        if formatoRUT(rut_proveedor):
            resultado_rut = [tupla for tupla in guardar if tupla[1] == rut_proveedor]
            if resultado_rut == []:
                obs += "El rut del proveedor que ingreso no existe en la Base de Datos\n"
        else:
            obs += "Formato del Rut invalido\n"

        if not str(total).isdigit(): obs += "El Valor total solo debe contener números\n"
    except:
        obs += "Falla en la conexion con la Base de Datos"
    


    if len(obs) < 1:

        fila = [tupla for tupla in guardar if tupla[0] == rut_const and tupla[1] == rut_proveedor and tupla[2] == int(dcto)]
        fila = fila[0]

        #ruta = 'C:/Users/vicho/Desktop/data/ACUSES/' + fila[4]
        ruta = 'Y:/EVALUACION DE PROYECTO/ACUSES/' + fila[4]

        df = pd.read_csv(ruta, sep=";", encoding="utf-8")
        row = df.index[(df['RUT'] == rut_const) & (df['FOLIO'] == int(dcto)) & (df['RUT PROVEEDOR'] == rut_proveedor) & (df['TOTAL'] == int(total)) & (df['CENTRO DE COSTO'] == edificio)]
        df = df.drop(row)  # row es el índice que encontraste antes
        df.to_csv(ruta, index=False, sep=";", encoding="utf-8")

        try:
            query = qs.eliminarFILA()
            values = (rut_const, rut_proveedor, dcto, total, edificio)
            cur.execute("""SELECT * FROM Resumen_ACUSE WHERE rut_empresa = (%s) and rut_proveedor = (%s) and folio = (%s) and total = (%s) and centro_costo = (%s);""", values)
            fila = cur.fetchall()
            cur.execute(query, values)
            conn.commit()
            obs += "La operacion de eliminar la factura de la Base de datos y del Excel de origen se ejecuto correctamente.\n" + str(fila)
        except Exception as error:
            obs += "\nFallo la operacion de eliminar una factura\n" + str(error)   
            
    

    cur.close()
    conn.close()

    return obs

def correoAsistencia(asunto, contenido):
    try:
        utl.mandarEmail(asunto, contenido)
        return "El correo fue enviado exitosamente."
    except Exception as error:
        return "Se produjo un error al intentar de enviar el correo.\n" + str(error)