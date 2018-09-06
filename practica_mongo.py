import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017,username='root',password='Cic1234*',authSource="admin")
db = client["test"]
collection = db["data"]

campos = {}
print ("\n El numero de elementos de la coleccion es: ", collection.count())
num = collection.count();
docs = collection.find()
for document in docs:
        for key in document:
            if key in campos:
               campos[key] +=1
            else:
               campos[key] = 1
print ("\n El porcentaje de apariciones de los elementos de la coleccion es : ")
for valor,frecuencia in campos.items():
         print (valor, ":", (frecuencia / num) * 100 )
