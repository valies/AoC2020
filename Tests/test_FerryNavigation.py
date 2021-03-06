import unittest
from Day12.ferryNavigation import FerryNavigation


class TestFerryNavigation(unittest.TestCase):

    def test_navigation_part1(self):
        lines = ["F10",
                 "N3",
                 "F7",
                 "R90",
                 "F11"]
        result = FerryNavigation.navigate_part1(lines)
        self.assertEqual(result, 25, "Should be the same.")

    def test_navigation_part2(self):
        lines = ["F10",
                 "N3",
                 "F7",
                 "R90",
                 "F11"]
        result = FerryNavigation.navigate_part2(lines)
        self.assertEqual(result, 286, "Should be the same.")
