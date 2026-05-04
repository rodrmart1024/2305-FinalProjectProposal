import sys
import random
from PySide6 import QtWidgets, QtCore, QtGui

CANVAS_WIDTH = 960
CANVAS_HEIGHT = 1000

def build_grid(vertical_lines, horizontal_lines):
    '''Function that Creates a list of random x y positions within a range'''
    vert_x_locations = []
    horiz_y_locations = []

    paint_x_range = range(50, CANVAS_WIDTH - 50)
    random_x_lines = random.sample(paint_x_range, vertical_lines)
    for xlines in sorted(random_x_lines):
        vert_x_locations.append(xlines)

    paint_y_range = range(50, CANVAS_HEIGHT - 50)
    random_y_lines = random.sample(paint_y_range, horizontal_lines)
    for ylines in sorted(random_y_lines):
        horiz_y_locations.append(ylines)

    return vert_x_locations, horiz_y_locations

def build_colored_squares(square_amount, saturation):
    pass

def build_signature(name, typeface, fontsize):
    pass


class MondrianUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mondrian Inspired Generator")
        self.resize(1920, 1000)
        window_layout = QtWidgets.QHBoxLayout(self)

        left_panel = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(left_panel)
        window_layout.addWidget(left_panel)

        self.canvas = MondrianCanvas()
        window_layout.addWidget(self.canvas)

        self.grid_lines_ui()
        self.square_amount_ui()
        self.signature_ui()
        self.saturation_ui()
        self.generate_button_ui()

    def grid_lines_ui(self):
        '''Creates the UI for Vertical and Horizontal Lines'''
        grid_group = QtWidgets.QGroupBox('Grid Lines:')
        grid_ui_layout = QtWidgets.QFormLayout()
        grid_ui_layout.setSpacing(10)

        self.vertical_input = QtWidgets.QSpinBox()
        self.vertical_input.setMinimum(1)
        self.vertical_input.setMaximum(5)
        grid_ui_layout.addRow("Amount of Vertical Lines: ", 
                           self.vertical_input)
        
        self.horizontal_input = QtWidgets.QSpinBox()
        self.horizontal_input.setMinimum(1)
        self.horizontal_input.setMaximum(5)
        grid_ui_layout.addRow("Amount of Horizontal Lines: ", 
                           self.horizontal_input)
        
        grid_group.setLayout(grid_ui_layout)
        self.layout.addWidget(grid_group)

    def square_amount_ui(self):
        '''Creates the UI for amount of Squares'''
        square_group = QtWidgets.QGroupBox('Squares:')
        square_ui_layout = QtWidgets.QFormLayout()
        square_ui_layout.setSpacing(10)

        self.square_amount_input = QtWidgets.QSpinBox()
        self.square_amount_input.setMinimum(3)
        self.square_amount_input.setMaximum(40)
        square_ui_layout.addRow("Amount of Squares: ", 
                           self.square_amount_input)

        square_group.setLayout(square_ui_layout)
        self.layout.addWidget(square_group)

    def signature_ui(self):
        """Creates the Signature UI comprised of TypeFace, FontSize, Name"""
        signature_group = QtWidgets.QGroupBox('Signature:')
        signature_ui_layout = QtWidgets.QFormLayout()
        signature_ui_layout.setSpacing(10)
        # CHECK TO MAKE SURE METHOD WORKS AND ALSO GNERATE ARTWORK SETUP
        self.username_input = QtWidgets.QLineEdit()
        signature_ui_layout.addRow("Name: ", self.username_input) 

        self.typeface_input = QtWidgets.QComboBox()
        self.typeface_input.addItems(["Arial", "Times New Roman"])
        signature_ui_layout.addRow("Select a Typeface: ", self.typeface_input) 

        self.fontsize_input = QtWidgets.QComboBox()
        self.fontsize_input.addItems(["10", "12", "16", "20"])
        signature_ui_layout.addRow("Select a Font Size: ", self.fontsize_input) 

        signature_group.setLayout(signature_ui_layout)
        self.layout.addWidget(signature_group)

    def saturation_ui(self):
        """Creates the Saturation UI where users can select percentages"""
        saturation_group = QtWidgets.QGroupBox('Saturation:')
        saturation_ui_layout = QtWidgets.QFormLayout()
        saturation_ui_layout.setSpacing(10)

        self.saturation_percent_input = QtWidgets.QComboBox()
        self.saturation_percent_input.addItems(["10", "20", "40", "60", "80"])
        saturation_ui_layout.addRow("Select a Percentage: ",
                                     self.saturation_percent_input) 

        saturation_group.setLayout(saturation_ui_layout)
        self.layout.addWidget(saturation_group)

    def generate_button_ui(self):
        """Creates a UI Button"""
        gen_button_layout = QtWidgets.QHBoxLayout()
        generate_btn = QtWidgets.QPushButton('Create Painting')
        generate_btn.clicked.connect(self.generate_artwork)

        gen_button_layout.addWidget(generate_btn)
        self.layout.addLayout(gen_button_layout)

    def generate_artwork(self):
        """Collects from input UI and sends to Build"""
        vertical_lines = self.vertical_input.value()
        horizontal_lines = self.horizontal_input.value()
        square_amount = self.square_amount_input.value()

        name = self.username_input.text()
        typeface = self.typeface_input.currentText()
        fontsize = int(self.fontsize_input.currentText())
        saturation = int(self.saturation_percent_input.currentText())

        vert_x_locations, horiz_y_locations = build_grid(vertical_lines,
                                                         horizontal_lines)
        self.canvas.vert_x_locations = vert_x_locations
        self.canvas.horiz_y_locations = horiz_y_locations
        self.canvas.update()
        
        build_colored_squares(square_amount, saturation)
        build_signature(name, typeface, fontsize)


class MondrianCanvas(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(960, 1000)
        self.vert_x_locations = []
        self.horiz_y_locations = []

    def paintEvent(self, event):
        paint = QtGui.QPainter(self)
        paint.fillRect(self.rect(), QtGui.QColor('white'))
        thickpen = QtGui.QPen(QtGui.QColor('black'))
        thickpen.setWidth(8)
        paint.setPen(thickpen)

        for xpositions in self.vert_x_locations:
            paint.drawLine(xpositions, 0, xpositions, CANVAS_HEIGHT)

        for ypositions in self.horiz_y_locations:
            paint.drawLine(0, ypositions, CANVAS_WIDTH, ypositions)
        
        paint.end()

def show_ui():
    app = QtWidgets.QApplication(sys.argv)
    window = MondrianUI()
    window.show()
    app.exec()

if __name__ == "__main__":
    show_ui()

# Using Pyside6 for the Widgets and Painter tools
# Create the Grid
# Create the Squares by trying the usage of cells
# Create the Signitures
