#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-04-10
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='FILE',help='File inputs',nargs=2)


    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# ----------------------------------------------------
def dist(s1,s2):
    
    len1 = len(s1)
    len2 = len(s2)
    diff = abs((len1)-(len2))

    for c1, c2 in zip(s1,s2): #unpacking
        if c1 != c2:
            diff += 1        
    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1,s2, diff))
    return diff


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file1, file2 = args.file

    for afile in [file1, file2]:
        if not os.path.isfile(afile):
            die('"{}" is not a file'.format(afile))

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )
    
    logging.debug('file1 = {}, file2 = {}'.format(file1, file2)) 
    words1 = open(file1).read().split()
    words2 = open(file2).read().split()

    count = 0
    for w1, w2 in zip(words1, words2):
        count += dist(w1,w2)
    print(count)

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
