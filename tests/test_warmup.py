import unittest
from tasks.warmup import warmup_one, warmup_two


class TestWarmup(unittest.TestCase):

    def test_warmup_one_wrong_input_data(self):
        """
        Provide wrong input parameters.
        We expect "Wrong input data" as a result
        """
        self.assertEqual('Wrong input data', warmup_one(13))

    def test_warmup_one_valid_input_data(self):
        """
        Provide valid input parameters "abcd".
        We expect ['aBcD','AbCd'] as a result
        """
        self.assertEqual(['aBcD', 'AbCd'], warmup_one('abcd'))

    def test_warmup_two_wrong_input_data(self):
        """
        Provide wrong input parameters.
        We expect "Wrong input data" as a result
        """
        self.assertEqual('Wrong input data', warmup_two(13))

    def test_warmup_two_valid_input_data(self):
        """
        Provide valid input parameters.
        We expect dict with letter:quantity pairs as a result
        """
        self.assertEqual({"a": 3, "b": 2}, warmup_two("aaabbc"))
        self.assertEqual({"a": 3, "b": 2}, warmup_two("aAabBc"))
        self.assertEqual({}, warmup_two("aBcDeF"))
        self.assertEqual({"a": 4, "b": 2, "r": 3}, warmup_two("RabarbArka"))
