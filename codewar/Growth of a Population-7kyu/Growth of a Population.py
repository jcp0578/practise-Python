#!/usr/bin/python3
# -*- coding: utf-8 -*-

debug = 1
#kan qing ti yi
#nb_year(1500, 5, 100, 5000), 15)
#nb_year(1500000, 2.5, 10000, 2000000), 10)
#nb_year(1500000, 0.25, 1000, 2000000), 94)


def debug_print(flag, out):
    if debug:
        print("temp" + str(flag) + ":" + str(out))


def nb_year(p0, percent, aug, p):
    sum_i = p0
    percent=percent/100
    i = 1
    while 1:
        sum_i = round(sum_i * (1 + percent)) + aug
        debug_print(1,sum_i)
        if sum_i >= p:
            return i
        else:
            i += 1


if __name__ == "__main__":
    nb_year(1000,2,50,1200)
    print(nb_year(1500,, 100, 5000))
    #print(nb_year(1500000, 2.5, 10000, 2000000))
    #print(nb_year(1500000, 0.25, 1000, 2000000))
