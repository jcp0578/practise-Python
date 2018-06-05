#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but ugly
'''
import sys
import time


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not len(word):
            return False
        len_y=len(board)        
        if len_y ==0:
            return False
        len_x=len(board[0])
        if len_x ==0:
            return False

        flag=[]
        for i in range(len_y):
            temp=[]
            for j in range(len_x):
                temp.append(0)
            flag.append(temp)  

        out_t =False
        def backtrack(word_t,x,y):
            nonlocal out_t
            nonlocal flag
            if out_t:
                return 0

            if x <0 or y<0:
                return 0
            try :
                if flag[y][x]==0:
                    if board[y][x] == word[len(word_t)]:
                        word_t=word_t+board[y][x]
                        flag[y][x]=1
                    else:
                        return 0
                else:
                    return 0
            except IndexError:
                return 0

            if len(word_t)==len(word):
                if word_t==word:
                    out_t =True
            else :
                backtrack(word_t,x+1,y)
                backtrack(word_t,x-1,y)
                backtrack(word_t,x,y+1)
                backtrack(word_t,x,y-1)
            flag[y][x]=0
            return out_t

        for i in range(len_y):
            for j in range(len_x):
                if board[i][j]==word[0]:
                    if backtrack("",j,i):
                        return True
        return False
        

            


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [['A', 'B', 'C', 'E'], 
                 ['S', 'F', 'C', 'S'],
                 ['A', 'D', 'E', 'E']]
    test_list_2 = ["ABCCED","SEE","ABCB",""]
    answer_list = [True,True,False,False]

    test = Solution()
    for i in range(len(test_list_2)):
        out_t = test.exist(test_list, test_list_2[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],
                   str(test_list[i]) + " " + str(test_list_2[i])))

    if sys.version_info.major == 3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))
'''

'''
