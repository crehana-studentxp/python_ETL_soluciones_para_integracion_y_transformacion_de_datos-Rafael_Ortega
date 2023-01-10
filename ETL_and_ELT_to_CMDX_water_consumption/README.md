# ELt_to_CMDX_water_consumption
This github repository develops the ETL process on the public water consumption database from Mexico City

The database can be found in [This Link](https://datos.cdmx.gob.mx/dataset/consumo-agua)

On this repo, the idea is to create the extraction from the water consumption database from Mexico City, extract the data, load into an AWS S3, and Transform it.

 python -m luigi --module transform_raw transformData --date '19-06-2003' --local-scheduler