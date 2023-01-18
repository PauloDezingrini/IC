from TSPDReader import TSPDReader
from Solver import Solver
from openpyxl import Workbook

import os
import time


sheetName = input("Digite o nome do arquivo com os resultados: ")
firstLine = ("Instância", "Tempo", "Tempo de execução")
sheet = Workbook()
sheet1 = sheet.active

sheet1.append(firstLine)

# print(os.curdir)
folders = os.listdir(TSPDReader.directory)
for folder in folders: # Percorre os diretórios da pasta raiz
    reader = TSPDReader()

    reader.read(folder)

    solver = Solver(reader.getTruckMatrix(), reader.getDroneMatrix(), reader.getNodes(), 1, 1, 20)

    startTime = time.time()
    result = solver.HVMP(1)
    endTime = time.time()

    sheet1.append((folder, result, endTime - startTime))
    sheet.save(sheetName + '.xlsx')
