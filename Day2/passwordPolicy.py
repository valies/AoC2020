class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(line.rstrip())
        return a


class Parser():

    @classmethod
    def parse_password_policy(cls, line):
        splitted_line = line.split(" ")
        integers = splitted_line[0].split("-")
        first_int = int(integers[0])
        second_int = int(integers[1])
        character = splitted_line[1].replace(":", "")
        password = splitted_line[2]
        return PasswordPolicy(first_int, second_int, character, password)


class PasswordPolicy():

    def __init__(self, first_int, second_int, character, password):
        self.first_int = first_int
        self.second_int = second_int
        self.character = character
        self.password = password

    @property
    def first_int(self):
        return self.internal_first_int

    @first_int.setter
    def first_int(self, value):
        self.internal_first_int = value

    @property
    def second_int(self):
        return self.internal_second_int

    @second_int.setter
    def second_int(self, value):
        self.internal_second_int = value

    @property
    def character(self):
        return self.internal_character

    @character.setter
    def character(self, value):
        self.internal_character = value

    @property
    def password(self):
        return self.internal_password

    @password.setter
    def password(self, value):
        self.internal_password = value

    def validate_password_v1(self):
        counter = self.password.count(self.character)
        if counter <= self.second_int and counter >= self.first_int:
            return 1
        return 0

    def validate_password_v2(self):
        if len(self.password) >= self.first_int and len(self.password) >= self.second_int:
            character1 = self.password[self.first_int - 1]
            character2 = self.password[self.second_int - 1]
            if (character1 == self.character) ^ (character2 == self.character):
                return 1
        return 0


if __name__ == '__main__':
    a = FileReader.read_file("input.txt")
    counter_v1 = 0
    counter_v2 = 0
    for line in a:
        p = Parser.parse_password_policy(line)
        counter_v1 += p.validate_password_v1()
        counter_v2 += p.validate_password_v2()
    print(counter_v1)
    print(counter_v2)
