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

def checkInputFilesPath(path):
    if os.access(path, mode=os.F_OK):
        if os.access(path, mode=os.X_OK):
            return True
        else:
            ui.
    else:
        print(4)

checkInputFilesPath('C:/Users/Michael/Desktop/test')





