#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-03-29
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = sys.argv
    date = args[1:]

    if len(date) < 1:
        script = os.path.basename(args[0])
        print('Usage: {} DATE'.format(script))
        sys.exit(1) 
 #   sep = ['/','-',', ']
    date_re4 = re.compile('(?P<month>\d{1,2})'
        '[/, -]'
        '(?P<year>\d{2})')
    date_re5 = re.compile('(?P<year>\d{4})'
        '[/, -]'
        '(?P<month>\d{1,2})')

    date_re1 = re.compile('(?P<year>\d{4})'
        #'[/, -]' # for diff case
        '(?P<month>\d{2})'
                         #'[/-]'
        '(?P<day>\d{2})')
    date_re2 = re.compile('(?P<year>\d{4})'
        '[/, -]' # for diff case
        '(?P<month>\d{1,2})'
        '[/, -]'
        '(?P<day>\d{1,2})'
        '($|\D)')
#        '[/ TZ-]')
        
    date_re3 = re.compile('(?P<month>[a-zA-Z]+)'
        '[, -]+' # for diff case
                        #'(?P<month>\d{2})'
                        #'[, -]'
        '(?P<year>\d{4})')

    dict_month = {'Jan':'01',
                    'Feb':'02',
                    'Mar':'03',
                    'Apr':'04',
                    'May':'05',
                    'Jun':'06',
                    'Jul':'07',
                    'Aug':'08',
                    'Sep':'09',
                    'Oct':'10',
                    'Nov':'11',
                    'Dec':'12'}
    digit1 = {'1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09',}
    for d in date:

        match = date_re1.match(d) or date_re2.match(d) or date_re3.match(d) or date_re4.match(d) or date_re5.match(d)
 
        if match:
            date_dict = match.groupdict()
            year_raw = date_dict.get('year')
            month_raw = date_dict.get('month')
            day_raw = date_dict.get('day')
            month_slice = month_raw[0:3]
         #   print(month_slice)
            if month_raw not in digit1:
                month_val = month_raw
            if day_raw not in digit1:
                day_val = day_raw

            if month_raw in digit1:
                month_val = digit1.get(month_raw)
            if day_raw in digit1:
                day_val = digit1.get(day_raw) 
            if month_slice in dict_month:
                month_val = dict_month.get(month_slice)
            if len(year_raw) == 2:
                year_val = '20'+year_raw
            print('{}-{}-{}'.format(year_raw if len(year_raw)==4 else year_val,month_val,day_val if day_val else '01'))
        else:
            print('No match')


# --------------------------------------------------
if __name__ == '__main__':
    main()
