#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        num_temp = amount+1
        out_t = [num_temp]*(num_temp)
        coins_len = len(coins)
        out_t[0] = 0
        for i in range(num_temp):
            for coin in coins:
                if i < coin:
                    continue
                if out_t[i]>out_t[i-coin]+1:
                    out_t[i] = out_t[i-coin]+1
        if out_t[i] == num_temp:
            return -1
        return out_t[i]


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[1, 2, 5], [2], [1], [186, 419, 83, 408], [2, 15], [1, 14, 15], [
        227, 99, 328, 299, 42, 322], [253, 27, 214, 340, 158, 92, 52, 126, 466, 431, 95], ]
    test_list_2 = [11, 3, 0, 6249, 31, 42, 9847, 3046]
    answer_list = [3, -1, 0, 20, 9, 3, 31, 8]

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
class Solution:
    def coinChangeCore(self,coins,amount,coins_num,list_num):
        if amount==0:
            if list_num[0] > coins_num:
                list_num[0] = coins_num
            return True
        elif amount<0:
            return False
        elif len(coins)==0:
            return False
        num = amount//coins[-1]+1
        for i in range(num)[::-1]:
            remainder = amount-coins[-1]*i
            if coins_num+i >= list_num[0]:
                return
            self.coinChangeCore(coins[:-1],remainder,coins_num+i,list_num)
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        remainder = amount - amount//coins[-1]*coins[-1]
        list_num = [21473648]
        coins.sort()
        self.coinChangeCore(coins, amount, 0, list_num)
        if list_num[0]!=21473648:
            return list_num[0]
        else:
            return -1



class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1
'''
