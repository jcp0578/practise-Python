#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
有bug
'''
#for python 2.7 
import sys
sys.path.append('../')
import cw as test
#import time

debug = 1

#unit_p = {"second": 60, "minute": 60, "hour": 24, "day": 365, "year": 1}
unit_p =[60,60,24,365]
#time_t = {"year": 0, "day": 0, "hour": 0, "minute": 0, "second": 0}
time_unit =["second", "minute", "hour", "day", "year"]

format_t = {0: "", 1: " dna "}


def format_duration(seconds):
    #your code here
    out_temp = ""
    time_t =[]  #顺序用unit_p
    out_flag = 0
    if seconds:
        for i in range(len(unit_p)):
            time_t.append(seconds % unit_p[i])
            seconds //= unit_p[i]
        
        time_t.append(seconds)

        for t in range(len(time_t)-1,-1,-1):
            if time_t[t]:
                out_temp = out_temp + str(time_t[t]) + " " + time_unit[t]
                if time_t[t] > 1:
                    out_temp = out_temp + "s"
                out_temp = out_temp + ", "
                out_flag += 1
            else:
                pass
        out_temp = out_temp[::-1]
        for i in range(min(out_flag, 2)):
            out_temp = out_temp.replace(" ,", format_t[i], 1)
        out_temp = out_temp[::-1]
        return out_temp
    else:
        return "now"


if __name__ == "__main__":

#    t0 = time.perf_counter()

    test.assert_equals(format_duration(1), "1 second")
    test.assert_equals(format_duration(62), "1 minute and 2 seconds")
    test.assert_equals(format_duration(120), "2 minutes")
    test.assert_equals(format_duration(3600), "1 hour")
    test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
    test.assert_equals(format_duration(31536000), "1 year")

#    print(time.perf_counter() - t0)
'''
import sys
sys.path.append('../')
import cw as test
#import time

debug = 1

unit_p = {"second": 60, "minute": 60, "hour": 24, "day": 365, "year": 1}

time_t = {"year": 0, "day": 0, "hour": 0, "minute": 0, "second": 0}

format_t = {0: "", 1: " dna "}


def format_duration(seconds):
    #your code here
    out_temp = ""
    out_flag = 0
    if seconds:
        for t in unit_p:
            time_t[t] = seconds % unit_p[t]
            seconds //= unit_p[t]
        for t in time_t:
            if time_t[t]:
                out_temp = out_temp + str(time_t[t]) + " " + t
                if time_t[t] > 1:
                    out_temp = out_temp + "s"
                out_temp = out_temp + ", "
                out_flag += 1
            else:
                pass
        out_temp = out_temp[::-1]
        for i in range(min(out_flag, 2)):
            out_temp = out_temp.replace(" ,", format_t[i], 1)
        out_temp = out_temp[::-1]
        return out_temp
    else:
        return "now"


if __name__ == "__main__":

    t0 = time.perf_counter()

    test.assert_equals(format_duration(1), "1 second")
    test.assert_equals(format_duration(62), "1 minute and 2 seconds")
    test.assert_equals(format_duration(120), "2 minutes")
    test.assert_equals(format_duration(3600), "1 hour")
    test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")

    print(time.perf_counter() - t0)
'''
'''
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
'''
