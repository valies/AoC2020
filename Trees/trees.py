class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(line.rstrip())
        return a
        

class TreeFlyer():

    @classmethod
    def fly(cls, lines, right, down):
        number_of_trees = lines[0][0].count("#")
        character_index = 0
        line_index = down
        for i in range(down, len(lines), down):
            if line_index % down == 0:
                line = lines[i]
                character_index += right
                character_index %= len(line)
                number_of_trees += line[character_index].count("#")
            line_index += down
        return int(number_of_trees)

    @classmethod
    def all_of_the_slopes(cls, lines):
        result = 1
        slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        for slope in slopes:
            slope_result = TreeFlyer.fly(lines, slope[0], slope[1])
            result = result * slope_result
        return int(result)


if __name__ == '__main__':
    lines = FileReader.read_file("input.txt")
    product = TreeFlyer.all_of_the_slopes(lines)
    print(product)
