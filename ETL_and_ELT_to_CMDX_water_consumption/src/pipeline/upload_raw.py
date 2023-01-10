import luigi
import pandas as pd
#import boto3
import json
import csv
#import metadataExtract
#from luigi import extractToJson
#from luigi.Version2.metadataExtract import metadataExtract
#from luigi import extract
import psycopg2
import pandas.io.sql as psql



#from metadataExtract import metadataExtract
#from metadataTestExtract import metadataTestExtract


import configparser
from extract import extractToJson
from luigi.contrib.postgres import CopyToTable
from luigi.contrib.postgres import PostgresTarget

class copyToPostgres(CopyToTable):
    """
    Function to copy raw data from the extracting process from mexico city metro data set on the database on postgres.
    It uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """
    
    print("credentials")
    
    # Load the aws_boto_credentials values
    parser = configparser.ConfigParser()
    parser.read("../../pipeline.conf")
    access_key = parser.get("aws_boto_credentials","access_key")
    secret_key = parser.get("aws_boto_credentials","secret_key")
    bucket = parser.get("aws_boto_credentials","bucket_name")
    
    # Load PostgreSQL credentials
    database = parser.get("postgres_config","database")
    user = parser.get("postgres_config","username")
    password = parser.get("postgres_config","password")
    host = parser.get("postgres_config","host")
    port = parser.get("postgres_config","port")
    table = "inai_raw"
    columns = [("id_registro","TEXT"),("folio","TEXT"),("fechasolicitud", "TEXT"),("dependencia", "TEXT"),
               ("estatus","TEXT"),("medioentrada","TEXT"),("tiposolicitud", "TEXT"),("descripcionsolicitud", "TEXT"),
               ("otrosdatos","TEXT"),("archivoadjuntosolicitud","TEXT"),("medioentrega", "TEXT"),
               ("fechalimite", "TEXT"), ("respuesta","TEXT"),("textorespuesta","TEXT"),("archivorespuesta", "TEXT"),
               ("fecharespuesta", "TEXT"),
               ("pais","TEXT"),("estado","TEXT"),("municipio", "TEXT"),("codigopostal", "TEXT"),
               ("sector","TEXT")]
    
    
    # Luigi parameters
    task_name = 'copyToPostgreSQL'
    date = luigi.Parameter()
    
    print(task_name)
    
    def requires(self):
        return extractToJson(date=self.date)

    def rows(self):
        print("using rows")
        with self.input().open('r') as json_file:
            data = json.load(json_file)
            #print(data)
            filas_a_cargar = len(data['results'])
            print(filas_a_cargar)
            
            
            
            for line in data['results']:

                id_registro = line.get('_id')
                folio = line.get('FOLIO')
                fechasolicitud = line.get('FECHASOLICITUD')
                dependencia = line.get('DEPENDENCIA')
                estatus = line.get('ESTATUS')
                medioentrada = line.get('MEDIOENTRADA')
                tiposolicitud = line.get('TIPOSOLICITUD')
                descripcionsolicitud = line.get('DESCRIPCIONSOLICITUD')
                otrosdatos = line.get('OTROSDATOS')
                archivoadjuntosolicitud = line.get('ARCHIVOADJUNTOSOLICITUD')
                medioentrega = line.get('MEDIOENTREGA')
                fechalimite = line.get('FECHALIMITE')
                respuesta = line.get('RESPUESTA')
                textorespuesta = line.get('TEXTORESPUESTA')
                archivorespuesta = line.get('ARCHIVORESPUESTA')
                fecharespuesta = line.get('FECHARESPUESTA')
                pais = line.get('PAIS')
                estado = line.get('ESTADO')
                municipio = line.get('MUNICIPIO')
                codigopostal = line.get('CODIGOPOSTAL')
                sector = line.get('SECTOR')
                yield (id_registro, folio, fechasolicitud,dependencia,estatus,medioentrada, 
                       tiposolicitud, descripcionsolicitud, otrosdatos, archivoadjuntosolicitud,
                       medioentrega, fechalimite, respuesta, textorespuesta, archivorespuesta,
                       fecharespuesta, pais, estado, municipio, codigopostal, sector)



if __name__ == '__main__':
    luigi.copyToPostgres()
