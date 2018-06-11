#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
time out 29/39
'''
import sys
import time

import collections
import string
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # wordList.add(endWord)
        queue = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        visited = set()
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
                            visited.add(newWord)  # wordList.remove(newWord)
        return 0


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = ["sb"]
    test_list_2 = ["ad"]
    test_word_list = [chr(a)+chr(b) for a in range(ord("a"),ord("z")+1) for b in range(ord("a"),ord("g")+1)]
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

'''
