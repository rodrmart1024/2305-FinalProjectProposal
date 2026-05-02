import sys
from PySide6 import QtWidgets, QtCore, QtGui


class MondrianInspiredArtBuild():

    def build_grid(self, vertical_lines, horizontal_lines):
        pass

    def build_colored_squares(self):
        pass

    def build_signature(self):
        pass


class MondrianInspiredArtUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mondrian Inspired Generator")
        self. resize(1920, 1080)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.grid_lines_ui()
        self.square_amount_ui()
        self.color_scheme_ui()
        self.signiture_ui()
        self.generate_button_ui()


    def grid_lines_ui(self):
        '''Creates the UI for Vertical and Horizontal Lines'''
        grid_group = QtWidgets.QGroupBox('Painting Lines:')
        grid_ui_layout = QtWidgets.QFormLayout()
        grid_ui_layout.setSpacing(10)

        self.vertical_input = QtWidgets.QSpinBox()
        self.vertical_input.setMinimum(2)
        self.vertical_input.setMaximum(10)
        grid_ui_layout.addRow("Amount of Vertical Lines: ", 
                           self.vertical_input)
        
        self.horizontal_input = QtWidgets.QSpinBox()
        self.horizontal_input.setMinimum(2)
        self.horizontal_input.setMaximum(6)
        grid_ui_layout.addRow("Amount of Horizontal Lines: ", 
                           self.horizontal_input)
        
        grid_group.setLayout(grid_ui_layout)
        self.layout.addWidget(grid_group)

    def square_amount_ui(self):
        '''Creates the UI for amount of Squares'''
        square_group = QtWidgets.QGroupBox('Painting Squares:')
        square_ui_layout = QtWidgets.QFormLayout()
        square_ui_layout.setSpacing(10)

        self.square_amount_input = QtWidgets.QSpinBox()
        self.square_amount_input.setMinimum(3)
        self.square_amount_input.setMaximum(40)
        square_ui_layout.addRow("Amount of Squares: ", 
                           self.square_amount_input)

        square_group.setLayout(square_ui_layout)
        self.layout.addWidget(square_group)

    def color_scheme_ui(self):
        pass

    def signiture_ui(self):
        pass

    def generate_button_ui(self):
        pass

    def generate_artwork(self):
        pass


def show_ui():
    app = QtWidgets.QApplication(sys.argv)
    window = MondrianInspiredArtUI()
    window.show()
    app.exec()

if __name__ == "__main__":
    show_ui()

# Using Pyside6 for the Widgets and Painter tools
# Create the Window
# Create the UI for all features
# Create the Grid
# Create the Squares by trying the usage of cells
# Create the Color Schemes
# Create the Signitures
