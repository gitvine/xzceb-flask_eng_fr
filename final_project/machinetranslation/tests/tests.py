import unittest
from ..translator import english_to_french,french_to_english

class Test_english_to_french(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(''),'')
        self.assertNotEqual(english_to_french('Man'),'')
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('Man'),'Homme')
        self.assertEqual(english_to_french('Woman'),'Femme')

class Test_french_to_english(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english(''),'')
        self.assertNotEqual(french_to_english('Man'),'')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Homme'),'Man')
        self.assertEqual(french_to_english('Femme'),'Woman')

unittest.main()