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
    def calc(numbers, bit1, bit2):
        index = 0
        oxygen = numbers
        while len(oxygen) > 1:
            half = len(oxygen) / 2
            summa = sum(map(lambda x: 1 if x[index] == '1' else 0, oxygen))
            if summa >= half:
                eq = bit1
            else:
                eq = bit2
            oxygen = list(filter(lambda x: x[index] == eq, oxygen))
            index += 1
        return int(oxygen[0], 2)

    return calc(numbers, '1', '0') * calc(numbers, '0', '1')

def test_03a():
    assert solve_a(example) == 198

def test_03b():
    assert solve_b(example) == 230

def test_a(day03_lines):
    assert solve_a(day03_lines) == 4147524

def test_b(day03_lines):
    assert solve_b(day03_lines) == 3570354
