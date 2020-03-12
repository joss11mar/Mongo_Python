# Insertar datos en MongoDB
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import csv
import urllib2
import json

# CONEXION CON MONGO ATLAS
def mongo_connect():
    uri_mongo = "mongodb+srv://joss11mar:*password*@proyecto1-olk1t.gcp.mongodb.net/test?retryWrites=true&w=majority" #Cadena MONGO ATLAS ---------> MODIFICAR
    client = MongoClient(uri_mongo)
    client.test
    return client


def read_csv(csv_path):

    ls_rows = {} #create dictionary
    file = urllib2.urlopen(csv_path) #open file in url
    ls_csv =  csv.DictReader(file,delimiter=';') #separate data

    for i in ls_csv:
        ls_rows.update(i) #add data to the dictionary
    return ls_rows


def insert_mongo_list(lista_data,client):
    db = client.Mongo #database ----------> MODIFICAR
    col = db.Prueba #collection ----------> MODIFICAR
    col.insert_one(lista_data) #insert in client.Mongo.Prueba


if __name__ == "__main__": #se define main
    url_file='http://apigobiernoabiertortod.valencia.es/apirtod/rest/datasets/intensidad_espiras.csv' #file
    #LLAMAR FUNCIONES
    client= mongo_connect()
    ls_csv = read_csv(url_file)
    insert_mongo_list(ls_csv,client)
