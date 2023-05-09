import Metodos
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
#db = client["AgendaAes"]
#coleccion = db["Contactos"]
agenda = Metodos.Agenda(client,"AgendaAes","Contactos")


print("--------------------------------------------")
print("---               AGENDA                 ---")
print("---       1.- INSERTAR CONTACTO          ---")
print("---       2.- BORRAR CONTACTO            ---")
print("---       3.- ACTUALIZAR CONTACTO        ---")
print("---       4.- LISTAR CONTACTOS           ---")
print("--------------------------------------------")
print("--------------------------------------------")
opcion=int(input("Seleccione una opcion: "))
if opcion== 1:
    print("Usted ha seleccionado la opcion 1")
    nombre=input("Introduzca el nombre a añadir: ")
    apellido=input("Introduzca el apellido a añadir: ")
    telefono=input("Introduzca el telefono a añadir: ")
    gmail=input("Introduzca el gmail a añadir: ")
    agenda.insertar_contacto(nombre,apellido,telefono,gmail)
    print("Se ha introducido correctamente")
if opcion== 2:
    print("Usted ha seleccionado la opcion 2")
    nombre=input("Introduzca la id del contacto a borrar: ")
    agenda.borrar_contacto(nombre)
    print("Se ha borrado correctamente")
if opcion== 3:
    print("Usted ha seleccionado la opcion 3")
    nombre=input("Introduzca el nombre del usuario a cambiar: ")
    nuevo_nombre=input("Introduzca el nombre a cambiar: ")
    nuevo_apellido=input("Introduzca el apellido a cambiar: ")
    nuevo_telefono=input("Introduzca el telefono a cambiar: ")
    nuevo_gmail=input("Introduzca el gmail a cambiar: ")
    agenda.actualizar_contacto(nombre,nuevo_nombre,nuevo_apellido,nuevo_telefono,nuevo_gmail)
if opcion== 4:
    listado=agenda.listar_contactos()
    for i in listado:
        print(i)
elif(opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4):
    print("La opcion seleccionada no es correcta")