'''
unittest / numpy.testing
'''

import unittest
from unittest import TestCase
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from pyadic import PAdic, ModP
from fractions import Fraction as Q
from functions import *


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

x1 = PAdic(Q(7, 43), 2, 7)  #1 + 1*2^2 + 1*2^4 + O(2^7)
b1 = np.array([0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 1.])

x2 = PAdic(-31, 2, 7)  #1 + 1*2^5 + 1*2^6 + O(2^7)
b2 = np.array([0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 1.])

x3 = PAdic(200, 2, 7) #1*2^3 + 1*2^6 + 1*2^7 + O(2^10)
b3 = np.array([0., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0.])

x4 = PAdic(12, 2, 7) #1*2^2 + 1*2^3 + O(2^9)
b4 = np.array([0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0.])

x5 = PAdic(Q(5, 34), 2, 7) #1*2^-1 + 1*2 + 1*2^3 + 1*2^4 + O(2^6)
b5 = np.array([0., 0., 0., 0., 0., 1., 1., 0., 1., 0., 1.])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

class TestPowerSeriesToBinary(TestCase):
    
    @staticmethod   
    def test_power_series_to_binary():
        np.testing.assert_array_equal(power_series_to_binary(x1), b1)
        np.testing.assert_array_equal(power_series_to_binary(x2), b2)
        np.testing.assert_array_equal(power_series_to_binary(x3), b3)
        np.testing.assert_array_equal(power_series_to_binary(x4), b4)
        np.testing.assert_array_equal(power_series_to_binary(x5), b5)


if __name__ == '__main__':
    unittest.main()
    
    