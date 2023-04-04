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
    if f'ВП {curDeviceCode}.xlsx' in devicesList:
        peData = pe.DataFrame(pe.read_excel(f'{inputFilesPath}/ВП {curDeviceCode}.xlsx'), columns=['Наименование ВП', 'Количество', 'Примечание'])
    wb = openpyxl.Workbook()
    ws = wb.active
    for row in range(len(peData)):
        if str(peData['Примечание'][row]) == 'nan':
            ws[f'A{row+1}'] = str(peData['Наименование ВП'][row])
            ws[f'B{row+1}'] = float(peData['Количество'][row]) * int(set_count)
        else:
            ws[f'A{row+1}'] = str(peData['Наименование ВП'][row])
            ws[f'B{row+1}'] = convert_formula(str(peData['Примечание'][row]), device_code, set_count)
    final_save_path = f'{file_save_path}/{device_code}_{datetime.datetime.now().strftime("%Y-%m-%d")}.xlsx'
    wb.save(final_save_path)

    row_final = 1
    app = xlwings.App(visible=False)
    wb = app.books.open(final_save_path)
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


