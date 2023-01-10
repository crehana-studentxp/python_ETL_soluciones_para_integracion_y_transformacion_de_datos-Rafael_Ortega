Crear cuenta
configuras S3
Configuras la RDS
Configuras tu computadora
Configuras tu ambiente de python

# Configuración de lainstancia S3

## Step 1: Configurar el IAM role para conectarse a la S3
Iniciaremos por configurar el IAM User para ello, nos vamos al menu de servicios en aws.
En la sección de Seguridad, identidad y conformidad encontraremos la opción de IAM.
![s3_config_01](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_01.JPG "s3_config_01")

En el panel de la izquierda, tendrás que navegar hasta la opción de Usuarios:
![s3_config_02](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_02.JPG "s3_config_02")

Dar clic en Agregar usuarios:
![s3_config_03](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_03.JPG "s3_config_03")

Escribir el nombre de usuario, en mi caso será "crehana_bi_specialist_s3 y marcar la opción de Clave de acceso: acceso mediante programación.
![s3_config_04](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_04.JPG "s3_config_04")

Esto te permitirá ingresar mediante los scripts de python.

dar clic en "siguiente: Permisos".

En la sección de permisos, ponerle la opción de "Asociar directamente las políticas existentes y buscar la política de AmazonS3FullAccess.
![s3_config_05](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_05.JPG "s3_config_05")

Dar clic en Siguiente:Etiquetas.

Las Etiquetas son opcionales. Sin embargo, te ayudan generalmente a identificar de mejor manera tus usuarios. Yo te recomendaría que le pongas una etiqueta que te ayude a saber para que es ese usuario.
![s3_config_06](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_06.JPG "s3_config_06")


Dar clic en Siguiente: Revisar

Debería aparecerte una ventana como la siguiente:
![s3_config_07](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_07.JPG "s3_config_07")

Dar clic en crear un usuario
Esto te generará la siguiente ventana de confirmación del usuario:
![s3_config_12](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_12.JPG "s3_config_12")

Es importante descargar el csv y guardarlo en algún lugar seguro, pues esto nos permitirá conectarnos a nuestra instancia de S3 desde la computadora localmente. 

Ahora que tenemos el rol con el que nos conectaremos a una instancia S3, vamos a configurarla.

## Step 2: Configuración de la instancia S3

La configuración de una S3 se puede ver directamente en la página de la documentación oficial, que es la siguiente [liga](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html). Por nuestra parte, yo les mostraré la forma de configurarla para seguir los procesos de este curso.

Volvemos a la sección de Todos los servicios y ahora seleccionamos la opción de S3:
![s3_config_09](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_09.JPG "s3_config_09")

Seleccionamos la opción de Crear Bucket
![s3_config_10](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_10.JPG "s3_config_10")

En esta sección agregaremos el nombre del bucket. En mi caso se llamará crehanabucket:
![s3_config_11](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_11.JPG "s3_config_11")

por el momento dejaremos todas las opciones como default, incluído el bloqueo al acceso público, pues nos conectaremos mediante nuestro usuario de IAM.

Damos clic en Crear bucket.

Listo, ya está configurada tu bucket de S3.

## Step 3: Configure our environment.
Primero, ingresamos a la carpeta del curso desde la terminal. En mi caso, sería con el siguiente comando:
```bash
cd C:\Users\rafae\OneDrive\Documentos\Crehana\ETL_and_ELT_to_CMDX_water_consumption
```

Ahora, tenemos que ingresar a nuestro environment con el siguiente comando en la terminal de windows:
```bash
.\crehana_md_bi_specialist\Scripts\activate
```
Ahora, instalaremos dos paqueterías que serán necesarias para el acceso a nuestra S3:
```bash
pip install configparser
pip install boto3
```

Configparser te servirá para leer la configuración de permisos y credenciales, mientras que boto3 será quien realizará la interacción directamente con nuestra instancia de S3.

Ahora crearemos un archivo vacío llamado _pipeline.conf_ mediante el siguiente comando:
```bash
touch pipeline.conf
```
Finalmente, agregamos una sección al _pipeline.conf_ llamada [aws_boto_credentials]. Para ello, necesitarás el ID de tu cuenta, que podrás encontrar en la pestaña superior derecha, al dar clic sobre tu nombre de usuario.


el archivo se vería de la siguiente forma:
[aws_boto_credentials]
access_key = AKI.....
secret_key = Xb5......
bucket_name = crehanabucket
account_id = 2.......

# Configuración de la instancia RDS

## Step 1: Configurar el IAM role para conectarse a la RDS
Iniciaremos por configurar el IAM User para ello, nos vamos al menu de servicios en aws.
En la sección de Seguridad, identidad y conformidad encontraremos la opción de IAM.
![s3_config_01](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_01.JPG "s3_config_01")

En el panel de la izquierda, tendrás que navegar hasta la opción de Usuarios:
![s3_config_02](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_02.JPG "s3_config_02")

Dar clic en Agregar usuarios:
![s3_config_03](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/s3_configuration/s3_configuration_03.JPG "s3_config_03")

Escribir el nombre de usuario, en mi caso será "crehana_bi_specialist_RDS" y marcar la opción de Clave de acceso: acceso mediante programación.
![rds_configuration_01](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_01.JPG "rds_configuration_01")

Esto te permitirá ingresar mediante los scripts de python.

dar clic en "siguiente: Permisos".

En la sección de permisos, ponerle la opción de "Asociar directamente las políticas existentes" y buscar la política de "AmazonRDSFullAccess".
![rds_configuration_02](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_02.JPG "rds_configuration_02")

Dar clic en Siguiente:Etiquetas.

Las Etiquetas son opcionales. Sin embargo, te ayudan generalmente a identificar de mejor manera tus usuarios. Yo te recomendaría que le pongas una etiqueta que te ayude a saber para que es ese usuario.
![rds_configuration_03](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_03.JPG "rds_configuration_03")


Dar clic en Siguiente: Revisar

Debería aparecerte una ventana como la siguiente:
![rds_configuration_04](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_04.JPG "rds_configuration_04")

Dar clic en crear un usuario
Esto te generará la siguiente ventana de confirmación del usuario:
![rds_configuration_43](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_43.JPG "rds_configuration_43")

Es importante descargar el csv y guardarlo en algún lugar seguro, pues esto nos permitirá conectarnos a nuestra instancia RDS desde la computadora localmente. 

Ahora que tenemos el rol con el que nos conectaremos a una instancia S3, vamos a configurarla.


## Step 2: Configuración de una instacia RDS:
La configuración de una RDS se puede encontrar en la [Documentación Oficial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.Security.html). Sin embargo, yo les mostraré el paso a paso de cómo configuré las que ocuparé para el curso.

En este caso, yo voy a configurar una instancia RDS de AWS accesible públicamente, pero las mejores prácticas necesitan ciertos candados de seguridad que podrás encontrar en la siguiente [Documentación Oficial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.Security.html)

Ahora, configuraré una instancia RDS con PostgreSQL.

Volvemos a la sección de Todos los servicios y ahora seleccionamos la opción de S3:
![rds_configuration_06](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_06.JPG "rds_configuration_06")

Damos clic en Crear Base de datos
![rds_configuration_07](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_07.JPG "rds_configuration_07")

Seleccionamos la opción de PostgreSQL
![rds_configuration_08](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_08.JPG "rds_configuration_08")

En Plantillas, seleccionamos la opción de Capa Gratuita, que nos permitirá utilizar las instancias gratuitas para realizar las actividades del curso.

![rds_configuration_09](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_09.JPG "rds_configuration_09")

En una situación normal, puedes necesitar crear una instancia de Producción para grandes cantidades de datos.

ahora, en la sección de Configuración ingresamos el nombre de la base de datos, el nombre del usuario maestro y la contraseña.

Para hacer sencilla la configuración, yo le dejaré el usuario postgres y la contraseña será "12345678"

![rds_configuration_17](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_17.JPG "rds_configuration_17")

En la configuración de la instancia seleccionaremos la db.t3.micro

Al momento de seleccionarla podrás ver algunas de sus características. Comúnmente, necesitarás una adecuada al tamaño de tus datos.

![rds_configuration_11](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_11.JPG "rds_configuration_11")

En almacenamiento, pondremos un almacenamiento de 50 GB, ya que no requeriremos más para los trabajos de este curso.

Adicionalmente, desmarcamos la casilla de Habilitar escalado automático de almacenamiento para limitarnos a 50 GB.

![rds_configuration_12](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_12.JPG "rds_configuration_12")

En Conectividad, queremos que la RDS sea accesible desde nuestro equipo local, por lo que no queremos conectarlo a un recurso informático EC2.

Seleccionamos crear nueva VPC
Crear un nuevo grupo de subredes de base de datos

Habilitamos el acceso público

Crear nuevo grupo de seguridad de VPC

el nombre será vpc_crehana
en zona de disponibilidad seleccionaré us-east-1a
y el puerto de la base de datos dejaré el default, que es 5432

![rds_configuration_13](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_13.JPG "rds_configuration_13")
![rds_configuration_14](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_14.JPG "rds_configuration_14")

La autenticación marcaremos la Autenticación de bases de datos con contraseña e IAM
![rds_configuration_15](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_15.JPG "rds_configuration_15")

En la configuración adicional, pondremos dbcrehana como nombre de base de datos inicial.
![rds_configuration_16](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_16.JPG "rds_configuration_16")

Todo lo demás lo dejaremos como viene por default.

Damos clic en crear base de datos.

Nos aparecerá la siguiente página de confirmación:



## Step 3: Agregar configuración al _pipeline.conf_

Agregamos lo siguiente:
```python
[postgres_config]
host = databasecrehana.cpoinii39vab.us-east-1.rds.amazonaws.com
port = 5432
username = postgres
password = 12345678
database = databasecrehana
```

## Step 4: Configure our environment.
Primero, ingresamos a la carpeta del curso desde la terminal. En mi caso, sería con el siguiente comando:
```bash
cd C:\Users\rafae\OneDrive\Documentos\Crehana\ETL_and_ELT_to_CMDX_water_consumption
```

Ahora, tenemos que ingresar a nuestro environment con el siguiente comando en la terminal de windows:
```bash
.\crehana_md_bi_specialist\Scripts\activate
```
Ahora, instalaremos dos paqueterías que serán necesarias para el acceso a nuestra S3:
```bash
pip install psycopg2
pip install boto3
pip install configparser
```





# Conectarse a una instancia RDS desde windows:

## Step 1: Obtener información de la instancia
Para conectarte a tu instancia RDS desde windows, podrás seguir la liga de la [documentación oficial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html)

Volvemos a la sección de Todos los servicios y ahora seleccionamos la opción de RDS:
![rds_configuration_06](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_06.JPG "rds_configuration_06")

En la parte izquierda encontrarás la opción de Bases de datos:
![rds_configuration_18](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_18.JPG "rds_configuration_18")

Ahí, le damos clic al nombre de la base de datos
![rds_configuration_19](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_19.JPG "rds_configuration_19")

Ahí encontrarás el punto de enlace y el puerto
![rds_configuration_20](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_20.JPG "rds_configuration_20")

## Step 2: Instalar PostgreSQL
En windows, es necesario que instales PostgreSQL en la siguiente [página oficial](https://www.postgresql.org/). Dando click en el botón de Download:
![rds_configuration_21](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_21.JPG "rds_configuration_21")

Ahí seleccionaremos la opción de tu sistema operativo. En mi caso, usaremos windows:
![rds_configuration_22](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_22.JPG "rds_configuration_22")

Damos clic en Download the installer:
![rds_configuration_23](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_23.JPG "rds_configuration_23")

dado que mi computadora es de 64 bits, descargaré el instalador para windows de 64 bits.
![rds_configuration_24](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_24.JPG "rds_configuration_24")

Se descargará un archivo ejecutable, el cual hay que abrir.

La guía de instalación se puede encontrar [aqui](https://www.enterprisedb.com/docs/supported-open-source/postgresql/installer/02_installing_postgresql_with_the_graphical_installation_wizard/01_invoking_the_graphical_installer/)

Al abrir, aparecerá la siguiente ventana: 
![rds_configuration_25](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_25.JPG "rds_configuration_25")

Dar clic en siguiente.

En cuanto a la ruta de instalación, mantendré la que viene por default
![rds_configuration_26](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_26.JPG "rds_configuration_26")

Dar clic en siguiente. 
Dejar todas las opciones seleccionadas por default.
![rds_configuration_27](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_27.JPG "rds_configuration_27")

En cuanto al directorio de datos, mantendré las opciones por default.
![rds_configuration_28](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_28.JPG "rds_configuration_28")
Dar clic en siguiente.

Pedirá una contraseña.
Por simplicidad pondré 12345678
![rds_configuration_29](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_29.JPG "rds_configuration_29")

Clic en siguiente

El puerto pondremos 5432 (el valor por default)
![rds_configuration_30](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_30.JPG "rds_configuration_30")

En opciones avanzadas mantendremos la configuración por defecto.
![rds_configuration_31](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_31.JPG "rds_configuration_31")

En el resumen de lo que se instalará, dar siguiente.
![rds_configuration_32](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_32.JPG "rds_configuration_32")


Aparecerá esta ventana, donde tendremos que elegir la instalación de PostgreSQL que hicimos.


![rds_configuration_34](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_34.JPG "rds_configuration_34")



![rds_configuration_33](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_33.JPG "rds_configuration_33")

seleccionar los siguientes paquetes:
![rds_configuration_35](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_35.JPG "rds_configuration_35")

Clic en siguiente.

No seleccionar la casilla de skip Installation y presionar cancel
![rds_configuration_36](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_36.JPG "rds_configuration_36")

## Step 3: Agregar psql al path del sistema
Nos vamos a inicio y tecleamos variables para que nos aparezca lo siguiente:
![rds_configuration_41](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_41.JPG "rds_configuration_41")

Entramos a la opción que dice "Editar las variables de entorno de esta cuenta

En la parte de Variables de usuario seleccionamos la variable Path y le damos editar...
![rds_configuration_42](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/rds_configuration/rds_configuration_42.JPG "rds_configuration_42")

Ponemos la opción de Nuevo y escribimos lo siguiente
```bash
C:\Program Files\PostgreSQL\14\bin
```
Clic en aceptar

Hora, si abres una nueva terminal y presionas psql, te darás cuenta de que ya está instalado postgres en tu computadora.

## Step 4: Conectarse a la base de datos
Ingresa desde la terminal el siguiente comando:
```bash
psql --host=your_host_name --port=5432 --username=postgres --password=your_password --dbname=your_database_name
```
En mi caso, el código fue el siguiente:

```bash
psql --host=databasecrehana.cpoinii39vab.us-east-1.rds.amazonaws.com --port=5432 --username=postgres --password=12345678 --dbname=dbcrehana
```

## Step 5: Añadir información a la base de datos
correr el siguiente comando:
```SQL
CREATE TABLE Ordenes (id_cliente int, cantidad_de_chapatas int, Estatus VARCHAR(30), precio_chapatas int, LastUpdated timestamp);

INSERT INTO Ordenes VALUES(1,2,'Backordered',190,'2021-10-09 12:00:00');
INSERT INTO Ordenes VALUES(2,2,'Shipped',190,'2021-10-09 13:00:00');
INSERT INTO Ordenes VALUES(1,1,'Delivered',95,'2021-10-09 12:30:00');
INSERT INTO Ordenes VALUES(3,2,'Backordered',190,'2021-10-09 15:00:00');
INSERT INTO Ordenes VALUES(4,2,'Shipped',190,'2021-10-09 10:00:00');
INSERT INTO Ordenes VALUES(5,2,'Delivered',190,'2021-10-09 16:20:00');
INSERT INTO Ordenes VALUES(6,3,'Backordered',285,'2021-10-09 09:00:00');
INSERT INTO Ordenes VALUES(7,2,'Shipped',190,'2021-10-09 18:50:00');
INSERT INTO Ordenes VALUES(8,4,'Backordered',380,'2021-10-09 14:30:00');
INSERT INTO Ordenes VALUES(4,2,'Shipped',190,'2021-10-09 12:00:00');
```

Verificar creación de datos con el siguiente comando:
```SQL
SELECT * FROM Ordenes;
```
```SQL

CREATE TABLE inai.raw (id_registro VARCHAR(30), FOLIO VARCHAR(30), FECHASOLICITUD TIMESTAMP, DEPENDENCIA TEXT, ESTATUS VARCHAR(30), MEDIOENTRADA VARCHAR(30), TIPOSOLICITUD VARCHAR(30), DESCRIPCIONSOLICITUD TEXT, OTROSDATOS TEXT, ARCHIVOADJUNTOSOLICITUD TEXT, MEDIOENTREGA VARCHAR(30), FECHALIMITE DATE,RESPUESTA TEXT, TEXTORESPUESTA TEXT, ARCHIVORESPUESTA TEXT, FECHARESPUESTA DATE,PAIS  VARCHAR(30), ESTADO VARCHAR(30), MUNICIPIO VARCHAR(30), CODIGOPOSTAL VARCHAR(30), SECTOR VARCHAR(30));

```

# Instalación para el AWS CLI en Windows
El AWS CLI es la Command Line Interface o interfaz de línea de comandos de AWS.

Para instalarlo en tu sistema operativo, solo necesitarás seguir los pasos en la siguiente [liga](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## Instalación en Windows:
descargar el archivo en la siguiente [liga](https://awscli.amazonaws.com/AWSCLIV2.msi)

abrir el ejecutable para instalar.

![\aws_cli_config_01](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/\aws_cli_config/\aws_cli_config_01.JPG "\aws_cli_config_01")

Clic en Next
Aceptar los terminos y condiciones de la licencia

![\aws_cli_config_02](../ETL_and_ELT_to_CMDX_water_consumption/imagenes/\aws_cli_config/\aws_cli_config_02.JPG "\aws_cli_config_02")

Clic en Next

En el custom setup usaremos la configuraicón por default. cicl en next

Clic en Install.

una vez instalado, dar clic en aceptar, cerrar la terminal y volver a abrirla.

Para confirmar la correcta instalación, ejecutar el siguiente comando:
```bash
aws --version
```
Escibir algo para que tenga movimiento no se que deebería estar escribiendo jeje




The process for creating a virtual environment for python on windows followed [this link](https://medium.com/co-learning-lounge/create-virtual-environment-python-windows-2021-d947c3a3ca78)

This is the process to follow on windows

# Creación de un ambiente virtual para python en windows

## Step 1: Crear
Para crear un ambiente virtual, debes decidir en qué directorio lo quieres colocar, dirigirte ahí desde la terminal y correr el módulo venv como un script en el path del directorio:

```bash
python3 -m venv crehana_md_bi_specialist
```

## Step 2: Activar

```bash
.\crehana_md_bi_specialist\Scripts\activate
```


## Step 3: Des activar
```bash
deactivate
```
# Instalando paquetes

```bash
pip install pandas
```

# Instalando Jupyter lab en el ambiente de python

```bash
pip install ipykernel
```

```bash
pip install jupyterlab
```

```bash
pip install jupyter
```

```bash
python3 -m ipykernel install --user --name crehana_md_bi_specialist --display-name crehana_md_bi_specialist
```

## Abrir Jupter lab
```bash
jupyter lab
```


## Instalando el requirements.txt
ponerse en la carpeta donde se encuentra el archivo requirements.txt
correr el comando 
```bash
pip install -r requirements.txt
```

## De otra forma, instalar paquete por paquete
```bash
pip install matplotlib
pip install numpy
pip install pandas
pip install seaborn
pip install plotly

```