# módulo para controlar o navegador
from selenium import webdriver

# permite esperar a que certa condición ocorra antes de continuar. Axuda con certos elementos que poden tardar tempo en cargarse
from selenium.webdriver.support.ui import WebDriverWait

# proporciona condicións predefinidas que pode usar WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# módulo para localizar elementos HTML
from selenium.webdriver.common.by import By

import time

import os

from selenium.webdriver.support.select import Select

# iniciar Chrome con opcións básicas
options = webdriver.ChromeOptions()

# para que chrome se manteña aberto cando remate o proceso, se non se envía o comando quit
options.add_experimental_option("detach", True)

# non se mostra o navegador
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Crear unha espera máxima de 10 segundos
    wait = WebDriverWait(driver, 10)

    # acceder ao título da páxina
    title = driver.title
    print("Page title:", title)

    # tempo de espera por se hai elementos que non están dispoñibles inmediatamente
    driver.implicitly_wait(0.5)

    # acceder á caixa de texto polo atributo name
    text_box = driver.find_element(by=By.NAME, value="my-text")

    # escribir na caixa de texto
    text_box.send_keys("Selenium")

    time.sleep(3)

    # password

    text_pass = driver.find_element(by=By.NAME, value="my-password")

    text_pass.send_keys("abc123.")

    time.sleep(3)

    # textarea

    text_area = driver.find_element(by=By.NAME, value="my-textarea")

    text_area.send_keys("textarea.")

    time.sleep(3)

    # #password

    # text_disabled = driver.find_element(by=By.NAME, value="my-disabled")

    # text_disabled.__setattr__(
    #     placeholder: "enabled",
    #     /

    # )

    # text_disabled.send_keys("abc123.")

    time.sleep(3)

    # # readonly

    # text_readonly = driver.find_element(by=By.NAME, value="my-readonly")

    # text_readonly.send_keys("readonly")

    # time.sleep(3)

    # select

    text_select = driver.find_element(by=By.NAME, value="my-select")

    select = Select(text_select)

    selection = driver.find_element(By.CSS_SELECTOR, "option[value=1]")

    selection.select_by_index(1)

    time.sleep(3)

    # dropdown

    # text_datalist = driver.find_element(by=By.NAME, value="my-datalist")

    # text_datalist.send_keys("s")

    # text_datalist.

    # time.sleep(3)

    # input

    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "requisitos.txt")
    )

    text_file = driver.find_element(by=By.NAME, value="my-file")

    text_file.send_keys(upload_file)

    time.sleep(3)

    # # acceder ao botón mediante selector CSS
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # # facer click no botón e enviar o formulario
    # submit_button.click()


finally:
    print("Confirmation message:")

# driver.quit()
