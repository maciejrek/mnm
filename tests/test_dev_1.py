import unittest
from tasks.dev_1 import is_gene_continuously_amplified, string_to_list, split_string, test_data


class TestDev1(unittest.TestCase):
    def test_split_string(self):
        """Provide string in defined format ('x-y/z') and split it to range and total part"""
        self.assertEqual(('1-4', 14), split_string('1-4/14'))

    def test_split_string_empty_string(self):
        """Provide empty string. False is expected as a result"""
        self.assertFalse(split_string(""))

    def test_split_string_wrong_input_data(self):
        """Provide wrong input. Error message is expected as a result"""
        self.assertEqual("Wrong input data", split_string(13))

    def test_string_to_list(self):
        """
        Verify that this method returns list from given string. This is an external method
        """
        self.assertEqual([1, 2, 3], string_to_list('1-3'))
        self.assertEqual([6, 7, 8, 9, 10], string_to_list('6-10'))

    def test_is_gene_continuously_amplified_wrong_input(self):
        """Provide wrong input. Error message is expected as a result"""
        self.assertEqual("Wrong input data", is_gene_continuously_amplified(13))

    def test_is_gene_continuously_amplified(self):
        """
        Simple test of is_gene_continuously_amplified cause i'm getting short on time :D
        """
        expected_result = {"KRAS": True,
                           "TP53": True,
                           "CCNE1": False,
                           "ERBB2": False}
        self.assertEqual(expected_result, is_gene_continuously_amplified(test_data))
