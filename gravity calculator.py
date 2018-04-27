# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a pyqt5 app with the following attributes:
# - use an App/Window class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function or custom method
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed. 
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 2 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.
import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

G = 6.67408e-11

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: #000000")

        # Set up the app layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(100, 100, 400, 200)

        # Make widgets
        self.title = QLabel("Gravity Calculator")
        self.title.setStyleSheet('color: white')
        self.grid.addWidget(self.title, 1, 1, 1 ,1)
        self.side1_label = QLabel("Mass of planet 1 (kg): ")
        self.side1_label.setStyleSheet('color: white')
        self.grid.addWidget(self.side1_label, 2, 1, 1, 1)
        self.side1_value = QLineEdit()
        self.side1_value.setStyleSheet("color: white")
        self.grid.addWidget(self.side1_value, 2, 2, 1, 1)
        self.side2_label = QLabel("Mass of planet 2 (kg): ")
        self.side2_label.setStyleSheet('color: white')
        self.grid.addWidget(self.side2_label, 3, 1, 1, 1)
        self.side2_value = QLineEdit()
        self.side2_value.setStyleSheet("color: white")
        self.grid.addWidget(self.side2_value, 3, 2, 1, 1)
        self.separation_value = QLineEdit()
        self.separation_value.setStyleSheet("color: white")
        self.grid.addWidget(self.separation_value, 4, 2, 1, 1)
        self.separation_label = QLabel("Separation (m): ")
        self.separation_label.setStyleSheet('color: white')
        self.grid.addWidget(self.separation_label, 4, 1, 1, 1)
        self.calc_button = QPushButton("Calculate")
        self.calc_button.setStyleSheet("background-color: red")
        self.grid.addWidget(self.calc_button, 5, 1, 1, 1)
        self.answer_value = QLabel("0")
        self.answer_value.setStyleSheet('color: white')
        self.grid.addWidget(self.answer_value, 5, 2, 1, 1)

        '''
        My stylistic modifications were:
        - White font color
        - Red push button
        - Black background (to look like space!)
        '''

        # Signals and slots
        self.calc_button.clicked.connect(self.calc_force)

        self.show()

    def calc_force(self):

        try:
            mass1 = float(self.side1_value.text())
            mass2 = float(self.side2_value.text())
            r = float(self.separation_value.text())
            force = G*mass1*mass2/r/r
            self.answer_value.setText(str(force) + " Newtons")
        except ZeroDivisionError:
            self.answer_value.setText("Separation of 0 not allowed")
        except ValueError:
            self.answer_value.setText("Enter numbers")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())