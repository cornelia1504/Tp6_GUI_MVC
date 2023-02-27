# encoding : utf8
"""tests the functionality of the Model class,
which manages the data of the application."""
import unittest
from model import Model

class TestModel(unittest.TestCase):
    
    def test_read_file(self):
        """checks that the data read from the file matches the expected values"""
        model = Model("test_animals.txt")
        # test the method read_file()
        model.read_file()
        # Verify the dictionary
        self.assertEqual(len(model.dico_animaux), 5)
        self.assertEqual(model.dico_animaux["Human"].name, "Cornelia")
        self.assertEqual(model.dico_animaux["Human"].age, "21")
        self.assertEqual(model.dico_animaux["Human"].diet, "omnivore")
        self.assertEqual(model.dico_animaux["Human"].foot, "2")
        self.assertEqual(model.dico_animaux["Cat"].name, "Art")
        self.assertEqual(model.dico_animaux["Cat"].age, "2")

##Todo test of all methodes
