import re

def solve_a(data):
    pos = {}
    for line in data:
        ax, ay, bx, by = map(int, re.split(' -> |,', line))
        if ax == bx or ay == by:
            currx = ax
            curry = ay
            diff = bx - ax + by - ay
            diff = diff // abs(diff)
            while True:
                pos[(currx, curry)] = pos.get((currx, curry), 0) + 1
                if currx == bx and curry == by:
                    break
                elif ax == bx:
                    curry += diff
                else:
                    currx += diff
    return len(list(filter(lambda x: x > 1, pos.values())))

def solve_b(data):
    pos = {}
    for line in data:
        ax, ay, bx, by = map(int, re.split(' -> |,', line))
        currx = ax
        curry = ay
        diffx = bx - ax
        diffy = by - ay
        if diffx != 0:
            diffx = diffx // abs(diffx)
        if diffy != 0:
            diffy = diffy // abs(diffy)
        while True:
            pos[(currx, curry)] = pos.get((currx, curry), 0) + 1
            if currx == bx and curry == by:
                break
            currx += diffx
            curry += diffy
    return len(list(filter(lambda x: x > 1, pos.values())))


input1 = ['0,9 -> 5,9',
          '8,0 -> 0,8',
          '9,4 -> 3,4',
          '2,2 -> 2,1',
          '7,0 -> 7,4',
          '6,4 -> 2,0',
          '0,9 -> 2,9',
          '3,4 -> 1,4',
          '0,0 -> 8,8',
          '5,5 -> 8,2']


def test_a():
    assert solve_a(input1) == 5

def test_b():
    assert solve_b(input1) == 12


def test_part_a(day05_lines):
    print(solve_a(day05_lines))
    assert solve_a(day05_lines) == 5084


def test_part_b(day05_lines):
    print(solve_b(day05_lines))
    assert solve_b(day05_lines) == 17882
