#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-04-02
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='A positional argument', nargs='+')

#    parser.add_argument(
#        '-a',
#        '--arg',
#        help='A named string argument',
#        metavar='str',
#        type=str,
#        default='')

#    parser.add_argument(
#        '-i',
#        '--int',
#        help='A named integer argument',
#        metavar='int',
#        type=int,
#        default=0)

#    parser.add_argument(
#        '-f', '--flag', help='A boolean flag', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
#def warn(msg):
#    """Print a message to STDERR"""
#    print(msg, file=sys.stderr)


# --------------------------------------------------
#def die(msg='Something bad happened'):
#    """warn() and exit with error"""
#    warn(msg)
#    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = sys.argv
    pass_arg = args[1:]

    if not len(pass_arg) == 2:
        script = os.path.basename(args[0])
        print('Usage: {} PASSWORD ALT'.format(script))
        sys.exit(1)

    pass1 = pass_arg[0]
    pass2 = pass_arg[1]
    pass2_1 = pass2[0]
#    if not pass2_1.isalpha() and not pass2_1.isdigit():
    pass_re1 = re.compile('^.?' + pass1 + '.?$') 
    pass_re2 = re.compile(pass1.upper())
    pass_left = pass2[0]
    pass_right = pass2[1:]
    pass_re3 = re.compile(pass_left.upper()+ pass_right)
    pass_match = pass_re1.match(pass2) or pass_re2.match(pass2) or pass_re3.match(pass2) 
    
#        if pass_match:
#            pass2 = pass_match.group(0)
    if pass_match:
        print('ok')
    else: 
        print('nah')
# --------------------------------------------------
if __name__ == '__main__':
    main()
