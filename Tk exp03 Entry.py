from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()


        self.var = StringVar()
        e = Entry(master, textvariable=self.var, show="*")
        e.pack()

        e.focus_set()

        
        b = Button(master, text='get', width=10, command=self.callback)
        
        #command with lambda trick, so the method can have some parameters
        b2 = Button(master, text='get', width=10, command=lambda:self.callback())
        b3 = Button(master, text='get', width=10, command=lambda:self.callback2(self.var))
        b4 = Button(master, text='get', width=10, command=lambda:self.callback2(e))
        
        #if callback just print someting, defining callback isn't necessary
        b5 = Button(master, text='get', width=10, command=lambda:print(e.get()))
        b.pack()
        b2.pack()
        b3.pack()
        b4.pack()
        b5.pack()
             
        
    def callback(self):
        print(self.var.get())

    def callback2(self, x):
        print(x.get())

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
