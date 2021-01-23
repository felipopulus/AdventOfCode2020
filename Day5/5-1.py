from readInput import read_input
from measureTime import measure_time

lines = read_input(day=5).splitlines()


def get_seat_ids():
    for each_input in lines:
        binary_map = []
        for each_char in each_input:
            binary_map.append("1" if each_char in "BR" else "0")
        yield int("".join(binary_map), 2)  # convert to decimal


@measure_time
def solution():
    seat_ids = list(get_seat_ids())
    return max(seat_ids)


print(solution())