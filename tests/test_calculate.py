import unittest
import datetime
from modules.calculate import Calculate

class TestCalculate(unittest.TestCase):

    def test_adjust_longitudes_no_discontinuity(self):
        """Test that longitudes without discontinuity remain unchanged."""
        longitudes = [10, 20, 30]
        adjusted = Calculate.adjust_longitudes(longitudes)
        self.assertEqual(adjusted, [10, 20, 30])

    def test_adjust_longitudes_360_crossing(self):
        """Test that crossing from 350 to 10 is handled correctly."""
        longitudes = [350, 355, 5, 10]
        # Expected: 350, 355, 365, 370 (adding 360 to the values after crossing)
        expected = [350, 355, 365, 370]
        adjusted = Calculate.adjust_longitudes(longitudes)
        self.assertEqual(adjusted, expected)

    def test_adjust_longitudes_retrograde(self):
        """Test that crossing from 10 to 350 (retrograde) is handled correctly."""
        longitudes = [10, 5, 355, 350]
        # Expected: 10, 5, -5, -10 (subtracting 360)
        expected = [10, 5, -5, -10]
        adjusted = Calculate.adjust_longitudes(longitudes)
        self.assertEqual(adjusted, expected)

    def test_calculate_zodiac_sign(self):
        """Test zodiac sign calculation."""
        self.assertEqual(Calculate.calculate_zodiac_sign(15), "Aries")
        self.assertEqual(Calculate.calculate_zodiac_sign(45), "Taurus")
        self.assertEqual(Calculate.calculate_zodiac_sign(350), "Pisces")

    def test_sign_to_value(self):
        """Test sign to value conversion."""
        self.assertEqual(Calculate.sign_to_value("Aries"), 0)
        self.assertEqual(Calculate.sign_to_value("Pisces"), 11)

if __name__ == '__main__':
    unittest.main()
