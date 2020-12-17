import unittest
from Day11.seatPlacement import SeatPlacement

class TestSeatPlacement(unittest.TestCase):

    def test_rule_applier_part1(self):
        a = ["L.LL.LL.LL",
            "LLLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLLL",
            "L.LLLLLL.L",
            "L.LLLLL.LL"]
        self.assertEqual(SeatPlacement.rule_applier_part1(a), 37, "Should be the same.")

    def test_rule_applier_part2(self):
        a = ["L.LL.LL.LL",
            "LLLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLLL",
            "L.LLLLLL.L",
            "L.LLLLL.LL"]
        self.assertEqual(SeatPlacement.rule_applier_part2(a), 26, "Should be the same.")


if __name__ == '__main__':
    unittest.main()
