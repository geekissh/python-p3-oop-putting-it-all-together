from shoe import Shoe
import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.size = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "size must be an integer"
