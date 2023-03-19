# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:08:29 2023

@author: zyf
"""

import sys


def run(sampler_count, vol_count, list_n):
    res = 0

    gain = []
    for n in list_n:
        gain.append((0.2 * n, 0))
        res += 0.8 * n

    for i in range(vol_count):
        gain.sort(reverse=True)
        res += gain[0][0]
        count = gain[0][1] + 1

        if(count == 1):
            gain[0] = (0.5 * gain[0][0], count)
        elif(count < 4):
            gain[0] = (gain[0][0], count)
        else:
            gain[0] = (0, count)

    return int(res)

if __name__ == "__main__":
    sampler_count_str, vol_count_str = sys.stdin.readline().strip().split(' ')
    sampler_count, vol_count = int(sampler_count_str), int(vol_count_str)

    list_n_str = sys.stdin.readline().strip().split(' ')
    list_n = []
    for i in list_n_str:
        list_n.append(int(i))


    res = run(sampler_count, vol_count, list_n)
    print(res)
