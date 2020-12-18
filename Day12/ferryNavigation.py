class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                text = line.rstrip().replace("S", "N-").replace("W", "E-").replace("L","R-")
                a.append(text)
        return a
        

class FerryNavigation():

    @classmethod
    def navigate_part1(cls, lines):
        position_north = 0
        position_east = 0
        face = "E"
        faces = ["N", "E", "S", "W"]
        for line in lines:
            command = line[0]
            move = int(line[1:])
            turn = int(move/90)
            if command == "R":
                face_index = faces.index(face)
                new_index = face_index + turn
                while new_index >= 4:
                    new_index = face_index + turn - 4
                face = faces[new_index]
            elif command == "N":
                position_north += move
            elif command == "E":
                position_east += move
            elif command == "F":
                if face == "N":
                    position_north += move
                elif face == "E":
                    position_east += move
                elif face == "S":
                    position_north -= move
                elif face == "W":
                    position_east -= move
        return abs(position_north) + abs(position_east)


    @classmethod
    def navigate_part2(cls, lines):
        ship_north = 0
        ship_east = 0
        waypoint_north = 1
        waypoint_east = 10
        for line in lines:
            command = line[0]
            move = int(line[1:])
            if command == "R":
                if move == 90 or move == -270:
                    new_waypoint_east = waypoint_north
                    waypoint_north = -waypoint_east
                    waypoint_east = new_waypoint_east
                elif move == 180 or move == -180:
                    waypoint_east = -waypoint_east
                    waypoint_north = -waypoint_north
                elif move == 270 or move == -90:
                    new_waypoint_east = -waypoint_north
                    waypoint_north = waypoint_east
                    waypoint_east = new_waypoint_east
            elif command == "N":
                waypoint_north += move
            elif command == "E":
                waypoint_east += move
            elif command == "F":
                ship_north += move * waypoint_north
                ship_east += move * waypoint_east
        return abs(ship_north) + abs(ship_east)

            
if __name__ == '__main__':
    lines = FileReader.read_file("Day12/input.txt")
    print(FerryNavigation.navigate_part1(lines))
    print(FerryNavigation.navigate_part2(lines))