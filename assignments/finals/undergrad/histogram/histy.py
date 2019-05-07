#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Histogrammer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='int', help='the following arguments are required: int',nargs='+')

    parser.add_argument(
        '-c',
        '--character',
        help='Character to represent',
        metavar='str',
        type=str,
        default='|')

    parser.add_argument(
        '-m',
        '--minimum',
        help='Minimum value to print',
        metavar='int',
        type=int,
        default=1)

    parser.add_argument(
        '-s',
        '--scale',
        help='Scale inputs',
        metavar='int',
        type=int,
        default=1)


#    parser.add_argument(
#        '-f', '--flag', help='A boolean flag', action='store_true')

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
    char_arg = args.character
    min_arg = args.minimum
    scale_arg = args.scale
 #   flag_arg = args.flag
    pos_arg = args.positional

    
    pair = {}
    #print(pos_arg)
    for i in pos_arg :
        i = int(i)
        if i >= min_arg :
            his = char_arg
            i_s = i/scale_arg
        #print(i_s)
            for n in range(1,int(i_s)):
                his = his + char_arg
#        print('{} {}'.format(i,his))
            pair[i] = his
#        print(pair)
    for mmm in sorted(pair.keys()):
        print('{:3} {}'.format(mmm, pair[mmm]))
    
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
