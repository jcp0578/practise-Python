#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
ExamRoom - not finish
'''
import sys
import time



class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        _len=N
        _next_seat=0
        _seat_list=[(0,N)]
        _seat_len=[N]
        return None
        

    def seat(self):
        """
        :rtype: int
        """
        

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)


if __name__ == "__main__":

    if sys.version_info.major ==3: 
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [0,1,1,1,1,2,1]
    test_list_2 = [10,0,0,0,0,4,0]
    answer_list = [None,0,9,4,2,None,5]

    
    for i in range(len(test_list)):
        if test_list[i]==1:
            out_t = test.seat()
        elif test_list[i]==2:
            out_t = test.leave(test_list_2[i])
        elif test_list[i]==0:
            test = ExamRoom(test_list_2[i])
            out_t=None
        else:
            out_t=-1

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
