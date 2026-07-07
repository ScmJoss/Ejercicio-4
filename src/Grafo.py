class Grafo:

    def __init__(self):

        # Diccionario donde se guardan los nodos
        self.grafo = {}


    # --------------------------------------
    # Agregar una zona (nodo)
    # --------------------------------------
    def agregar_zona(self, zona):

        if zona not in self.grafo:
            self.grafo[zona] = []


    # --------------------------------------
    # Conectar dos zonas
    # --------------------------------------
    def conectar_zonas(self, origen, destino, distancia):

        self.agregar_zona(origen)
        self.agregar_zona(destino)

        self.grafo[origen].append((destino, distancia))
        self.grafo[destino].append((origen, distancia))


    # --------------------------------------
    # Mostrar el grafo
    # --------------------------------------
    def mostrar_grafo(self):

        print("\n===== MAPA DE LA CIUDAD =====")

        for zona in self.grafo:

            print("\n", zona)

            for vecino in self.grafo[zona]:

                print("   ->", vecino[0], "-", vecino[1], "km")


    # --------------------------------------
    # Buscar ruta usando DFS Recursivo
    # --------------------------------------
    def buscar_ruta(self, origen, destino):

        visitados = []

        camino = self.__dfs(origen, destino, visitados)

        if camino is None:

            print("\nNo existe una ruta.")
            return None

        else:

            print("\nRuta encontrada:")

            for lugar in camino:
                print(lugar)

            return camino


    # --------------------------------------
    # Función recursiva DFS
    # --------------------------------------
    def __dfs(self, actual, destino, visitados):

        visitados.append(actual)

        if actual == destino:
            return [actual]

        for vecino, distancia in self.grafo.get(actual, []):

            if vecino not in visitados:

                camino = self.__dfs(
                    vecino,
                    destino,
                    visitados
                )

                if camino:

                    return [actual] + camino

        return None


    # --------------------------------------
    # Calcular distancia de una ruta
    # --------------------------------------
    def calcular_distancia(self, ruta):

        distancia_total = 0

        for i in range(len(ruta)-1):

            origen = ruta[i]
            destino = ruta[i+1]

            for vecino, distancia in self.grafo[origen]:

                if vecino == destino:

                    distancia_total += distancia

        return distancia_total