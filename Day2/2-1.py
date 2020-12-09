from readInput import read_input
from measureTime import measure_time

str_input = read_input(day=2).splitlines()


@measure_time
def solution():
    count = 0
    for line in str_input:
        min_max, letter, password = line.split(" ")
        l_min, l_max = min_max.split("-")
        l_min = int(l_min) - 1
        l_max = int(l_max) - 1
        letter = letter.replace(":", "")
        letter_count = password.count(letter) - 1
        if l_min <= letter_count <= l_max:
            count += 1
    return count


print(solution())


