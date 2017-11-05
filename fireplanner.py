import random
from ship import Ship


class FirePlanner:
    def fire(self, matrix):
        goals = self.possibleGoals(matrix)

        if len(goals) > 0:
            return random.choice(goals)

        return self.randomEmptyCell(matrix)

    def randomEmptyCell(self, matrix):
        chessCoords = self.getChessBoardBlackPosCoords(len(matrix), len(matrix[0]))

        random.shuffle(chessCoords)

        emptyCell = [-1, -1]

        for coord in chessCoords:
            if matrix[coord[0]][coord[1]] == 0:
                emptyCell = coord
                break

        return emptyCell

    def getChessBoardBlackPosCoords(self, n, m):
        chessCoords = []
        for row in range(n):
            for col in range(m):
                if (row + col) % 2 == 0:
                    chessCoords.append([row, col])

        return chessCoords

    def possibleGoals(self, matrix):
        shipInMatrix = self.getLengthiestShipFromMatrix(matrix)

        return shipInMatrix.getUndiscoveredPositions()

    def getLengthiestShipFromMatrix(self, matrix):
        rowShip = self.getLengthiestShipFromRows(matrix)
        colShip = self.getLengthiestShipFromCols(matrix)

        if rowShip.length < colShip.length:
            return colShip

        return rowShip

    def getLengthiestShipFromRows(self, matrix):
        maxShip = Ship()

        for row in range(len(matrix)):
            ship = Ship().setToTheLengthiestShipFromString(''.join(map(str, matrix[row])))
            if ship.length > maxShip.length:
                maxShip = ship
                maxShip.row = row

        return maxShip

    def getLengthiestShipFromCols(self, matrix):
        transposed = map(list, zip(*matrix))
        ship = self.getLengthiestShipFromRows(transposed)
        ship.col = ship.row
        ship.row = None

        return ship
