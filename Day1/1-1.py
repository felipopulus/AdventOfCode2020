from readInput import read_input
from measureTime import measure_time

str_input = read_input(day=1).splitlines()

@measure_time
def solution():
    int_input = [int(x) for x in str_input]  # convert input lines to int
    for index_x, num_x in enumerate(int_input):
        for num_y in int_input[index_x:]:
            if num_x + num_y == 2020:
                return num_x * num_y


print(solution())


