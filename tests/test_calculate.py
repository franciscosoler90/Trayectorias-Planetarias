import unittest
import datetime
from modules.calculate import Calculate

class TestCalculate(unittest.TestCase):

    def test_handle_discontinuities_no_jump(self):
        """Test that longitudes without discontinuity remain unchanged."""
        dates = [1, 2, 3]
        longitudes = [10, 20, 30]
        new_dates, new_longitudes = Calculate.handle_discontinuities(dates, longitudes)
        self.assertEqual(new_dates, [1, 2, 3])
        self.assertEqual(new_longitudes, [10, 20, 30])

    def test_handle_discontinuities_jump_forward(self):
        """Test that crossing from 350 to 10 inserts a break."""
        dates = [1, 2]
        longitudes = [350, 10]
        # Expected: Insert None and duplicate the date of the jump
        expected_dates = [1, 2, 2]
        expected_longitudes = [350, None, 10]

        new_dates, new_longitudes = Calculate.handle_discontinuities(dates, longitudes)
        self.assertEqual(new_dates, expected_dates)
        self.assertEqual(new_longitudes, expected_longitudes)

    def test_handle_discontinuities_jump_backward(self):
        """Test that crossing from 10 to 350 (retrograde) inserts a break."""
        dates = [1, 2]
        longitudes = [10, 350]
        # Expected: Insert None and duplicate the date of the jump
        expected_dates = [1, 2, 2]
        expected_longitudes = [10, None, 350]

        new_dates, new_longitudes = Calculate.handle_discontinuities(dates, longitudes)
        self.assertEqual(new_dates, expected_dates)
        self.assertEqual(new_longitudes, expected_longitudes)

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
