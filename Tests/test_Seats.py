import unittest
from Day5.seat import SeatFinder


class TestSeatFinder(unittest.TestCase):

    def test_get_occupied_seat(self):
        code = "FBFBBFFRLR"
        result = SeatFinder.get_occupied_seat(code)
        self.assertEqual(result, 357, "Should be the same.")

        code = "BFFFBBFRRR"
        result = SeatFinder.get_occupied_seat(code)
        self.assertEqual(result, 567, "Should be the same.")

        code = "FFFBBBFRRR"
        result = SeatFinder.get_occupied_seat(code)
        self.assertEqual(result, 119, "Should be the same.")

        code = "BBFFBBFRLL"
        result = SeatFinder.get_occupied_seat(code)
        self.assertEqual(result, 820, "Should be the same.")

        code = "FFFFFFFLLL"
        result = SeatFinder.get_occupied_seat(code)
        self.assertEqual(result, 0, "Should be the same.")

        code = "BBBBBBBRRR"
        result = SeatFinder.get_occupied_seat(code)
        self.assertEqual(result, (127 * 8) + 7, "Should be the same.")
