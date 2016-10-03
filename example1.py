#!/usr/bin/env python3
import tkinter as Tk
import time,threading

class Model():
    def __init__(self):
        self.total=1
        self.list=[]
class View():
    def __init__(self,master):
        self.entry_text=Tk.StringVar()
        self.frame=Tk.Frame(master)
        self.frame.pack(side=Tk.LEFT,fill=Tk.BOTH,expand=1)
        self.e=Tk.Entry(self.frame,textvariable=self.entry_text)
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
        self.stopBut=Tk.Button(self.frame,text='Stop')
        self.stopBut.pack(side='top',fill=Tk.BOTH)
def run_thread(func,args=[]):
    t=threading.Thread(target=func,args=args)
    t.start()
class Controller():
    def __init__(self):
        self.root=Tk.Tk()
        self.model=Model()
        self.view=View(self.root)
        self.running_state=None
        self.view.sidepanel.addBut.bind('<Button>',self.add)
        self.view.sidepanel.minusBut.bind('<Button>',self.minus)
        self.view.sidepanel.stopBut.bind('<Button>',self.stop)
    def run(self):
        self.root.title('Tkinter MVC example')
        self.refresh_total()
        self.root.deiconify()
        self.root.mainloop()
    def refresh_total(self):
        self.view.e.delete(0,Tk.END)
        self.view.e.insert(0,self.model.total)
    def get_entry(self):
        return self.view.entry_text.get()
    def add(self,event):
        self.view.sidepanel.addBut.unbind('<Button>')
        self.view.sidepanel.addBut.config(state=Tk.DISABLED)
        self.view.sidepanel.minusBut.config(state=Tk.NORMAL)
        self.view.sidepanel.minusBut.bind('<Button>',self.minus)
        self.running_state='add'
        try:
            self.model.total=int(self.get_entry())
        except:
            pass
        def f():
            while self.running_state=='add':
                self.model.total+=1
                self.refresh_total()
                time.sleep(0.1)
        run_thread(f) 
    def minus(self,event):
        self.view.sidepanel.minusBut.unbind('<Button>')
        self.view.sidepanel.minusBut.config(state=Tk.DISABLED)
        self.view.sidepanel.addBut.config(state=Tk.NORMAL)
        self.view.sidepanel.addBut.bind('<Button>',self.add)
        self.running_state='minus'
        try:
            self.model.total=int(self.get_entry())
        except:
            pass
        def f():
            while self.running_state=='minus':
                self.model.total-=1
                self.refresh_total()
                time.sleep(0.1)
        run_thread(f)
    def stop(self,event):
        self.running_state=None
        self.view.sidepanel.addBut.bind('<Button>',self.add)
        self.view.sidepanel.minusBut.bind('<Button>',self.minus)
        self.view.sidepanel.stopBut.bind('<Button>',self.stop)
        self.view.sidepanel.addBut.config(state=Tk.NORMAL)
        self.view.sidepanel.minusBut.config(state=Tk.NORMAL)
if __name__=='__main__':
    c=Controller()
    c.run()
