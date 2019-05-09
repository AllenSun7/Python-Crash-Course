#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:30:28 2019

@author: allen
"""

from pygal.maps.world import World

wm = World()
wm.title = 'North, Central, South America, China'

wm.add('North America', {'ca': 34126000, 'mx': 113423000, 'us': 309349000})
wm.add('Central America', ['ba', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add('China',['cn'])

wm.render_to_file('americas.svg')
