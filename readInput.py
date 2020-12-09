import os
import urllib2


def read_input(day=1):
    dir_path = os.path.dirname(__file__)
    file_path = "{}/Day{}/input.txt".format(dir_path, day)

    if os.path.exists(file_path):
        with open(file_path, "r") as reader:
            return reader.read()
    else:
        url_path = "https://adventofcode.com/2020/day/{}/input".format(day)
        return urllib2.urlopen(url_path)