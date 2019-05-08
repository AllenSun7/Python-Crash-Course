#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:45:24 2019

@author: allen
"""
import pygal
from die import Die

#Create two D6 dice.
die_1 = Die()
die_2 = Die(10)

#Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# sort with dictionary
frequency = dict()
for num in range(len(results)):          
    frequency[results[num]] = frequency.get(results[roll_num], 0) + 1
    
print(sorted(frequency.items()))

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency1 = results.count(value)
    frequencies.append(frequency1)
print(frequencies)

#Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."

values = sorted(frequency.keys())
hist.x_labels = values # map(str, values)
#hist.x_lables = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')


















