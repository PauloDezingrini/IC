from TSPDReader import TSPDReader
from Solver import Solver

import os

print(os.curdir)
folders = os.listdir(TSPDReader.directory)
for folder in folders: # Percorre os diretórios da pasta raiz
    reader = TSPDReader()

    reader.read(folder)

    solver = Solver(reader.getTruckMatrix(), reader.getDroneMatrix(), reader.getNodes(), 1, 1, 100)

    solver.HVMP(1)

    # solver.printSolution()
    # solver.localSearchSwap()
    # solver.localSearchInsertion()
    # solver.localSearch2OPT()
    # solver.RVND()
    solver.split2()
    # solver.printSolution()

    break