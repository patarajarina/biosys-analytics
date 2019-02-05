#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-02-05
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    
    stringi = sys.argv[1:]
    #stringi = str(stringi)
    if len(stringi) != 1:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    word = stringi[0]
  
    if len(word) > 1:
        i=0      
        for letter in word:
             if letter in 'aeiou' or letter in 'EAIOU':
             #if 'a' or 'e' or 'i' or 'o' or 'u' in word:
                 i=i+1
    #         if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
 
        if i==1:
              print('There is {} vowel in \"{}.\"'.format(i,word))
        if i>1 or i == 0: 
              print('There are {} vowels in \"{}.\"'.format(i,word)) 
    
    
    
    
    #arg = string_in[0]

    #print('Arg is "{}"'.format(arg))


# --------------------------------------------------
main()
