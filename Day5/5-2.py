from readInput import read_input
from measureTime import measure_time

str_input = read_input(day=5).splitlines()


def get_seat_ids():
    for each_input in str_input:
        binary_map = []
        for each_char in each_input:
            binary_map.append("1" if each_char in "BR" else "0")
        yield int("".join(binary_map), 2)  # convert to decimal

@measure_time
def solution():
    seat_ids = list(get_seat_ids())
    min_rep = min(seat_ids)
    max_rep = max(seat_ids)
    for index in range(min_rep, max_rep):
        if index not in seat_ids:
            return index

print(solution())