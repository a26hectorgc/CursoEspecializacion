from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
import os


from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    # cargar unha BD de test
    fixtures = ["testdb.json"]

    # execútase unha vez antes dos tests da clase
    def setUp(self):
        super().setUp()

        options = webdriver.ChromeOptions()
        if os.environ.get("CHROME_HEADLESS") == "1":
            options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        #     # cerrar o navegador
        time.sleep(5)  # Agardar 5 segundos
        self.driver.quit()
        super().tearDownClass()

    def test_login_error(self):
        # comprobar que falla ao iniciar sesión con datos incorrectos
        self.driver.get("%s%s" % (self.live_server_url, "/admin/login/"))
        self.assertEqual(self.driver.title, "Log in | Django site admin")

        # introducir os datos de login e pulsar o botón “Log in” para entrar
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("non_existen_user")
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("abc")
        self.driver.find_element(By.XPATH, '//input[@value="Log in"]').click()

        # utiliar assertNotEqual para probar que non entrou
        self.assertNotEqual(
            self.driver.title, "Site administration | Django site admin"
        )

    def test_login(self):
        # acceder á páxina de login de admin
        self.driver.get("%s%s" % (self.live_server_url, "/admin/login/"))

        # comprobar que o título da páxina é o esperado
        self.assertEqual(self.driver.title, "Log in | Django site admin")

        # introducir os datos de login e pulsar o botón “Log in” para entrar
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("admin")
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("abcd1234.")
        self.driver.find_element(By.XPATH, '//input[@value="Log in"]').click()
        time.sleep(5)

        # comprobar se se conseguiu entrar
        self.assertEqual(self.driver.title, "Site administration | Django site admin")
