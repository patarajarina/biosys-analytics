#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-02-26
Purpose: Rock the Casbah
"""
import os
import argparse
import sys
from Bio import SeqIO
import collections

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='FILE', help='FASTA file(s)', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Out dir',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='A named integer argument',
        metavar='int',
        type=int,
        default=50)

    parser.add_argument(
        '-f', '--flag', help='A boolean flag', action='store_true')

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
    fasta= args.fasta
    pct_gc = args.pct_gc
    # = args.flag
    outdir = args.outdir
    seqspl=0

    if not os.path.isdir(outdir):
        os.mkdir(outdir)

    if not pct_gc in range(1,101):
        die('--pct_gc "{}" must be between 0 and 100'.format(pct_gc))    

    for n, file in enumerate(fasta,1):
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue
        print("{}: {}".format(n, file))
        base_name, ext = os.path.splitext(os.path.basename(file))
        lowf = os.path.join(outdir,base_name+'_low'+ext)
        highf = os.path.join(outdir, base_name+'_high'+ext)
        lowfhandle = open(lowf,'wt')
        highfhandle = open(highf, 'wt')

#        print(file)
        
        for record in SeqIO.parse(file, 'fasta'):
            #lengths.append(len(record.seq))
            seq_len=len(record.seq)
            nucs=collections.Counter(record.seq)  #collections.Counter
            gc_num=nucs.get('G',0)+nucs.get('C',0)
#            print(record.seq)
            gcp=int(gc_num/seq_len * 100)
            if gcp < pct_gc:
                SeqIO.write(record, lowfhandle, 'fasta')
            else:
                SeqIO.write(record, highfhandle, 'fasta')
            seqspl=seqspl+1
    print('Done, wrote {} sequences to out dir "{}"'.format(seqspl, outdir))        
#            print(gc)
#            print('HIGH')
#    print('str_arg = "{}"'.format(str_arg))
#    print('int_arg = "{}"'.format(int_arg))
#    print('flag_arg = "{}"'.format(flag_arg))
#    print('positional = "{}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
