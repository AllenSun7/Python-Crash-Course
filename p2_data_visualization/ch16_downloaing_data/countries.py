#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:11:19 2019

@author: allen
"""

from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])