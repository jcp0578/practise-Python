#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
time out
'''

import time


class Solution:
    _out_t=[]

    def RestCoinChange(self, coins, amount,sum):

        if len(coins) == 1:
            if amount % coins[0] == 0:
                self._out_t.append(sum+ amount // coins[0])
                return 0
            else:
                return -1
        else:
            if amount % coins[0] == 0:
                self._out_t.append(sum+amount // coins[0])
                return 0
            i = amount // coins[-0]
            while i >= 0:
                self.RestCoinChange(coins[1:], amount - i * coins[0],sum+i)
                i -= 1
        return -1

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        self._out_t=[]
        coins.sort(reverse=True)
        self.RestCoinChange(coins, amount,0)
        return min(self._out_t) if len(self._out_t) else -1


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[1, 2, 5], [2], [1], [186, 419, 83, 408], [2, 15],[1,14,15],[227,99,328,299,42,322]]
    test_list_2 = [11, 3, 0, 6249, 31,42,9847]
    answer_list = [3, -1, 0, 20, 9,3,31]

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
