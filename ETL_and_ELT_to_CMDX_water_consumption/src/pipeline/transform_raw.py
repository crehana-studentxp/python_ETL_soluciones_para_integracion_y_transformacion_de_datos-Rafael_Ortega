import pandas as pd
import requests
import numpy as np
import json
import csv

import configparser
import luigi
import logging
import psycopg2
import pandas as pd
import pandas.io.sql as psql
from luigi.contrib.postgres import PostgresQuery, PostgresTarget
from utils import EstandarizaFormato
from sqlalchemy import create_engine

from upload_raw import copyToPostgres
#from metadataLoad import metadataLoad
#from metadataTestLoad import metadataTestLoad
#from loadCleaned import loadCleaned

logger = logging.getLogger('luigi-interface')

class transformData(PostgresQuery):
    """
    Function to load cleaned data from the extracting process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket. Requires extractToJson
    """
    
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
    table = 'inai_refined'
    
    # Luigi parameters
    task_name = 'transforming_data'
    date = luigi.Parameter()



    print('Credenciales leídas correctamente')

    database = database

    query = """ SELECT * from inai_raw; """ 

  
    def requires(self):
        return copyToPostgres(date=self.date)
    
    def run(self):

        connection = psycopg2.connect(user=self.user,
                                 password=self.password,
                                 host=self.host,
                                 port=self.port,
                                 database=self.database)
        cursor = connection.cursor()
        sql = self.query
        
        logger.info('Executing query from task: {name}'.format(name=self.task_name))
        cursor.execute(sql)


        df = psql.read_sql(self.query, connection)
        print(df.columns)

        
        lower_cols = (map(lambda x: x.lower(), df.columns))
        df.columns = lower_cols
        print(df.columns)
        
        df.loc[(df['folio'] =="'0001700000303"),'codigopostal']='06000'
        df.loc[(df['folio'] =="'0917900000103"),'codigopostal']='03000'
        
        print(df.dtypes)
        date_col = ['fechasolicitud','fecharespuesta','fechalimite']
        
        for element in df.columns:
            if element not in date_col:
                df[element] = df[element].replace('',None)
        
        print(df.dtypes)
        
        df = df.drop(columns = ['id_registro'])
        
        # for col in date_col:
        #     df[col] = pd.to_datetime(df[col]) 
            
        print(df.dtypes)
        
        df["folio"] = df["folio"].str.replace("'","")
        
        print("estandarizando")
        df = EstandarizaFormato(df)     
        #fin de sección        
        
        print(df.head())
        
        records_to_upload = list(df.itertuples(index=False, name=None))
        
        engine = create_engine('postgresql+psycopg2://postgres:12345678@databasecrehana.cpoinii39vab.us-east-1.rds.amazonaws.com:5432/dbcrehana')
        df.to_sql(self.table, con=engine, if_exists='replace', index=False)
        # Update marker table
        self.output().touch(connection)

        # commit and close connection
        connection.commit()
        connection.close()
        
        
#    def output(self):
#        """
#        Returns a PostgresTarget representing the executed query.
#
#        Normally you don't override this.
#        """
#        return PostgresTarget(
#            host=self.host,
#            database=self.database,
#            user=self.user,
#            password=self.password,
#            table=self.table,
#            update_id=self.update_id,
#            port=self.port
#        )

if __name__ == '__main__':
    luigi.transformData()