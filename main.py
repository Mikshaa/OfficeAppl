import os
import xlwings, xlrd
import pandas
import datetime
import threading
import urllib.request
from time import sleep


'''
def connect(mode = 'check'):
    if mode == 'check':
        host = 'http://google.com'
    elif mode == 'recheck':
        host = 'https://ya.ru/'
    else:
        return 'ModeError: parametr mode can takes "check" or "recheck"'
    try:
        urllib.request.urlopen(host)
        connected = True
    except:
        connected = False
    if not connected:
        ui.showErrorMessagebox(mode='connection')
'''

with open("C:/Users/Michael/Desktop/test/Перечень изделий ЗАО ЗЭТ.txt", encoding='utf-8') as file:
    for item in file:
        print(item.replace('\n',''))





