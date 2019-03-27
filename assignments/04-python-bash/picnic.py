#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    items = sys.argv[1:]

    if len(items) < 1:
        print('Usage: {} ITEM [ITEM2..]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    item = items[0]

    print('Arg is "{}"'.format(item))


# --------------------------------------------------
main()
