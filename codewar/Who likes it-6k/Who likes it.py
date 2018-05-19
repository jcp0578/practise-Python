#!/usr/bin/python3
# -*- coding: utf-8 -*-

debug = 1

#likes([]), 'no one likes this')
#likes(['Peter']), 'Peter likes this')
#likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
#likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
#likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')


def likes(names):
    out_temp = ""
    if names == []:
        out_temp = "no one likes this"
    elif len(names) == 1:
        out_temp = names[0] + " likes this"
    elif len(names) == 2:
        out_temp = names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        out_temp = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        out_temp = names[0] + ", " + names[1] + " and " + str(
            len(names) - 2) + " others like this"
    return out_temp


if __name__ == "__main__":
    print(likes([]))
    print(likes(['Peter']))
    print(likes(['Jacob', 'Alex']))
    print(likes(['Max', 'John', 'Mark']))
    print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
