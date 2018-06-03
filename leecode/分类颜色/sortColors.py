#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return nums
        len_t = len(nums)
        front_pos = 0

        # while front_pos < len_t and nums[front_pos] == 0:
        #     front_pos += 1

        back_pos = len_t - 1
        # while back_pos > 0 and nums[back_pos] == 2:
        #     back_pos -= 1

        i = front_pos
        while i <= back_pos:
            temp = nums[i]
            if temp == 0:
                nums[front_pos], nums[i] = nums[i], nums[front_pos]
                front_pos += 1
                i += 1
            elif temp == 2:
                nums[back_pos], nums[i] = nums[i], nums[back_pos]
                back_pos -= 1
                # while back_pos > 0 and nums[back_pos] == 2:
                #     back_pos -= 1
            else:
                i+=1


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[2, 0, 2, 1, 1, 0], [0,2,2,2,0,1,1],[]]
    answer_list = [[0, 0, 1, 1, 2, 2], [0,0,1,1,2,2,2],[]]
    test = Solution()
    for i in range(len(test_list)):
        test.sortColors(test_list[i])
        out_t = test_list[i]
        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], test_list[i]))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
I think my solution is best,hhh
'''
