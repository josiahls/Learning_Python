"""
The next couple videos with allow gui building
"""

# import everything from tkinter
# so you can use the methods directly
from tkinter import *


# we are creating a window with a frame
class Window(Frame):
    def __init__(self, master=None):
        # creates a frame
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        # sets the title of the window
        self.master.title("GUI")
        # sets properties of the window
        # pack will put those changes into the frame
        self.pack(fill=BOTH, expand=1)

        # creates a button with certain properties
        quitButton = Button(self, text='quit', command=self.client_exit)

        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()


# create a Tk object
root = Tk()
root.geometry("400x300")

# make an object Window
app = Window(root)

# run the loop on the main thread
root.mainloop()
