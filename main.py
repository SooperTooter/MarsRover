from roverClass import Rover
from plateauClass import Plateau

NUMBER_OF_ROVERS = 2  # Change this to adjust the total number of rovers
roverArray = []

# Construct the plateau
print("Welcome to the Mars Rover terminal!")
plateauCoordinatesString = input("Enter the upper coordinates of the plateau divided by space (e.g. '5 5') >: ")
plateauCoordinates = plateauCoordinatesString.split()
inputIsValid = False
newPlateau = None
while not inputIsValid:  # Ensure the user input is valid; query the user until valid coordinates are given
    try:
        newPlateau = Plateau(int(plateauCoordinates[0]), int(plateauCoordinates[1]))
    except:
        plateauCoordinatesString = input("Please enter valid coordinates >: ")
        plateauCoordinates = plateauCoordinatesString.split()
    else:
        inputIsValid = True

# Place rovers on the plateau and execute commands
roverCounter = 1
while roverCounter <= NUMBER_OF_ROVERS:  # Add rovers one by one
    roverCoordinatesString = input("Enter the starting coordinates of rover number " + str(roverCounter) + " and its heading divided by space (e.g. '1 2 N') >: ")
    roverCoordinates = roverCoordinatesString.split()
    inputIsValid = False
    newRover = None
    while not inputIsValid or not newPlateau.position_is_valid(int(roverCoordinates[0]), int(roverCoordinates[1])):  # Ensure the user input is valid; query the user until valid coordinates are given
        try:
            newRover = Rover(int(roverCoordinates[0]), int(roverCoordinates[1]), roverCoordinates[2])
        except:
            roverCoordinatesString = input("Please enter valid coordinates >: ")
            roverCoordinates = roverCoordinatesString.split()
        else:
            inputIsValid = True
    inputString = input("Enter movement commands for rover number " + str(roverCounter) + " >: ")
    newRover.process_input_string(inputString)
    while not newPlateau.position_is_valid(newRover.get_coordinates()[0], newRover.get_coordinates()[1]):  # Ensure the rover doesn't fall off the plateau
        newRover.set_position(int(roverCoordinates[0]), int(roverCoordinates[1]), roverCoordinates[2])  # Reset the rover's position
        print("Warning! This command may result in the rover falling off the plateau. Please input a different command.")
        inputString = input(">: ")
        newRover.process_input_string(inputString)
    print("Finished moving rover number " + str(roverCounter) + "!")
    roverArray.append(newRover)
    roverCounter += 1
print("Finished moving all rovers!")

# Print coordinates and headings of all rovers
for rover in roverArray:
    rover.print_position()
