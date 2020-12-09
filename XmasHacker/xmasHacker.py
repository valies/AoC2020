import copy

class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(int(line.rstrip()))
        return a
        

class XmasHacker():

    @classmethod
    def find_culprit_part1(cls, lines, preambles_length):
        for i in range(len(lines)):
            preambles = lines[i:i+preambles_length]
            number = lines[i+preambles_length]
            something_found = 0
            for preamble in preambles:
                preambles_without_preamble = copy.deepcopy(preambles)
                for element in preambles:
                    if preamble == element:
                        preambles_without_preamble.remove(preamble)
                        break
                if number - preamble in preambles_without_preamble:
                    something_found += 1
            if something_found == 0:
                return number
        return "you should not be here"


    @classmethod
    def find_sum_part2(cls, lines, preambles_length):
        number = XmasHacker.find_culprit_part1(lines, preambles_length)
        counter = 0
        while True:
            sum = 0
            numbers = []
            for j in range(len(lines)):
                sum += lines[j+counter]
                numbers.append(lines[j+counter])
                if sum == number:
                    result = min(numbers) + max(numbers)
                    return result
                elif sum > number:
                    counter += 1
                    numbers.clear()
                    break
        return "you should not be here"

            
if __name__ == '__main__':
    lines = FileReader.read_file("xmasHacker/input.txt")
    print(XmasHacker.find_culprit_part1(lines, 25))
    print(XmasHacker.find_sum_part2(lines, 25))
