import math

class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(line.rstrip())
        return a
        

class SeatFinder():

    @classmethod
    def find_available_seat(cls, lines):
        occupied_seats = []
        for line in lines:
            occupied_seats.append(SeatFinder.get_occupied_seat(line))
        min_seat = min(occupied_seats)
        max_seat = max(occupied_seats)
        print(max_seat)
        for seat in range(min_seat, max_seat):
            if min_seat < seat < max_seat and not(seat in occupied_seats) and seat-1 in occupied_seats and seat-1 in occupied_seats:
                return seat
        return "no seat found"


    @classmethod
    def get_occupied_seat(cls, line):
        line = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        return (int(line[:7], 2) * 8) + int(line[7:], 2)
        

if __name__ == '__main__':
    lines = FileReader.read_file("seat/input.txt")
    seat = SeatFinder.find_available_seat(lines)
    print(seat)