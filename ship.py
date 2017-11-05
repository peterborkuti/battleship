import re

class Ship:
    def __init__(self, row = None, col = None, ship = '', length = 0, pos = -1):
        self.row = row
        self.col = col
        self.ship = ship
        self.length = length
        self.pos = pos

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def setToTheLengthiestShipFromString(self, places):
        maxPos = -1
        maxStr = ''
        maxLen = 0

        for match in re.finditer('02+.?|.?2+0', places):
            s = match.group(0)
            l = s.count('2')
            if l > maxLen:
                maxLen = l
                maxStr = s
                maxPos = match.start(0)

        self.ship = maxStr
        self.pos = maxPos
        self.length = maxLen

        return self

    def getUndiscoveredPositions(self):
        places = []

        if self.length > 0:
            if self.ship[0] == '0':
                places.append(self.pos)
            if self.ship[-1] == '0':
                places.append(self.pos + len(self.ship) - 1)

        goals = []

        for place in places:
            if self.col is not None:
                goals.append([place, self.col])
            else:
                goals.append([self.row, place])

        return goals
