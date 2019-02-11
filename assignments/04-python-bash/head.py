#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-02-11
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))

        sys.exit(1)

    file = args[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)
    #print('Arg is "{}"'.format(arg))
    i = 1
   
    if len(args) == 1: # incase there is not specific number of lines
        for line in open(file):
            print('{}'.format(line))
            i=i+1
            if i == 4:
                break
            
    elif len(args) == 2:
        line_num = int(args[1])
        if line_num <= 0:
            print('lines ({}) must be a positive number'.format(line_num))   
            sys.exit(1)  
        for line in open(file):
            if i<= int(line_num):
                print('{}'.format(line),end='')
                i=i+1 
            else:
                break
            

# --------------------------------------------------
main()
