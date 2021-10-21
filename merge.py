#!/usr/bin/python
# -*- coding: utf-8 -*-

#*****************************************************************************************
#
#  Write generator merge(…) which accepts as arguments an arbitrary number of iterables,
#  each of which generates sorted numbers, not necessarily one after another. merge() 
#  must merge the outputs of the iterables, i.e. give sorted queue of all the numbers 
#  from the input iterables. merge() must correctly stop if all of the input iterables 
#  have stopped. Please supply unit tests for your solution.
#
#  E.g., the input iterables are three generators giving the following numbers:
#
# 
#
#  Iterable 1: 1, 5, 9
#
#  Iterable 2: 2, 5
#
#  Iterable 3: 1, 6, 10, 11
#
#  The sequence generated by merge(…) in this case must be: 1, 1, 2, 5, 5, 6, 9, 10, 11
#
#*****************************************************************************************

""" Python script to demonstrate merge of iterables, generated based on cli args passed.
"""


import sys
import random
from collections import OrderedDict
import itertools


def _check_cli_args():
    """ Check if cli arguments are valid
    """

    if len(sys.argv) < 2:
        print("Arbitrary number of digits need to be passed as cli arguments.")
        sys.exit(1)
    for arg in sys.argv[1:]:
        try:
            arg_int = int(arg)
        except ValueError, e:
            print("Unable to parse arg \'{}\' as a digit.".format(arg))
            sys.exit(1)


def merge(**iterable_dict):
    """ Merge and sort values of passed dictionary into single list
    """

    merged = [item for sublist in iterable_dict.values() for item in sublist]     
    merged.sort()
    return merged


def generate_dict():
    """ Generate dictionary of iterables based on cli args passed,
        each iterable is a list of random digits in range 1-15
    """
    
    dict_of_iterables=OrderedDict()
    for i in range(len(sys.argv[1:])):
        for x in range(int(sys.argv[1:][i])):
          if 'iterable{}'.format(i+1) not in dict_of_iterables:
            dict_of_iterables['iterable{}'.format(i+1)]=[]
            dict_of_iterables['iterable{}'.format(i+1)].append(random.randint(1,15))
          else:
            dict_of_iterables['iterable{}'.format(i+1)].append(random.randint(1,15)) 
    return dict_of_iterables    


def main():
    _check_cli_args()
    try:
        d = generate_dict()
    except:
        print("Unable to generate dictionary of iterables")
        sys.exit(1)
    print("Before merge:")
    for key, val in d.items():
        val.sort()
        print("{}: {}".format(key, val))
    print("After merge:")
    print merge(**d)
     

if __name__ == '__main__':
    main()