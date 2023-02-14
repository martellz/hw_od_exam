# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 21:14:24 2023

@author: zyf
"""


import sys


def solve(taskNum: int, tasks: [[str, str, str]]):
    assert(taskNum == len(tasks))

    timeMap = {}

    for task in tasks:
        start = int(task[0])
        end = int(task[1])
        paral = int(task[2])

        for i in range(start, end + 1):
            if(timeMap.get(i) == None):
                timeMap[i] = paral
            else:
                timeMap[i] += paral

    print(max(timeMap.values()))


def run():
    taskNum = int(sys.stdin.readline())
    tasks = []
    for i in range(taskNum):
        tasks.append(sys.stdin.readline().replace('\n', '').split(' '))

    solve(taskNum, tasks)


if __name__ == '__main__':
    run()
