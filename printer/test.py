#!/usr/bin/env python

import sys
from os import path
from datetime import datetime, timedelta
from win32com.client import Dispatch
from tkinter import Tk
import tkinter.messagebox as mbox

curdir = None

#curdir = path.dirname(sys.executable)
#print('curdir: sys.executable: ',curdir)

curdir = path.dirname(path.abspath(__file__))
print('curdir: path.abspath: ',curdir)

#mylabel = path.join(curdir,'my.label')
mylabel = path.join(curdir,'logo.label')
print('mylabel: ',mylabel)
#window = Tk()
#window.wm_withdraw()


#print('TRY...')
#now = datetime.now()
#print('now: ',now)
#next = now + timedelta(30)
#print('next: ',next)

labelCom = Dispatch('Dymo.DymoAddIn')
labelText = Dispatch('Dymo.DymoLabels')
isOpen = labelCom.Open(mylabel)
selectPrinter = 'DYMO LabelWriter 450'
labelCom.SelectPrinter(selectPrinter)

#labelText.SetField('TEXT1', now.strftime('%Y/%m/%d'))
#labelText.SetField('TEXT2', next.strftime('%Y/%m/%d'))

labelCom.StartPrintJob()
labelCom.Print(1,False)
labelCom.EndPrintJob()
