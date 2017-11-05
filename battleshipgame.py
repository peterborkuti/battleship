from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from fireplanner import FirePlanner
from grid import GridStates


class BattleShipGame(BoxLayout):
    def __init__(self, **kwargs):
        super(BattleShipGame, self).__init__(**kwargs)
        self.fireplanner = FirePlanner()

    def fire(self, *args):
        coord = self.fireplanner.fire(self.aiboard.grid.getMatrix())
        if coord != [-1, -1]:
            state = self.playerboard.grid.getCellState(coord[0], coord[1])

            if state == GridStates.EMPTY:
                self.aiboard.grid.setButtonText(coord[0], coord[1], GridStates.MISS)
                Clock.schedule_once(self.fire, 0.1)
            else:
                self.aiboard.grid.setButtonText(coord[0], coord[1], GridStates.HIT)
                shipCells = self.playerboard.grid.getNumberOfShipCells()
                hits = self.aiboard.grid.getNumberOfShipCells(cellState=GridStates.HIT)

                print "shipcells:", shipCells, "hits:", hits
                if shipCells > hits:
                    Clock.schedule_once(self.fire, 0.1)
                else:
                    print "All the ships sank. I win."
        else:
            print "No possible move, game over"

    def startAI(self):
        shipCells = self.playerboard.grid.getNumberOfShipCells()
        if shipCells > 0:
            self.aiboard.grid.clearButtons()
            self.fire()
        else:
            print "No ships, no game"