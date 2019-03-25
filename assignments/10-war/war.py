#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys
from itertools import product
import random
import collections

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
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
    seed = args.seed

#Create a deck of card

    suits = list('♥♠♣♦')
    cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
#    deck={}
        
    deck = list(product(suits,cards))

    card=[]
    for i in deck:
        decks = ''.join(i)
        card.append(decks)
#        print(decks)

    #print(card)
#    for j in range(4):
#        for i in range(13):
#            val_card[card[count]] = i+1
#            count=count+1
#    print(val_card.keys)

#    val_card.sort()
#    sort_card = collections.OrderedDict(sorted(val_card.keys))
#    print(sort_card)
#    print(card)
    card.sort()  
    #print(card) 
    if not seed:
        seed = None
    else:
        random.seed(seed)
        
    random.shuffle(card)
    card.reverse()
#    print(card)

    val_card = {}
    val = 2
    for i in cards:
        val_card[i] = val
        val = val+1
#    print(val_card)

    p1score = 0
    p2score = 0
    for i, dcard in enumerate(card):
        if i%2 == 0:
            p1 = dcard
            p1_val = val_card[p1[1:]]
#            print(p1,p1_val) 
        if i%2 == 1:
            p2 = dcard
            p2_val = val_card[p2[1:]]
            #print(p1,p2)
            print('{:>3} {:>3} {}'.format(p1,p2, 'P1' if p1_val>p2_val else 'P2' if p1_val<p2_val else 'WAR!'))         
            if p1_val>p2_val:
                p1score = p1score+1 
            elif p1_val<p2_val:
                p2score = p2score+1
            
    print('P1 {} P2 {}: {}'.format(p1score, p2score, 'Player 1 wins' if p1score > p2score else 'DRAW' if p2score==p1score else 'Player 2 wins'))
            
     



# --------------------------------------------------
if __name__ == '__main__':
    main()
