import os
import readchar
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_MAP_OBJECTS = 12

my_position = [15, 0]
map_objects = []
new_position_object = []
tail_length = 0
tail = []
end_game = False
died = False


#Generate an obstacle map

obstacle_definition = """\
############               #################
##########      ###     ###########     ####
############    #####    ##########    #####
  ########            ##############        
  #############   ################      ####
   #####                               #####
   ################          #######  ######
                     ###########         ### 
   ##############                           
#    ######################       ##########
###     ###                    #############
######       ###      #####       ##########
###################         ################\
"""

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

#Generate random objects on the map. First attemp to do it. Using "for"
""" 
for object_number in range(NUM_MAP_OBJECTS + 1):
    new_position_object = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
    
    if new_position_object not in map_objects and new_position_object != my_position:
        map_objects.append(new_position_object)
print (map_objects)
"""

#Second attemp to do it. Using "while" to secure the lenght of the list is correct

while len(map_objects) < NUM_MAP_OBJECTS:
    new_position_object = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

    if (new_position_object not in map_objects and new_position_object != my_position
            and obstacle_definition[new_position_object[POS_Y]][new_position_object[POS_X]] != "#"):
        map_objects.append(new_position_object)

print (map_objects)


#We create an infinite cycle/loop. The main loop

while not end_game:
    #Draw the map

    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    for coordinate_y in range (MAP_HEIGHT):
        print("|", end ="")

        for coordinate_x in range(MAP_WIDTH):

            chart_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects: #We do it to print the objects in our map
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    chart_to_draw = "0"
                    object_in_cell = map_object

            for tail_piece in tail: #We want to print the tail in our map when we eat an object
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    chart_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y: #We do it to print the position
                chart_to_draw = "X"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                    #We want to generate a new random object in the map after we "eat" someone on the original list
                    new_position_object = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
                    map_objects.append(new_position_object)

                if tail_in_cell:
                    died = True
                    end_game = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                chart_to_draw = "#"

            print(" {} ".format(chart_to_draw), end = "")
        print("|")

    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    #Ask user where he/she wants to move

    direction = readchar.readchar() #Be careful, readchar doesn't work on the Pycharm console. We need to open in the CMD.
    new_position_user = None

    if direction == "w":
        new_position_user = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "s":
        new_position_user = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":
        new_position_user = [(my_position[POS_X] - 1) % MAP_WIDTH , my_position[POS_Y]]

    elif direction == "d":
        new_position_user = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        end_game = True

    if new_position_user:
        if obstacle_definition[new_position_user[POS_Y] % MAP_HEIGHT][new_position_user[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[: tail_length]
            my_position = new_position_user

    os.system("cls") #This is used to clear the console

if died == True:
    print("\n" + "HAS MUERTO!!" + "\n")
