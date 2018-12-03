from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        c = Canvas(master, width=200,height=100)
        c.pack()

        line1 = c.create_line(0,0,200,100)
        line2 = c.create_line(0,100,200,0, fill='red', dash=(4,4))
        rectangle1 = c.create_rectangle(50,25,150,75, fill='blue')

        #c.coords(rectangle1, 0,25,50,75)
        #c.itemconfig(line2,fill='yellow')
        #c.delete(line1)
        #c.delete(ALL)
        #c.lift(line1)
        c.lower(rectangle1)
        c.move(rectangle1,0,25)
if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
