class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(line)
        return a
        

class CustomsQuestionaire():

    @classmethod
    def get_result_part1(cls, lines):
        sum = 0
        group_answers = []
        lines.append("end")
        for line in lines:
            if line == "\n" or line == "" or line == "end":
                number_of_answers = len(set(group_answers))
                sum += number_of_answers
                group_answers = []
            else: 
                group_answers.extend(char for char in line.rstrip())
        return sum


    @classmethod
    def get_result_part2(cls, lines):
        sum = 0
        person_answers = []
        lines.append("end")
        for line in lines:
            if line == "\n" or line == "" or line == "end":
                string = "".join(person_answers)
                number_of_persons = len(person_answers)
                unique_answers = set(string)
                for a in unique_answers:
                    if string.count(a) >= number_of_persons:
                        sum += 1
                person_answers = []
            else: 
                person_answers.append("".join(set(line.rstrip())))
        return sum


if __name__ == '__main__':
    lines = FileReader.read_file("customs/input.txt")
    print(CustomsQuestionaire.get_result_part1(lines))
    print(CustomsQuestionaire.get_result_part2(lines))