from clases import Cliente, Paquete, Repartidor

# ==========================================
# DICCIONARIO PARA BUSCAR PAQUETES
# ==========================================

diccionario_paquetes = {}


# ==========================================
# CLIENTES
# ==========================================

def agregar_cliente(lista_clientes):

    print("\n===== REGISTRAR CLIENTE =====")

    id_cliente = input("ID: ")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")

    cliente = Cliente(id_cliente, nombre, direccion)

    lista_clientes.append(cliente)

    print("\nCliente registrado correctamente.")


def mostrar_clientes(lista_clientes):

    print("\n===== LISTA DE CLIENTES =====")

    if len(lista_clientes) == 0:
        print("No hay clientes registrados.")
        return

    for cliente in lista_clientes:

        print("--------------------------")
        print("ID:", cliente.id)
        print("Nombre:", cliente.nombre)
        print("Dirección:", cliente.direccion)

        if len(cliente.historial_pedidos) == 0:
            print("Pedidos: Ninguno")
        else:
            print("Pedidos:", cliente.historial_pedidos)


def buscar_cliente(lista_clientes):

    id_cliente = input("\nIngrese el ID del cliente: ")

    for cliente in lista_clientes:

        if cliente.id == id_cliente:

            print("\nCliente encontrado")

            print("Nombre:", cliente.nombre)
            print("Dirección:", cliente.direccion)

            return cliente

    print("\nCliente no encontrado.")
    return None


def eliminar_cliente(lista_clientes):

    id_cliente = input("\nID del cliente a eliminar: ")

    for cliente in lista_clientes:

        if cliente.id == id_cliente:

            lista_clientes.remove(cliente)

            print("\nCliente eliminado correctamente.")
            return

    print("\nCliente no encontrado.")


# ==========================================
# PAQUETES
# ==========================================

def registrar_paquete(lista_paquetes, lista_clientes):

    print("\n===== REGISTRAR PAQUETE =====")

    codigo = input("Código: ")

    peso = float(input("Peso (kg): "))

    destino = input("Destino: ")

    cliente = input("Nombre del cliente: ")

    paquete = Paquete(
        codigo,
        peso,
        destino,
        "Pendiente",
        cliente
    )

    lista_paquetes.append(paquete)

    diccionario_paquetes[codigo] = paquete

    for persona in lista_clientes:

        if persona.nombre == cliente:

            persona.historial_pedidos.append(codigo)

    print("\nPaquete registrado correctamente.")


def mostrar_paquetes(lista_paquetes):

    print("\n===== PAQUETES =====")

    if len(lista_paquetes) == 0:

        print("No hay paquetes.")

        return

    for paquete in lista_paquetes:

        print("--------------------------")
        print("Código:", paquete.codigo)
        print("Peso:", paquete.peso, "kg")
        print("Destino:", paquete.destino)
        print("Estado:", paquete.estado)
        print("Cliente:", paquete.cliente)


def cambiar_estado(lista_paquetes):

    codigo = input("\nCódigo del paquete: ")

    for paquete in lista_paquetes:

        if paquete.codigo == codigo:

            print("\n1. Pendiente")
            print("2. En ruta")
            print("3. Entregado")
            print("4. Cancelado")

            opcion = input("Nuevo estado: ")

            if opcion == "1":
                paquete.estado = "Pendiente"

            elif opcion == "2":
                paquete.estado = "En ruta"

            elif opcion == "3":
                paquete.estado = "Entregado"

            elif opcion == "4":
                paquete.estado = "Cancelado"

            else:
                print("\nOpción inválida.")
                return

            print("\nEstado actualizado.")
            return

    print("\nPaquete no encontrado.")


# ==========================================
# BUSCAR PAQUETE
# ==========================================

def buscar_paquete():

    codigo = input("\nCódigo del paquete: ")

    if codigo in diccionario_paquetes:

        paquete = diccionario_paquetes[codigo]

        print("\n===== PAQUETE =====")
        print("Código:", paquete.codigo)
        print("Cliente:", paquete.cliente)
        print("Destino:", paquete.destino)
        print("Peso:", paquete.peso)
        print("Estado:", paquete.estado)

    else:

        print("\nNo existe ese paquete.")


# ==========================================
# REPARTIDORES
# ==========================================

def registrar_repartidor(lista_repartidores):

    print("\n===== REGISTRAR REPARTIDOR =====")

    nombre = input("Nombre: ")

    vehiculo = input("Vehículo: ")

    zona = input("Zona actual: ")

    repartidor = Repartidor(
        nombre,
        vehiculo,
        zona
    )

    lista_repartidores.append(repartidor)

    print("\nRepartidor registrado correctamente.")


def mostrar_repartidores(lista_repartidores):

    print("\n===== REPARTIDORES =====")

    if len(lista_repartidores) == 0:

        print("No hay repartidores.")

        return

    for repartidor in lista_repartidores:

        print("--------------------------")
        print("Nombre:", repartidor.nombre)
        print("Vehículo:", repartidor.vehiculo)
        print("Zona:", repartidor.zona_actual)

        if len(repartidor.paquetes_asignados) == 0:
            print("Paquetes: Ninguno")
        else:
            print("Paquetes:", repartidor.paquetes_asignados)
            
# ==========================================
# ASIGNAR PAQUETE A REPARTIDOR
# ==========================================

def asignar_paquete(lista_paquetes, lista_repartidores):

    print("\n===== ASIGNAR PAQUETE =====")

    codigo = input("Código del paquete: ")

    paquete_encontrado = None

    for paquete in lista_paquetes:

        if paquete.codigo == codigo:
            paquete_encontrado = paquete
            break

    if paquete_encontrado is None:

        print("\nEl paquete no existe.")
        return

    print("\nRepartidores disponibles:")

    for i in range(len(lista_repartidores)):

        print(i + 1, "-", lista_repartidores[i].nombre)

    opcion = int(input("\nSeleccione un repartidor: "))

    if opcion < 1 or opcion > len(lista_repartidores):

        print("Opción inválida.")
        return

    repartidor = lista_repartidores[opcion - 1]

    repartidor.paquetes_asignados.append(paquete_encontrado.codigo)

    paquete_encontrado.estado = "En ruta"

    print("\nPaquete asignado correctamente.")


# ==========================================
# REPORTE POR PESO
# ==========================================

def reporte_por_peso(lista_paquetes):

    print("\n===== PAQUETES ORDENADOS POR PESO =====")

    paquetes = sorted(
        lista_paquetes,
        key=lambda paquete: paquete.peso
    )

    for paquete in paquetes:

        print("----------------------")
        print("Código:", paquete.codigo)
        print("Peso:", paquete.peso, "kg")
        print("Destino:", paquete.destino)
        print("Estado:", paquete.estado)


# ==========================================
# REPORTE POR DESTINO
# ==========================================

def reporte_por_destino(lista_paquetes):

    print("\n===== PAQUETES ORDENADOS POR DESTINO =====")

    paquetes = sorted(
        lista_paquetes,
        key=lambda paquete: paquete.destino
    )

    for paquete in paquetes:

        print("----------------------")
        print("Código:", paquete.codigo)
        print("Destino:", paquete.destino)
        print("Cliente:", paquete.cliente)


# ==========================================
# MOSTRAR PAQUETES DE UN REPARTIDOR
# ==========================================

def paquetes_repartidor(lista_repartidores):

    nombre = input("\nNombre del repartidor: ")

    for repartidor in lista_repartidores:

        if repartidor.nombre.lower() == nombre.lower():

            print("\n===== PAQUETES ASIGNADOS =====")

            if len(repartidor.paquetes_asignados) == 0:

                print("No tiene paquetes asignados.")

            else:

                for paquete in repartidor.paquetes_asignados:

                    print(paquete)

            return

    print("\nRepartidor no encontrado.")


# ==========================================
# ASIGNACIÓN INTELIGENTE
# ==========================================

def asignacion_inteligente(lista_paquetes, lista_repartidores):

    print("\n===== ASIGNACIÓN INTELIGENTE =====")

    codigo = input("Código del paquete: ")

    paquete = None

    for p in lista_paquetes:

        if p.codigo == codigo:

            paquete = p
            break

    if paquete is None:

        print("Paquete no encontrado.")
        return

    if len(lista_repartidores) == 0:

        print("No existen repartidores.")
        return

    mejor = lista_repartidores[0]

    for repartidor in lista_repartidores:

        if len(repartidor.paquetes_asignados) < len(mejor.paquetes_asignados):

            mejor = repartidor

    mejor.paquetes_asignados.append(paquete.codigo)

    paquete.estado = "En ruta"

    print("\nEl sistema asignó automáticamente el paquete a:")

    print(mejor.nombre)

    print("Zona:", mejor.zona_actual)

    print("Vehículo:", mejor.vehiculo)


# ==========================================
# BUSCAR RUTA EN EL GRAFO
# ==========================================

def buscar_ruta_ciudad(ciudad):

    print("\n===== BUSCAR RUTA =====")

    origen = input("Origen: ")

    destino = input("Destino: ")

    ruta = ciudad.buscar_ruta(origen, destino)

    if ruta is not None:

        distancia = ciudad.calcular_distancia(ruta)

        print("\nDistancia total:", distancia, "km")