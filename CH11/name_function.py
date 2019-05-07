#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:22:02 2019

@author: allen
"""

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:  
        full_name = first + ' ' + middle + ' ' + last
    else:    
        full_name = first + ' ' + last
    return full_name.title()    