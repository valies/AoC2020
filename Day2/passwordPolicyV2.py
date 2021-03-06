counter_part1 = 0
counter_part2 = 0
with open("input.txt") as my_file:
    for line in my_file:
        splitted_line = line.split(" ")
        integers = splitted_line[0].split("-")
        character = splitted_line[1].replace(":", "")
        password = splitted_line[2]
        occurrences = password.count(character)
        if int(integers[0]) <= occurrences <= int(integers[1]):
            counter_part1 += 1
        if int(integers[0]) <= len(password) >= int(integers[1]):
            if (password[int(integers[0]) - 1] == character) ^ (password[int(integers[1]) - 1] == character):
                counter_part2 += 1
print(counter_part1)
print(counter_part2)
