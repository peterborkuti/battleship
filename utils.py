class ShipUtil:
    def fromStringToMap(self, stringMap):
        return map(lambda line: map(int, list(line)), stringMap.split(','))


class ShipOrganizer:
    ships = {
        'Carrier':
            {'len': 5, 'pieces':1},
        'Battleship':
            {'len': 4, 'pieces': 1},
        'Cruiser':
            {'len': 3, 'pieces': 1},
        'Submarine':
            {'len': 2, 'pieces': 1},
        'Destroyer':
            {'len': 2, 'pieces': 1}
    }
