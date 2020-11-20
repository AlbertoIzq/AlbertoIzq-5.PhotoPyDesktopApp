from tkinter import *

def getListMaxLen(lst):
    ln = 0
    for text in lst:
        if len(text) > ln:
            ln = len(text)
    return ln

CHANGE_ORIENTATION = [
"Rotate left",
"Rotate right",
"Flip vertical",
"Flip horizontal"
]
CHANGE_ORIENTATION_len = getListMaxLen(CHANGE_ORIENTATION)

RESIZE_IMAGE = [
"Resize ratio percent",
"Resize ratio by width",
"Resize ratio by height",
"Resize width & height"
]
RESIZE_IMAGE_len = getListMaxLen(RESIZE_IMAGE)

REMOVE_COLOR = [
"Remove blue",
"Remove green",
"Remove red"
]
REMOVE_COLOR_len = getListMaxLen(REMOVE_COLOR)

EXTRACT_COLOR = [
"Extract blue",
"Extract green",
"Extract red"
]
EXTRACT_COLOR_len = getListMaxLen(EXTRACT_COLOR)

INVERT_COLOR = [
"Invert all",
"Invert blue",
"Invert green",
"Invert red"
]
INVERT_COLOR_len = getListMaxLen(INVERT_COLOR)

APPLY_EFFECT = [
"Apply gray effect",
"Apply blur effect",
"Apply pencil sketch effect",
"Apply charcoal effect",
"Apply sharpen effect",
"Apply sepia effect",
"Apply emboss effect",
"Apply edge effect",
"Apply pixel effect"
]
APPLY_EFFECT_len = getListMaxLen(APPLY_EFFECT)

MAX_LISTS_len = max([CHANGE_ORIENTATION_len,
                     RESIZE_IMAGE_len,
                     REMOVE_COLOR_len,
                     EXTRACT_COLOR_len,
                     INVERT_COLOR_len,
                     APPLY_EFFECT_len])
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

        # Edit image
        self.change_orientation = StringVar()
        self.o1 = OptionMenu(window, self.change_orientation, *CHANGE_ORIENTATION)
        self.o1.configure(width = (MAX_LISTS_len))
        self.o1.grid(row = 0, column = 3)

        self.resize_image = StringVar()
        self.o2 = OptionMenu(window, self.resize_image, *RESIZE_IMAGE)
        self.o2.configure(width = (MAX_LISTS_len))
        self.o2.grid(row = 1, column = 3)

        self.remove_color = StringVar()
        self.o3 = OptionMenu(window, self.remove_color, *REMOVE_COLOR)
        self.o3.configure(width = (MAX_LISTS_len))
        self.o3.grid(row = 2, column = 3)

        self.extract_color = StringVar()
        self.o4 = OptionMenu(window, self.extract_color, *EXTRACT_COLOR)
        self.o4.configure(width = (MAX_LISTS_len))
        self.o4.grid(row = 3, column = 3)

        self.invert_color = StringVar()
        self.o5 = OptionMenu(window, self.invert_color, *INVERT_COLOR)
        self.o5.configure(width = (MAX_LISTS_len))
        self.o5.grid(row = 4, column = 3)

        self.apply_effect = StringVar()
        self.o6 = OptionMenu(window, self.apply_effect, *APPLY_EFFECT)
        self.o6.configure(width = (MAX_LISTS_len))
        self.o6.grid(row = 5, column = 3)

window = Tk()
Window(window)
window.mainloop()