# ==========================================
# main.py
# Proyecto: Logística de Entregas Inteligentes
# ==========================================

from Funciones import *
from Archivos import *
from Grafo import Grafo

# ==========================================
# CARGAR DATOS
# ==========================================

clientes, paquetes, repartidores = cargar_todo()

# ==========================================
# CREAR EL GRAFO DE LA CIUDAD
# ==========================================

ciudad = Grafo()

ciudad.conectar_zonas("Centro", "Avenida 1", 5)
ciudad.conectar_zonas("Centro", "Mercado", 8)
ciudad.conectar_zonas("Avenida 1", "Zona Norte", 4)
ciudad.conectar_zonas("Mercado", "Hospital", 3)
ciudad.conectar_zonas("Hospital", "Zona Norte", 2)
ciudad.conectar_zonas("Hospital", "Zona Sur", 6)
ciudad.conectar_zonas("Zona Norte", "Parque", 5)
ciudad.conectar_zonas("Parque", "Zona Sur", 4)

# ==========================================
# MENÚ PRINCIPAL
# ==========================================

while True:

    print("\n====================================")
    print(" LOGÍSTICA DE ENTREGAS INTELIGENTES ")
    print("====================================")
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Buscar cliente")
    print("4. Eliminar cliente")
    print("5. Registrar paquete")
    print("6. Mostrar paquetes")
    print("7. Cambiar estado de paquete")
    print("8. Buscar paquete")
    print("9. Registrar repartidor")
    print("10. Mostrar repartidores")
    print("11. Asignar paquete")
    print("12. Asignación inteligente")
    print("13. Mostrar paquetes de repartidor")
    print("14. Mostrar mapa de la ciudad")
    print("15. Buscar ruta")
    print("16. Reporte por peso")
    print("17. Reporte por destino")
    print("18. Guardar datos")
    print("19. Salir")

    opcion = input("\nSeleccione una opción: ")

    
  
    if opcion == "1":
        agregar_cliente(clientes)

    elif opcion == "2":
        mostrar_clientes(clientes)

    elif opcion == "3":
        buscar_cliente(clientes)

    elif opcion == "4":
        eliminar_cliente(clientes)

    elif opcion == "5":
        registrar_paquete(paquetes, clientes)

    elif opcion == "6":
        mostrar_paquetes(paquetes)

    elif opcion == "7":
        cambiar_estado(paquetes)

    elif opcion == "8":
        buscar_paquete()

    elif opcion == "9":
        registrar_repartidor(repartidores)

    elif opcion == "10":
        mostrar_repartidores(repartidores)

    elif opcion == "11":
        asignar_paquete(paquetes, repartidores)

    elif opcion == "12":
        asignacion_inteligente(paquetes, repartidores)

    elif opcion == "13":
        paquetes_repartidor(repartidores)

    elif opcion == "14":
        ciudad.mostrar_grafo()

    elif opcion == "15":
        buscar_ruta_ciudad(ciudad)

    elif opcion == "16":
        reporte_por_peso(paquetes)

    elif opcion == "17":
        reporte_por_destino(paquetes)

    elif opcion == "18":

        guardar_todo(
            clientes,
            paquetes,
            repartidores
        )

    elif opcion == "19":

        print("Gracias por utilizar el sistema.")

        break

    else:
        print("\nOpción inválida.")