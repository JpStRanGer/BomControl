import tkinter as Tkinter
import tkinter.messagebox as tkMessageBox


class printer:
    def __init__(self):
        self.streng = "tekststreng"
        print("printer er laget")
        self.boolVar = True
    def Print(self):
        print("printer tekst")
        self.boolVar = False


printer1 = printer()

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")


#B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
B = Tkinter.Button(top, text ="Hello", command = printer1.Print)

B.pack()
top.mainloop()