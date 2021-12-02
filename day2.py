from util import read_from_file


F = "forward"
D = "down"
U = "up"

class Direction:
    def __init__(self, rawtext):
        d, n = rawtext.split(" ")
        self.direction = d
        self.magnitude = int(n)
        

def run():
    directions = [Direction(l) for l in read_from_file("data/day2.txt")]
    hor = 0
    dep = 0
    aim = 0
    for d in directions:
        if d.direction == F:
            hor += d.magnitude
            dep += aim * d.magnitude
        elif d.direction == D:
            aim += d.magnitude
        elif d.direction == U:
            aim -= d.magnitude
        else:
            raise Exception("WTF IS THIS SHIT MAN: %s", d.direction)
    print(hor * dep)


if __name__ == "__main__":
    run()
