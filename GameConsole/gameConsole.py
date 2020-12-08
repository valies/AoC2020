class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(line.rstrip())
        return a


class Accumulator():

    @classmethod
    def form_instructions(cls, lines):
        instructions = []

        for i in range(len(lines)):
            line = lines[i]
            instruction = line.split(" ")[0]
            move = int(line.split(" ")[1])
            instruction = {"instruction": instruction, "move": move, "used": False}
            instructions.append(instruction)
        return instructions
            

    @classmethod
    def process_part1(cls, instructions):
        instruction_index = 0
        used = False
        accumulator = 0
        while not used:
            this_instruction = instructions[instruction_index]
            move = this_instruction["move"]
            instruction = this_instruction["instruction"]
            used = this_instruction["used"]
            if not used:
                instructions[instruction_index]["used"] = True
                if instruction == "acc":
                    accumulator += move
                    instruction_index += 1
                if instruction == "jmp":
                    instruction_index += move
                if instruction == "nop":
                    instruction_index += 1
        return accumulator


    @classmethod
    def process_part2(cls, lines):
        these_instructions = Accumulator.form_instructions(lines)
        instruction_index = 0
        accumulator = 0
        turned_index = 0
        turned_indexes = []
        while True:
            this_instruction = these_instructions[instruction_index]
            move = this_instruction["move"]
            instruction = this_instruction["instruction"]
            used = this_instruction["used"]
            if used:
                these_instructions = Accumulator.form_instructions(lines)
                instruction_index = 0
                accumulator = 0
                turned_index = 0
                this_instruction = these_instructions[instruction_index]
                move = this_instruction["move"]
                instruction = this_instruction["instruction"]
                used = this_instruction["used"]
            if instruction_index == len(these_instructions)-1:
                if instruction == "acc":
                    accumulator += move
                return accumulator
            if turned_index == 0 and instruction in ("jmp", "nop") and instruction_index not in turned_indexes:
                if instruction == "jmp":
                    these_instructions[instruction_index]["instruction"] = "nop"
                    instruction = "nop"
                elif instruction == "nop" and abs(move) > 0:
                    these_instructions[instruction_index]["instruction"] = "jmp"
                    instruction = "jmp"
                turned_index = instruction_index
                turned_indexes.append(turned_index)
            if not used:
                these_instructions[instruction_index]["used"] = True
                if instruction == "acc":
                    accumulator += move
                    instruction_index += 1
                elif instruction == "jmp":
                    instruction_index += move
                elif instruction == "nop":
                    instruction_index += 1
        return "you should not be here"
            

if __name__ == '__main__':
    lines = FileReader.read_file("gameConsole/input.txt")
    instructions = Accumulator.form_instructions(lines)
    print(Accumulator.process_part1(instructions))
    print(Accumulator.process_part2(lines))
