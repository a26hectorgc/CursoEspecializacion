import unittest
from calculadora import sumar, restar, multiplicar, dividir


# Crear unha clase TestCalculadora que estenda de unittest.TestCase.
# Recoméndase usar nomes significativos para o nome da clase
class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_exception(self):
        self.assertRaises(ValueError, dividir, 2, 0)


if __name__ == "__main__":
    unittest.main()
