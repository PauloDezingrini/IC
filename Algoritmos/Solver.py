import heapq
from random import randint

class Solver(object):
    def __init__(self, truckMatrix, droneMatrix, nodes):
        self.__truckMatrix = truckMatrix
        self.__droneMatrix = droneMatrix
        self.__nodes = nodes
        self.__solution = []
        self.__time = 0

    # Funções auxiliares
    def printSolution(self):
        print("Time: ", self.__time)
        print(len(self.__solution))
        print(self.__solution)

    def getTime(self, _from, _to):
        return float(self.__truckMatrix[self.__solution[_from]][self.__solution[_to]])


    def calcDist(self):
        self.__time = 0;
        for i in range(len(self.__solution) - 1):
            # print(self.__solution[i], " - ", self.__solution[i+1], " | ",self.__truckMatrix[self.__solution[i]][self.__solution[i + 1]]);
            self.__time += float(self.__truckMatrix[self.__solution[i]][self.__solution[i + 1]])

    def closestPoints(self, num_points):
        pq = []
        lastInsert = self.__solution[-1]
        size = len(self.__nodes) - 1
        for j in range(size):
            if j not in self.__solution and j != lastInsert:
                heapq.heappush(pq, (self.__truckMatrix[lastInsert][j], j))
        closest = heapq.nsmallest(num_points, pq)
        return closest

    def adjustTimeSwap(self, i, j):
        self.__time = self.__time - self.getTime(i-1,i) - self.getTime(i, i+1) - self.getTime(j,j+1)
        self.__time = self.__time + self.getTime(i-1,j) + self.getTime(j, i+1) + self.getTime(i, j+1)
        if(i != j - 1):
            self.__time = self.__time - self.getTime(j-1,j)
            self.__time = self.__time + self.getTime(j-1,i)
        print("TESTE:" , self.__time)

    # Heurísitca do vizinho mais próximo com escolhas aleatórias. Utilizar m = 1 para a versão tradicional.
    def HVMP(self, m):
        self.__solution.append(0) # Adiciona o depósito a solução.
        count = 1
        while(count < len(self.__nodes) - 1):
            closest = self.closestPoints(m); # Recupera os m pontos mais próximos
            m1 = min(len(closest), m) # Trata a questão de não existir m pontos que não estão na solução
            index = randint(0, m1 - 1) # Define o indice do ponto que será inserido
            lastInsert = self.__solution[-1] # Recupera o último ponto a ser inserido
            # print(self.__solution[-1], " - ", closest[index][1], " | ",closest[index][0]);
            self.__solution.append(closest[index][1]) # Adiciona na solução
            self.__time += float(closest[index][0]) # Acrescenta a distância
            count += 1
        lastInsert = self.__solution[-1]
        self.__solution.append(0) # Adiciona o depósito, para fechar o ciclo
        self.__time += float(self.__truckMatrix[lastInsert][0])
        self.__time = round(self.__time,2)
        # print(self.__time)
        # self.calcDist()
        # print(self.__time)

    def localSearchSwap(self):
        better = True
        while better:
            better = False
            lessTime = self.__time
            lessSol = self.__solution.copy()
            for i in range(1,len(self.__solution) - 1):
                for j in range(i + 1, len(self.__solution) - 1):
                    self.__solution[i], self.__solution[j] = self.__solution[j] , self.__solution[i]
                    self.calcDist()
                    if(self.__time < lessTime):
                        better = True
                        lessTime = self.__time
                        lessSol = self.__solution.copy()
                    else:
                        self.__solution[i], self.__solution[j] = self.__solution[j] , self.__solution[i]
                        self.calcDist()
            self.__time = lessTime
            self.__solution = lessSol

    def localSearchInsertion(self):
        better = True
        while better:
            better = False
            lessTime = self.__time
            lessSol = self.__solution.copy()
            for i in range(1, len(self.__solution) - 1):
                for j in range(1, len(self.__solution) - 1):
                    sol = self.__solution.copy()
                    valueToInsert = self.__solution[i]
                    self.__solution.pop(i)
                    self.__solution.insert(j, valueToInsert)
                    self.calcDist()
                    if(self.__time < lessTime):
                        better = True
                        lessTime = self.__time
                        lessSol = self.__solution.copy()
                    self.__solution = sol
            self.__time = lessTime
            self.__solution = lessSol

    def localSearch2OPT(self):
        better = True
        while better:
            better = False
            lessTime = self.__time
            lessSol = self.__solution.copy()
            for i in range(1,len(self.__solution)-1):
                for j in range(len(self.__solution) - 2, -1, -1):
                    if j > i:
                        sol = self.__solution.copy()
                        self.__solution[i:j+1] = reversed(self.__solution[i:j+1])
                        self.calcDist()
                        if(self.__time < lessTime):
                            better = True
                            lessTime = self.__time
                            lessSol = self.__solution.copy()
                        self.__solution = sol
                    else:
                        break
            self.__time = lessTime
            self.__solution = lessSol

    def RVND(self):
        localSearchs = randomizeLocalSearchs()
        k = 1
        while k <= 3:
            oldTime = self.__time
            chosenLS = localSearchs.pop()
            if chosenLS == 1:
                self.localSearchSwap()
            elif chosenLS == 2:
                self.localSearchInsertion()
            elif chosenLS == 3:
                self.localSearch2OPT()
            if(self.__time < oldTime):
                k = 1
                localSearchs = randomizeLocalSearchs()
            else:
                k+=1


    def split1(self):
        arcs = []
        T = []
        for i in range(len(self.__solution) - 1):
            arcs.append((self.__solution[i], self.__solution[i+1], self.getTime(i,i+1)))

        for i in range(len(self.__solution) - 2):
            for j in range(len(self.__solution) - 1):
                if(j >= i + 2):
                    minValue = -1
                    miIndex = -1
                    for k in range(len(self.__solution)):
                        if(i < k and k < j):
                            if(True):# ?
                                # cost ?
                                if(cost < minValue):
                                    minValue = cost;
                                    minIndex = k
                    arcs.append((self.__solution[i], self.__solution[j], minValue))
                    if minIndex not in T:
                        T.append((self.__solution[i],self.__solution[minIndex], self.__solution[j], minValue))

        V = []
        P = []  
        # Como inicializar / O que é V
        V = [-1 for i in range(len(self.__solution) - 1)]
        P = [-1 for i in range(len(self.__solution) - 1)] 
        V[0] = 0
        P[0] = 0
        for i in self.__solution[0]:
            if(i != 0):
                for arc in arcs:
                    if(V[arc[1]] == -1 or V[arc[1]] > V[arc[0]] + arc[2]):
                        V[arc[1]] = V[arc[0]] + arc[2]
                        P[arc[1]] = i



def randomizeLocalSearchs():
    localSearchs = []
    availableValues = [1, 2, 3]
    while len(availableValues) != 0:
        newInsert = randint(0, len(availableValues) - 1)
        localSearchs.append(availableValues.pop(newInsert))

    return localSearchs