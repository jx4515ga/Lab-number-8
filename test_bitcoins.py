import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoins

class TestBitCoins(TestCase):

    # Testing the converision is the correct 
    @patch('bitcoins.requests_rate')
    def test_convert(self, mock_rate ):
        mock_rate_float = 1234.56
        example_api_response={'bpi': 'USD', 'rate_float': mock_rate_float}
        mock_rate.side_effect = [example_api_response]
        conversion = bitcoins.math_conversion(100, mock_rate_float)
        self.assertEqual(123456, conversion)

    # Testing user can only enter numbers 
    @patch('builtins.input', side_effect=['2', '', 'cat', 'sdfa', 'dfs5'])
    def test_get_coins_input(self, mock_input):
        coins = bitcoins.get_coins()
        self.assertEqual(2, coins)
    
    #testing that user can not use negative numbers 
    @patch('builtins.input', side_effect=['5', '-5', '-1000', '0', '-45'])
    def test_get_coins_negative(self, mock_input):
        coins = bitcoins.get_coins()
        self.assertEqual(5, coins)

    # Testing the amount of bitcoins because people won't have that much of bitcoins
    @patch('builtins.input', side_effect=['50000000000000000', '10', '-100000000000000', '30000000000000000', '-4000000000000000050005'])
    def test_get_coins_high_numbers(self, mock_input):
        coins = bitcoins.get_coins()
        self.assertNotEqual(10, coins)



if __name__ == "__main__":
    unittest.main()
