import sys
import random
from PySide6 import QtWidgets, QtCore, QtGui

CANVAS_WIDTH = 980
CANVAS_HEIGHT = 980

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MondrianUI()
    window.show()
    app.exec()

def build_grid(vertical_lines, horizontal_lines):
    '''Builds a list of random x y positions for lines within a range'''
    vert_x_locations = []
    horiz_y_locations = []

    paint_x_range = range(50, CANVAS_WIDTH)
    random_x_lines = random.sample(paint_x_range, vertical_lines)
    for xlines in sorted(random_x_lines):
        vert_x_locations.append(xlines)

    paint_y_range = range(50, CANVAS_HEIGHT)
    random_y_lines = random.sample(paint_y_range, horizontal_lines)
    for ylines in sorted(random_y_lines):
        horiz_y_locations.append(ylines)

    return vert_x_locations, horiz_y_locations

def build_rectangles(vert_x_locations, horiz_y_locations,rectangle_amount,
                          saturation):
    '''Call Builder to create cells and random colors'''
    xaxis_boundaries = [0] + vert_x_locations + [CANVAS_WIDTH]
    yaxis_boundaries = [0] + horiz_y_locations + [CANVAS_HEIGHT]
    all_rectangles, rectangle_amount = build_rectangle_cells(xaxis_boundaries,
                                                             yaxis_boundaries,
                                                             rectangle_amount)

    random_colors = build_rectangle_colors(saturation)
    selected_rectangles = random.sample(all_rectangles, rectangle_amount)
    
    return selected_rectangles, random_colors, all_rectangles

def build_rectangle_cells(xaxis_boundaries, yaxis_boundaries, rectangle_amount):
    '''Builds the cells from the x and y boundaries'''
    all_rectangles = []

    for x in range(len(xaxis_boundaries) - 1):
        for y in range(len(yaxis_boundaries) - 1):
            rectangle_x = xaxis_boundaries[x]
            rectangle_y = yaxis_boundaries[y]
            rectangle_width = xaxis_boundaries[x + 1] - xaxis_boundaries[x]
            rectangle_height = yaxis_boundaries[y + 1] - yaxis_boundaries[y]

            all_rectangles.append((rectangle_x, rectangle_y, rectangle_width,
                                    rectangle_height))
    
    if rectangle_amount > len(all_rectangles):
        rectangle_amount = len(all_rectangles)
    
    return all_rectangles, rectangle_amount

def build_rectangle_colors(saturation):
    '''Builds the three random HSV colors for the rectangles'''
    hsv_saturation = int((saturation/100) * 255)
    random_colors = []

    for num in range(3):
        hue = random.randint(0, 359)
        color = QtGui.QColor.fromHsv(hue, hsv_saturation, 220)
        random_colors.append(color)
    
    random_colors.append(QtGui.QColor('black'))

    return random_colors

def build_signature(paint, name, typeface, fontsize):
    '''Builds the signature in the bottom right usng margins'''
    signature_font = QtGui.QFont(typeface, fontsize)
    paint.setFont(signature_font)
    paint.setPen(QtGui.QPen(QtGui.QColor('black')))

    bottom_margin = 100
    right_margin = 200
    paint.drawText(CANVAS_WIDTH - right_margin, CANVAS_HEIGHT - bottom_margin,
                   name)


class MondrianUI(QtWidgets.QDialog):

    def __init__(self):
        '''Creates the Split Screen View of the Window'''
        super().__init__()
        self.setWindowTitle("Mondrian Inspired Generator")
        self.resize(1920, 980)
        window_layout = QtWidgets.QHBoxLayout(self)

        left_panel = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(left_panel)
        window_layout.addWidget(left_panel)

        self.canvas = MondrianCanvas()
        window_layout.addWidget(self.canvas)

        self.title_ui()
        self.grid_lines_ui()
        self.rectangle_amount_ui()
        self.signature_ui()
        self.saturation_ui()
        self.generate_button_ui()

    def title_ui(self):
        '''A Title UI for the Window'''
        title_group = QtWidgets.QGroupBox()
        title_layout = QtWidgets.QFormLayout()
        title_layout.setSpacing(10)

        title = QtWidgets.QLabel("🎨 Mondrian Composition II Art Generator")
        title.setFont(QtGui.QFont("Times New Roman", 40, QtGui.QFont.Weight.Bold))
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setWordWrap(True)
        title_layout.addRow(title)

        title_group.setLayout(title_layout)
        self.layout.addWidget(title_group)
    
    def grid_lines_ui(self):
        '''Creates the UI Spinbox for Vertical and Horizontal Lines'''
        grid_group = QtWidgets.QGroupBox('Grid Lines:')
        grid_ui_layout = QtWidgets.QFormLayout()
        grid_ui_layout.setSpacing(10)

        self.vertical_input = QtWidgets.QLineEdit()
        self.vertical_input.setPlaceholderText("Enter a number 1-3")
        self.vertical_input.setValidator(QtGui.QIntValidator(1, 3))
        grid_ui_layout.addRow("Amount of Vertical Lines: ", 
                           self.vertical_input)
        
        self.horizontal_input = QtWidgets.QLineEdit()
        self.horizontal_input.setPlaceholderText("Enter a number 1-3")
        self.horizontal_input.setValidator(QtGui.QIntValidator(1, 3))
        grid_ui_layout.addRow("Amount of Horizontal Lines: ", 
                           self.horizontal_input)
        
        grid_group.setLayout(grid_ui_layout)
        self.layout.addWidget(grid_group)

    def rectangle_amount_ui(self):
        '''Creates the UI Spinboxfor amount of Rectangles'''
        rectangle_group = QtWidgets.QGroupBox('Rectangles:')
        rectangle_ui_layout = QtWidgets.QFormLayout()
        rectangle_ui_layout.setSpacing(10)

        self.rectangle_amount_input = QtWidgets.QSpinBox()
        self.rectangle_amount_input.setMinimum(4)
        self.rectangle_amount_input.setMaximum(9)
        rectangle_ui_layout.addRow("Amount of Colored Rectangles: ", 
                           self.rectangle_amount_input)

        rectangle_group.setLayout(rectangle_ui_layout)
        self.layout.addWidget(rectangle_group)

    def signature_ui(self):
        '''Creates the Signature UI comprised of TypeFace, FontSize, Name'''
        signature_group = QtWidgets.QGroupBox('Signature:')
        signature_ui_layout = QtWidgets.QFormLayout()
        signature_ui_layout.setSpacing(10)
        self.username_input = QtWidgets.QLineEdit()
        signature_ui_layout.addRow("Name: ", self.username_input) 

        self.typeface_input = QtWidgets.QComboBox()
        self.typeface_input.addItems(["Arial", "Times New Roman"])
        signature_ui_layout.addRow("Select a Typeface: ", self.typeface_input) 

        self.fontsize_input = QtWidgets.QComboBox()
        self.fontsize_input.addItems(["16", "20", "24", "30"])
        signature_ui_layout.addRow("Select a Font Size: ", self.fontsize_input) 

        signature_group.setLayout(signature_ui_layout)
        self.layout.addWidget(signature_group)

    def saturation_ui(self):
        '''Creates the Saturation UI Dropbox where users can select percentages'''
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
        '''Creates a UI Button'''
        gen_button_layout = QtWidgets.QHBoxLayout()
        generate_btn = QtWidgets.QPushButton('Create Painting')
        generate_btn.clicked.connect(self.generate_artwork)

        gen_button_layout.addWidget(generate_btn)
        self.layout.addLayout(gen_button_layout)

    def generate_artwork(self):
        '''Collects from input UI and sends to Build'''
        if not self.vertical_input.text() or not self.horizontal_input.text():
            return
        
        vertical_lines = int(self.vertical_input.text())
        horizontal_lines = int(self.horizontal_input.text())
        rectangle_amount = self.rectangle_amount_input.value()

        name = self.username_input.text()
        typeface = self.typeface_input.currentText()
        fontsize = int(self.fontsize_input.currentText())
        saturation = int(self.saturation_percent_input.currentText())

        vert_x_locations, horiz_y_locations = build_grid(vertical_lines,
                                                         horizontal_lines)
        self.canvas.vert_x_locations = vert_x_locations
        self.canvas.horiz_y_locations = horiz_y_locations
        
        selected_rectangles, random_colors, all_rectangles = build_rectangles(
                                                            vert_x_locations,
                                                            horiz_y_locations,
                                                            rectangle_amount,
                                                            saturation)
        
        self.canvas.selected_rectangles = selected_rectangles
        self.canvas.random_colors = random_colors
        self.canvas.all_rectangles = all_rectangles

        self.canvas.signature_name = name
        self.canvas.signature_typeface = typeface
        self.canvas.signature_fontsize = fontsize

        QtCore.QTimer.singleShot(600, lambda: self.advance_canvas(1))
        QtCore.QTimer.singleShot(2000, lambda: self.advance_canvas(2))
        QtCore.QTimer.singleShot(3000, lambda: self.advance_canvas(3))

    def advance_canvas(self, state):
        '''Advances the canvas to next state which starts a redraw'''
        self.canvas.paint_state = state
        self.canvas.update()
        self.canvas.signature_opacity = 0.0

        if state == 3:
            self.start_signature_fade()
    
    def start_signature_fade(self):
        '''Starts a fade QTimer for the signature'''
        self.fade_timer = QtCore.QTimer()
        self.fade_timer.timeout.connect(self.fade_signature)
        self.fade_timer.start(30)

    def fade_signature(self):
        """Actual fade opacity for the signature"""
        self.canvas.signature_opacity += 0.02
        if self.canvas.signature_opacity >= 1.0:
            self.canvas.signature_opacity = 1.0
            self.fade_timer.stop()
        self.canvas.update()


class MondrianCanvas(QtWidgets.QWidget):

    def __init__(self):
        '''Initializes all drawable elements'''
        super().__init__()
        self.setMinimumSize(960, 980)
        self.vert_x_locations = []
        self.horiz_y_locations = []
        self.all_rectangles = []
        self.selected_rectangles = []
        self.random_colors = []
        self.signature_name = ''
        self.signature_typeface = 'Arial'
        self.signature_fontsize = 10
        self.paint_state = 0
        self.signature_opacity = 0.0

    def paintEvent(self, event):
        '''Master Painter that calls sub functions based off state'''
        paint = QtGui.QPainter(self)

        if self.paint_state >= 1:
            self.paint_grid(paint)
        if self.paint_state >= 2:
            self.paint_rectangles(paint)
        if self.paint_state >= 3:
            self.paint_signature(paint)

        paint.end()

    def paint_grid(self, paint):
        """Paints the vertical and horizontal lines onto canvas"""
        thickpen = QtGui.QPen(QtGui.QColor('black'))
        thickpen.setWidth(8)
        paint.setPen(thickpen)

        for xpositions in self.vert_x_locations:
            paint.drawLine(xpositions, 0, xpositions, CANVAS_HEIGHT)

        for ypositions in self.horiz_y_locations:
            paint.drawLine(0, ypositions, CANVAS_WIDTH, ypositions)
    
    def paint_rectangles(self, paint):
        """Paints the cells with their asssigned color"""
        paint.setPen(QtCore.Qt.NoPen)
        offset = 4

        for rectangle in self.all_rectangles:
            if rectangle not in self.selected_rectangles:
                rectangle_x, rectangle_y, rectangle_width, rectangle_height = rectangle

                paint.fillRect(rectangle_x + offset, rectangle_y + offset,
                               rectangle_width - offset * 2,
                               rectangle_height - offset * 2,
                               QtGui.QColor('white'))
        
        for num, rectangle in enumerate(self.selected_rectangles):
            rectangle_x, rectangle_y, rectangle_width, rectangle_height = rectangle
            color = self.random_colors[num % len(self.random_colors)]
            
            paint.fillRect(rectangle_x + offset, rectangle_y + offset,
                           rectangle_width - offset * 2,
                           rectangle_height - offset * 2, color)
            
    def paint_signature(self, paint):
        '''Paints the siganture fading in'''
        paint.setOpacity(self.signature_opacity)
        build_signature(paint, self.signature_name, self.signature_typeface,
                        self.signature_fontsize)
        paint.setOpacity(1.0)


if __name__ == "__main__":
    main()
