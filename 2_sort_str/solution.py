# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 21:53:20 2023

@author: zyf
"""

import sys


def solve(string: str):
    words = string.split(' ')
    words_ = {}
    for word in words:
        word_ = ''.join(sorted(word))
        if (words_.get(word_) == None):
            words_[word_] = [1, len(word_)]  # appearCount, length
        else:
            words_[word_][0] += 1

    sorted(words_, key = lambda k, v: v[1], reverse=True)


def run():
    string = sys.stdin.readline()
    solve(string)


if __name__ == '__main__':
    run()
