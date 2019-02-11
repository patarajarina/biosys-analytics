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
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

    #print('Arg is "{}"'.format(arg))

    #i = 1
    lines = []
    for line in open(file):
        lines.append(line)
     #   print('   {}: '.format(str(i)), lines)
     #   i = i+1
    for i, line_n in enumerate(lines): 
         print('   {}: {}'.format(i+1, line_n), end='')
    
 
  #  for line in lines
   #     print(line, end='')

# --------------------------------------------------
main()
