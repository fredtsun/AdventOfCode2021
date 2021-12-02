from util import read_from_file


def run():
    lines = read_from_file("data/day1.txt")
    count = 0
    for p, n in zip(lines[:-1], lines[1:]):
        if int(p) < int(n):
            count += 1
    print(count)

def run2():
    nums = [int(l) for l in read_from_file("data/day1.txt")]
    sums = [x + y + z for x, y, z in zip(nums[:-2], nums[1:-1], nums[2:])]
    count = 0
    for p, n in zip(sums[:-1], sums[1:]):
        if p < n:
            count += 1
    print(count)

if __name__ == "__main__":
    run()
    run2()
