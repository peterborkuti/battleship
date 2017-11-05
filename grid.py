from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
import warnings

from kivy.graphics.vertex_instructions import Line
from kivy.properties import ListProperty, StringProperty, ObjectProperty

class GridStates:
    EMPTY = 0
    MISS = 1
    HIT = 2
    SUNK = 3

    SHIP = 1
    UNKNOWN = 5

class GridButton(ToggleButton):

    def __init__(self, text='', row=0, col=0, **kwargs):
        super(GridButton, self).__init__(text=text, **kwargs)

        self.button_background_normal_orig = self.background_normal
        self.button_background_color_orig = self.background_color
        self.button_background_normal_set = ''
        self.button_background_color_set = [1, 0, 0, 1]

        self.row = row
        self.col = col
        self.mstate = GridStates.EMPTY

    def pressed(self):
        if self.background_normal == '':
            self.mstate = GridStates.EMPTY
            self.background_normal = self.button_background_normal_orig
            self.background_color = self.button_background_color_orig
        else:
            self.mstate = GridStates.SHIP
            self.background_normal = self.button_background_normal_set
            self.background_color = self.button_background_color_set

    def getState(self):
        return self.mstate

    def setText(self, text):
        self.text = str(text)


class Grid(GridLayout):

    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.buttons = []

        self.drawRowTitle()

        rowTitles = ['a','b','c','d','e','f','g','h','i','j']

        for row in range(len(rowTitles)):
            self.add_widget(Label(text=rowTitles[row],size_hint=(0.3, 0.1)))
            self.buttons.append([])
            self.drawRowButtons(row, rowTitles[row])

    def drawRowTitle(self):
        self.add_widget(Label(text='',size_hint=(0.3, 0.1)))

        for i in range(10):
            self.add_widget(Label(text=str(i)))

    def getButtonDefaultText(self, row=None, col=None):
        return str(row) + str(col)

    def drawRowButtons(self, row, rowTitle):
        for col in range(10):
            button = GridButton(text=self.getButtonDefaultText(rowTitle, col), row=row, col=col)
            button.bind(on_press=self.pressed)
            self.add_widget(button)
            self.buttons[row].append(button)

    def pressed(self, instance):
        instance.pressed()

    def clearButtons(self):
        for row in range(len(self.buttons)):
            for col in range(len(self.buttons[0])):
                self.buttons[row][col].text = self.getButtonDefaultText(row, col)

    def getMatrix(self):
        matrix = []

        for row in range(10):
            matrix.append([])
            for col in range(10):
                matrix[row].append(self.buttons[row][col].getState())

        return matrix

    def getNumberOfShipCells(self, matrix=None, cellState=GridStates.SHIP):
        if not matrix:
            matrix = self.getMatrix()

        num = 0

        for row in range(len(matrix)):
            num += ''.join(map(str, matrix[row])).count(str(cellState))

        return num

    def getCellState(self, row, col):
        if 0 <= row < 10 and 0 <= col < 10:
            return self.buttons[row][col].getState()

        warnings.warn("Invalid coords:" + str(row) + str(col))

        return GridStates.UNKNOWN

    def getButtonText(self, row, col):
        return self.buttons[row][col].text

class PlayerGrid(Grid):
    def __init__(self, **kwargs):
        super(PlayerGrid, self).__init__(buttonText = '', **kwargs)

class AIGrid(Grid):
    def __init__(self, **kwargs):
        super(AIGrid, self).__init__(buttonText = '?', **kwargs)

    def getButtonDefaultText(self, row=None, col=None):
        return '0'

    def getMatrix(self):
        matrix = []

        for row in range(10):
            matrix.append([])
            for col in range(10):
                matrix[row].append(int(self.getButtonText(row, col)))

        return matrix

    def setButtonText(self, row, col, text):
        self.buttons[row][col].setText(text)
