from PySide6 import QtWidgets, QtCore, QtGui

class MondrianInspiredArtBuild():

    def build_grid():
        pass

    def build_colored_squares():
        pass

    def build_signiture():
        pass


class MondrianInspiredArtUI():

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mondrian Inspired Generator")
        self. resize(400, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.grid_lines_ui()
        self.square_amount_ui()
        self.color_scheme_ui()
        self.signiture_ui()
        self.generate_button_ui()


    def grid_lines_ui():
        pass

    def square_amount_ui():
        pass

    def color_scheme_ui():
        pass

    def signiture_ui():
        pass

    def generate_button_ui():
        pass

    def generate_artwork():
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
