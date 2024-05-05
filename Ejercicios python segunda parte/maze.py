import os
import readchar

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]

while True: #We create an infinite cycle
    #Draw the map

    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    for coordinate_y in range (MAP_HEIGHT):
        print("|", end ="")
        for coordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ", end = "")
            else:
                print("   ", end = "") #We did this becouse we don't want an enter at the finish. We put 3 spaces becouse we have multiplied the width by 3.
        print("|")

    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    #Ask user where he/she wants to move

    direction = readchar.readchar() #Be careful, readchar doesn't work on the Pycharm console. We need to open in the CMD.

    if direction == "w":
        my_position[POS_Y] -= 1 #To move across the map
        my_position[POS_Y] %= MAP_HEIGHT #When you go to the finish, this code redirect you to the start of the map
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break

    os.system("cls") #This is used to clear the console

