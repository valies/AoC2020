import unittest
from Day2.passwordPolicy import PasswordPolicy
from Day2.passwordPolicy import Parser


class TestPasswordPolicy(unittest.TestCase):

    def test_parser(self):
        line = "2-9 c: ccccccccc"
        result = Parser.parse_password_policy(line)
        p = PasswordPolicy(2, 9, "c", "ccccccccc")
        self.assertEqual(p.first_int, result.first_int, "Should be the same")
        self.assertEqual(p.second_int, result.second_int, "Should be the same")
        self.assertEqual(p.character, result.character, "Should be the same")
        self.assertEqual(p.password, result.password, "Should be the same")

    def test_passwords_v1(self):
        a = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        counter = 0
        for line in a:
            p = Parser.parse_password_policy(line)
            counter += p.validate_password_v1()
        self.assertEqual(counter, 2, "Should be the same.")

    def test_passwords_v2(self):
        a = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        counter = 0
        for line in a:
            p = Parser.parse_password_policy(line)
            counter += p.validate_password_v2()
        self.assertEqual(counter, 1, "Should be the same.")


if __name__ == '__main__':
    unittest.main()
