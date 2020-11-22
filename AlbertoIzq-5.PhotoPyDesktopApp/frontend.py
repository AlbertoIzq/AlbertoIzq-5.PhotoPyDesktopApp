from tkinter import *
from backend import *
import cv2, numpy, os

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

entry_files_len = 60
entry_parameters_len = 6

# Function limit values
PERCENTAGE_MIN = 1.0
PERCENTAGE_MAX = 1000.0
WIDTH_MULTIPLIER = 10
HEIGHT_MULTIPLIER = 10

class Window(object):
    """Class to store window object"""

    def __init__(self, window):
        self.window = window
        self.window.title("PhotoPy by Alberto Izquierdo")

        # INPUT FILE
        l1 = Label(window, text = "INPUT FILE")
        l1.grid(row = 0, column = 0, columnspan = 2)

        l2 = Label(window, text = "Path")
        l2.grid(row = 1, column = 0)

        l3 = Label(window, text = "Full file name")
        l3.grid(row = 2, column = 0)

        self.input_path = StringVar()
        self.e1 = Entry(window, textvariable = self.input_path, width = entry_files_len)
        self.e1.grid(row = 1, column = 1)

        self.input_file_name = StringVar()
        self.e2 = Entry(window, textvariable = self.input_file_name, width = entry_files_len)
        self.e2.grid(row = 2, column = 1)

        b1 = Button(window, text = "Load", command = self.load_command)
        b1.grid(row = 2, column = 2)

        # OUTPUT FILE
        l4 = Label(window, text = "OUTPUT FILE")
        l4.grid(row = 3, column = 0, columnspan = 2)

        l5 = Label(window, text = "Path")
        l5.grid(row = 4, column = 0)

        l6 = Label(window, text = "Full file name")
        l6.grid(row = 5, column = 0)

        self.output_path = StringVar()
        self.e3 = Entry(window, textvariable = self.output_path, width = entry_files_len)
        self.e3.grid(row = 4, column = 1)

        self.output_file_name = StringVar()
        self.e4 = Entry(window, textvariable = self.output_file_name, width = entry_files_len)
        self.e4.grid(row = 5, column = 1)

        b2 = Button(window, text = "Save", command = self.save_command)
        b2.grid(row = 5, column = 2)

        # MESSAGE
        self.message = StringVar()
        self.message_back_color = None
        l7 = Label(window, textvariable = self.message, background = self.message_back_color)
        l7.grid(row = 6, column = 0, columnspan = 2)

        # EDIT IMAGE
        l8 = Label(window, text = "EFFECTS")
        l8.grid(row = 0, column = 3, columnspan = 2)

        self.change_orientation = StringVar()
        self.o1 = OptionMenu(window, self.change_orientation, *CHANGE_ORIENTATION)
        self.o1.configure(width = (MAX_LISTS_len))
        self.o1.grid(row = 1, column = 3)

        self.resize_image = StringVar()
        self.o2 = OptionMenu(window, self.resize_image, *RESIZE_IMAGE)
        self.o2.configure(width = (MAX_LISTS_len))
        self.o2.grid(row = 2, column = 3)

        self.remove_color = StringVar()
        self.o3 = OptionMenu(window, self.remove_color, *REMOVE_COLOR)
        self.o3.configure(width = (MAX_LISTS_len))
        self.o3.grid(row = 3, column = 3)

        self.extract_color = StringVar()
        self.o4 = OptionMenu(window, self.extract_color, *EXTRACT_COLOR)
        self.o4.configure(width = (MAX_LISTS_len))
        self.o4.grid(row = 4, column = 3)

        self.invert_color = StringVar()
        self.o5 = OptionMenu(window, self.invert_color, *INVERT_COLOR)
        self.o5.configure(width = (MAX_LISTS_len))
        self.o5.grid(row = 5, column = 3)

        self.apply_effect = StringVar()
        self.o6 = OptionMenu(window, self.apply_effect, *APPLY_EFFECT)
        self.o6.configure(width = (MAX_LISTS_len))
        self.o6.grid(row = 6, column = 3)

        b3 = Button(window, text = "Change orientation", command = self.change_orientation_command, width = BUTTON_NAMES_len)
        b3.grid(row = 1, column = 4)

        b4 = Button(window, text = "Resize image", command = self.resize_image_orientation_command, width = BUTTON_NAMES_len)
        b4.grid(row = 2, column = 4)

        b5 = Button(window, text = "Remove color", command = self.remove_color_command, width = BUTTON_NAMES_len)
        b5.grid(row = 3, column = 4)

        b6 = Button(window, text = "Extract color", command = self.extract_color_command, width = BUTTON_NAMES_len)
        b6.grid(row = 4, column = 4)

        b7 = Button(window, text = "Invert color", command = self.invert_color_command, width = BUTTON_NAMES_len)
        b7.grid(row = 5, column = 4)

        b8 = Button(window, text = "Apply effect", command = self.apply_effect_command, width = BUTTON_NAMES_len)
        b8.grid(row = 6, column = 4)

        # PARAMETERS
        l9 = Label(window, text = "Percentage (%)")
        l9.grid(row = 1, column = 5)

        l10 = Label(window, text = "Width (pixels)")
        l10.grid(row = 2, column = 5)

        l11 = Label(window, text = "Height (pixels)")
        l11.grid(row = 3, column = 5)

        l12 = Label(window, text = "k")
        l12.grid(row = 6, column = 5)

        self.percentage = StringVar()
        self.e5 = Entry(window, textvariable = self.percentage, width = entry_parameters_len)
        self.e5.grid(row = 1, column = 6)

        self.width = StringVar()
        self.e5 = Entry(window, textvariable = self.width, width = entry_parameters_len)
        self.e5.grid(row = 2, column = 6)

        self.height = StringVar()
        self.e5 = Entry(window, textvariable = self.height, width = entry_parameters_len)
        self.e5.grid(row = 3, column = 6)

        self.k = StringVar()
        self.e5 = Entry(window, textvariable = self.k, width = entry_parameters_len)
        self.e5.grid(row = 6, column = 6)

        # Image initialization
        self.img = None

    def load_command(self):
        self.img = cv2.imread(os.path.join(self.input_path.get(), self.input_file_name.get()), cv2.IMREAD_UNCHANGED)
        if self.img is not None:
            self.message.set('Image loaded correctly!')
            #self.message_back_color = 'green'
        else:
            self.message.set('Image could not be loaded. Check path and file name (with extension)')
            #self.message_back_color = 'red'

    def save_command(self):
        if self.img is not None:
            try:
                cv2.imwrite(os.path.join(self.output_path.get(), self.output_file_name.get()), self.img)
                self.message.set('Image saved successfully!')
                #self.message_back_color = 'green'
            except:
                self.message.set('Image could not be saved. Check path and file name (with extension)')
                #self.message_back_color = 'red'
    
    def show_image(self):
        '''
        HEIGHT_PREV_MAX = 640
        WIDTH_PREV_MAX = 480

        if self.img.shape[0] > HEIGHT_PREV_MAX:
           self.height_prev = HEIGHT_PREV_MAX
           self.width_prev = int(HEIGHT_PREV_MAX * self.img.shape[1] / self.img.shape[0])
        if self.img.shape[1] > WIDTH_PREV_MAX:
           self.width_prev = WIDTH_PREV_MAX
           self.width_prev = int(WIDTH_PREV_MAX * self.img.shape[0] / self.img.shape[1])

        self.img_prev = resizeWidthHeight(img, self.width_prev, self.height_prev)
        '''
        cv2.imshow("Modified image", self.img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows() # Method to close the window

    def change_orientation_command(self):
        if self.img is not None:
            if self.change_orientation.get() == "Rotate left":
                self.img = rotateLeft(self.img)
                #self.show_image()
                self.message.set(self.change_orientation.get() + ' done!')
                #self.message_back_color = 'green'

            elif self.change_orientation.get() == "Rotate right":
                self.img = rotateRight(self.img)
                #self.show_image()
                self.message.set(self.change_orientation.get() + ' done!')
                #self.message_back_color = 'green'

            elif self.change_orientation.get() == "Flip vertical":
                self.img = flipVertical(self.img)
                #self.show_image()
                self.message.set(self.change_orientation.get() + ' done!')
                #self.message_back_color = 'green'

            elif self.change_orientation.get() == "Flip horizontal":
                self.img = flipHorizontal(self.img)
                #self.show_image()
                self.message.set(self.change_orientation.get() + ' done!')
                #self.message_back_color = 'green'


    def resize_image_orientation_command(self):
        if self.img is not None:
            if self.resize_image.get() == "Ratio percent":
                try:
                    self.percentage_value = float(self.percentage.get())
                    if self.percentage_value >= PERCENTAGE_MIN and self.percentage_value <= PERCENTAGE_MAX:
                        self.img = resizeRatioPercent(self.img, self.percentage_value)
                        self.message.set(self.resize_image.get() + ' done!')
                        #self.message_back_color = 'green'
                    else:
                        self.message.set(str(PERCENTAGE_MIN) + ' <= Percentage <= ' + str(PERCENTAGE_MAX))
                    #self.message_back_color = 'red'
                except ValueError:
                    self.message.set('Percentage must be a real number')
                    #self.message_back_color = 'red'
                if self.percentage is None:
                    self.message.set('Percentage must be a real number')
                    #self.message_back_color = 'red'

            elif self.resize_image.get() == "Ratio by width":
                try:
                    self.width_value = int(self.width.get())
                    self.WIDTH_MIN = 1
                    self.WIDTH_MAX = self.img.shape[1] * WIDTH_MULTIPLIER

                    if self.width_value >= self.WIDTH_MIN and self.width_value <= self.WIDTH_MAX:
                        self.img = resizeRatioWidth(self.img, self.width_value)
                        self.message.set(self.resize_image.get() + ' done!')
                        #self.message_back_color = 'green'
                    else:
                        self.message.set(str(self.WIDTH_MIN) + ' <= Width <= ' + str(self.WIDTH_MAX))
                    #self.message_back_color = 'red'
                except ValueError:
                    self.message.set('Width must be an integer')
                    #self.message_back_color = 'red'
                if self.percentage is None:
                    self.message.set('Width must be an integer')
                    #self.message_back_color = 'red'

            elif self.resize_image.get() == "Ratio by height":
                try:
                    self.height_value = int(self.height.get())
                    self.HEIGHT_MIN = 1
                    self.HEIGHT_MAX = self.img.shape[1] * HEIGHT_MULTIPLIER

                    if self.height_value >= self.HEIGHT_MIN and self.height_value <= self.HEIGHT_MAX:
                        self.img = resizeRatioHeight(self.img, self.height_value)
                        self.message.set(self.resize_image.get() + ' done!')
                        #self.message_back_color = 'green'
                    else:
                        self.message.set(str(self.HEIGHT_MIN) + ' <= Height <= ' + str(self.HEIGHT_MAX))
                    #self.message_back_color = 'red'
                except ValueError:
                    self.message.set('Height must be an integer')
                    #self.message_back_color = 'red'
                if self.percentage is None:
                    self.message.set('Height must be an integer')
                    #self.message_back_color = 'red'

            elif self.resize_image.get() == "Width & height":
                try:
                    self.width_value = int(self.width.get())
                    self.height_value = int(self.height.get())
                    self.WIDTH_MIN = 1
                    self.WIDTH_MAX = self.img.shape[1] * WIDTH_MULTIPLIER
                    self.HEIGHT_MIN = 1
                    self.HEIGHT_MAX = self.img.shape[1] * HEIGHT_MULTIPLIER

                    if self.width_value >= self.WIDTH_MIN and self.width_value <= self.WIDTH_MAX and self.height_value >= self.HEIGHT_MIN and self.height_value <= self.HEIGHT_MAX:
                        self.img = resizeWidthHeight(self.img, self.width_value, self.height_value)
                        self.message.set(self.resize_image.get() + ' done!')
                        #self.message_back_color = 'green'
                    else:
                        self.message.set(str(self.WIDTH_MIN) + ' <= Width <= ' + str(self.WIDTH_MAX) + '. ' +
                                         str(self.HEIGHT_MIN) + ' <= Height <= ' + str(self.HEIGHT_MAX))
                    #self.message_back_color = 'red'
                except ValueError:
                    self.message.set('Wdith and height must be integers')
                    #self.message_back_color = 'red'
                if self.percentage is None:
                    self.message.set('Wdith and height must be integers')
                    #self.message_back_color = 'red'

    def remove_color_command(self):
        if self.img is not None:
            if self.remove_color.get() == "Blue":
                self.img = removeBlueChannel(self.img)
                self.message.set('Remove ' + self.remove_color.get() + ' done!')
                #self.message_back_color = 'green'

            elif self.remove_color.get() == "Green":
                self.img = removeGreenChannel(self.img)
                self.message.set('Remove ' + self.remove_color.get() + ' done!')
                #self.message_back_color = 'green'

            elif self.remove_color.get() == "Red":
                self.img = removeRedChannel(self.img)
                self.message.set('Remove ' + self.remove_color.get() + ' done!')
                #self.message_back_color = 'green'

    def extract_color_command(self):
        if self.img is not None:
            if self.extract_color.get() == "Blue":
                self.img = extractBlueChannel(self.img)
                self.message.set('Extract ' + self.extract_color.get() + ' done!')
                #self.message_back_color = 'green'

            elif self.extract_color.get() == "Green":
                self.img = extractGreenChannel(self.img)
                self.message.set('Extract ' + self.extract_color.get() + ' done!')
                #self.message_back_color = 'green'

            elif self.extract_color.get() == "Red":
                self.img = extractRedChannel(self.img)
                self.message.set('Extract ' + self.extract_color.get() + ' done!')
                #self.message_back_color = 'green'

    def invert_color_command(self):
        pass

    def apply_effect_command(self):
        pass

window = Tk()
Window(window)
window.mainloop()