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
        # self.color_scheme_ui()
        self.signature_ui()
        self.saturation_ui()
        self.generate_button_ui()


    def grid_lines_ui(self):
        '''Creates the UI for Vertical and Horizontal Lines'''
        grid_group = QtWidgets.QGroupBox('Grid Lines:')
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

    # def color_scheme_ui(self):
    #     """Creates Checkboxes for Color Schemes"""
    #     color_scheme_group = QtWidgets.QGroupBox('Color Scheme:')
    #     color_scheme_layout = QtWidgets.QGridLayout()
    #     self.color_scheme_checkboxes = {}

    #     schemes = ['Monochromatic', 'Analogous', 'Complementary']
    #     for value, scheme_type in enumerate(schemes):
    #         checkbox = QtWidgets.QCheckBox(scheme_type)
    #         checkbox.stateChanged.connect(self.color_scheme_limiter)

    #         self.color_scheme_checkboxes[scheme_type] = checkbox
    #         color_scheme_layout.addWidget(checkbox, value // 3, value % 3)

    #     color_scheme_group.setLayout(color_scheme_layout)
    #     self.layout.addWidget(color_scheme_group)

    # def color_scheme_limiter(self):
    #     """UI Function that Limits Scheme to One"""
    #     selected = []

    #     for scheme_type in self.color_scheme_checkboxes:
    #         if self.color_scheme_checkboxes[scheme_type].isChecked():
    #             selected.append(scheme_type)
        
    #     if len(selected) == 1:
    #         for scheme_type in self.color_scheme_checkboxes:
    #             if scheme_type not in selected:
    #                 self.color_scheme_checkboxes[scheme_type].setEnabled(False)
    #     else:
    #         for scheme_type in self.color_scheme_checkboxes:
    #             self.color_scheme_checkboxes[scheme_type].setEnabled(True)

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
        pass

    def generate_artwork(self):
        """Collects from input UI and sends to Build"""
        name = self.username_input.text()
        typeface = self.typeface_input.currentText()
        fontsize = self.fontsize_input.currentText()


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
