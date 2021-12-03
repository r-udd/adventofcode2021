from itertools import *

def solve_a (numbers):
    return sum(map(lambda x: x[0] < x[1], pairwise(numbers)))

def solve_b(numbers):
    return sum(map(lambda x: x[0] < x[1], zip(numbers, numbers[3:])))

def test_01a():
    assert solve_a([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7

def test_01b():
    assert solve_b([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 5

def test_a(day01_numbers):
    assert solve_a(day01_numbers) == 1215

def test_b(day01_numbers):
    assert solve_b(day01_numbers) == 1150
