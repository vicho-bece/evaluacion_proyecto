----------------------------------------------------
-- BASE DE DATOS QUE RECIBE LAS FILAS DE LOS EXCEL'S
-- COLUMNAS SIMILARES AL EXCEL
----------------------------------------------------
DROP TABLE IF EXISTS Resumen_ACUSE;
CREATE TABLE Resumen_ACUSE(
	autorizacion_Miramar varchar(10),
	periodo integer,
	iva_recuperable varchar(3),
	empresa varchar(100) not null,
	rut_empresa varchar(11) not null,
	codigo_documento smallint,
	tipo_Documento varchar(30),
	cc varchar(7),
	cuenta_contable varchar(100),
	rut_proveedor varchar(11) not null,
	razon_social varchar(100),
	folio integer not null,
	fecha_dcto date not null,
	exento integer not null,
	neto integer not null,
	iva integer not null,
	ceec varchar(100),
	total integer not null,
	otros integer,
	archivos_ant varchar(10),
	envio_dcto varchar(10),
	notas varchar(100),
	estado varchar(100),
	centro_costo varchar(100),
	cta_contable varchar(50),
	autorizacion varchar(20),
	observacion varchar(50),
	ruta varchar(150)
);

DROP TABLE IF EXISTS Sin_asignar;
CREATE TABLE Sin_asignar(
	autorizacion_Miramar varchar(10),
	periodo integer,
	iva_recuperable varchar(3),
	empresa varchar(100) not null,
	rut_empresa varchar(11) not null,
	codigo_documento smallint,
	tipo_Documento varchar(30),
	cc varchar(7),
	cuenta_contable varchar(100),
	rut_proveedor varchar(11) not null,
	razon_social varchar(100),
	folio integer not null,
	fecha_dcto date not null,
	exento integer not null,
	neto integer not null,
	iva integer not null,
	ceec varchar(100),
	total integer not null,
	otros integer,
	archivos_ant varchar(10),
	envio_dcto varchar(10),
	notas varchar(100),
	estado varchar(100),
	centro_costo varchar(100),
	cta_contable varchar(50),
	autorizacion varchar(20),
	observacion varchar(50),
	ruta varchar(150)
);

DROP TABLE IF EXISTS Libro_compras_diez;
CREATE TABLE Libro_compras_diez(

	codigo_SII smallint not null,
	num_Documento integer not null,
	corr_Interno integer not null,
	fecha date not null,
	rut varchar(13) not null,
	nombre_Proveedor varchar(100) not null,
	neto_Afecto integer not null,
	neto_Exento integer not null,
	iva integer not null,
	iva_no_recjuperable integer not null,
	credito_especial integer not null,
	otros_impuestos integer not null,
	total bigint not null
);
DROP TABLE IF EXISTS Libro_constructora_vyv;
CREATE TABLE Libro_constructora_vyv(

	codigo_SII smallint not null,
	num_Documento integer not null,
	corr_Interno integer not null,
	fecha date not null,
	rut varchar(13) not null,
	nombre_Proveedor varchar(100) not null,
	neto_Afecto integer not null,
	neto_Exento integer not null,
	iva integer not null,
	iva_no_recjuperable integer not null,
	credito_especial integer not null,
	otros_impuestos integer not null,
	total bigint not null
);

DROP TABLE IF EXISTS Libro_constr_inmob_vyv;
CREATE TABLE Libro_constr_inmob_vyv(

	codigo_SII smallint not null,
	num_Documento integer not null,
	corr_Interno integer not null,
	fecha date not null,
	rut varchar(13) not null,
	nombre_Proveedor varchar(100) not null,
	neto_Afecto integer not null,
	neto_Exento integer not null,
	iva integer not null,
	iva_no_recjuperable integer not null,
	credito_especial integer not null,
	otros_impuestos integer not null,
	total bigint not null
);