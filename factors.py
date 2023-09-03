#!/usr/bin/python3
import sys
import math


def find_factors(num):
    if num % 2 == 0:
        print(f"{num}={num // 2}*{2}")
        return

    factors = [3, 5, 7, 11]
    for fact in factors:
        if num % fact == 0:
            print(f"{num}={num // fact}*{fact}")
            return

    down = int(math.sqrt(num))
    up = down + 1

    while True:
        if num % down == 0:
            print(f"{num}={num // down}*{down}")
            return
        elif num % up == 0:
            print(f"{num}={up}*{num // up}")
            return

        down -= 1
        up += 1


def main():
    if len(sys.argv) < 2:
        return

    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            number = int(line)
            find_factors(number)


if __name__ == "__main__":
    main()
