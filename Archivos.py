import csv
import os
from clases import Cliente, Paquete, Repartidor


# ==========================================
# GUARDAR CLIENTES
# ==========================================

def guardar_clientes(lista_clientes):

    with open("clientes.csv", "w", newline="", encoding="utf-8") as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow(["ID", "Nombre", "Direccion"])

        for cliente in lista_clientes:

            escritor.writerow([
                cliente.id,
                cliente.nombre,
                cliente.direccion
            ])


# ==========================================
# CARGAR CLIENTES
# ==========================================

def cargar_clientes():

    clientes = []

    if os.path.exists("clientes.csv"):

        with open("clientes.csv", "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)

            next(lector)

            for fila in lector:

                cliente = Cliente(
                    fila[0],
                    fila[1],
                    fila[2]
                )

                clientes.append(cliente)

    return clientes


# ==========================================
# GUARDAR PAQUETES
# ==========================================

def guardar_paquetes(lista_paquetes):

    with open("paquetes.csv", "w", newline="", encoding="utf-8") as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow([
            "Codigo",
            "Peso",
            "Destino",
            "Estado",
            "Cliente"
        ])

        for paquete in lista_paquetes:

            escritor.writerow([
                paquete.codigo,
                paquete.peso,
                paquete.destino,
                paquete.estado,
                paquete.cliente
            ])


# ==========================================
# CARGAR PAQUETES
# ==========================================

def cargar_paquetes():

    paquetes = []

    if os.path.exists("paquetes.csv"):

        with open("paquetes.csv", "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)

            next(lector)

            for fila in lector:

                paquete = Paquete(
                    fila[0],
                    float(fila[1]),
                    fila[2],
                    fila[3],
                    fila[4]
                )

                paquetes.append(paquete)

    return paquetes


# ==========================================
# GUARDAR REPARTIDORES
# ==========================================

def guardar_repartidores(lista_repartidores):

    with open("repartidores.csv", "w", newline="", encoding="utf-8") as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow([
            "Nombre",
            "Vehiculo",
            "Zona"
        ])

        for repartidor in lista_repartidores:

            escritor.writerow([
                repartidor.nombre,
                repartidor.vehiculo,
                repartidor.zona_actual
            ])


# ==========================================
# CARGAR REPARTIDORES
# ==========================================

def cargar_repartidores():

    repartidores = []

    if os.path.exists("repartidores.csv"):

        with open("repartidores.csv", "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)

            next(lector)

            for fila in lector:

                repartidor = Repartidor(
                    fila[0],
                    fila[1],
                    fila[2]
                )

                repartidores.append(repartidor)

    return repartidores


# ==========================================
# GUARDAR TODO
# ==========================================

def guardar_todo(clientes, paquetes, repartidores):

    guardar_clientes(clientes)
    guardar_paquetes(paquetes)
    guardar_repartidores(repartidores)

    print("\nDatos guardados correctamente.")


# ==========================================
# CARGAR TODO
# ==========================================

def cargar_todo():

    clientes = cargar_clientes()
    paquetes = cargar_paquetes()
    repartidores = cargar_repartidores()

    return clientes, paquetes, repartidores