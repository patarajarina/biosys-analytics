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

#    if not os.path.isdir(DIRS):
#        print('"{}" is not a directory'.format(dirname), file=sys.stderr)        
#    print(DIRS)
#    dirname = args[0] #check
    for dirname in DIRS:
        if not dirname[-1:] == '/':
            dirname = dirname + '/'
        if not os.path.isdir(dirname):
            if dirname[-1:] == '/':
                dirname = dirname[:-1] 
            print('"{}" is not a directory'.format(dirname), file=sys.stderr)
        else:
            #if len(DIRS)>1:
            print(dirname[:-1])
#            for tup in dirname.items():
#                print(tup)    
            out = {}
            for eachfile in os.listdir(dirname):
                #print(eachfile)
                f = open(dirname + eachfile, "r")
                firstline = f.readline()
                firstline=firstline.strip()
                                
                out[firstline]=eachfile
            #print(out)        
            for keyline, valfile in sorted(out.items()):
                leftlen = width - len(keyline) - len(valfile)
                dots ='.'
                
                for i in range(1,leftlen):
                    dots = dots+'.'
                #print(len(dots+keyline+valfile))
                print('{} {} {}'.format(keyline, dots,valfile))



# --------------------------------------------------
if __name__ == '__main__':
    main()
