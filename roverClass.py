class Rover:  # This class describes a martian rover
    def __init__(self, xCoordinates, yCoordinates, heading):  # Constructor which takes rover's initial coordinates and heading
        self.xCoordinates = xCoordinates
        self.yCoordinates = yCoordinates
        self.heading = heading
        self.headingArray = ["N", "E", "S", "W"]  # Contains the possible directions and the order in which they appear
        if self.heading not in self.headingArray or self.xCoordinates < 0 or self.yCoordinates < 0:  # Throw an error if heading or coordinates are invalid
            raise Exception()

    def rotate_right(self):  # Rotate the rover to the right
        headingIndex = self.headingArray.index(self.heading)
        if headingIndex < len(self.headingArray) - 1:
            self.heading = self.headingArray[headingIndex + 1]
        else:
            self.heading = self.headingArray[0]

    def rotate_left(self):  # Rotate the rover to the left
        headingIndex = self.headingArray.index(self.heading)
        if headingIndex > 0:
            self.heading = self.headingArray[headingIndex - 1]
        else:
            self.heading = self.headingArray[len(self.headingArray) - 1]

    def move(self):  # Move the rover in the direction of its heading
        if self.heading == "N":
            self.yCoordinates += 1
        elif self.heading == "E":
            self.xCoordinates += 1
        elif self.heading == "S":
            self.yCoordinates -= 1
        else:
            self.xCoordinates -= 1

    def set_position(self, xCoordinates, yCoordinates, heading):  # Manually set position of the rover
        self.xCoordinates = xCoordinates
        self.yCoordinates = yCoordinates
        self.heading = heading

    def process_input_string(self, inputString):  # Execute commands contained in the input string; ignore illegal commands
        for character in inputString:
            if character == "L":
                self.rotate_left()
                print("Rotating left...")
            elif character == "R":
                self.rotate_right()
                print("Rotating right...")
            elif character == "M":
                self.move()
                print("Moving (" + self.heading + ")...")
            else:
                print("Illegal character in the input string; ignoring command '" + character + "'")

    def print_position(self):  # Print coordinates and heading
        print(str(self.xCoordinates) + " " + str(self.yCoordinates) + " " + self.heading)

    def get_coordinates(self):  # Return an array containing the rover's current coordinates
        return [self.xCoordinates, self.yCoordinates]
