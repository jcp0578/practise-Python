#!/usr/bin/python3
# -*- coding: utf-8 -*-

#array=["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"] # 'b***i***t***c***o***i***n'
#array=["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]# 'a***r***e'
#array=["lets", "talk", "about", "javascript", "the", "best", "language"]#  'a***b***o***u***t'
#array=["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]#  'c***o***d***e'




#best
def two_sort(lst):
    return '***'.join(min(lst))

from operator import gt

array=["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]#  'L***e***t***s'
if __name__ == "__main__":
    print(two_sort(array))


    # min_temp="z"
    # for temp in array:
    #     if gt(min_temp,temp):
    #         min_temp=temp
    # out =''
    # for tpm in min_temp:
    #     out = out + "***" + tpm
    # out=out[3:]
    # print(out)

