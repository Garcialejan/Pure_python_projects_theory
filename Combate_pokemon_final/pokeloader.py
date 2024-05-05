from requests_html import HTMLSession
import pickle

pokemon_base = {"name": "",
                "current_health": 100,
                "base_health": 100,
                "level": 1,
                "pokemon_type": None,
                "current_exp": 1}

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="


def get_pokemon(pokemon_index):
    url = "{}{}".format(URL_BASE, pokemon_index)
    session = HTMLSession()

    new_pokemon = pokemon_base.copy()
    pokemon_page = session.get(url)
    new_pokemon["name"] = pokemon_page.html.find(".mini", first=True).text.split("\n")[0]
    # He usado el split ya que había problemas y me cogía muchos elementos de la página. Solo me interesaba el primero

    new_pokemon["pokemon_type"] = []  # Por como funciona Python es mejor crear la lista cuando la necesitemos que
    # crearla en el diccionario de pokemon_base

    for img in (pokemon_page.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img")):
        new_pokemon["pokemon_type"].append(img.attrs["alt"])

    new_pokemon["attacks"] = []

    for attack_item in pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {"name": attack_item.find("td", first=True).find("a", first=True).text,
                  "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
                  "min_level": attack_item.find("th", first=True).text,
                  "damage": int(attack_item.find("td")[3].text.replace("--", "0"))}
        new_pokemon["attacks"].append(attack)

    return new_pokemon


def get_all_pokemons():
    try:
        print("Cargando el archivo con todos los pokemons...")
        with open("pokefile.pkl", "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)

    except FileNotFoundError:
        print("Archivo no encotrado! Cargando los pokemons desde la web...")
        all_pokemons = []
        for index in range(151):
            all_pokemons.append(get_pokemon(index + 1))
            print("*", end="")

        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)
            print("\n Todos los pokemons han sido cargados correctamente")

    print("Lista de pokemons cargada correctamente!!")
    return all_pokemons

