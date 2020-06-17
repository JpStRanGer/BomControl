#!/usr/bin/env python

import sys
from os import path
from datetime import datetime, timedelta
from win32com.client import Dispatch
from tkinter import Tk
import tkinter
import tkinter.messagebox as mbox
import PIL

def printer():
    im = PIL.Image.open("test.png")
    labelText.SetField('TEXT', now.strftime('%Y/%m/%d'))
    labelText.SetField('GRAPHIC', im)
    
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
    #print('OBJECT NAMES: ',labelText.GetObjectNames())
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