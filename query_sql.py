def resumen_libro():
    consulta = """
            DO
            $do$
            DECLARE
                dup_count INT;
            BEGIN
                SELECT COUNT(*)
                INTO dup_count
                FROM (
                    SELECT *
                    FROM Resumen_ACUSE
                    WHERE rut_empresa = %s and rut_proveedor = %s and folio = %s and centro_costo = %s and cta_contable = %s and total = %s
                ) subquery;
                IF dup_count > 0 THEN
                    RAISE NOTICE 'A';
                ELSE
                    INSERT INTO Resumen_ACUSE ( autorizacion_miramar,periodo,iva_recuperable,empresa,rut_empresa,codigo_documento,tipo_documento,cc,cuenta_contable,rut_proveedor,razon_social,folio,fecha_dcto,exento,neto,iva,ceec,total,otros,archivos_ant,envio_dcto,notas,estado,centro_costo,cta_contable,autorizacion,observacion,ruta) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                END IF;
            END
            $do$;
            """
    return consulta

def sin_asignar():
    consulta = """
    DROP TABLE IF EXISTS Sin_asignar;
    CREATE TABLE Sin_asignar(
        autorizacion_Miramar varchar(10),
        periodo integer not null,
        iva_recuperable varchar(3) not null,
        empresa varchar(100) not null,
        rut_empresa varchar(11) not null,
        codigo_documento smallint not null,
        tipo_Documento varchar(30) not null,
        cc varchar(7) not null,
        cuenta_contable varchar(100) not null,
        rut_proveedor varchar(11) not null,
        razon_social varchar(100) not null,
        folio integer not null,
        fecha_dcto date not null,
        exento integer not null,
        neto integer not null,
        iva integer not null,
        ceec varchar(100),
        total integer not null,
        otros integer not null,
        archivos_ant varchar(3) not null,
        envio_dcto varchar(10),
        notas varchar(100),
        estado varchar(100),
        centro_costo varchar(100),
        cta_contable varchar(10),
        autorizacion varchar(20),
        observacion varchar(50),
        ruta varchar(150)
    );
    INSERT INTO Sin_asignar
    SELECT * FROM Resumen_ACUSE
    WHERE cta_contable = '' and autorizacion = '';

    Delete from Resumen_ACUSE Where cta_contable = '' and autorizacion = '';
    """
    return consulta

def traspaso(tabla):
    consulta = """
            DO
            $do$
            DECLARE
                dup_count INT;
            BEGIN
                SELECT COUNT(*)
                INTO dup_count
                FROM (
                    SELECT num_Documento
                    FROM """ + tabla + """
                    WHERE num_Documento = %s and rut = %s
                ) subquery;

                IF dup_count > 0 THEN
                    RAISE NOTICE 'Se encontraron registros duplicados.';
                ELSE
                    INSERT INTO """ + tabla + """ (
                        codigo_SII, num_Documento, corr_Interno, fecha, 
                        rut, nombre_Proveedor, neto_Afecto, neto_Exento, 
                        iva, iva_no_recjuperable, credito_especial, 
                        otros_impuestos, total
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                END IF;
            END
            $do$;
    """
    return consulta

def constructora10():
    consulta = """
        DROP TABLE IF EXISTS Constructora_DIEZ;
        CREATE TABLE Constructora_DIEZ(

            rut_proveedores varchar(13) not null,
            numero_dcto integer not null,
            fecha date not null,
            proveedor varchar(200) not null,
            resumen_neto integer not null,
            resumen_iva integer not null,
            resumen_otros integer,
            resumen_total bigint not null,
            centro_de_costo VARCHAR(200) not null,
            cuentas_agrupadas VARCHAR(200) not null
        );


        INSERT INTO Constructora_DIEZ(rut_proveedores, numero_dcto, fecha, proveedor, resumen_neto, resumen_iva, resumen_otros, resumen_total, centro_de_costo, cuentas_agrupadas)
        SELECT r.rut_proveedor, r.folio, l.fecha, l.nombre_proveedor, SUM(r.neto), SUM(r.iva), SUM(r.otros), SUM(r.total), r.centro_costo, STRING_AGG(r.cta_contable, ' - ') AS cuentas_agrupadas
        FROM Resumen_ACUSE as r, Libro_compras_DIEZ as l
        WHERE r.folio = l.num_documento
        AND r.rut_proveedor = l.rut
		AND r.rut_empresa = '77298664-5'
        GROUP BY r.rut_proveedor, r.folio, l.fecha, l.nombre_proveedor, r.centro_costo;

        DELETE 
        FROM Constructora_DIEZ fact
        USING Libro_compras_DIEZ lib
        WHERE fact.numero_dcto = lib.num_documento
        AND fact.rut_proveedores = lib.rut
        AND (fact.resumen_total != lib.total AND (fact.resumen_neto + fact.resumen_iva - fact.resumen_otros != lib.total));

        INSERT INTO Constructora_DIEZ(rut_proveedores, numero_dcto, fecha, proveedor, resumen_neto, resumen_iva, resumen_otros, resumen_total, centro_de_costo, cuentas_agrupadas)
        SELECT r.rut_proveedor,r.folio, r.fecha_dcto ,r.razon_social, r.neto, r.iva, r.otros, r.total, r.centro_costo, r.cta_contable
        FROM Resumen_ACUSE as r, Constructora_DIEZ as fact
        WHERE r.folio = fact.numero_dcto
        AND r.rut_proveedor = fact.rut_proveedores
        AND r.total != fact.resumen_total
        AND r.rut_empresa = '77298664-5';

        DELETE FROM constructora_diez
        WHERE cuentas_agrupadas LIKE '%-%';
        """
    return consulta

def constructoraVYV():
    consulta = """
        DROP TABLE IF EXISTS Constructora_VYV;
        CREATE TABLE Constructora_VYV(

            rut_proveedores varchar(13) not null,
            numero_dcto integer not null,
            fecha date not null,
            proveedor varchar(100) not null,
            resumen_neto integer not null,
            resumen_iva integer not null,
            resumen_otros integer,
            resumen_total bigint not null,
            centro_de_costo VARCHAR(100) not null,
            cuentas_agrupadas VARCHAR(100) not null
        );


        INSERT INTO Constructora_VYV(rut_proveedores, numero_dcto, fecha, proveedor, resumen_neto, resumen_iva, resumen_otros, resumen_total, centro_de_costo, cuentas_agrupadas)
        SELECT r.rut_proveedor, r.folio, l.fecha, l.nombre_proveedor, SUM(r.neto), SUM(r.iva), SUM(r.otros), SUM(r.total), r.centro_costo, STRING_AGG(r.cta_contable, ' - ') AS cuentas_agrupadas
        FROM Resumen_ACUSE as r, Libro_constructora_VYV as l
        WHERE r.folio = l.num_documento
        AND r.rut_proveedor = l.rut
		AND r.rut_empresa = '78901770-0'
        GROUP BY r.rut_proveedor, r.folio, l.fecha, l.nombre_proveedor, r.centro_costo;

        DELETE 
        FROM Constructora_VYV fact
        USING Libro_constructora_VYV lib
        WHERE fact.numero_dcto = lib.num_documento
        AND fact.rut_proveedores = lib.rut
        AND (fact.resumen_total != lib.total AND (fact.resumen_neto + fact.resumen_iva - fact.resumen_otros != lib.total));

        INSERT INTO Constructora_VYV(rut_proveedores, numero_dcto, fecha, proveedor, resumen_neto, resumen_iva, resumen_otros, resumen_total, centro_de_costo, cuentas_agrupadas)
        SELECT r.rut_proveedor,r.folio, r.fecha_dcto ,r.razon_social, r.neto, r.iva, r.otros, r.total, r.centro_costo, r.cta_contable
        FROM Resumen_ACUSE as r, Constructora_VYV as fact
        WHERE r.folio = fact.numero_dcto
        AND r.rut_proveedor = fact.rut_proveedores
        AND r.total != fact.resumen_total
        AND r.rut_empresa = '78901770-0';

        DELETE FROM Constructora_VYV
        WHERE cuentas_agrupadas LIKE '%-%';
        """
    return consulta

def construc_inmob_VYV():
    consulta = """
        DROP TABLE IF EXISTS Construc_Inmob_VYV;
        CREATE TABLE Construc_Inmob_VYV(

            rut_proveedores varchar(13) not null,
            numero_dcto integer not null,
            fecha date not null,
            proveedor varchar(100) not null,
            resumen_neto integer not null,
            resumen_iva integer not null,
            resumen_otros integer,
            resumen_total bigint not null,
            centro_de_costo VARCHAR(100) not null,
            cuentas_agrupadas VARCHAR(100) not null
        );


        INSERT INTO Construc_Inmob_VYV(rut_proveedores, numero_dcto, fecha, proveedor, resumen_neto, resumen_iva, resumen_otros, resumen_total, centro_de_costo, cuentas_agrupadas)
        SELECT r.rut_proveedor, r.folio, l.fecha, l.nombre_proveedor, SUM(r.neto), SUM(r.iva), SUM(r.otros), SUM(r.total), r.centro_costo, STRING_AGG(r.cta_contable, ' - ') AS cuentas_agrupadas
        FROM Resumen_ACUSE as r, Libro_constr_inmob_VYV as l
        WHERE r.folio = l.num_documento
        AND r.rut_proveedor = l.rut
		AND r.rut_empresa = '76680204-4'
        GROUP BY r.rut_proveedor, r.folio, l.fecha, l.nombre_proveedor, r.centro_costo;

        DELETE 
        FROM Construc_Inmob_VYV fact
        USING Libro_constr_inmob_VYV lib
        WHERE fact.numero_dcto = lib.num_documento
        AND fact.rut_proveedores = lib.rut
        AND (fact.resumen_total != lib.total AND (fact.resumen_neto + fact.resumen_iva - fact.resumen_otros != lib.total));

        INSERT INTO Construc_Inmob_VYV(rut_proveedores, numero_dcto, fecha, proveedor, resumen_neto, resumen_iva, resumen_otros, resumen_total, centro_de_costo, cuentas_agrupadas)
        SELECT r.rut_proveedor,r.folio, r.fecha_dcto ,r.razon_social, r.neto, r.iva, r.otros, r.total, r.centro_costo, r.cta_contable
        FROM Resumen_ACUSE as r, Construc_Inmob_VYV as fact
        WHERE r.folio = fact.numero_dcto
        AND r.rut_proveedor = fact.rut_proveedores
        AND r.total != fact.resumen_total
        AND r.rut_empresa = '76680204-4';

        DELETE FROM Construc_Inmob_VYV
        WHERE cuentas_agrupadas LIKE '%-%';
        """
    return consulta

def noRepetidos():
    consulta = """
    SELECT rut_empresa, rut_proveedor, folio, razon_social, ruta
    FROM Resumen_ACUSE;
    """
    return consulta

def eliminarFILA():
    consulta = """
    DELETE FROM Resumen_ACUSE
    WHERE rut_empresa = (%s) and rut_proveedor = (%s) and folio = (%s) and total = (%s) and centro_costo = (%s);
    """
    return consulta   
