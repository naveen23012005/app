import unittest
from app import add, sub, mul


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(24, 3), 21)

    def test_mul(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(5, 0), 0)


if __name__ == "__main__":
    unittest.main()