#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
time out 21/39
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
        min_word_depth=dict()
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
            nonlocal min_word_depth
            if wordlist_t[-1] == endWord:
                if depth < min_t:
                    min_t = depth
                    return 1
                if depth < (min_word_depth[wordlist_t[-1]]):
                    min_word_depth[wordlist_t[-1]]=depth
                else:
                    return 0
            except KeyError:
                min_word_depth[wordlist_t[-1]]=depth

            for word_t in wordDice[wordlist_t[-1]]:
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
