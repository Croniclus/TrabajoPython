import pymongo

class Agenda:
    def __init__(self, cliente, db, coleccion):
        self.cliente = cliente
        self.db = self.cliente[db]
        self.coleccion = self.db[coleccion]
        
    def insertar_contacto(self, nombre, apellido, telefono, gmail):
        if nombre is None or apellido is None or telefono is None or gmail is None:
            raise ValueError("Todos los valores introducidos tienen que estar llenos")
        inserccion = {"nombre": nombre, "apellido": apellido, "telefono": telefono, "gmail": gmail}
        self.coleccion.insert_one(inserccion)
        
    def borrar_contacto(self, nombre):
        self.coleccion.delete_one({"nombre": nombre})
        
    def actualizar_contacto(self, nombre ,nombre_nuevo, apellido_nuevo, telefono_nuevo, gmail_nuevo):
            self.coleccion.update_many({"nombre": nombre}, {"$set": {"gmail": gmail_nuevo,"nombre": nombre_nuevo,"telefono": telefono_nuevo,"apellido": apellido_nuevo }})
            # self.coleccion.update_one({"_id": id}, {"$set": actualizacion})
    def listar_contactos(self):
        listado= self.coleccion.find({})
        listadoArr= []
        
        for i in listado:
            print("Nombre: ", i["nombre"])
            print("Apellido: ", i["apellido"])
            print("Telf: ", i["telefono"])
            print("Correo: ", i["gmail"])
            listadoArr.append(i)
        return listadoArr
    
    #conexion a la base de datos
    #conexion = pymongo.MongoClient("mongodb://localhost:27017/")
    #creo la agenda y la coleccion de contactos
    #db = conexion["BDD_AGENDA"]
    #coleccion = db["contacto"]
    
    
    
    
    
#opcion=0
#while opcion!=1 | opcion!=2 | opcion!=3 | opcion!=4: 
#    print("--------------------------------------------")
#    print("---               AGENDA                 ---")
#    print("---       1.- INSERTAR CONTACTO          ---")
#    print("---       2.- BORRAR CONTACTO            ---")
#    print("---       3.- ACTUALIZAR CONTACTO        ---")
#    print("--------------------------------------------")
#    print("--------------------------------------------")
#    opcion=input("Seleccione una opcion: ")
#if opcion==1:
#    print("Usted ha seleccionado la opcion 1")
#    
#if opcion==1:
#    print("Usted ha seleccionado la opcion 2")
#if opcion==1:
#    print("Usted ha seleccionado la opcion 3")
#if opcion==1:
#    print("Usted ha seleccionado la opcion 4")

