#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:51:33 2020

@author: alina

This program extracts fluorescence data from structured .csv files and
plots the values in a box-plot, fluorescence vs. date.

First approach: csv + pygal

Second approach: pandas + matplotlib 
"""

import os
import csv
import itertools

# import datetime
import pygal
import matplotlib.pyplot as plt

# program starts here
file_path = '/home/alina/Learning_to_Code/My_Projects/raw_readings/test_files'

# these are the files to iterate over:
test_files = os.listdir(file_path)
test_files.sort()

all_data = {}

start = 46
stop = 62

for filename in test_files:
    try:
        raw_data =[]
        for i in range(start, stop):
            with open(filename) as f:
                row = next(itertools.islice(csv.reader(f), i, None))
                raw_data.append(row)
    except StopIteration:
        continue
    
    file_date = filename[0:8]
    data_points_lists = []
    for item in raw_data:
        x = item[1:len(item)-1]   # I only need raw_data[item][1:25]
        data_points_lists.append(x)
    data_points = [float(data_point) for inner_list in data_points_lists for data_point in inner_list]

    if file_date not in all_data.keys():
        all_data[file_date] = data_points
    else:
        for data_point in data_points:
            all_data[file_date].append(data_point)


# Plot with matplotlib.
data = [value for value in all_data.values()]
dates = [key for key in all_data.keys()]

fig1, ax1 = plt.subplots()
ax1.set_title("Fluorescence vs. date")
ax1.boxplot(data)
ax1.set_xlabel("Days")
ax1.set_ylabel("Fluorescence")
ax1.set_xticklabels(dates, rotation=30, fontsize=10)
plt.show()


# Plot with pygal.
box_plot = pygal.Box()
box_plot.title = "Fluorescence vs. date"
for key, value in all_data.items():
    box_plot.add(key, value)
box_plot.render_to_file('fluorescence_vs_date.svg')
