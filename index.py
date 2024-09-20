
import pymongo
from pymongo import MongoClient

# Conectar a la base de datos
client = MongoClient('mongodb://localhost:27017/')
db = client['tareas_db']  # Nombre de la base de datos
tareas_collection = db['tareas']  # Nombre de la colección

def mostrar_tareas():
    tareas = list(tareas_collection.find())  # Convertir el cursor a una lista
    if len(tareas) == 0:  # Verificar la longitud de la lista
        print("No hay tareas.")
    else:
        for tarea in tareas:
            estado = "✔️" if tarea['completada'] else "❌"
            print(f"{tarea['_id']}: {tarea['descripcion']} [{estado}]")

def agregar_tarea(descripcion):
    tarea = {"descripcion": descripcion, "completada": False}
    tareas_collection.insert_one(tarea)
    print("Tarea agregada.")

def eliminar_tarea(tarea_id):
    result = tareas_collection.delete_one({"_id": tarea_id})
    if result.deleted_count > 0:
        print("Tarea eliminada.")
    else:
        print("Tarea no encontrada.")

def marcar_completada(tarea_id):
    result = tareas_collection.update_one({"_id": tarea_id}, {"$set": {"completada": True}})
    if result.modified_count > 0:
        print("Tarea marcada como completada.")
    else:
        print("Tarea no encontrada o ya completada.")

def main():
    while True:
        print("\nLista de Tareas")
        print("1. Mostrar Tareas")
        print("2. Agregar Tarea")
        print("3. Eliminar Tarea")
        print("4. Marcar Tarea como Completada")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_tareas()
        elif opcion == '2':
            descripcion = input("Descripción de la tarea: ")
            agregar_tarea(descripcion)
        elif opcion == '3':
            tarea_id = input("ID de la tarea a eliminar: ")
            eliminar_tarea(tarea_id)
        elif opcion == '4':
            tarea_id = input("ID de la tarea a marcar como completada: ")
            marcar_completada(tarea_id)
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
