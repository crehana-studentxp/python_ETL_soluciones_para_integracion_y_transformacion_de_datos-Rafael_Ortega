import pandas as pd
import re

def StringLowercase(df):
    """
    Función cambiar todos los strings de un dataframe a lowercase
    (columnas y observaciones)
    ==========
    * Args:
         - df: dataframe al que se desea hacer la modificación.
    * Return:
         - df: dataframe modificado
    ==========
    Ejemplo:
        >>df = StringLowercase(df)
    """
    ### Columnas

    DataFrameColumns = df.columns

    for col in DataFrameColumns:
        df.rename(columns={col:col.lower()}, inplace=True)

    ### Observaciones

    filtro = df.dtypes == object
    objects = df.dtypes[filtro]
    StringColumns = list(objects.index)

    for col in StringColumns:
        df[col] = df[col].str.lower()

    return df

def StringAcentos(df):
    """
    Función para eliminar acentos, dieresis y eñes de los strings de un
    dataframe (columnas y observaciones)
    ==========
    * Args:
         - df: dataframe al que se desea hacer la modificación.
    * Return:
         - df: dataframe modificado
    ==========
    Ejemplo:
        >>df = StringAcentos(df)
    """
    ### Columnas

    df.columns = df.columns.str.replace('á', 'a')
    df.columns = df.columns.str.replace('é', 'e')
    df.columns = df.columns.str.replace('í', 'i')
    df.columns = df.columns.str.replace('ó', 'o')
    df.columns = df.columns.str.replace('ú', 'u')
    df.columns = df.columns.str.replace('ü', 'u')
    df.columns = df.columns.str.replace('ñ', 'n')

    ### Observaciones

    filtro = df.dtypes == object
    objects = df.dtypes[filtro]
    StringColumns = list(objects.index)

    for col in StringColumns:
        df[col] = df[col].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    return df

def StringStrip(df):
    """
    Función para eliminar espacios al inicio y al final de los strings de un
    dataframe (columnas y observaciones)
    ==========
    * Args:
         - df: dataframe al que se desea hacer la modificación.
    * Return:
         - df: dataframe modificado
    ==========
    Ejemplo:
        >>df = StringStrip(df)
    """
    ### Columnas

    df.columns = [col.strip() for col in df.columns]

    ### Observaciones

    filtro = df.dtypes == object
    objects = df.dtypes[filtro]
    StringColumns = list(objects.index)

    for col in StringColumns:
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

    return df

def StringEspacios(df):
    """
    Función para eliminar espacios dobles (o mas) de los strings de un
    dataframe (columnas y observaciones)
    ==========
    * Args:
         - df: dataframe al que se desea hacer la modificación.
    * Return:
         - df: dataframe modificado
    ==========
    Ejemplo:
        >>df = StringEspacios(df)
    """
    ### Columnas

    df.columns = [re.sub(' +', ' ', col) for col in df.columns]

    ### Observaciones

    filtro = df.dtypes == object
    objects = df.dtypes[filtro]
    StringColumns = list(objects.index)

    for col in StringColumns:
        df[col] = df[col].apply(lambda x: re.sub(' +', ' ', x) if isinstance(x, str) else x)

    return df

def EstandarizaFormato(df):
    """
    Función para estandarizar un dataframe: minúsculas, sin espacios en blanco,
    sin signos de puntuación (columnas y observaciones)
    ==========
    * Args:
         - df: dataframe al que se desea hacer la modificación.
    * Return:
         - df: dataframe modificado
    ==========
    Ejemplo:
        >>df = EstandarizaFormato(df)
    """
    ### Quita espacios en columnas
    df.columns = df.columns.str.replace(' ', '_')

    ### Minúsculas
    df = StringLowercase(df)

    ### Acentos
    df = StringAcentos(df)

    ### Quitamos espacios al principio y al final
    df = StringStrip(df)

    ### Quitamos espacios
    df = StringEspacios(df)

    return df