from time import sleep
from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

url = "https://www.sivasdescalzo.com/es/p/air-jordan-12-retro-sp-dv1758-108"

session = HTMLSession()

product_page = session.get(url)
found = product_page.html.find("#maincontent")

if len(found) > 0:
    driver = webdriver.Firefox()
    driver.get(url)
    sleep(1)
    def check_stock(url, session):
        while True:
            r = session.get(url)
            buy_zone = r.html.find("#product-addtocart-button")
            if len(buy_zone) > 0:
                print("HAY STOCK!!")
                break
            else:
                print("Sigue sin haber stock :(")
            sleep(30)

    def decline_cookies(url, session):
        driver.find_element(By.CLASS_NAME, "amgdprcookie-button.-settings").click()
        #sleep(1)
        driver.find_element(By.CLASS_NAME, "amgdprcookie-done").click()
        sleep(2)

    def choose_size(url, session):
        driver.find_element(By.ID, "option-label-size_us-138-item-114").click()

    def add_to_shopping_cart(url, session):
        driver.find_element(By.ID, "product-addtocart-button").click()
        sleep(2)
        driver.find_element(By.CLASS_NAME, "btn-primary.btn--full.mb-3").click()

    def log_in_account(url, session):
        global form_password
        is_form_loaded = False
        form = None
        while not is_form_loaded:
            try:
                form = driver.find_element(By.CLASS_NAME, "field ")
                is_form_loaded = True
            except NoSuchElementException:
                print("Puess no esta el formulario...")

        email = form.find_element(By.CLASS_NAME, "input-text.boxed")
        email.send_keys("blablabla@gmail.com")

        driver.find_element(By.CLASS_NAME, "general-button.cta").click()
        driver.find_element(By.CLASS_NAME, "link-list").click()

        is_form_loaded = False
        form = None
        while not is_form_loaded:
            try:
                form_password = driver.find_element(By.CLASS_NAME, "inp-pass-input.boxed")
                is_form_loaded = True
            except NoSuchElementException:
                print("Puess no esta el formulario...")

        password = form_password.find_element(By.CLASS_NAME, "input-text.boxed")
        password.send_keys("tomate11")
        sleep(1)
        driver.find_element(By.CLASS_NAME, "general-button.cta").click()


    def main():
        check_stock(url,session)
        decline_cookies(url, session)
        choose_size(url, session)
        add_to_shopping_cart(url, session)
        log_in_account(url, session)

    if __name__ == "__main__":
        main()