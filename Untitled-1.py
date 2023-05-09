import pymongo


class Agenda:
        
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client["Python"]
    coleccion = db["Python"]

    documento = {"nombre": "Antonio"}
    coleccion.insert_one(documento)
    resultados=coleccion.find({"nombre" : "Antonio","apellidos":"Ramirez"})
    coleccion.delete_many({"nombre":"Antonio"})
    

