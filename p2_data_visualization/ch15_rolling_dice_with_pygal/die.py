#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:50:48 2019

@author: allen
"""

from random import randint

class Die():
    """A class representing a single die."""
    
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
        
    def roll(self):
        """Reture a random value between 1 and numbe of sides."""
        return randint(1, self.num_sides)