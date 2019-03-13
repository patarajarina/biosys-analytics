#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-02-27
Purpose: Rock the Casbah
"""

import argparse
import sys
import csv
import os
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotations file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default=sys.stdout)

    #parser.add_argument(
    #    '-f', '--flag', help='A boolean flag', action='store_true')

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
    pos_arg = args.positional

    ann_arg = args.annotations
    out_arg = args.outfile

    if not os.path.isfile(ann_arg):
        die('"{}" is not a file'.format(ann_arg))
    if not os.path.isfile(pos_arg):
        die('"{}" is not a file'.format(pos_arg))


    Alldata = {}

    with open(ann_arg) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            Alldata[row['centroid']] = row
#            Alldata[i] = {row['centroid']:{row['genus'],row['species']}}
            


    inputdata = {}
    with open(pos_arg) as csvfile:
        fieldnames = ['qaccver', 'saccver', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
        reader = csv.DictReader(csvfile, delimiter='\t',fieldnames=fieldnames)
        for row in reader:
            seq_id = row['saccver']
            if seq_id not in Alldata:
                warn('cannot find "{}" in lookup'.format(seq_id))
                continue
           
            pident = row['pident']
            genus = Alldata[seq_id]['genus'] or 'NA'
            species = Alldata[seq_id]['species'] or 'NA'
            inorder = [seq_id, pident, genus, species]

            with open(out_arg, "w") as fh:
                fh.write('\t'.join(inorder) +'\n')   
            #out_arg.write(seq_id, '\t', pident, '\t', genus, '\t', species, '\n')
            
               

                
#die(row)
#            inputdata[row['bfb6f5dfb4d0ef0842be8f5df6c86459']]={row['99.567']}
            #inputdata[i] = row['bfb6f5dfb4d0ef0842be8f5df6c86459']
            #print(inputdata)
            
#    for centroid in Alldata:
#        #print(centroid)
#        for seq_id in inputdata:
#            if centroid == seq_id:
#                pident = inputdata['seq_id']
#                genus = Alldata.get(centroid, default = NA)

                
                
            
     
# --------------------------------------------------
if __name__ == '__main__':
    main()
