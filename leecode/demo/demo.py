#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
code demo
'''
import sys
import time



class Solution:
    def coinChange(self, coins, amount):
        return None


if __name__ == "__main__":

    if sys.version_info.major ==3: 
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = []
    test_list_2 = []
    answer_list = []

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.coinChange(test_list[i], test_list_2[i])


        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],
                   str(test_list[i]) + " " + str(test_list_2[i])))
    
    if sys.version_info.major ==3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))
    
'''

'''
