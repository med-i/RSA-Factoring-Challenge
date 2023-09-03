#!/usr/bin/python3
from sys import argv, stderr
from math import sqrt


def find_factors(num):
    if num % 2 == 0:
        print(f"{num}={num // 2}*{2}")
        return

    factors = [3, 5, 7, 11]
    for fact in factors:
        if num % fact == 0:
            print(f"{num}={num // fact}*{fact}")
            return

    down = int(sqrt(num))
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
    if len(argv) < 2:
        print("Usage: factors <file>", file=stderr)
        exit(1)

    file_path = argv[1]

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                number = int(line)
                find_factors(number)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found", file=stderr)
        exit(1)
    except ValueError:
        print(f"Error: Invalid number '{line}'", file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
