import random
from io import BytesIO
from speak_and_listen import speak, hear_me
from requests_html import HTMLSession
from PIL import Image

# Hay que tener cuidado con la pagina que seleccionamos para realizar las compras ya que estas puede estar protegidas
# para prevenir el acceso automatizado o no autorizado a través de bots
URL_NIKE = "https://www.nike.com/es/"


def hear_price_and_get_number():
    while True:
        try:
            price = hear_me()
            # Nos aseguramos que digamos lo que digamos nos devuelva un número con decicmal
            price = price.replace(",", ".").replace(" con ", ".").replace("€", "").replace("euros", "")
            final_price = float(price)
            return final_price
        except ValueError:
            print("No te he entendido bien, repite el número por favor")


def get_product_categories(session):
    main_web = session.get(URL_NIKE)
    return main_web.html.find(".body-2")


def get_random_products(session, categories):
    # Dentro de todas las opciones que tenemos (zapataillas, sudaderas, ...) escogemos un tipo de producto random
    category = random.choice(categories)
    # Si coge un elemento que no queremos no lo tenemos en cuenta. Filtramos para que solo nos coja la ropa
    while category.tag != "a" and category.text != "Toda la ropa":
        category = random.choice(categories)
    # Una vez seleccionado el tipo producto de forma aleatoria vamos a la pagina de estos productos a traves de su
    # enlace href.
    products_page = session.get(category.attrs["href"])
    # Definimos cual es la class de los modelos del tipo de producto seleccionado. Seleccionamos un modelo aleatorio
    elements = products_page.html.find(".product-card__link-overlay")
    final_product = random.choice(elements)
    # Vamos a la página del producto y obtenemos su precio
    final_product_page = session.get(final_product.attrs["href"])
    product_price = final_product_page.html.find(".product-price", first=True).text
    product_name = final_product_page.html.find("#pdp_product_title", first=True).text
    product_image_src = final_product_page.html.find(".css-viwop1", first=True).attrs["src"]

    final_price = float(product_price.replace("€", "").replace(",", "."))

    return final_price, product_name, product_image_src


def show_image(session, product_image_src):
    img_downloaded = session.get(product_image_src)
    image = Image.open(BytesIO(img_downloaded.content))
    image.show()


def players_and_rules():
    # We define the name of the players
    speak("El nombre del primer jugador es...")
    player1 = hear_me()
    speak("El nombre del segundo jugador es...")
    player2 = hear_me()
    NUMBER_OF_ROUNDS = 2
    speak("El jugador que más se acerque al precio sin pasarse recibirá un punto. El primero en llegar a {} "
          "puntos gana.".format(NUMBER_OF_ROUNDS))

    return NUMBER_OF_ROUNDS, player1, player2


def gameplay(final_price, player1, player2, score_player1, score_player2):
    speak("¿{} cuál crees que es su precio?".format(player1))
    player1_guess = hear_price_and_get_number()
    speak("¿{} cuál crees que es su precio?".format(player2))
    player2_guess = hear_price_and_get_number()

    if player1_guess == player2_guess:
        speak("Ambos jugadores habéis escogido el mismo precio. Ninguno de los dos gana puntos.")
    elif player1_guess < final_price < player2_guess:
        speak("{} se ha acercado más y {} se ha pasado. El precio era {}".format(player1, player2, final_price))
        score_player1 += 1
        speak("La puntuación de {} es {} y la de {} es de {}"
              .format(player1, score_player1, player2, score_player2))
    elif player2_guess < final_price < player1_guess:
        speak("{} se ha acercado más y {} se ha pasado. El precio era {}".format(player2, player1, final_price))
        score_player2 += 1
        speak("La puntuación de {} es {} y la de {} es de {}"
              .format(player1, score_player1, player2, score_player2))
    elif player1_guess > final_price and player2_guess > final_price:
        speak("Ambos os habéis pasado del precio. El precio era {}".format(player2, player1, final_price))
    elif player1_guess < final_price and player2_guess < final_price and abs(final_price - player1_guess) < abs(
            final_price - player2_guess):
        speak("{} se ha acercado más. El precio era {}".format(player1, final_price))
        score_player1 += 1
        speak("La puntuación de {} es {} y la de {} es de {}"
              .format(player1, score_player1, player2, score_player2))
    elif player1_guess < final_price and player2_guess < final_price and abs(final_price - player2_guess) < abs(
            final_price - player1_guess):
        speak("{} se ha acercado más. El precio era {}".format(player2, final_price))
        score_player2 += 1
        speak("La puntuación de {} es {} y la de {} es de {}"
              .format(player1, score_player1, player2, score_player2))

    return score_player1, score_player2


def main():
    session = HTMLSession()
    speak("Bienvenidos al precio justo. Vamos a intentar adivinar los precios de algunos productos")
    NUMBER_OF_ROUNDS, player1, player2 = players_and_rules()

    score_player1 = 0
    score_player2 = 0

    while True:
        categories = get_product_categories(session)
        final_price, product_name, product_image_src = get_random_products(session, categories)
        speak("El nombre del producto es {}.".format(product_name))
        print(product_name)
        show_image(session, product_image_src)
        score_player1, score_player2 = gameplay(final_price, player1, player2, score_player1, score_player2)
        if score_player1 >= NUMBER_OF_ROUNDS:
            speak("El ganador es {}".format(player1))
            print("El ganador es {}".format(player1))
            break

        elif score_player2 >= NUMBER_OF_ROUNDS:
            speak("El ganador es {}".format(player2))
            print("El ganador es {}".format(player2))
            break


if __name__ == "__main__":
    main()
