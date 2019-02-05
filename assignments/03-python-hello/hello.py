#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-01-31
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    names = sys.argv[1:]

    if len(names) == 0:
        print('Usage: {} NAME [NAME2 ...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    if len(names) == 1:
       print('Hello to the 1 of you:',names[0] + '!') 
       #//print('... {}!'.format(names))
    
    elif len(names) == 2:
       print('Hello to the 2 of you: {}!'.format(' and '.join(names)))
    
    elif len(names) > 2:
       num = len(names)
       names2 = names[0:(len(names)-1)]
       print('Hello to the {} of you: {}{}'.format(num,', '.join(names2),', and ' + names[len(names)-1]+'!'))
       #print(', and '+ names[len(names)-1]+'!')
       
    #print('Name is "{}"'.format(names))
    #print(names)

# --------------------------------------------------
main()
