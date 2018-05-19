#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

https://www.codewars.com/kata/domino-tiling-2-x-n-board/python
A domino is a rectangular block with 2 units wide and 1 unit high. A domino can be placed on a grid in two ways: horizontal or vertical.

The task is to find the number of ways you can fill the given grid with dominoes.



# K == 1: only one color
two_by_n(1, 1) == 1
two_by_n(3, 1) == 0

# K == 2: two colors
two_by_n(1, 2) == 2
two_by_n(4, 2) == 4
two_by_n(7, 2) == 2

# K == 3: three colors
two_by_n(1, 3) == 3
two_by_n(2, 3) == 12
two_by_n(5, 3) == 168 # yes, the numbers grow quite quickly

# You must handle big values
two_by_n(10, 5) == 7802599
two_by_n(20, 10) == 4137177

1 <= N <= 10000

1 <= K <= 100
'''
import sys
sys.path.append('../')
import cw as Test

debug = 1


def debug_print(flag, out):
    if debug:
        print("temp" + str(flag) + ":" + str(out))


def move_zeros(array):
    times = array.count(0)
    pos = []
    bool_times=0;
    if times:
        for i in range(times):
            if isinstance(array[array.index(0)], bool):
                pos.append(array.index(0)+bool_times)
                bool_times+=1
            else:
                array.append(0)
            array.remove(0)
        for i in pos:
            array.insert(i,False)               
    else:
        pass
    return array


if __name__ == "__main__":
    Test.describe("Basic tests")
    Test.assert_equals(
        move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    Test.assert_equals(
        move_zeros(
            [9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Test.assert_equals(
        move_zeros([
            "a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9
        ]),
        ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Test.assert_equals(
        move_zeros([
            "a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1,
            9, 0, 0, {}, 0, 0, 9
        ]), [
            "a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0
        ])
    Test.assert_equals(
        move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])

    Test.assert_equals(move_zeros(['pippi', 0, 0, 2, 0, 3, 2, 0, 0, 2, 'z', 10, 0, -5, -10, 'y', -4, False, 0, -10, 0, -2, 0, -3, 0, False, 2, -8, -10, -2, 1, -3, -4]),
    ['pippi', 2, 3, 2, 2, 'z', 10, -5, -10, 'y', -4, False, -10, -2, -3, False, 2, -8, -10, -2, 1, -3, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Test.assert_equals(move_zeros(["a", "b"]), ["a", "b"])
    Test.assert_equals(move_zeros(["a"]), ["a"])
    Test.assert_equals(move_zeros([0, 0]), [0, 0])
    Test.assert_equals(move_zeros([0]), [0])
    Test.assert_equals(move_zeros([]), [])

    Test.assert_equals(move_zeros(['pippi', 0, 0, 2, 0, 3, 2, 0, 0, 2, 'z', 10, 0, -5, -10, 'y', -4, False, 0, -10, 0, -2, 0, -3, 0, False, 2, -8, -10, -2, 1, -3, -4]),
    ['pippi', 2, 3, 2, 2, 'z', 10, -5, -10, 'y', -4, False, -10, -2, -3, False, 2, -8, -10, -2, 1, -3, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    Test.assert_equals(move_zeros([False, 9, -1, False, 1, 4, 0, 3, -7, 0, 'b', 0, 4, 0, 6, 0, 'c', 0, -9, 10, 4, -4, 'y', 'y', False, -1, 9, 6, 'b', True, 8, False, 0, -8, 1, -9, 'y', True]),
    [False, 9, -1, False, 1, 4, 3, -7, 'b', 4, 6, 'c', -9, 10, 4, -4, 'y', 'y', False, -1, 9, 6, 'b', True, 8, False, -8, 1, -9, 'y', True, 0, 0, 0, 0, 0, 0, 0])

'''
o(n)
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

o(nlogn)
def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)
'''
