from pokeloader import get_all_pokemons
import random
from pprint import pprint
import os


def get_player_profile(pokemons_list):  # Vamos a asignar al player tres pokemons completamente aleatorios de la lista
    return {"player_name": input("¿Cuál es tu nombre?"),
            "pokemon_inventory": [random.choice(pokemons_list) for a in range(3)],
            "number_of_combats": 0,
            "pokeballs": 0,
            "health_potion": 0}


def any_pokemon_player_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def get_pokemon_info(pokemon):
    return "{} | lvl {} | HP {}/{}".format(pokemon["name"], pokemon["level"], pokemon["current_health"]
                                           , pokemon["base_health"])


def choose_pokemon(player_profile):
    choosen = None
    while not choosen:
        print("Elige con que pokemon quieres luchar en este combate")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))

        try:
            return player_profile["pokemon_inventory"][int(input("¿Qué pokemon eliges?"))]
        except (ValueError, IndexError):
            print("Opción escogida no valida")


def available_attacks(player_pokemon):
    # En función del nivel de nuestro pokemon tendremos asignados unos ataques disponibles u otros
    level = player_pokemon["level"]
    if level <= 15:
        return player_pokemon["attacks"][:4]  # Muestra los 5 primeros ataques para niveles <= 15
    elif 15 < level <= 30:
        return player_pokemon["attacks"][:8]  # Muestra los 8 primeros ataques para niveles entre el 15 y el 30
    else:
        return player_pokemon["attacks"]  # Muestra todos los ataques para niveles mayores a 30


def get_attack_info(pokemon_attack):
    # Se muestra la información de los ataques para que el usuario pueda elegir el que más le convenga
    return "{} | type: {} | damage: {}".format(pokemon_attack["name"],
                                               pokemon_attack["type"],
                                               pokemon_attack["damage"])


def choose_attack(attacks):
    chosen_attack = None
    while chosen_attack is None:
        for i, attack in enumerate(attacks):
            print("{} - {}".format(i, get_attack_info(attack)))
        try:
            chosen_index = int(input("\n¿Con cuál ataque quieres atacar? (0-{}): ".format(len(attacks) - 1)))
            if 0 <= chosen_index < len(attacks):
                chosen_attack = attacks[chosen_index]
            else:
                print("Opción fuera de rango. Introduce un número válido.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    return chosen_attack


def player_attack(player_pokemon, pokemon_enemy, attacks):
    chosen_attack = choose_attack(attacks)
    pokemon_enemy["current_health"] -= chosen_attack["damage"]
    print("\n{} ataca con {}".format(player_pokemon["name"], chosen_attack["name"]))
    print("{} recibe {} de daño\n".format(pokemon_enemy["name"], chosen_attack["damage"]))


def enemy_attack(pokemon_enemy, player_pokemon):
    attack = random.choice(pokemon_enemy["attacks"])
    player_pokemon["current_health"] -= attack["damage"]
    print("\n{} ataca con {}".format(pokemon_enemy["name"], attack["name"]))
    print("{} recibe {} de daño\n".format(player_pokemon["name"], attack["damage"]))
    pass


def cure_pokemon(player_pokemon, player_profile):
    if player_profile["health_potion"] >= 1:
        print("Ahora vas a aumentar la vida de {} en 50, recuerda que el máximo de vida que puedes alcanzar para este"
              " pokemon es {}".format(player_pokemon["name"], player_pokemon["base_health"]))
        player_profile["health_potion"] -= 1
        if player_profile["current_health"] >= 1:
            player_pokemon["current_health"] += 50
            if player_pokemon["current_health"] > player_pokemon["base_health"]:
                player_pokemon["current_health"] = player_profile["base_health"]
            print("{} ha recuperado vida, ahora su vida es {}".format(player_pokemon["name"],
                                                                      player_pokemon["current_health"]))
    elif player_profile["health_potion"] == 0:
        print("No posees pociones, has perdido el turno de ataque por no fijarte en tu inventario, inútil")


def capture_with_pokeball(pokemon_enemy, player_profile):
    probability = None
    if player_profile["pokeballs"] >= 1:
        print("\nLa vida de el {} que deseas atrapar es {} y su tipo es {}\n".format(pokemon_enemy["name"],
                                                                                     pokemon_enemy["current_health"],
                                                                                     pokemon_enemy["pokemon_type"]))
        player_profile["pokeballs"] -= 1
        if pokemon_enemy["current_health"] > 50:
            probability = random.randint(1, 10)
        elif pokemon_enemy["current_health"] > 20:
            probability = random.randint(1, 5)
        elif pokemon_enemy["current_health"] > 5:
            probability = random.randint(1, 2)
        elif pokemon_enemy["current_health"] == 1:
            probability = 1

        if probability == 1:
            player_profile["pokemon_inventory"].append(enemy_pokemon)
            print("\nHas obtenido a {} su vida es {} y su tipo {}\n".format(pokemon_enemy["name"],
                                                                            pokemon_enemy["current_health"],
                                                                            pokemon_enemy["pokemon_type"]))
        else:
            print("No ha sido posible capturarlo. !Debes debilitarlo más para poder capturarlo!")
            fight(player_profile, pokemon_enemy)

    elif player_profile["pokeballs"] == 0:
        print("No posees pokeballs, has perdido el turno de ataque por no fijarte en tu inventario, inútil")



def assign_XP(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 10)
        pokemon["current_exp"] += points

    while pokemon["current_exp"] >= 20:
        pokemon["current_exp"] -= 20
        pokemon["level"] += 1
        pokemon["base_health"] += 10  # Cada vez que subimos de nivel aumentamos la vida máxima de los pokemon 10 puntos
        pokemon["current_health"] += 25  # Cada vez que subimos de nivel recuperamos 25 puntos de vida
        if pokemon["current_health"] > pokemon["base_health"]:  # Condición para no sobrepasar la vida máxima
            pokemon["current_health"] = pokemon["base_health"]
        print("Enhorabuena!! Tú pokemon ha subido al nivel {}.".format(get_pokemon_info(pokemon)))


def fight(player_profile, pokemon_enemy):
    print("--- NUEVO COMBATE ---")

    attack_history = []
    player_pokemon = choose_pokemon(player_profile)
    print("Los contricantes son: {} VS {}".format(get_pokemon_info(player_pokemon),
                                                  get_pokemon_info(pokemon_enemy)))

    while any_pokemon_player_lives(player_profile) and pokemon_enemy["current_health"] > 0:
        action = None
        while action not in ["A", "P", "V", "C"]:
            action = input("¿Qué deseas hacer: [A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar pokemon?")

            if action == "A":
                attacks = available_attacks(player_pokemon)
                chosen_attack = choose_attack(attacks)
                player_attack(player_pokemon, pokemon_enemy, attacks)
                attack_history.append(player_pokemon)
            elif action == "V":
                cure_pokemon(player_pokemon, player_profile)
            elif action == "P":
                capture_with_pokeball(pokemon_enemy, player_profile)
            elif action == "C":
                player_pokemon = choose_pokemon(player_profile)
            if player_pokemon["current_health"] == 0 and any_pokemon_player_lives(player_profile):
                player_pokemon = choose_pokemon(player_profile)

            enemy_attack(pokemon_enemy, player_pokemon)

    if pokemon_enemy["current_health"] <= 0:
        pokemon_enemy["current_health"] = 0
        print("Has ganado el combate")
        player_profile["number_of_combats"] += 1
        assign_XP(attack_history)

    print("--- FIN DEL COMBATE ---")
    input("\n" + "Presiona ENTER para continuar" + "\n")
    os.system("cls")


def item_lotery(player_profile):
    # Según un factor aleatorio puede tocar una pokeball, una cura o ambas que se suman a nuestro inventario
    chance = random.randint(1, 4)
    if chance == 1:
        print("\nHas ganado una PokeBall\n")
        player_profile["pokeballs"] += 1
    elif chance == 2:
        print("\nHas ganado un pocion de vida para tu Pokemon\n")
        player_profile["health_potion"] += 1
    elif chance == 3:
        print("\nEnhorabuena, has ganado un pocion de vida y una PokeBall\n")
        player_profile["health_potion"] += 1
        player_profile["pokeballs"] += 1
    else:
        print("\nLo sentimos, no ha habido suerte. El contrincante no tenía ningun objeto que pudieras aprovechar\n")


def main():
    pokemons_list = get_all_pokemons()
    player_profile = get_player_profile(pokemons_list)

    while any_pokemon_player_lives(player_profile):
        pokemon_enemy = random.choice(pokemons_list)
        fight(player_profile, pokemon_enemy)
        item_lotery(player_profile)

    print("Finalmente has perdido en el combate número {}".format(player_profile["number_of_combats"]))


if __name__ == "__main__":
    main()
