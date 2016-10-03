#!/usr/bin/python3
import tkinter as Tk

class Model():
    def __init__(self):
        self.total=1
class View():
    def __init__(self,master):
        self.frame=Tk.Frame(master)
        self.frame.pack(side=Tk.LEFT,fill=Tk.BOTH,expand=1)
        self.e=Tk.Entry(self.frame)
        self.e.pack(side=Tk.TOP,fill=Tk.BOTH,expand=1)
        self.sidepanel=SidePanel(master)
class SidePanel():
    def __init__(self,master):
        self.frame=Tk.Frame(master)
        self.frame.pack(side=Tk.LEFT,fill=Tk.BOTH,expand=1)
        self.addBut=Tk.Button(self.frame,text='Add')
        self.addBut.pack(side='top',fill=Tk.BOTH)
        self.minusBut=Tk.Button(self.frame,text='Minus')
        self.minusBut.pack(side='top',fill=Tk.BOTH)
class Controller():
    def __init__(self):
        self.root=Tk.Tk()
        self.model=Model()
        self.view=View(self.root)
        self.view.sidepanel.addBut.bind('<Button>',self.add)
        self.view.sidepanel.minusBut.bind('<Button>',self.minus)
    def run(self):
        self.root.title('Tkinter MVC example')
        self.refresh_total()
        self.root.deiconify()
        self.root.mainloop()
    def refresh_total(self):
        self.view.e.delete(0,Tk.END)
        self.view.e.insert(0,self.model.total)
    def add(self,event):
        #print(dir(event))
        print(event.state)
        self.model.total+=1
        self.view.sidepanel.addBut.config(state=Tk.DISABLED)
        print(event.state)
        self.refresh_total()
    def minus(self,event):
        self.model.total-=1
        self.refresh_total()
if __name__=='__main__':
    c=Controller()
    c.run()
