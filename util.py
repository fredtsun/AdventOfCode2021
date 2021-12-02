def read_from_file(filename):
    with open(filename) as f:
        return [l.rstrip("\n") for l in f.readlines()]

