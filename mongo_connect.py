# TO-DO: Instalar previamente los paquetes pymongo y dnspython
# -*- coding: utf-8 -*-

from pymongo import MongoClient

def mongo_connect():
    uri_mongo = "mongodb+srv://joss11mar:dalmau11ok@proyecto1-olk1t.gcp.mongodb.net/test?retryWrites=true&w=majority" # TO-DO: Poner vuestra cadena de conexiÃ³n de MongoDB Atlas
    client= MongoClient(uri_mongo)
    db = client.Mongo #database
    ls_dbs = db.Prueba #collection
    #for db in ls_dbs:
    #    print(db)

if __name__ == "__main__":
    print("Hello, I'm using Python...")
    client = None
    mongo_connect()
    print("Finish script...")

