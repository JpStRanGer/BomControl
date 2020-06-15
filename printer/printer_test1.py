#!/usr/bin/env python

import sys
from os import path
from datetime import datetime, timedelta
from win32com.client import Dispatch
from tkinter import Tk
import tkinter
import tkinter.messagebox as mbox

def printer():
    labelText.SetField('TEXT1', now.strftime('%Y/%m/%d'))
    labelText.SetField('TEXT2', next.strftime('%Y/%m/%d'))
    
    labelCom.StartPrintJob()
    labelCom.Print(1,False)
    labelCom.EndPrintJob()

curdir = None
print('curdir: ',curdir)
if getattr(sys, 'frozen', False):
    # frozen
    curdir = path.dirname(sys.executable)
    print('curdir: sys.executable: ',curdir)
else:
	# unfrozen
    curdir = path.dirname(path.abspath(__file__))
    print('curdir: path.abspath: ',curdir)

#mylabel = path.join(curdir,'my.label')
mylabel = path.join(curdir,'logo.label')
print('mylabel: ',mylabel)

if not path.isfile(mylabel):
	print('PyDymoLabel','Template file my.label does not exist')
	mbox.showinfo('PyDymoLabel','Template file my.label does not exist')
	sys.exit(1)

try:
    print('TRY...')
    now = datetime.now()
    print('now: ',now)
    next = now + timedelta(30)
    print('next: ',next)
    
    labelCom = Dispatch('Dymo.DymoAddIn')
    labelText = Dispatch('Dymo.DymoLabels')
    isOpen = labelCom.Open(mylabel)
    selectPrinter = 'DYMO LabelWriter 450'
    labelCom.SelectPrinter(selectPrinter)
    

except:
    mbox.showinfo('PyDymoLabel','An error occurred during printing.')
    sys.exit(1)


window = Tk()
B = tkinter.Button(window, text ="PRINT", command = printer)
B.pack()
window.mainloop()

#mbox.showinfo('PyDymoLabel','Label printed!')
#sys.exit(0)