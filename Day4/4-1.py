from readInput import read_input
from measureTime import measure_time

str_input = read_input(day=4).split("\n\n")
required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


@measure_time
def solution():
    count = 0
    for line in str_input:
        short_codes = [x.split(":")[0] for x in line.replace("\n", " ").split(" ")]
        if all(x in short_codes for x in required_fields):
            count += 1
    return count


print(solution())
