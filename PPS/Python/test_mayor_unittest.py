import unittest

from mayor import mayor


class TestMayor(unittest.TestCase):
    def test_mayor(self):
        self.assertEqual(mayor(30, 2, 3), 30)

    def test_mayor2(self):
        self.assertEqual(mayor(2, 5, -7), 5)

    def test_mayor3(self):
        self.assertEqual(mayor(1.2, 5, -454.454), 5)

    def test_mayor4(self):
        self.assertEqual(mayor(1.2, 5, 454.454), 454.454)


if __name__ == "__main__":
    unittest.main()
