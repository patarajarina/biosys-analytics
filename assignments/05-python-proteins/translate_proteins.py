#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-02-18
Purpose: Rock the Casbah
"""
import os
import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='A positional argument')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codons translation',
        metavar='FILE',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')

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
    input_codons = args.codons
    output_data = args.output
    
#    flag_arg = args.flag
    pos_arg = args.positional
    input_seq = pos_arg.upper()
    
  

    if not os.path.isfile(input_codons):
        die('--codons "{}" is not a file'.format(input_codons))

    translate={}
    for line in open(input_codons):
        codon, aa = line.split()
        translate[codon] = aa
       
    n = 3
    m = len(pos_arg)-n+1
    prot = ''
    for line in range(0,m,n):
        one_codon = input_seq[line:line+n]
        if one_codon in translate.keys():
            one_aa = translate[one_codon]
        else:
            one_aa = '-'
        prot += one_aa
    #print(prot)
        
        
    with open(output_data,"w") as fileout:
        print(prot,file=fileout)               
        print('Output written to "{}"'.format(output_data))       


# --------------------------------------------------
if __name__ == '__main__':
    main()
