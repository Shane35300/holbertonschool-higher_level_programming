#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_assignment(self):
        # Créez une instance de la classe Base
        instance1 = Base()
        instance2 = Base()
        instance3 = Base(12)

        # Vérifiez si les identifiants sont attribués correctement
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 12)

if __name__ == '__main__':
    unittest.main()
