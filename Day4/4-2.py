import re
from readInput import read_input
from measureTime import measure_time

str_input = read_input(day=4).split("\n\n")
required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


# Part 2
def validate_hgt(s):
    if len(s) >= 4:
        m = ((s[-2:] == "in") & (59 <= int(s[:-2]) <= 76)) | \
            ((s[-2:] == "cm") & (150 <= int(s[:-2]) <= 193))
    else:
        m = False
    return (m)


def validate_passport(p):
    pd = dict(item.split(":") for item in p if len(item) > 1)
    if all(key in pd.keys() for key in required_fields):
        return all([
            1920 <= int(pd["byr"]) <= 2002,
            2010 <= int(pd["iyr"]) <= 2020,
            2020 <= int(pd["eyr"]) <= 2030,
            2020 <= int(pd["eyr"]) <= 2030,
            bool(re.match("^#[0-9a-f]{6}$", pd["hcl"])),
            pd["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            bool(re.match("^[0-9]{9}$", pd["pid"])),
            validate_hgt(pd["hgt"])
        ])

    else:
        return False


@measure_time
def solution():
    passport_list = [x.replace("\n", " ").split(" ") for x in str_input]
    count = 0
    for passport in passport_list:
        if validate_passport(passport):
            count += 1
    return count


print(solution())
