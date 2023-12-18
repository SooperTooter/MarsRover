class Plateau:  # This class describes a martian plateau
    def __init__(self, upperXCoordinates, upperYCoordinates):
        self.upperXCoordinates = upperXCoordinates
        self.upperYCoordinates = upperYCoordinates
        if self.upperYCoordinates <= 0 or self.upperXCoordinates <= 0:  # Throw an error if coordinates are invalid
            raise Exception()

    def position_is_valid(self, xCoordinates, yCoordinates):  # Check if a position is valid on the given plateau
        if xCoordinates > self.upperXCoordinates or yCoordinates > self.upperYCoordinates or xCoordinates < 0 or yCoordinates < 0:
            return False
        else:
            return True
