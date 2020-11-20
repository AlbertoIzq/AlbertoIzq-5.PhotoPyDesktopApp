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
"Ratio percent",
"Ratio by width",
"Ratio by height",
"Width & height"
]
RESIZE_IMAGE_len = getListMaxLen(RESIZE_IMAGE)

REMOVE_COLOR = [
"Blue",
"Green",
"Red"
]
REMOVE_COLOR_len = getListMaxLen(REMOVE_COLOR)

EXTRACT_COLOR = [
"Blue",
"Green",
"Red"
]
EXTRACT_COLOR_len = getListMaxLen(EXTRACT_COLOR)

INVERT_COLOR = [
"All",
"Blue",
"Green",
"Red"
]
INVERT_COLOR_len = getListMaxLen(INVERT_COLOR)

APPLY_EFFECT = [
"Gray effect",
"Blur effect",
"Pencil sketch effect",
"Charcoal effect",
"Sharpen effect",
"Sepia effect",
"Emboss effect",
"Edge effect",
"Pixel effect"
]
APPLY_EFFECT_len = getListMaxLen(APPLY_EFFECT)

MAX_LISTS_len = max([CHANGE_ORIENTATION_len,
                     RESIZE_IMAGE_len,
                     REMOVE_COLOR_len,
                     EXTRACT_COLOR_len,
                     INVERT_COLOR_len,
                     APPLY_EFFECT_len])

BUTTON_NAMES = [
"Change orientation",
"Resize image",
"Remove color",
"Extract color",
"Invert color",
"Apply effect"
]
BUTTON_NAMES_len = getListMaxLen(BUTTON_NAMES)

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

        b3 = Button(window, text = "Change orientation", width = BUTTON_NAMES_len)
        b3.grid(row = 0, column = 4)

        b4 = Button(window, text = "Resize image", width = BUTTON_NAMES_len)
        b4.grid(row = 1, column = 4)

        b5 = Button(window, text = "Remove color", width = BUTTON_NAMES_len)
        b5.grid(row = 2, column = 4)

        b6 = Button(window, text = "Extract color", width = BUTTON_NAMES_len)
        b6.grid(row = 3, column = 4)

        b7 = Button(window, text = "Invert color", width = BUTTON_NAMES_len)
        b7.grid(row = 4, column = 4)

        b8 = Button(window, text = "Apply effect", width = BUTTON_NAMES_len)
        b8.grid(row = 5, column = 4)



window = Tk()
Window(window)
window.mainloop()