import os
import readchar
import random

titulo = "Bienvenido a este nuevo mapa en el que tendrás que derrotar a todos los entrenadores para ganar."
print("\n" + titulo + "\n" + len(titulo) * "_" + "\n")

#Now, in this part, we are going to define the main variables of our program

obstacle_definition = []
NUM_POKEMON_TRAINERS = 5
pokemon_trainers_position = []
my_position = [15, 0]
POS_X = 0
POS_Y = 1
end_game = False


#The first thing we are going to do is generate the map for our game. You can change it when you want

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

#Now, we are going to define the position of the Pokemon trainers on the map generated
#Remember, we don't want to generate one more Pokemon trainer if one of the originals is defeated

while len(pokemon_trainers_position) < NUM_POKEMON_TRAINERS:
    new_position_trainer = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

    if (new_position_trainer not in pokemon_trainers_position and new_position_trainer != my_position
            and obstacle_definition[new_position_trainer[POS_Y]][new_position_trainer[POS_X]] != "#"):
        pokemon_trainers_position.append(new_position_trainer)

#We create an infinite loop. This loop is bassically craeated to draw the map and make the move of the protagonist possible
#Inside of this loop we are going to create the Pokemon fights

while end_game == False:
    #Now we are going to draw the map that we have created before
    print("+" + "-" * (MAP_WIDTH * 3) + "+") #We draw the limits of the superior part of the map

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="") #We draw the limits of the left part of the map

        for coordinate_x in range(MAP_WIDTH):
            chart_to_draw = " "
            object_in_cell = None

            for trainer_position in pokemon_trainers_position: #We do it to print the Pokemon trainers in our map
                if trainer_position[POS_X] == coordinate_x and trainer_position[POS_Y] == coordinate_y:
                    chart_to_draw = "0"
                    object_in_cell = trainer_position

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y: #To print our position
                chart_to_draw = "X"

                if object_in_cell: #THE POKEMON FIGHT STARTS. After the fight, if we win, we are going to remove the trainer defeated
                    pokemon_trainers_position.remove(object_in_cell)
                    os.system("cls")  # This is used to clear the console

                    titulo2 = "Empieza el combate Pokemon contra uno de los {} oponentes del mapa.".format(
                        NUM_POKEMON_TRAINERS)
                    print("\n" + titulo2 + "\n" + len(titulo2) * "_" + "\n")

                    #The first thing we are going to do is define the variables of the pokemon fight
                    vida_inicial_pikachu = 80
                    vida_inicial_squirttle = 90
                    vida_pikachu = vida_inicial_pikachu
                    vida_squirttle = vida_inicial_squirttle
                    ataque_squirttle = None
                    print ("El rival decide utilizar su Pikachu\n"
                           "El protagonista opta por usar su Squirttle\n")

                    #We define the loop of the fight
                    while vida_pikachu > 0 and vida_squirttle > 0:

                        print("Turno de ataque del rival.")
                        ataque_pikachu = random.randint(1, 2) #We define a random attack for the oponent

                        if ataque_pikachu == 1:
                            print("Pikachu ha elegigo el ataque: Bola voltio")
                            vida_squirttle -= 10
                            if vida_squirttle <= 0:
                                print("\n" + "Tu Squirttle ha sido debilitado. HAS PERDIDO")
                                exit()

                        elif ataque_pikachu == 2:
                            print("Pikachu ha elegigo el ataque: Onda trueno\n")
                            vida_squirttle -= 12
                            if vida_squirttle <= 0:
                                print("\n" + "Tu Squirttle ha sido debilitado. HAS PERDIDO")
                                exit()
                                break #Our pokemon is down, so we lose and break the whole loop

                        #We define in this part the life level of the Pokemons after the oponent turn
                        resultado_vida_pikachu = 100 * (vida_pikachu / vida_inicial_pikachu)
                        resultado_vida_squirttle = 100 * (vida_squirttle / vida_inicial_squirttle)
                        barra_vida = "#"
                        print("La vida del Pikachu es:\n", int(resultado_vida_pikachu) * barra_vida)
                        print("La vida del Squirttle es:\n", int(resultado_vida_squirttle) * barra_vida)
                        input("Enter para pasar a tu turno...\n")
                        os.system("cls")  # Para borrar la pantalla. Cuidado, pycharm no lo ejecuta correctamente

                        #Now is our turn. We decide between three options to attack
                        print("Turno de nuestro Squirttle")
                        ataque_squirttle = input("¿Qué ataque vas a querer realizar?\n"
                                                 "a- Placaje\n"
                                                 "b- Pistola de agua\n"
                                                 "c- Burbuja\n")

                        while ataque_squirttle != "a" and ataque_squirttle != "b" and ataque_squirttle != "c":
                            ataque_squirttle = input("¿Qué ataque vas a querer realizar?\n"
                                                     "a- Placaje\n"
                                                     "b- Pistola de agua\n"
                                                     "c- Burbuja\n")
                        if ataque_squirttle == "a":
                            print("Squirttle ha elegigo el ataque: Placaje\n")
                            vida_pikachu -= 10
                        elif ataque_squirttle == "b":
                            print("Squirttle ha elegigo el ataque: Pistola de agua\n")
                            vida_pikachu -= 12
                        elif ataque_squirttle == "c":
                            print("Squirttle ha elegigo el ataque: Burbuja\n")
                            vida_pikachu -= 9

                        # We define in this part the life level of the Pokemons after our turn
                        resultado_vida_pikachu = 100 * (vida_pikachu / vida_inicial_pikachu)
                        resultado_vida_squirttle = 100 * (vida_squirttle / vida_inicial_squirttle)
                        barra_vida = "#"
                        print("La vida del Pikachu es:\n", int(resultado_vida_pikachu) * barra_vida)
                        print("La vida del Squirttle es:\n", int(resultado_vida_squirttle) * barra_vida)
                        input("Enter para pasar a tu turno...\n")
                        os.system("cls")

                    if vida_pikachu <= 0:
                        print("\n" + "El Pikachu ha sido debilitado. ERES EL GANADOR \n"
                                     "Tu Squirttle recupera toda su vida gracias a una medicina que te da el oponente \n")
                        os.system("cls")
                    os.system("cls")

            if obstacle_definition[coordinate_y][coordinate_x] == "#": #To define the map obstacles
                chart_to_draw = "#"

            print(" {} ".format(chart_to_draw), end = "")
        print("|") #We draw the limits of the right part of the map

    print("+" + "-" * (MAP_WIDTH * 3) + "+") #We draw the limits of the inferior part of the map

#Now, we are going to create the movement of the protagonist . Ask user where he/she wants to move

    direction = readchar.readchar() #Be careful, readchar doesn't work on the Pycharm console. We need to open in the CMD.
    new_position_user = None

    if direction == "w": #To go up
            new_position_user = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT] #We use the module to allow the protagonist to go round the map

    elif direction == "s": #To go down
            new_position_user = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a": #To go on the left
            new_position_user = [(my_position[POS_X] - 1) % MAP_WIDTH , my_position[POS_Y]]

    elif direction == "d": #To go on the right
            new_position_user = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q": #To quit the game
            end_game = True

    if new_position_user is not None and obstacle_definition[new_position_user[POS_Y] % MAP_HEIGHT][
        new_position_user[POS_X]] != "#":  # Motion logic and character collision detection
        my_position = new_position_user

    os.system("cls")  # This is used to clear the console