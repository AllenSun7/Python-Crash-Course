#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:11:14 2019

@author: allen
"""

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test name_function.py"""
    
    def test_first_last_name(self):
        """Can it correctly deal with names such as Janis Joplin?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_lat_middle_name(self):
        """ Can it correctly deal with names like Wolfgang Amadeus Mozrat?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
unittest.main()