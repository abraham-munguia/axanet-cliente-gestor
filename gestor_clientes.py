import json
import os

clientes = {}

# Función para agregar un nuevo cliente
def agregar_cliente(nombre, servicio):
    archivo = f"{nombre}.json"
    if nombre in clientes:
        print("Cliente recurrente. Agregando nuevo servicio.")
        actualizar_cliente(nombre, servicio)
    else:
        print("Cliente nuevo. Creando archivo.")
        cliente_data = {"nombre": nombre, "servicios": [servicio]}
        with open(archivo, "w") as file:
            json.dump(cliente_data, file)
        clientes[nombre] = archivo

# Función para actualizar información de un cliente recurrente
def actualizar_cliente(nombre, nuevo_servicio):
    archivo = clientes.get(nombre)
    if archivo and os.path.exists(archivo):
        with open(archivo, "r+") as file:
            cliente_data = json.load(file)
            cliente_data["servicios"].append(nuevo_servicio)
            file.seek(0)
            json.dump(cliente_data, file)
            file.truncate()
        print(f"Servicio agregado para {nombre}.")
    else:
        print("Cliente no encontrado.")

# Función para consultar un cliente
def consultar_cliente(nombre):
    archivo = clientes.get(nombre)
    if archivo and os.path.exists(archivo):
        with open(archivo, "r") as file:
            cliente_data = json.load(file)
            print(cliente_data)
    else:
        print("Cliente no encontrado.")

# Función para borrar un cliente
def borrar_cliente(nombre):
    archivo = clientes.pop(nombre, None)
    if archivo and os.path.exists(archivo):
        os.remove(archivo)
        print(f"Cliente {nombre} borrado.")
    else:
        print("Cliente no encontrado.")

# Ejemplo de uso
agregar_cliente("Juan Perez", "Mantenimiento anual")
consultar_cliente("Juan Perez")
actualizar_cliente("Juan Perez", "Reparación urgente")
consultar_cliente("Juan Perez")
borrar_cliente("Juan Perez")
