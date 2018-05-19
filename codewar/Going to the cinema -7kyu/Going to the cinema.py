#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import pow, ceil
debug = 1

#ceil  AC


# movie(500, 15, 0.9), 43
# movie(100, 10, 0.95), 24
def debug_print(flag, out):
    if debug:
        print("temp" + str(flag) + ":" + str(out))


def movie(card, ticket, perc):
    sum_a = card
    sum_b = 0.0
    i = 1
    while 1:
        sum_a += (ticket * pow(perc, i))
        sum_b += ticket
        if sum_b > ceil(sum_a):
            return i
        else:
            i += 1


if __name__ == "__main__":
    print(movie(100, 10, 0.95))
    print(movie(500, 15, 0.9))
