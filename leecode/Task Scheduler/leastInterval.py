#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


class Solution:
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

        out_t=(task_list[0]-1)*(n+1)+1
        for i in range(1,26):
            if task_list[i]==task_list[0]: 
                out_t+=1
            else:
                break
        
        return max(out_t,sum(task_list))

        


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [["A","A","A","B","B","B","C"],["A","A","A"]]
    test_list_2 = [2,1]
    answer_list = [8,5]

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
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        helper = [0]*26
        for x in tasks:
            helper[ord(x)-65]+=1
        helper.sort(reverse = True)
        ans = helper[0]*(n+1)-n
        for i in range(1,len(helper)):
            if(helper[0] == helper[i]):
                ans+=1
            else:
                break
        return max(ans,sum(helper))

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        letter_count = collections.Counter(tasks)
        count_max = max(letter_count.values())
        count = 0
        for cnt in letter_count.values():
            if cnt == count_max:
                count += 1
        result = (count_max - 1) * n + count_max + count - 1
        if result < len(tasks):
            return len(tasks)
        else:
            return result
'''
