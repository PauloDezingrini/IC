import os

from numpy import linspace

class TSPDReader(object):

    directory = './tsplib_generated_instances' # Atributo estático

    def __init__(self):
        self.__truckMatrix = []
        self.__droneMatrix = []
        self.__nodes = []
        self.__droneDeliveries = []

    def getTruckMatrix(self):
        return self.__truckMatrix

    def getDroneMatrix(self):
        return self.__droneMatrix

    def getNodes(self):
        return self.__nodes

    def getDroneDeliveries(self):
        return self.__droneDeliveries

    def read(self,folder):
        subFolder = TSPDReader.directory + '\\' + folder
        # print(subFolder)
        for filename in os.listdir(subFolder): # Percorre os arquivos dentro do sub-diretório
            if(folder + '.tsp' == filename): # Evitar a leitura do tsp
                continue
            fullPath = os.path.join(subFolder, filename) 
            if filename == 'nodes.csv':
                self.readNodes(fullPath)
            elif filename == 'tau.csv':
                self.readTau(fullPath,'truck')
            elif filename == 'tauprime.csv':
                self.readTau(fullPath,'drone')

    def readNodes(self,fullPath):
        file = open(fullPath, 'r')
        lines = file.readlines()
        for line in lines:
            line = stringToIntArray(line)
            self.__nodes.append([float(line[0].strip()), float(line[1].strip()), float(line[2].strip()), float(line[3].strip())])

    def readTau(self,fullPath,type):
        file = open(fullPath, 'r')
        lines = file.readlines()
        for line in lines:
            line = stringToIntArray(line)
            if type == 'truck':
                self.__truckMatrix.append(line)
            else:
                self.__droneMatrix.append(line)

# Funções auxiliares
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def stringToIntArray(str):
 str = str.strip('\n')
 str = str.split(',')
 str = remove_values_from_list(str,' ')
 str = remove_values_from_list(str,'')
 return str
