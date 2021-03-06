import unittest
from Day6.customs import CustomsQuestionaire


class TestCustomsIdentifier(unittest.TestCase):

    def test_customs_part1(self):
        lines = ["abc",
                 "",
                 "a",
                 "b",
                 "c",
                 "",
                 "ab",
                 "ac",
                 "",
                 "a",
                 "a",
                 "a",
                 "a",
                 "",
                 "b"]
        customs = CustomsQuestionaire.get_result_part1(lines)
        self.assertEqual(customs, 11, "Should be the same.")

    def test_customs_part2(self):
        lines = ["abc",
                 "",
                 "a",
                 "b",
                 "c",
                 "",
                 "ab",
                 "ac",
                 "",
                 "a",
                 "a",
                 "a",
                 "a",
                 "",
                 "b"]
        customs = CustomsQuestionaire.get_result_part2(lines)
        self.assertEqual(customs, 6, "Should be the same.")
