#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''
import sys
import time

import collections
import string
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        queue = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        visited = set()
        wordList =set(wordList)
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in ls:
                    if j != word[i]:
                        newWord = word[:i]+j+word[i+1:]
                        if newWord not in visited and newWord in wordList:
                            queue.append((newWord, dist+1))
                            visited.add(newWord)
        return 0


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = ["zb"]
    test_list_2 = ["ad"]
    test_word_list = [chr(a)+chr(b) for a in range(ord("a"),ord("y")+1) for b in range(ord("a"),ord("z")+1)]
    answer_list = [3]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.ladderLength(test_list[i], test_list_2[i], test_word_list)

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
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        if endWord not in wordList:
            return 0
        
        d = construct_dict(set(wordList) | set([beginWord, endWord]))
        return bfs_words(beginWord, endWord, d)
'''
