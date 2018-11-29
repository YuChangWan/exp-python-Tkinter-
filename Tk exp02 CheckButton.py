from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        #All of tk methods are usable with 'root' as 'Tk()'
        self.var = IntVar()
        c = Checkbutton(
            frame, text="check button",
            variable=self.var,
            command=self.printVar,
            )
        
        c.pack()
 
        self.var2 =StringVar()
        self.var2.set("checked")
        c2 = Checkbutton(
            frame,
            textvariable=self.var2,
            variable=self.var2,
            onvalue="checked",
            offvalue="not checked",
            command=self.printVar2
            )
        c2.pack()
        
        #The checkbutton with an integer variable has been non-checked as a default.
        #But the checkbutton with a string variable has been checked as a default.
        #So to prevent confusion, deselect all button, primarily. 
        c.deselect()
        c2.deselect()


        #deselect() or select() methods are don't make an event, so don't causes the command to be executed.
        #but the invoke() method makes a event, so command is executed.
        c2.invoke()
        c2.invoke()
        
    def printVar(self):
        print("variable is", self.var.get())
        
    def printVar2(self):
        print("checkbutton is", self.var2.get())

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
