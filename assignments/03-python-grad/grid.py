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

    if len(args) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    number = int(args[0])

    if number not in range(2,9):
        print('NUM ({}) must be between 1 and 9'.format(number))
        sys.exit(1)
  
#    sq = number**2
 #   sq_ls = range(1,sq+1)
#
#    for numbers in sq_ls:
 #       print('{:3}'.format(numbers), end='')
  #      if numbers % number == 0:
   #          print('')

              
    for j in range(1,number*number+1):
        print(' '.join(str(j)), \n if j%number == 0)          
    #   print('{} '.format(i+1), end=' ') 



# --------------------------------------------------
main()
