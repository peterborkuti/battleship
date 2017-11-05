from kivy.app import App

from battleshipgame import BattleShipGame


class BattleShipApp(App):
    def build(self):
        return BattleShipGame()


if __name__ == '__main__':
    BattleShipApp().run()