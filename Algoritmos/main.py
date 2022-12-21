from TSPDReader import TSPDReader
from Solver import Solver

import os

print(os.curdir)
folders = os.listdir(TSPDReader.directory)
for folder in folders: # Percorre os diretórios da pasta raiz
    reader = TSPDReader()

    reader.read(folder)

    solver = Solver(reader.getTruckMatrix(), reader.getDroneMatrix(), reader.getNodes(), 1, 1, 20)


    solver.HVMP(1)

    # solver.localSearchSwap()
    # solver.localSearchInsertion()
    # solver.localSearch2OPT()
    solver.RVND()
    # solver.printSolution()
    solver.split2()
    solver.createRepresentation()
    solver.calculateTime()

    # print(solver.getTotalTime())

    # solver.printSolution()

    break