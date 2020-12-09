from readInput import read_input
from measureTime import measure_time

str_input = read_input(day=3).splitlines()


class Coordinates(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Coordinates(self.x * other, self.y * other)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


def get_item_at(coord):
    map_x = coord.x % 31
    return str_input[coord.y][map_x]


@measure_time
def solution():
    slope = Coordinates(3, 1)

    count = 0
    for index in range(1, len(str_input)):
        current_position = slope * index
        tree_or_snow = get_item_at(current_position)
        if tree_or_snow == "#":
            count += 1
    return count


print(solution())