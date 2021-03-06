import re

ecl_matches = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
four_digits_regex = re.compile(r'^\d{4}$')
cm_regex = re.compile(r'\d+cm$')
in_regex = re.compile(r'\d+in$')
hcl_regex = re.compile('^#[A-Fa-f0-9]{6}$')
pid_regex = re.compile(r'^\d{9}$')


class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(line)
        return a


class PassportChecker():

    @classmethod
    def identify_passports(cls, lines):
        passports = []
        passport = ""
        lines.append("end")
        for line in lines:
            if line == "\n" or line == "" or line == "end":
                passports.append(passport)
                passport = ""
            else:
                if passport == "":
                    passport += line.rstrip()
                else:
                    passport += " " + line.rstrip()
        return passports

    @classmethod
    def validate_passports_v1(cls, passports):
        valid_passports = 0
        matches = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
        for passport in passports:
            if passport != "\n" and passport is not None:
                if all(x in passport for x in matches):
                    valid_passports += 1
        return valid_passports

    @classmethod
    def validate_passports_v2(cls, passports):
        valid_passports = 0
        key_matches = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
        for passport in passports:
            if passport != "\n" and passport is not None:
                if all(x in passport for x in key_matches):
                    if PassportChecker.validate_passport(passport):
                        valid_passports += 1
        return valid_passports

    @classmethod
    def validate_passport(cls, passport):
        ecl_matches = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        global four_digits_regex
        global cm_regex
        global in_regex
        global hcl_regex
        global pid_regex
        elements = dict(y.split(":") for y in passport.split(" "))
        elements_sorted = dict(sorted(elements.items(), key=lambda x: x[0]))
        for key, value in elements_sorted.items():
            if key == "byr" and not (re.match(four_digits_regex, value) and 1920 <= int(value) <= 2002):
                return False
            if key == "ecl" and not (any(x == value for x in ecl_matches)):
                return False
            if key == "eyr" and not (re.match(four_digits_regex, value) and 2020 <= int(value) <= 2030):
                return False
            if key == "hcl" and not (re.match(hcl_regex, value)):
                return False
            if key == "hgt" and not (((re.match(cm_regex, value) and 150 <= int(value.replace("cm", "")) <= 193) or (re.match(in_regex, value) and 59 <= int(value.replace("in", "")) <= 76))):
                return False
            if key == "iyr" and not (re.match(four_digits_regex, value) and 2010 <= int(value) <= 2020):
                return False
            if key == "pid" and not (re.match(pid_regex, value)):
                return False
        return True


if __name__ == '__main__':
    lines = FileReader.read_file("input.txt")
    passports = PassportChecker.identify_passports(lines)
    print(PassportChecker.validate_passports_v1(passports))
    print(PassportChecker.validate_passports_v2(passports))
