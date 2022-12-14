    def split1(self):
        arcs = []
        T = []
        for i in range(len(self.__solution) - 1):
            arcs.append((self.__solution[i], self.__solution[i+1], self.getTime(i,i+1)))

        for i in range(len(self.__solution) - 2):
            for j in range(len(self.__solution) - 1):
                if(j >= i + 2):
                    minValue = -1
                    minIndex = -1
                    for k in range(len(self.__solution)):
                        if(i < k and k < j):
                            if((i,k,j) in self.__droneDeliveries):
                                cost = max(self.__truckMatrix[i][j], self.__droneMatrix[i][k] + self.__droneMatrix[k][j]) + self.__st + self.__sr
                                if(minValue == -1 or cost < minValue):
                                    minValue = cost;
                                    minIndex = k
                    if(minValue != -1):                
                        arcs.append((self.__solution[i], self.__solution[j], minValue))
                    t = (self.__solution[i],self.__solution[minIndex], self.__solution[j], minValue)
                    if t not in T and minIndex != -1:
                        T.append(t)

        # print(arcs)
        print(T)
        V = []
        P = []  
        # Como inicializar / O que é V
        V = [-1 for i in range(len(self.__solution) - 1)]
        P = [-1 for i in range(len(self.__solution) - 1)] 
        V[0] = 0
        P[0] = 0
        for i in self.__solution:
            if(i != 0):
                for arc in arcs:
                    if(i == arc[1]):
                        if(V[arc[1]] == -1 or V[arc[1]] > V[arc[0]] + arc[2]):
                            V[arc[1]] = V[arc[0]] + arc[2]
                            P[arc[1]] = arc[0]
        # print(P)
        # print(V)
        return P, V, T
    def split2(self):
        
        pass