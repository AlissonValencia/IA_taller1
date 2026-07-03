import json
import os
from datetime import datetime

ARCHIVO_TAREAS = "tareas.json"


def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        return []

    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print("Error al leer el archivo de tareas. Se iniciará una lista vacía.")
        return []


def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)


def mostrar_menu():
    print("\n========== LISTA DE TAREAS ==========")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Editar tarea")
    print("5. Eliminar tarea")
    print("6. Ver estadísticas")
    print("7. Salir")
    print("=====================================")


def agregar_tarea(tareas):
    descripcion = input("Ingrese la descripción de la tarea: ").strip()

    if descripcion == "":
        print("No se puede agregar una tarea vacía.")
        return

    tarea = {
        "id": len(tareas) + 1,
        "descripcion": descripcion,
        "completada": False,
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tareas.append(tarea)
    guardar_tareas(tareas)

    print("Tarea agregada correctamente.")


def ver_tareas(tareas):
    if len(tareas) == 0:
        print("\nNo hay tareas registradas.")
        return

    print("\n" + "=" * 45)
    print("           LISTA DE TAREAS")
    print("=" * 45)

    for tarea in tareas:
        estado = "Completada" if tarea["completada"] else "Pendiente"

        print(f"\nID: {tarea['id']}")
        print(f"Descripción : {tarea['descripcion']}")
        print(f"Estado      : {estado}")
        print(f"Fecha       : {tarea['fecha_creacion']}")
        print("-" * 45)

    print("=" * 45)


def buscar_tarea_por_id(tareas, id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            return tarea

    return None


def marcar_completada(tareas):
    ver_tareas(tareas)

    if len(tareas) == 0:
        return

    try:
        id_tarea = int(input("Ingrese el ID de la tarea completada: "))
        tarea = buscar_tarea_por_id(tareas, id_tarea)

        if tarea is None:
            print("No existe una tarea con ese ID.")
        else:
            tarea["completada"] = True
            guardar_tareas(tareas)
            print("Tarea marcada como completada.")

    except ValueError:
        print("Debe ingresar un número válido.")


def editar_tarea(tareas):
    ver_tareas(tareas)

    if len(tareas) == 0:
        return

    try:
        id_tarea = int(input("Ingrese el ID de la tarea a editar: "))
        tarea = buscar_tarea_por_id(tareas, id_tarea)

        if tarea is None:
            print("No existe una tarea con ese ID.")
            return

        nueva_descripcion = input("Ingrese la nueva descripción: ").strip()

        if nueva_descripcion == "":
            print("La descripción no puede estar vacía.")
            return

        tarea["descripcion"] = nueva_descripcion
        guardar_tareas(tareas)

        print("Tarea editada correctamente.")

    except ValueError:
        print("Debe ingresar un número válido.")


def eliminar_tarea(tareas):
    ver_tareas(tareas)

    if len(tareas) == 0:
        return

    try:
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        tarea = buscar_tarea_por_id(tareas, id_tarea)

        if tarea is None:
            print("No existe una tarea con ese ID.")
            return

        tareas.remove(tarea)
        guardar_tareas(tareas)

        print("Tarea eliminada correctamente.")

    except ValueError:
        print("Debe ingresar un número válido.")


def mostrar_estadisticas(tareas):
    total = len(tareas)
    completadas = sum(1 for tarea in tareas if tarea["completada"])
    pendientes = total - completadas

    print("\n------------- ESTADÍSTICAS -------------")
    print(f"Total de tareas: {total}")
    print(f"Tareas completadas: {completadas}")
    print(f"Tareas pendientes: {pendientes}")
    print("----------------------------------------")


def ejecutar_programa():
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            editar_tarea(tareas)
        elif opcion == "5":
            eliminar_tarea(tareas)
        elif opcion == "6":
            mostrar_estadisticas(tareas)
        elif opcion == "7":
            print("Gracias por usar la Lista de Tareas.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()