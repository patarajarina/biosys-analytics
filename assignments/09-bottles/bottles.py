#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-03-18
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-n',
        '--num_bottles',
        help='bottles of beer on the wall song',
        metavar='int',
        type=int,
        default=10)


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


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    numbot_arg = args.num_bottles

    if numbot_arg < 1:
        die('N ({}) must be a positive integer'.format(numbot_arg))

    list_num = list(range(1,numbot_arg+1))
    list_num.reverse()
    for i in list_num:
        j=i-1
        print('{} bottle{} of beer on the wall,'.format(i, '' if i == 1 else 's'))
        print('{} bottle{} of beer,'.format(i, '' if i == 1 else 's'))
        print('Take one down, pass it around,')
        print('{} bottle{} of beer on the wall!{}'.format(j, '' if j ==1 else 's', '' if j==0 else '\n'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
