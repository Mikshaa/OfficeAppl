import os
import xlwings, xlrd, openpyxl
import pandas as pe
import datetime
import threading
import urllib.request
from time import sleep
from graphics import*

def create_file():
    if f'ВП {curDeviceCode}.xls' in devicesList:
        peData = pe.DataFrame(pe.read_excel(f'{inputFilesPath}/ВП {curDeviceCode}.xls'), columns=['Наименование ВП', 'Количество', 'Примечание'])
    elif f'ВП {curDeviceCode}.xlsx' in devicesList:
        peData = pe.DataFrame(pe.read_excel(f'{inputFilesPath}/ВП {curDeviceCode}.xlsx'), columns=['Наименование ВП', 'Количество', 'Примечание'])
    wb = openpyxl.Workbook()
    ws = wb.active
    for row in range(len(peData)):
        if str(peData['Примечание'][row]) == 'nan':
            ws[f'A{row+1}'] = str(peData['Наименование ВП'][row])
            #if float(peData['Количество'][row]) != 0.0:
            ws[f'B{row+1}'] = float(peData['Количество'][row]) * int(curAmount)
            #else:
            #pass #Вызов ошибки на ноль в ашблоне
        else:
            ws[f'A{row+1}'] = str(peData['Наименование ВП'][row])
            ws[f'B{row+1}'] = pasteVarsInFormula(str(peData['Примечание'][row]))
    finalSavePath = f'{outputFilesPath}/{curDeviceCode}_{datetime.datetime.now().strftime("%Y-%m-%d")}.xlsx'
    wb.save(finalSavePath)
    print(1)

    row_final = 1
    app = xlwings.App(visible=False)
    wb = app.books.open(finalSavePath)
    ws = wb.sheets[0]
    for row in range(1,len(peData)+1):
        if ws.range(f'b{row}').value == 0:
            continue
        else:
            ws.range(f'a{row_final}').value = ws.range(f'a{row}').value
            ws.range(f'b{row_final}').value = ws.range(f'b{row}').value
            row_final+=1
    wb.save()
    wb.close()
    app.quit()


