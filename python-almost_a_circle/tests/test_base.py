#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        # Créez une instance de la classe Base
        instance1 = Base()
        instance2 = Base()
        instance3 = Base(12)

        # Vérifiez si les identifiants sont attribués correctement
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 12)

class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_invalid_width(self):
        # Test d'une largeur invalide (doit lever une exception TypeError)
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 5)

    def test_negative_width(self):
        # Test d'une largeur négative (doit lever une exception ValueError)
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 5)

    def test_zero_value_width(self):
        # Test d'une largeur égale à zéro (doit lever une exception ValueError)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 6)

    def test_invalid_height(self):
        # Test d'une hauteur invalide (doit lever une exception TypeError)
        with self.assertRaises(TypeError):
            r = Rectangle(5, "invalid")

    def test_negative_height(self):
        # Test d'une hauteur négative (doit lever une exception ValueError)
        with self.assertRaises(ValueError):
            r = Rectangle(5, -5)

    def test_zero_value_width(self):
        # Test d'une hauteur égale à zéro (doit lever une exception ValueError)
        with self.assertRaises(ValueError):
            r = Rectangle(4, 0)

    def test_invalid_x(self):
        # Test d'une position X invalide (doit lever une exception TypeError)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 5, "invalid", 0)

    def test_negative_x(self):
        # Test d'une position X négative (doit lever une exception ValueError)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 5, -5, 0)

    def test_invalid_y(self):
        # Test d'une position Y invalide (doit lever une exception TypeError)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 5, 0, "invalid")

    def test_negative_y(self):
        # Test d'une position Y négative (doit lever une exception ValueError)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 5, 0, -5)

if __name__ == '__main__':
    unittest.main()
