#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-02-12
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    answers = {} #define the variable
    for things in ['name','quest','fav color']:
        answer = input('What is your {}? '.format(things))
        print(answer)
        answers[things] = answer

    print(answers)
# --------------------------------------------------
main()
