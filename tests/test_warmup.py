import unittest
from tasks.warmup import warmup_one


class TestWarmup(unittest.TestCase):

    def test_wrong_input_data(self):
        """
        Provide wrong input parameters.
        We expect "Wrong input data" as a result
        """
        self.assertEqual('Wrong input data', warmup_one(13))

    def test_valid_input_data(self):
        """
        Provide valid input parameters "abcd".
        We expect ['aBcD','AbCd'] as a result
        """
        self.assertEqual(['aBcD', 'AbCd'], warmup_one('abcd'))
