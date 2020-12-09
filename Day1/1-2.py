from readInput import read_input
from measureTime import measure_time
from itertools import combinations

str_input = read_input(day=1).splitlines()


def multiply_values(values):
    result = 1
    for x in values:
        result *= x
    return result


@measure_time
def solution():
    int_input = [int(x) for x in str_input]  # convert input lines to int
    for each_combination in combinations(int_input, 3):
        if sum(each_combination) == 2020:
            return multiply_values(each_combination)

print(solution())


