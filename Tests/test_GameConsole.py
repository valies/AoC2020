import unittest
from Day8.gameConsole import Accumulator


class TestGameConsole(unittest.TestCase):

    def test_accumulator_part1(self):
        lines = ["nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"]
        instructions = Accumulator.form_instructions(lines)
        result = Accumulator.process_part1(instructions)
        self.assertEqual(result, 4, "Should be the same.")

    def test_accumulator_part1(self):
        lines = ["nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"]
        result = Accumulator.process_part2(lines)
        self.assertEqual(result, 8, "Should be the same.")