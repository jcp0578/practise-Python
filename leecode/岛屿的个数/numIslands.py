#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC - simply code
'''

import time


class Solution:
    _grid=[[]]
    def dfs(self,x,y):
        try:
            if x <0 or y<0:
                return 0
            if self._grid[y][x]=="1":
                    self._grid[y][x]="2"
                    self.dfs(x+1,y)
                    self.dfs(x-1,y)
                    self.dfs(x,y+1)
                    self.dfs(x,y-1)
            return 0
        except IndexError:
            return 0
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        len_y=len(grid)        
        if len_y ==0:
            return 0
        len_x=len(grid[0])
        self._grid=grid
        out_t=0
        for i in range(len_y):
            for j in range(len_x):
                if grid[i][j]=="1":
                    out_t+=1
                    self.dfs(j,i)
        return out_t
                




if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[["1", "1", "0", "0", "0"], 
                  ["1", "1", "1", "0", "0"],
                  ["0", "0", "1", "0", "0"], 
                  ["0", "0", "0", "1", "1"]],

                 [["1", "1", "0", "0", "0"], 
                  ["1", "1", "0", "0", "0"],
                  ["0", "0", "1", "0", "0"], 
                  ["0", "0", "0", "1", "1"]]
                ]
    answer_list = [2,3]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.numIslands(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))

'''
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        if len(grid)==0:
            return count
        else:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j]=='1':
                        self.searchLand(grid,i,j)
                        count+=1
            return count
    def searchLand(self,grid,i,j):
        grid[i][j]=0
        if(i>0 and grid[i-1][j]=='1'):#上
            self.searchLand(grid,i-1,j)
        if(j>0 and grid[i][j-1]=='1'):#左
            self.searchLand(grid,i,j-1)
        if(i+1<len(grid) and grid[i+1][j]=='1'):#下
            self.searchLand(grid,i+1,j)
        if(j+1<len(grid[i]) and grid[i][j+1]=='1'):#右
            self.searchLand(grid,i,j+1)
'''
