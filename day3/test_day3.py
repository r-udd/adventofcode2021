from itertools import *

example = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

def solve_a (numbers):
    half = len(numbers) / 2
    ones = [x.count('1') > half for x in zip(*numbers)]
    gamma = ''
    epsilon = ''
    for e in ones:
        if e:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)

def solve_b(numbers):
    return 0

def test_03a():
    assert solve_a(example) == 198

def test_03b():
    assert solve_b(example) == 230

def test_a(day03_lines):
    assert solve_a(day03_lines) == 4147524

def test_b(day03_numbers):
    assert solve_b(day03_numbers) == 1150
