from factory_class import Factory 
import unittest
import pytest

class TestFactory(unittest.TestCase):

    # instantiating the class so we can test it 
    factory_instance = Factory()

    # test fails when 
    def test_make_naan(self):
        self.assertEqual(self.factory_instance.make_naan('water','bread'), 'naan')

