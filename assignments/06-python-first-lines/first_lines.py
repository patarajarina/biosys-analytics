#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-02-25
Purpose: Rock the Casbah
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
           
    parser.add_argument(
        'positional', metavar='DIR', help='A positional argument', nargs='+')

#    parser.add_argument(
#        'DIR',
#        '--',
#        help='A named string argument',
#        metavar='DIR',
#        type=dir,
#        default=None,
#        nargs='+',
#        default='')

    parser.add_argument(
        '-w',
        '--width',
        help='A named integer argument',
        metavar='int',
        type=int,
        
        default=50)

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
#    args = sys.argv[1:]
 #   str_arg = args.arg
    DIRS = args.positional
#    flag_arg = args.flag
    width = args.width
    
#    print(DIRS)
#    dirname = args[0] #check
    for dirname in DIRS:
        if not os.path.isdir(dirname):
            print('"{}" is not a directory'.format(dirname), file=sys.stderr)
        else:
    
            for eachfile in os.listdir(dirname):
                out={}
                with open('{}/{}'.format(dirname,eachfile)) as temp:
                    out[temp.readline().strip()]=temp
            thelines={}
            for thelines in out.items():
                aline = thelines[0]
                afile = thelines[1]
                print('{} {} {}'.format(aline, ['.' for j in width-len(aline)+1],afile))  
                                

#    print('str_arg = "{}"'.format(str_arg))
#    print('int_arg = "{}"'.format(int_arg))
#    print('flag_arg = "{}"'.format(flag_arg))
#    print('positional = "{}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
