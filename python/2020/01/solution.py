#!/usr/bin/env python3

import typing

PROD="input.txt"
TEST="test_input.txt"

SUM = 2020


class CatastrophicFailure(Exception):
    """
    """
    pass


class EmptyResult(Exception):
    """
    """
    pass


def format_input(filename):
    """
    """
    formatted_input: typing.List[int] = []

    with open(filename, 'r') as f:
        formatted_input = list(map(int, f.readlines()))

    return formatted_input


def product_of_2_entries(puzzle_input):
    """
    """
    try:
        first, second = find_complement(SUM, puzzle_input)
    except EmptyResult:
        raise CatastrophicFailure("This should never have happened!!")

    return first * second


def find_complement(number, puzzle_input):
    """
    """
    for first in puzzle_input:
        second = number - first

        if second in puzzle_input:
            return first, second

    raise EmptyResult("No result found")
    

def product_of_3_entries(puzzle_input):
    """
    """
    for first in puzzle_input:
        rest = SUM - first

        try:
            second, third = find_complement(rest, puzzle_input)
        except EmptyResult:
            continue
        return first * second * third

    raise CatastrophicFailure("This should never have happened!!")


def main():
    """
    """
    formatted_input = format_input(PROD)
    print("Part 1 result: {}".format(product_of_2_entries(formatted_input)))
    print("Part 2 result: {}".format(product_of_3_entries(formatted_input)))

if __name__ == '__main__':
    main()
