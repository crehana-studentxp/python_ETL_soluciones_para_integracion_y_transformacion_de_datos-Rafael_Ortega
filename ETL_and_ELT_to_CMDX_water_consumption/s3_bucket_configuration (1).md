
# Step 1: Configurar el IAM role para conectarse a la S3
Iniciaremos por configurar el IAM User para ello, nos vamos al menu de servicios en aws.
En la sección de Seguridad, identidad y conformidad encontraremos la opción de IAM.
![s3_config_01](imagenes/s3_configuration/s3_configuration_01.JPG "s3_config_01")

En el panel de la izquierda, tendrás que navegar hasta la opción de Usuarios:
![s3_config_02](imagenes/s3_configuration/s3_configuration_02.JPG "s3_config_02")

Dar clic en Agregar usuarios:
![s3_config_03](imagenes/s3_configuration/s3_configuration_03.JPG "s3_config_03")

Escribir el nombre de usuario, en mi caso será "crehana_bi_specialist_s3 y marcar la opción de Clave de acceso: acceso mediante programación.
![s3_config_04](imagenes/s3_configuration/s3_configuration_04.JPG "s3_config_04")

Esto te permitirá ingresar mediante los scripts de python.

dar clic en "siguiente: Permisos".

En la sección de permisos, ponerle la opción de "Asociar directamente las políticas existentes y buscar la política de AmazonS3FullAccess.
![s3_config_05](imagenes/s3_configuration/s3_configuration_05.JPG "s3_config_05")

Dar clic en Siguiente:Etiquetas.

Las Etiquetas son opcionales. Sin embargo, te ayudan generalmente a identificar de mejor manera tus usuarios. Yo te recomendaría que le pongas una etiqueta que te ayude a saber para que es ese usuario.
![s3_config_06](imagenes/s3_configuration/s3_configuration_06.JPG "s3_config_06")


Dar clic en Siguiente: Revisar

Debería aparecerte una ventana como la siguiente:
![s3_config_07](imagenes/s3_configuration/s3_configuration_07.JPG "s3_config_07")

Dar clic en crear un usuario
Esto te generará la siguiente ventana de confirmación del usuario:
![s3_config_08](imagenes/s3_configuration/s3_configuration_08.JPG "s3_config_08")

Es importante descargar el csv y guardarlo en algún lugar seguro, pues esto nos permitirá conectarnos a nuestra instancia de S3 desde la computadora localmente. 

ID de clave de acceso: AKIAULCJ6RPVU652Z4GU
Clave de acceso secreta: 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
user: crehana_bi_specialist_s3

Ahora que tenemos el rol con el que nos conectaremos a una instancia S3, vamos a configurarla.

# Step 2: Configuración de la instancia S3

La configuración de una S3 se puede ver directamente en la página de la documentación oficial, que es la siguiente [liga](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html). Por nuestra parte, yo les mostraré la forma de configurarla para seguir los procesos de este curso.

Volvemos a la sección de Todos los servicios y ahora seleccionamos la opción de S3:
![s3_config_09](imagenes/s3_configuration/s3_configuration_09.JPG "s3_config_09")

Seleccionamos la opción de Crear Bucket
![s3_config_10](imagenes/s3_configuration/s3_configuration_10.JPG "s3_config_10")

En esta sección agregaremos el nombre del bucket. En mi caso se llamará crehanabucket:
![s3_config_11](imagenes/s3_configuration/s3_configuration_11.JPG "s3_config_11")

por el momento dejaremos todas las opciones como default, incluído el bloquo al acceso público, pues nos conectaremos mediante nuestro usuario de IAM.

Damos clic en Crear bucket.

Listo, ya está configurada tu bucket de S3.

# Step 3: Configure our environment.
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
