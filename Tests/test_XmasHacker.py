import unittest
from XmasHacker.xmasHacker import XmasHacker


class TestXmasHacker(unittest.TestCase):

    def test_xmas_hacker_part1(self):
        lines = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
        result = XmasHacker.find_culprit_part1(lines, 5)
        self.assertEqual(result, 127, "Should be the same.")

    def test_xmas_hacker_part2(self):
        lines = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
        result = XmasHacker.find_sum_part2(lines, 5)
        self.assertEqual(result, 62, "Should be the same.")
