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

    def testPerimeterCorrectValue(self):
        #test the getPerimeter function returns correct value when length is a non-negative number
        s1 = square(1)
        self.assertAlmostEqual(s1.getPerimeter(),4)
        s2 = square(3.0)
        self.assertEqual(s2.getPerimeter(),12.0)
        s3 = square(2.2)
        self.assertEqual(s3.getPerimeter(),8.8)

    def testperimeterShouldRaiseValueError(self):
        #test getPerimeter should raise a valueerror when length is not non-negative real number
        s1 = square(-1)
        self.assertRaises(ValueError, s1.getPerimeter)
        s2 = square(1j+4)
        self.assertRaises(ValueError, s2.getPerimeter)
        s3 = square(-0.3)
        self.assertRaises(ValueError, s3.getPerimeter)
    def testShouldRaiseValueErrorForNotNumber(self):
        s1 = square(True)
        self.assertRaises(ValueError, s1.getPerimeter)
        s2 = square(False)
        self.assertRaises(ValueError, s2.getPerimeter)
        s3 = square("length")
        self.assertRaises(ValueError, s3.getPerimeter)
if __name__ == '__main__':
    unittest.main()
