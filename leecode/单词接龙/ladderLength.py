#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
time out
'''
import sys
import time


class Solution:
    def wordCompare(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        len(word1)=len(word2)
        :rtype: bool
        """
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
                if diff > 1:
                    return False
        return True

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not beginWord:
            return 0
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        wordDice = {}
        for word in wordList:
            wordDice[word] = []
        len_t = len(wordList)
        min_t = len_t + 2
        for i in range(len_t):
            for j in range(i):
                if self.wordCompare(wordList[i], wordList[j]):
                    wordDice[wordList[i]].append(wordList[j])
                    wordDice[wordList[j]].append(wordList[i])

        def findWord(wordlist_t, depth):
            """
            :type word1: str
            :type word2: str
            len(word1)=len(word2)
            :rtype: bool
            """
            nonlocal min_t
            if wordlist_t[-1] == endWord:
                if depth < min_t:
                    min_t = depth
                    return 1
            for word_t in wordDice[wordlist_t[-1]]:
                if word_t not in wordlist_t:
                    wordlist_t.append(word_t)
                    findWord(wordlist_t, depth + 1)
                    wordlist_t.pop()
            return 0

        findWord([beginWord], 1)

        return min_t if min_t < len_t + 2 else 0


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = ["si"]
    test_list_2 = ["ar"]
    test_word_list = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba"]
    answer_list = [6]

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
