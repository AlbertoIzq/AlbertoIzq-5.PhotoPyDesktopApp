from tkinter import *

class Window(object):
    """Class to store window object"""

    def __init__(self, window):
        self.window = window
        self.window.title("PhotoPy by Alberto Izquierdo")

        # buttons, labels and shite

window = Tk()
Window(window)
window.mainloop()