import pandas as pd
import requests
import numpy as np
import json
import csv



import configparser
import luigi
import pandas as pd
import requests
import numpy as np
import json
import csv
import boto3
from luigi.contrib.s3 import S3Target

class transformData(luigi.Task):
    """_summary_

    Args:
        luigi (_type_): _description_
    """
    
    # Load the aws_boto_credentials values
    parser = configparser.ConfigParser()
    parser.read("../../../pipeline.conf")
    access_key = parser.get("aws_boto_credentials","access_key")
    secret_key = parser.get("aws_boto_credentials","secret_key")
    bucket = parser.get("aws_boto_credentials","bucket_name")
    
    # Luigi parameters
    task_name = 'laa'
    date = luigi.Parameter()
    
    s3 = boto3.client('s3',aws_access_key_id = access_key, aws_secret_access_key = secret_key)
    
    
    def requires(self):
        return None
    
    def run(self):
        fecha = str(self.date)
        data_raw = requests.get('https://api.datos.gob.mx/v1/inai.solicitudes&rows=100000&sort=-FECHARESPUESTA&refine.FECHARESPUESTA={fecha}')
        
        # Escribir JSON con la información descargada de la API
        with self.output().open('w') as json_file:
            json.dump(data_raw.json(),json_file)
            
    
    def output(self):
        output_path = "s3://{}/{}/extraction_{}.json".format(self.bucket,self.task_name,str(self.date))
        
        return luigi.contrib.s3.S3Target(path=output_path)
    

if __name__=='__main__':
    luigi.extractToJson()
    
# Command: 
#python -m luigi --module extract extractToJson --date '2022/01/01' --local-scheduler