from PySide6 import QtWidgets, QtCore, QtGui
class MondrianInspiredArtBuild():

    def build_grid(veritcal_lines, horizaontal_lines):
        pass

    def build_colored_squares():
        pass

    def build_signiture():
        pass


class MondrianInspiredArtUI():

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mondrian Inspired Generator")
        self. resize(1080, 1920)
        self.layout = QtWidgets.QVBoxL3ayout(self)

        self.grid_lines_ui()
        self.square_amount_ui()
        self.color_scheme_ui()
        self.signiture_ui()
        self.generate_button_ui()


    def grid_lines_ui(self):
        grid_ui_layout = QtWidgets.QVBoxLayout()
        grid_ui_layout.setSpacing(10)

        self.vertical_input = QSpinBox()
        self.vertial_input.setMinimum(2)
        self.vertical_input.setMaximum(10)
        self.vertical_input.valueChanged.connect(self)
        grid_ui_layout.addRow("Select Amount of Horizontal Lines: ", 
                           self.horizontal_input)
        
        self.horizontal_input = QSpinBox()
        self.horizontal_input.setMinimum(2)
        self.horizontal_input.setMaximum(6)
        self.horizontal_input.valueChanged.connect(self)
        grid_ui_layout.addRow("Select Amount of Horizontal Lines: ", 
                           self.horizontal_input)

    def square_amount_ui(self):
        pass

    def color_scheme_ui(self):
        pass

    def signiture_ui(self):
        pass

    def generate_button_ui(self):
        pass

    def generate_artwork(self):
        pass


def show_ui():
    app = QtWidgets.QApplication()
    MondrianInspiredArtUI().show()
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
