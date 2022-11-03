import os

from numpy import linspace

class TSPDReader(object):

    directory = 'tsplib_generated_instances' # Atribuo estático

    def __init__(self):
        self.__truckMatrix = []
        self.__droneMatrix = []
        self.__nodes = []

    def read(self):
        folders = os.listdir(TSPDReader.directory)
        for folder in folders: # Percorre os diretórios da pasta raiz
            subFolder = TSPDReader.directory + '\\' + folder
            for filename in os.listdir(subFolder): # Percorre os arquivos dentro do sub-diretório
                if(folder + '.tsp' == filename): # Evitar a leitura do tsp
                    continue
                fullPath = os.path.join(subFolder, filename) 
                if filename == 'nodes.csv':
                    self.readNodes(fullPath)
                elif filename == 'tau.csv':
                    self.readTau(fullPath,'truck')
                    return
                elif filename == 'tauprime.csv':
                    self.readTau(fullPath,'drone')

    def readNodes(self,fullPath):
        file = open(fullPath, 'r')
        lines = file.readlines()
        for line in lines:
            line = stringToIntArray(line)
            self.__nodes.append([line[1].strip(), line[2].strip(),line[3].strip()])

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
