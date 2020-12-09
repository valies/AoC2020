import unittest
from Day7.bags import BagProcessing


class TestBagProcessing(unittest.TestCase):

    def test_bags_part1(self):
        lines = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."]
        bags_tree = BagProcessing.form_bags_tree(lines)
        result = BagProcessing.number_of_bags_part1(bags_tree)
        self.assertEqual(result, 4, "Should be the same.")

    def test_bags_part2(self):
        lines = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."]
        bags_tree = BagProcessing.form_bags_tree(lines)
        result = BagProcessing.number_of_bags_part2(bags_tree)
        self.assertEqual(result, 32, "Should be the same.")


if __name__ == '__main__':
    unittest.main()
