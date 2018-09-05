import mysql.connector
from mysql.connector import errorcode

#### SE CREA UNA BD EN CASO DE QUE NO EXISTA ##
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


#### CONEXION A LA BD  ####
config = {
  'user': 'root',
  'password': 'Cic1234*',
   'host': 'localhost', 
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=True) # Se declara un curson el cual nos permite inerractuar con mysql

DB_NAME = 'university'
#### CREACION DE TABLAS ####
TABLES = {}
TABLES['clientes'] = (
    "CREATE TABLE clientes ("
    "  cliente_id int(11) NOT NULL,"
    "  Nombre varchar(30) NOT NULL,"
    "  Apellidos varchar(130) NOT NULL,"
    "  PRIMARY KEY (cliente_id)"
    ") ENGINE=InnoDB")

TABLES['articulos'] = (
    "CREATE TABLE articulos ("
    "  articulo_id int(11) NOT NULL,"
    "  Descripcion varchar(130) NOT NULL,"
    "  Tipo varchar(30) NOT NULL,"
    "  PRIMARY KEY (articulo_id)"
    ") ENGINE=InnoDB")

TABLES['almacen'] = (
    "CREATE TABLE almacen ("
    "  almacen_id int(11) NOT NULL,"
    "  Ubicacion varchar(130) NOT NULL,"
    "  Tipo varchar(30) NOT NULL,"
    "  PRIMARY KEY (almacen_id)"
    ") ENGINE=InnoDB")

TABLES['ventas'] = (
    "CREATE TABLE ventas ("
    "  ventas_id int(11) NOT NULL,"
    "  almacen_id int(11) NOT NULL,"
    "  articulo_id int(11) NOT NULL,"
    "  INDEX par_ind (almacen_id),"
    "  FOREIGN KEY (almacen_id)"
    "  REFERENCES almacen(almacen_id)"
    "  ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['vendedor'] = (
    "CREATE TABLE vendedor ("
    "  vendedor_id int(11) NOT NULL,"
    "  Nombre varchar(30) NOT NULL,"
    "  Apellidos varchar(130) NOT NULL,"
    "  PRIMARY KEY (vendedor_id)"
    ") ENGINE=InnoDB")

try:
    cnx.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

####### INSERCCION DE DATOS A LAS TABLAS ###
add_cliente = ("INSERT INTO clientes (cliente_id, nombre, Apellidos) VALUES (%(cliente_id)s, %(Nombre)s, %(Apellidos)s)")
data_cliente = [
	{
	'cliente_id' : 1,
	'Nombre' : 'Luis',
	'Apellidos' : 'Hernandez Britos'
	},
	{
	'cliente_id' : 2,
	'Nombre' : 'Jorge',
	'Apellidos' : 'Guiterrez Gutierrez'
	},
        {
        'cliente_id' : 3,
        'Nombre' : 'Jose',
        'Apellidos' : 'Canseco Carrasco'
        }
]
add_articulo = ("INSERT INTO articulos (articulo_id, Descripcion, Tipo) VALUES (%(articulo_id)s, %(Descripcion)s, %(Tipo)s)")
data_articulo = [
        {
        'articulo_id' : 1,
        'Descripcion' : 'Zapatos',
        'Tipo' : 'Uno'
        },
        {
        'articulo_id' : 2,
        'Descripcion' : 'Cartera',
        'Tipo' : 'Dos'
        },
        {
        'articulo_id' : 3,
        'Descripcion' : 'Playera',
        'Tipo' : 'Dos'
        }
]
add_almacen = ("INSERT INTO almacen (almacen_id, Ubicacion, Tipo) VALUES (%(almacen_id)s, %(Ubicacion)s, %(Tipo)s)")
data_almacen = [
        {
        'almacen_id' : 101,
        'Ubicacion' : 'Norte',
        'Tipo' : 'Chico'
        },
        {
        'almacen_id' : 202,
        'Ubicacion' : 'Sur',
        'Tipo' : 'Mediano'
        },
        {
        'almacen_id' : 303,
        'Ubicacion' : 'Este',
        'Tipo' : 'Grande'
        }
]
add_venta = ("INSERT INTO ventas (ventas_id, almacen_id, articulo_id) VALUES (%(ventas_id)s, %(almacen_id)s, %(articulo_id)s)")
data_venta = [
        {
        'ventas_id' : 10,
        'almacen_id' : 101,
        'articulo_id' : 1 
        },
        {
        'ventas_id' : 20,
        'almacen_id' : 202,
        'articulo_id' : 2 
        },
        {
        'ventas_id' : 30,
        'almacen_id' : 303,
        'articulo_id' : 3 
        }
]
add_vendedor = ("INSERT INTO vendedor (vendedor_id, nombre, Apellidos) VALUES (%(vendedor_id)s, %(Nombre)s, %(Apellidos)s)")
data_vendedor = [
        {
        'vendedor_id' : 1,
        'Nombre' : 'Roberto',
        'Apellidos' : 'Britos'
        },
        {
        'vendedor_id' : 2,
        'Nombre' : 'Aldair',
        'Apellidos' : 'Gutierrez'
        },
        {
        'vendedor_id' : 3,
        'Nombre' : 'Rocio',
        'Apellidos' : 'Carrasco'
        }
]
for row in range(0,len(data_cliente)):
	cursor.execute(add_cliente,data_cliente[row])

for row in range(0,len(data_articulo)):
        cursor.execute(add_articulo,data_articulo[row])

for row in range(0,len(data_almacen)):
        cursor.execute(add_almacen,data_almacen[row])

for row in range(0,len(data_venta)):
        cursor.execute(add_venta,data_venta[row])

for row in range(0,len(data_vendedor)):
        cursor.execute(add_vendedor,data_vendedor[row])

cnx.commit()

##### SE EJECUTAN LAS CONSULTA DE LA INFO A LA BD ###
print ("\nDatos de la tabla clientes")
query_clientes = ("SELECT * from clientes")
cursor.execute(query_clientes)
for row in cursor:
	print (row)

print ("\nDatos de la tabla articulos")
query_articulos = ("SELECT * from articulos")
cursor.execute(query_articulos)
for row in cursor:
	print (row)

print ("\nDatos de la tabla almacen")
query_almacen = ("SELECT * from almacen")
cursor.execute(query_almacen)
for row in cursor:
        print (row)

print ("\nDatos de la tabla ventas")
query_ventas = ("SELECT * from ventas")
cursor.execute(query_ventas)
for row in cursor:
        print (row)

print ("\nDatos de la tabla vendedor")
query_vendedor = ("SELECT * from vendedor")
cursor.execute(query_vendedor)
for row in cursor:
        print (row)


#### SE CEIRRAN LAS CONEXIONNES A LA BD ###
cursor.close()
cnx.close()
