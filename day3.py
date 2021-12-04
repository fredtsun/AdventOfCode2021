from collections import Counter
from os import read
from util import read_from_file


def run():
    lines = read_from_file('data/day3.txt')
    bin_gamma = ''
    bin_epsilon = ''
    for c in range(len(lines[0])):
        bin_gamma += scan_vertical(lines, c, lambda x, y: '0' if x > y else '1')
        bin_epsilon += scan_vertical(lines, c, lambda x, y: '0' if x < y else '1') 

    gamma = int(bin_gamma, 2)
    epsilon = int(bin_epsilon, 2)
    print(gamma)
    print(epsilon)
    print(gamma * epsilon)

def run2():
    lines = read_from_file('data/day3.txt')
    bin_ogr = list(lines)
    bin_co2 = list(lines)
    for c in range(len(lines[0])):
        if len(bin_ogr) > 1:
            ogr_freq = scan_vertical(bin_ogr, c, lambda x, y: '0' if x > y else '1')
            bin_ogr = [r for r in bin_ogr if r[c] == ogr_freq]
        if len(bin_co2) > 1:
            co2_freq = scan_vertical(bin_co2, c, lambda x, y: '0' if x <= y else '1') 
            bin_co2 = [r for r in bin_co2 if r[c] == co2_freq]
    ogr = int(bin_ogr[0], 2)
    co2 = int(bin_co2[0], 2) 
    print(ogr)
    print(co2)
    print(ogr * co2)
    



def scan_vertical(input, column, compare_key):
    c = Counter([input[i][column] for i in range(len(input))])
    return compare_key(c['0'], c['1']) 


if __name__ == '__main__':
    run2()
