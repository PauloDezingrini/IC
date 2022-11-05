class Solver(object):
    def __init__(self, truckMatrix, droneMatrix, nodes):
        self.__truckMatrix = truckMatrix
        self.__droneMatrix = droneMatrix
        self.__nodes = nodes
        self.__solution = []

    # Heurísitca do vizinho mais próximo com escolhas aleatórias. Utilizar m = 1 para a versão tradicional.
    def HVMP(self, m):
        
        pass