#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
error
'''

import time


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <0:
            return -1
        elif amount ==0:
            return 0
        
        coins.sort(reverse=True)
        len_t=len(coins)
        for i in range(len_t):
            out=0
            amount_t=amount
            for j in range(i,len_t):
                if amount_t:
                    out+=amount_t//coins[j]
                    amount_t%=coins[j]
                else:
                    return out
            else:
                if amount_t==0:
                    return out                   
        return -1

        
         


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[1,2,5],[2],[1],[186,419,83,408],[2,15]]
    test_list_2 = [11,3,0,6249,31]
    answer_list = [3,-1,0,20,9]

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

    print("\nRun Time is %f s" % (time.perf_counter() - t0))

'''

'''
