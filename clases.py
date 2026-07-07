
# -------------------------------
# Clase Cliente
# -------------------------------

class Cliente:

    def __init__(self, id_cliente, nombre, direccion):
        self.id = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.historial_pedidos = []


# -------------------------------
# Clase Paquete
# -------------------------------

class Paquete:

    def __init__(self, codigo, peso, destino, estado, cliente):
        self.codigo = codigo
        self.peso = peso
        self.destino = destino
        self.estado = estado
        self.cliente = cliente


# -------------------------------
# Clase Repartidor
# -------------------------------

class Repartidor:

    def __init__(self, nombre, vehiculo, zona_actual):
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.zona_actual = zona_actual
        self.paquetes_asignados = []


# ==========================================
# Funciones para mostrar información
# ==========================================

def mostrar_cliente(cliente):
    print("\n------ CLIENTE ------")
    print("ID:", cliente.id)
    print("Nombre:", cliente.nombre)
    print("Dirección:", cliente.direccion)

    if len(cliente.historial_pedidos) == 0:
        print("Historial: Sin pedidos")
    else:
        print("Historial:", cliente.historial_pedidos)


def mostrar_paquete(paquete):
    print("\n------ PAQUETE ------")
    print("Código:", paquete.codigo)
    print("Peso:", paquete.peso, "kg")
    print("Destino:", paquete.destino)
    print("Estado:", paquete.estado)
    print("Cliente:", paquete.cliente)


def mostrar_repartidor(repartidor):
    print("\n------ REPARTIDOR ------")
    print("Nombre:", repartidor.nombre)
    print("Vehículo:", repartidor.vehiculo)
    print("Zona actual:", repartidor.zona_actual)

    if len(repartidor.paquetes_asignados) == 0:
        print("Paquetes asignados: Ninguno")
    else:
        print("Paquetes asignados:", repartidor.paquetes_asignados)
    
    