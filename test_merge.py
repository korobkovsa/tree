#!/usr/bin/python

from merge import _check_cli_args
from merge import generate_dict 
from merge import merge 
from merge import sys 
import unittest 


class TestMerge(unittest.TestCase):
    """TestCase
    """

    def test_args_exception_exit(self):
        """ test _check_cli_args function sys exit
        """
        sys.argv=['string','3','r']
        with self.assertRaises(SystemExit):
            _check_cli_args()
            
        sys.argv=['string',]
        with self.assertRaises(SystemExit):
            _check_cli_args()


    def test_dictionary(self):
        """ test generate_dict function
        """
        sys.argv=['string','3','3']
        self.assertEqual(len(generate_dict()), 2)
        self.assertEqual(len(generate_dict()['iterable1']), 3)

    def test_merge(self):
        """ test merge function
        """
        
        d = {"iterable1": [1, 5, 9], "iterable2":[2, 5], "iterable3": [1, 6, 10, 11]}     
        self.assertEqual(merge(**d), [1, 1, 2, 5, 5, 6, 9, 10, 11])

        pass
if __name__ == '__main__':
    unittest.main()
