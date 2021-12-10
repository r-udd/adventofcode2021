from itertools import *

def points(line):
    start = '([{<'
    end = ')]}>'
    point = [3, 57, 1197, 25137]
    stack = []
    for char in line:
        if char in start:
            stack.append(char)
        else:
            s = stack.pop()
            if end.find(char) != start.find(s):
                return point[end.find(char)]
    return 0

def points_b(line):
    start = ' ([{<'
    stack = []
    for char in line:
        if char in start:
            stack.append(char)
        else:
            stack.pop()
    res = 0
    for char in stack[::-1]:
        res = res * 5 + start.find(char)
    return res

def solve_a(data):
    return sum(map(points, data))


def solve_b(data):
    data = list(filter(lambda x: points(x) == 0, data))
    res = list(map(points_b, data))
    return sorted(map(points_b, data))[len(data) // 2]


input1 = ['[({(<(())[]>[[{[]{<()<>>',
         '[(()[<>])]({[<{<<[]>>(',
         '{([(<{}[<>[]}>{[]{[(<()>',
         '(((({<>}<{<{<>}{[]{[]{}',
         '[[<[([]))<([[{}[[()]]]',
         '[{[{({}]{}}([{[{{{}}([]',
         '{<[[]]>}<{[{[{[]{()[[[]',
         '[<(<(<(<{}))><([]([]()',
         '<{([([[(<>()){}]>(<<{{',
         '<{([{{}}[<[[[<>{}]]]>[]]']


def test_0():
    assert points(input1[0]) == 0


def test_1():
    assert points(input1[1]) == 0


def test_2():
    assert points(input1[2]) == 1197

def test_a():
    assert solve_a(input1) == 26397

def test_b():
    assert solve_b(input1) == 288957


def test__part_a(day10_lines):
    print(solve_a(day10_lines))
    assert solve_a(day10_lines) == 311949


def test_part_b(day10_lines):
    print(solve_b(day10_lines))
    assert solve_b(day10_lines) == 3042730309
