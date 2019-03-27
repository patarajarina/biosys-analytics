#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-02-12
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():

    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe borad',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='The state of the board',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='The player to modify the state',
        metavar='str',
        type=str)

    parser.add_argument(
        '-c', 
        '--cell', 
    #     help='Cell to apply -p', 
     #    metavar='str',
      #   type=str,
        help='The cell to alter',
        metavar='int',
        type=int,
        default=None)

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
#    str_arg = args.arg
#    int_arg = args.int
#    flag_arg = args.flag
#    pos_arg = args.positional
#
#    print('str_arg = "{}"'.format(str_arg))
#    print('int_arg = "{}"'.format(int_arg))
#    print('flag_arg = "{}"'.format(flag_arg))
#    print('positional = "{}"'.format(pos_arg))

# no cell selecting


    state = args.state
    player = args.player
    cell = args.cell
    cells = [1,2,3,4,5,6,7,8,9]
#    print(state)
#    for i, c in enumerate(state):
#        cell = i+1 if c == '.' else c
#        print(cell, end='')
#        if (i+1)%3 == 0:
#            print('')
    # Bad state
    if len(state) != 9:
        print('State "{}" must be 9 characters of only ., X, O'.format(state))
        sys.exit(1)

    for letter in state:
        if letter != '.' and letter != 'X' and letter != 'O':
            print('State "{}" must be characters of only ., X, O'.format(state))
            sys.exit(1)
    #invalid player
    if player is not None and (player != 'X' and player != 'O'):
        die('Invalid player "{}", must be X or O'.format(player))

    #invalid cell
    
#    print(type(cell))
    if cell is not None and not 1 <= cell <= 9:
        die('Invalid cell "{}", must be 1-9'.format(cell))

    #good state

    h_sep = '-------------' 
    for i, c in enumerate(state):
        if i == 0:
            print(h_sep)
        cells = i+1 if c == '.' else c

        if player and cell == i+1:
            cells = player

        print('|',cells, end=' ')
        if (i+1)%3==0:
            print('|')
            print(h_sep)
    


    #board


#------------------------------------------------
if __name__ == '__main__':
    main()
