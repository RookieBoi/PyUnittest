import unittest
from square import square
class squareTest(unittest.TestCase):

    def testCorrectValue(self):
        #test the function correctly computes the area of the square when length >= 0
        s = square(0)
        self.assertAlmostEqual(s.getArea(),0)
        s1 = square(1.5)
        self.assertAlmostEqual(s1.getArea(),2.25)
        s2 = square(4.0)
        self.assertAlmostEqual(s2.getArea(), 16.0)

    def testNegativeValueShouldRaiseError(self):
        #test the function raises a valueError when the lenght is a negative value
        s = square(-1)
        self.assertRaises(ValueError,s.getArea)
        s1 = square(-0.01)
        self.assertRaises(ValueError, s1.getArea)
        s2 = square(-3)
        self.assertRaises(ValueError, s2.getArea)

    def testNonRealNumberShouldRaiseError(self):
        # test the function raises an error when the length is not a real number
        s = square(1j+6)
        self.assertRaises(ValueError,s.getArea)
        s1 = square(2j+1)
        self.assertRaises(ValueError, s1.getArea)
        s2 = square(True)
        self.assertRaises(ValueError, s2.getArea)
        s3 = square('length')
        self.assertRaises(ValueError, s3.getArea)
        
if __name__ == '__main__':
    unittest.main()
