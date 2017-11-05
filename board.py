from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class PlayerBoard(BoxLayout):
    def __init__(self, **kwargs):
        super(PlayerBoard, self).__init__(**kwargs)

class AIBoard(BoxLayout):
    def __init__(self, **kwargs):
        super(AIBoard, self).__init__(**kwargs)
