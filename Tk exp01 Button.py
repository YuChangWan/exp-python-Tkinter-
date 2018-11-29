from tkinter import *

class App:

    def __init__(self, master):
        frame = Frame(master)
        #frame.pack_propagate(0)
        frame.pack()

        self.button = Button(
            frame, text="OK", command=self.callback
            )
        self.button.pack(side='left')
        self.button.config(relief=SUNKEN)
        
        self.button_disabled = Button(
            frame, text="XX", state=DISABLED
            )
        self.button_disabled.pack(side='left')
        
        self.button_long = Button(
            
            frame, text="anchor\nand\njustify", anchor=SW, justify=RIGHT,
            height=5, width=10
            )
        self.button_long.pack(side='left')

    def callback(self):
            print("click!")

    

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
    
