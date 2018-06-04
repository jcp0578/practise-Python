#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
error
'''

import time


class Solution:
    def task_count(self,task_list,n):
        out_t=task_list[0]*(n+1)
        task_sum=sum(task_list)
        if out_t >=task_sum:
            return out_t
        else:
            temp=out_t
            temp-=task_list[0]
            for i in range(1,len(task_list)):
                if temp >= task_list[i]:
                    temp-=task_list[i]
                else:
                    task_list[i]-=temp
                    break
            out_t +=self.task_count(task_list[i:],n)
            return out_t


    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_list=[0]*26
        for task in tasks:
            task_list[ord(task)-65]+=1
        task_list.sort(reverse=True)
        return self.task_count(task_list,n)

        


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [["A","A","A","B","B","B"],]
    test_list_2 = [2]
    answer_list = [8]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.leastInterval(test_list[i], test_list_2[i])

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
