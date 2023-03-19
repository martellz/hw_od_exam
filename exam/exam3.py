# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:11:04 2023

@author: zyf
"""

import sys


def iteration(m, list_n):
    if(len(list_n) == 1):
        return 1
    res = 0
    max_n = list_n[-1]
    for i in range(m // max_n + 1):
        res += iteration(m - i * max_n, list_n[:-1])

    return res


if __name__ == "__main__":
    list_n_str = sys.stdin.readline().strip().split(' ')
    M = int(sys.stdin.readline().strip())

    list_n = []
    for i in list_n_str:
        list_n.append(int(i))

    print(iteration(M, list_n))
