

import math
import sys

with open("test.txt","r") as f:
    input = map(int,f.read().split("\n"))

def part1(str):
    return [math.floor(n/3)-2 for n in str]

def part2(str):
    str = [max(0,n) for n in str]
    while 


if __name__ == "__main__":
    print(sum(part1(input)))
    print(part2(input))