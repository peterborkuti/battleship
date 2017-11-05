import unittest
from utils import ShipUtil
from fireplanner import FirePlanner
from ship import Ship
from grid import Grid


def fire(shipMap):
    return FirePlanner().fire(ShipUtil().fromStringToMap(shipMap))

def getShip(shipMap):
    return FirePlanner().getLengthiestShipFromMatrix(ShipUtil().fromStringToMap(shipMap))

def getGoals(shipMap):
    return FirePlanner().possibleGoals(ShipUtil().fromStringToMap(shipMap))

def assertAny(coord, coords):
    pass


class TestSinkHolePlanner(unittest.TestCase):

    def test_getShip(self):
        self.assertEqual(
            getShip('022220,002000,002000,002000,002000,000000'),
            Ship(length= 5, ship='222220', pos=0, row=None, col=2))

    def test_goals(self):
        self.assertEqual(
            getGoals('022220,002000,002000,002000,002000,000000'),
            [[5, 2]])
        self.assertEqual(
            getGoals('020220,002000,002000,002000,002000,000000'),
            [[0,2],[5, 2]])
        self.assertEqual(
            getGoals('022220,002000,000000,002000,002000,000000'),
            [[0,0],[0, 5]])
        self.assertEqual(
            getGoals('000000,002220,000000,002000,002000,000000'),
            [[1,1],[1, 5]])
        m = [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 1, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 0, 0, 1, 2, 1],
             [0, 0, 0, 0, 0, 0, 0, 1, 2, 1],
             [0, 0, 0, 0, 1, 0, 0, 1, 2, 1],
             [0, 0, 0, 0, 0, 1, 0, 1, 2, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
        self.assertEqual(
            FirePlanner().possibleGoals(m),
            [[1,0],[3,0]])

    def test_randomfire(self):
        self.assertEqual(
            fire('10,00'),[1, 1])
        self.assertEqual(
            fire('00,01'),[0, 0])
        self.assertEqual(
            fire('10,01'),[-1, -1])
        self.assertTrue(
            fire('00,00') in [[0, 0],[1,1]])

class TestPlayerGrid(unittest.TestCase):
    def numCells(self, shipMap):
        return Grid().getNumberOfShipCells(ShipUtil().fromStringToMap(shipMap))

    def test_numCells(self):
        self.assertEqual(
            self.numCells('011110,001000,001000,001000,001000,000000'), 8)



if __name__ == '__main__':
    unittest.main()
