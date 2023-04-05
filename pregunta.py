"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    df_clusters = pd.read_fwf('clusters_report.txt',skiprows=4, names=['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave','principales_palabras_clave'])
    df_clusters.fillna(method='ffill',inplace=True)
    df_clusters = df_clusters.groupby(['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave'])['principales_palabras_clave'].apply(' '.join).reset_index()
    df_clusters.principales_palabras_clave = df_clusters.principales_palabras_clave.str.split().apply(lambda x: " ".join(x))
    df_clusters.principales_palabras_clave = df_clusters.principales_palabras_clave.str.replace(".", "", regex=False)
    df_clusters.porcentaje_de_palabras_clave = df_clusters.porcentaje_de_palabras_clave.str.replace('%', '')
    df_clusters.porcentaje_de_palabras_clave = df_clusters.porcentaje_de_palabras_clave.str.replace(',', '.')
    df_clusters.porcentaje_de_palabras_clave = pd.to_numeric(df_clusters.porcentaje_de_palabras_clave)
    return df_clusters
