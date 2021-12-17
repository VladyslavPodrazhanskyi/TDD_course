import os


def read_from_file(path):
    if not os.path.exists(path):
        raise Exception("Bad File")
    infile = open(path, "r")
    line = infile.readline()
    return line
