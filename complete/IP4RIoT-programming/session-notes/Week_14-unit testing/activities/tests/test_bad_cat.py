import unittest
from bad_cat import Cat

class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Whiskers", "striped")

    def test_cat_has_a_name(self):
        self.assertEqual(self.cat.name, "Whiskers")

    def test_cat_has_a_coat(self):
        self.assertEqual(self.cat.coat, "striped")  # This will fail

    def test_cat_speaks(self):
        expected = "Whiskers says meow in a striped coat"
        self.assertEqual(self.cat.speak(), expected)  # Will also fail due to .coat missing

if __name__ == "__main__":
    unittest.main()
