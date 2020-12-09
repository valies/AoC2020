class Calculator():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(int(line.rstrip()))
        return a

    @classmethod
    def find_two(cls, a):
        i = 0
        while i < len(a):
            j = 0
            while j < len(a):
                if (i != j):
                    value1 = a[i]
                    value2 = a[j]
                    if(value1 + value2 == 2020):
                        return value1 * value2
                j += 1
            i += 1
        return "nothing found"

    @classmethod
    def find_three(cls, a):
        i = 0
        while i < len(a):
            j = 0
            while j < len(a):
                k = 0
                while k < len(a):
                    if (i != j and i != k and j != k):
                        value1 = a[i]
                        value2 = a[j]
                        value3 = a[k]
                        if(value1 + value2 + value3 == 2020):
                            return value1 * value2 * value3
                    k += 1
                j += 1
            i += 1


if __name__ == '__main__':
    a = Calculator.read_file("input.txt")
    print(Calculator.find_two(a))
    print(Calculator.find_three(a))
