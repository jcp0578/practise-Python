#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but bad
'''
import sys
import time


class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if position==[]:
            return 0
        distance_t = list(map(lambda x: target - x, position))
        time_dict={}
        for i in range(len(distance_t)):
            time_dict[distance_t[i]]=(distance_t[i]/speed[i])
        distance_t.sort()
        out_t=1
        last_max=time_dict[distance_t[0]]
        for i in range(1,len(distance_t)):
            if time_dict[distance_t[i]]>last_max:
                out_t+=1
                last_max=time_dict[distance_t[i]]
        return out_t


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [12,12,12]
    test_list_2 = [
        [10, 8, 0, 5, 3],[],[2]
    ]
    test_list_3 = [
        [2, 4, 1, 1, 3],[],[1]
    ]
    answer_list = [3,0,1]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.carFleet(test_list[i], test_list_2[i], test_list_3[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], str(test_list[i]) + " " +
                   str(test_list_2[i]) + " " + str(test_list_3[i])))

    if sys.version_info.major == 3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))
'''

'''
