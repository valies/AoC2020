import copy

class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(line.rstrip())
        return a
        

class SeatPlacement():

    @classmethod
    def rule_applier_part1(cls, seats):
        occupied_counter = 0
        new_seats = copy.deepcopy(seats)
        while True:
            for i in range(len(seats)):
                row = seats[i]
                for j in range(len(row)):
                    seat = list(row)[j]
                    if seat != ".":
                        adjacent_seats = SeatPlacement.get_adjacent_seats(i, j, seats)
                        if seat == "L" and "#" not in adjacent_seats:
                            new_seats[i] = SeatPlacement.toggle_seat_in_row(row, j)
                            row = new_seats[i]
                        elif seat == "#" and adjacent_seats.count("#") >= 4:
                            new_seats[i] = SeatPlacement.toggle_seat_in_row(row, j)
                            row = new_seats[i]
            if seats == new_seats:
                for row in new_seats:
                    occupied_counter += row.count("#")
                return occupied_counter
            else:
                seats = copy.deepcopy(new_seats)
        raise Exception("Shite.")  


    @classmethod
    def rule_applier_part2(cls, seats):
        occupied_counter = 0
        new_seats = copy.deepcopy(seats)
        while True:
            for i in range(len(seats)):
                row = seats[i]
                for j in range(len(row)):
                    seat = list(seats[i])[j]
                    if seat != ".":
                        visible_seats = SeatPlacement.get_visible_seats(i, j, seats)
                        if seat == "L" and "#" not in visible_seats:
                            new_seats[i] = SeatPlacement.toggle_seat_in_row(row, j)
                            row = new_seats[i]
                        elif seat == "#" and visible_seats.count("#") >= 5:
                            new_seats[i] = SeatPlacement.toggle_seat_in_row(row, j)
                            row = new_seats[i]
            if seats == new_seats:
                for row in new_seats:
                    occupied_counter += row.count("#")
                return occupied_counter
            else:
                seats = copy.deepcopy(new_seats)
        raise Exception("Shite.")  


    @classmethod
    def toggle_seat_in_row(cls, row, column_index):
        seat = row[column_index]
        if seat == "#":
            return row[:column_index]+"L"+row[column_index+1:]
        if seat == "L":
            return row[:column_index]+"#"+row[column_index+1:]


    @classmethod
    def get_visible_seats(cls, row_index, column_index, seats):
        visible_seats = []
        i = row_index
        j = column_index
        number_of_rows = len(seats)
        number_of_columns = len(seats[0])
        for x in range(1, max(number_of_rows, number_of_columns)):
            if i-x >= 0:
                this_seat = list(seats[i-x])[j]
                if this_seat in ["#","L"]:
                    visible_seats.append(this_seat)
                    break
            else:
                break
        for x in range(1, max(number_of_rows, number_of_columns)):
            if i-x >= 0 and j+x < number_of_columns:
                this_seat = list(seats[i-x])[j+x]
                if this_seat in ["#","L"]:
                    visible_seats.append(this_seat)
                    break
            else:
                break
        for x in range(1, max(number_of_rows, number_of_columns)):
            if j+x < number_of_columns:
                this_seat = list(seats[i])[j+x]
                if this_seat in ["#","L"]:
                    visible_seats.append(this_seat)
                    break
            else:
                break
        for x in range(1, max(number_of_rows, number_of_columns)):
            if i+x < number_of_rows and j+x < number_of_columns:
                this_seat = list(seats[i+x])[j+x]
                if this_seat in ["#","L"]:
                    visible_seats.append(this_seat)
                    break
            else:
                break
        for x in range(1, max(number_of_rows, number_of_columns)):
            if i+x < number_of_rows:
                this_seat = list(seats[i+x])[j]
                if this_seat in ["#","L"]:
                    visible_seats.append(this_seat)
                    break
            else:
                break
        for x in range(1, max(number_of_rows, number_of_columns)):
            if i+x < number_of_rows and j-x >= 0:
                this_seat = list(seats[i+x])[j-x]
                if this_seat in ["#","L"]:
                    visible_seats.append(this_seat)
                    break
            else:
                break
        for x in range(1, max(number_of_rows, number_of_columns)):
            if j-x >= 0:
                this_seat = list(seats[i])[j-x]
                if this_seat in ["#","L"]:
                    visible_seats.append(this_seat)
                    break
            else:
                break
        for x in range(1, max(number_of_rows, number_of_columns)):
            if i-x >= 0 and j-x >= 0:
                this_seat = list(seats[i-x])[j-x]
                if this_seat in ["#","L"]:
                    visible_seats.append(this_seat)
                    break
            else:
                break
        return visible_seats


    @classmethod
    def get_adjacent_seats(cls, row_index, column_index, seats):
        adjacent_seats = []
        row_start = 0 if row_index == 0 else row_index-1
        row_end = len(seats)-1 if row_index == len(seats)-1 else row_index+1
        column_start = column_index if column_index == 0 else column_index-1
        column_end = column_index+1
        for r in range(row_start,row_end+1,1):
            row = seats[r]
            seats_in_row = list(row)
            if column_index == len(seats_in_row)-1:
                column_end = len(seats_in_row)-1
            for c in range(column_start,column_end+1,1):
                if not (row_index == r and column_index == c):
                    adjacent_seats.extend(seats_in_row[c])
        return adjacent_seats

            
if __name__ == '__main__':
    lines = FileReader.read_file("Day11/input.txt")
    print(SeatPlacement.rule_applier_part1(lines))
    print(SeatPlacement.rule_applier_part2(lines))