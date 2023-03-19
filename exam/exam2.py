# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:47:46 2023

@author: zyf
"""

import sys

def isExist(sorted_list, x):
    length = len(x)
    if(length == 1):
        return True

    for y, y_exist in sorted_list:
        if(len(y) < length - 1):
            continue
        elif(len(y) > length - 1):
            return False
        else:
            if(x[:-1] == y):
                return y_exist



if __name__ == "__main__":
    list_n_str = sys.stdin.readline().strip().split(' ')

    # sort list by len(str)
    list_n_str.sort(key=lambda x: len(x))
    list_n_str_copy = list_n_str.copy()

    list_with_exist = []
    for i in list_n_str:
        list_with_exist.append([i, False])

    # print(list_with_exist)

    for j in list_with_exist:
        j[1] = isExist(list_with_exist, j[0])

    res = []
    length = 0
    list_with_exist.reverse()
    for k, exist in list_with_exist:
        if(exist):
            if(len(k) < length):
                break

            length = len(k)
            res.append(k)

    if(len(res) >= 1):
        print(res[0])
    else:
        print('')