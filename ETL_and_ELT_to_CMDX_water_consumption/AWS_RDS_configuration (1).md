# Step 1: Configurar el IAM role para conectarse a la S3
Iniciaremos por configurar el IAM User para ello, nos vamos al menu de servicios en aws.
En la sección de Seguridad, identidad y conformidad encontraremos la opción de IAM.
![s3_config_01](imagenes/s3_configuration/s3_configuration_01.JPG "s3_config_01")

En el panel de la izquierda, tendrás que navegar hasta la opción de Usuarios:
![s3_config_02](imagenes/s3_configuration/s3_configuration_02.JPG "s3_config_02")

Dar clic en Agregar usuarios:
![s3_config_03](imagenes/s3_configuration/s3_configuration_03.JPG "s3_config_03")

Escribir el nombre de usuario, en mi caso será "crehana_bi_specialist_s3 y marcar la opción de Clave de acceso: acceso mediante programación.
![rds_configuration_01](imagenes/rds_configuration/rds_configuration_01.JPG "rds_configuration_01")

Esto te permitirá ingresar mediante los scripts de python.

dar clic en "siguiente: Permisos".

En la sección de permisos, ponerle la opción de "Asociar directamente las políticas existentes y buscar la política de AmazonRDSFullAccess.
![rds_configuration_02](imagenes/rds_configuration/rds_configuration_02.JPG "rds_configuration_02")

Dar clic en Siguiente:Etiquetas.

Las Etiquetas son opcionales. Sin embargo, te ayudan generalmente a identificar de mejor manera tus usuarios. Yo te recomendaría que le pongas una etiqueta que te ayude a saber para que es ese usuario.
![rds_configuration_03](imagenes/rds_configuration/rds_configuration_03.JPG "rds_configuration_03")


Dar clic en Siguiente: Revisar

Debería aparecerte una ventana como la siguiente:
![rds_configuration_04](imagenes/rds_configuration/rds_configuration_04.JPG "rds_configuration_04")

Dar clic en crear un usuario
Esto te generará la siguiente ventana de confirmación del usuario:
![rds_configuration_05](imagenes/rds_configuration/rds_configuration_05.JPG "rds_configuration_05")

Es importante descargar el csv y guardarlo en algún lugar seguro, pues esto nos permitirá conectarnos a nuestra instancia de S3 desde la computadora localmente. 

ID de clave de acceso: AKIAULCJ6RPV4BW3LSMX
Clave de acceso secreta: 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
user: crehana_bi_specialist_RDS

Ahora que tenemos el rol con el que nos conectaremos a una instancia S3, vamos a configurarla.


# Step 2: Configuración de una instacia RDS:
La configuración de una RDS se puede encontrar en la [Documentación Oficial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.Security.html). Sin embargo, yo les mostraré el paso a paso de cómo configuré las que ocuparé para el curso.

En este caso, yo voy a configurar una instancia RDS de AWS accesible públicamente, pero las mejores prácticas necesitan ciertos candados de seguridad que podrás encontrar en la siguiente [Documentación Oficial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.Security.html)

Ahora, configuraré una instancia RDS con PostgreSQL.

Volvemos a la sección de Todos los servicios y ahora seleccionamos la opción de S3:
![rds_configuration_06](imagenes/rds_configuration/rds_configuration_06.JPG "rds_configuration_06")

Damos clic en Crear Base de datos
![rds_configuration_07](imagenes/rds_configuration/rds_configuration_07.JPG "rds_configuration_07")

Seleccionamos la opción de PostgreSQL
![rds_configuration_08](imagenes/rds_configuration/rds_configuration_08.JPG "rds_configuration_08")

En Plantillas, seleccionamos la opción de Capa Gratuita, que nos permitirá utilizar las instancias gratuitas para realizar las actividades del curso.

![rds_configuration_09](imagenes/rds_configuration/rds_configuration_09.JPG "rds_configuration_09")

En una situación normal, puedes necesitar crear una instancia de Producción para grandes cantidades de datos.

ahora, en la sección de Configuración ingresamos el nombre de la base de datos, el nombre del usuario maestro y la contraseña.

Para hacer sencilla la configuración, yo le dejaré el usuario postgres y la contraseña será "12345678"

![rds_configuration_17](imagenes/rds_configuration/rds_configuration_17.JPG "rds_configuration_17")

En la configuración de la instancia seleccionaremos la db.t3.micro

Al momento de seleccionarla podrás ver algunas de sus características. Comúnmente, necesitarás una adecuada al tamaño de tus datos.

![rds_configuration_11](imagenes/rds_configuration/rds_configuration_11.JPG "rds_configuration_11")

En almacenamiento, pondremos un almacenamiento de 50 GB, ya que no requeriremos más para los trabajos de este curso.

Adicionalmente, desmarcamos la casilla de Habilitar escalado automático de almacenamiento para limitarnos a 50 GB.

![rds_configuration_12](imagenes/rds_configuration/rds_configuration_12.JPG "rds_configuration_12")

En Conectividad, queremos que la RDS sea accesible desde nuestro equipo local, por lo que no queremos conectarlo a un recurso informático EC2.

Seleccionamos crear nueva VPC
Crear un nuevo grupo de subredes de base de datos

Habilitamos el acceso público

Crear nuevo grupo de seguridad de VPC

el nombre será vpc_crehana
en zona de disponibilidad seleccionaré us-east-1a
y el puerto de la base de datos dejaré el default, que es 5432

![rds_configuration_13](imagenes/rds_configuration/rds_configuration_13.JPG "rds_configuration_13")
![rds_configuration_14](imagenes/rds_configuration/rds_configuration_14.JPG "rds_configuration_14")

La autenticación marcaremos la Autenticación de bases de datos con contraseña e IAM
![rds_configuration_15](imagenes/rds_configuration/rds_configuration_15.JPG "rds_configuration_15")

En la configuración adicional, pondremos dbcrehana como nombre de base de datos inicial.
![rds_configuration_16](imagenes/rds_configuration/rds_configuration_16.JPG "rds_configuration_16")

Todo lo demás lo dejaremos como viene por default.

Damos clic en crear base de datos.

Nos aparecerá la siguiente página de confirmación:



# Step 3: Agregar configuración al _pipeline.conf_

Agregamos lo siguiente:
```python
[postgres_config]
host = databasecrehana.cpoinii39vab.us-east-1.rds.amazonaws.com
port = 5432
username = postgres
password = 12345678
database = databasecrehana
```

# Step 4: Configure our environment.
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