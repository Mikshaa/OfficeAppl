import os
import xlwings, xlrd
import pandas
import datetime
import threading
import urllib.request
from time import sleep

ghb

def connect(mode = 'check'):
    if mode == 'check':
        host = 'http://google.com'
    elif mode == 'recheck':
        host = 'https://ya.ru/'
    else:
        return 'ModeError: parametr mode can takes "check" or "recheck"'
    try:
        urllib.request.urlopen(host)
        return True
        connected = True
    except:
        return False
        connected = False
    if not connected:
        print('окно')

higi

if connect():
    print('connected')
elif connect(mode='recheck'):
    print('connected')
else:
    print('NO')


