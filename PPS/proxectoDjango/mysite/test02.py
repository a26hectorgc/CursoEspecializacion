from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time


class TestApp(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()

        options = webdriver.ChromeOptions()

        # executa Chrome sen mostrar a xanela gráfica
        # options.add_argument("--headless=new")

        # gardar o navegador como atributo da clase (cls)
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        time.sleep(5)  # Agardar 5 segundos

        self.driver.quit()

        super().tearDown()

    def test_admin_page(self):
        self.driver.get(self.live_server_url + "/admin/")
        print("Título:", self.driver.title)

        # Comprobar o título da páxina
        self.assertIn("Log in | Django site admin", self.driver.title)
