from tkinter import *

CATEGORY = [
"",
"Restaurant",
"Bar",
"Supermarket",
"Transport",
"Other"
]

class Window(object):
    """Class to store window object"""

    def __init__(self, window):
        self.window = window
        self.window.title("PhotoPy by Alberto Izquierdo")

        # Input file
        l1 = Label(window, text = "Input file")
        l1.grid(row = 0, column = 0, columnspan = 2)

        l2 = Label(window, text = "Path")
        l2.grid(row = 1, column = 0)

        l3 = Label(window, text = "Full file name")
        l3.grid(row = 2, column = 0)

        self.input_path = StringVar()
        self.e1 = Entry(window, textvariable = self.input_path, width = 60)
        self.e1.grid(row = 1, column = 1)

        self.input_file_name = StringVar()
        self.e2 = Entry(window, textvariable = self.input_file_name, width = 60)
        self.e2.grid(row = 2, column = 1)

        b1 = Button(window, text = "Load")
        b1.grid(row = 2, column = 2)

        # Output file
        l4 = Label(window, text = "Output file")
        l4.grid(row = 3, column = 0, columnspan = 2)

        l5 = Label(window, text = "Path")
        l5.grid(row = 4, column = 0)

        l6 = Label(window, text = "Full file name")
        l6.grid(row = 5, column = 0)

        self.output_path = StringVar()
        self.e3 = Entry(window, textvariable = self.output_path, width = 60)
        self.e3.grid(row = 4, column = 1)

        self.output_file_name = StringVar()
        self.e4 = Entry(window, textvariable = self.output_file_name, width = 60)
        self.e4.grid(row = 5, column = 1)

        b2 = Button(window, text = "Save")
        b2.grid(row = 5, column = 2)

window = Tk()
Window(window)
window.mainloop()