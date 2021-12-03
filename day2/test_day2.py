from itertools import *

example_1 = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]

def solve_a (data):
    x,y = 0, 0
    for direction, amount in map(str.split, data):
        match direction:
            case 'forward':
                x += int(amount)
            case 'up':
                y -= int(amount)
            case 'down':
                y += int(amount)
    return x * y


def solve_b(data):
    x, y, aim = 0, 0, 0
    for direction, amount in map(str.split, data):
        match direction:
            case 'forward':
                x += int(amount)
                y += aim * int(amount)
            case 'up':
                aim -= int(amount)
            case 'down':
                aim += int(amount)
    return x * y

def test_1a():
    assert solve_a(example_1) == 150

def test_1(day02_lines):
    assert solve_a(day02_lines) == 1990000

def test_02b():
    assert solve_b(example_1) == 900


def test_b(day02_lines):
    assert solve_b(day02_lines) == 1975421260
