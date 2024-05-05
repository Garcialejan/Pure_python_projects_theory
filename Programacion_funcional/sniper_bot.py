from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Definimos las URL del producto que queremos comprar
url_pccomponentes = "https://www.pccomponentes.com/msi-geforce-rtx-4080-ventus-3x-e-oc-16gb-gddr6x-dlss3"
url_coolmod = "https://www.coolmod.com/msi-geforce-rtx-4080-ventus-3x-oc-16gb-gddr6x/?_gl=1*5s79by*_up*MQ..&gclid=Cj0KCQiA6vaqBhCbARIsACF9M6kCnnxwpF_v-ElEkuI1McadFrRcKSfyVYeMnA7-qdE2p2Yz1Irv1sIaAgyfEALw_wcB"

# Se crea una sesión HTML utilizando requests_html para realizar solicitudes y procesar el contenido HTML.
# Necesario instalarlo con "pip install requests-html". Lo que se hace es permitir a Python que acceda a una página web.
session = HTMLSession()

#REALIZAMOS PRIMERO EL CÓDIGO PARA LA PÁGINA DE COOLMOD.

# Ahora se realiza una solicitud HTTP para obtener el contenido HTML de la página del producto. Obtenemos el código
product_page = session.get(url_pccomponentes)

# Se busca un elemento con el ID del HTML para comprobar la disponibilidad del producto. Si hay, automatizamos la compra
found = product_page.html.find("#pdp-add-to-cart-sticky")
if len(found) > 0:
    driver = webdriver.Chrome() # Abrimos un navegador Chrome para que el programa navegue en al web
    driver.get(url_pccomponentes)
    sleep(1)
    driver.find_element_by_class_name("cookiesAcceptAll").click()
    driver.find_element_by_class_name("sc-iGgWBj eHXVeU sc-bfUCjU hwinbZ").click()
    driver.find_element_by_class_name("sc-iGgWBj fBITwV sc-bKNmIE cGPzJX").click()

# Comprobamos que el formulario para ingresar nuestra cuenta existe y se ha cargado correctamente.
# Muy útil si nuestros tiempos de carga son lentos
    is_form_loaded = False
    form = None
    while not is_form_loaded:
        try:
           form = driver.find_element_by_class_name("sc-jIGnZt euUYOm sc-iHmpnF glnAlU").click()
        except NoSuchElementException:
            print("No se puede iniciar sesión. Ha habido algún fallo")

# Encontramos los formularios que hay que rellenar para iniciar sesión en nuestra cuenta
    email = form.find_element_by_name("username")
    password = form.find_element_by_name("password")

# Indicamos nuestro correo y constraseña de inicio de sesión
    email.send_keys("garcialejan@gmail.com")
    password.send_keys("147258369")
    driver.find_element_by_class_name("sc-iGgWBj eHXVeU").click()
