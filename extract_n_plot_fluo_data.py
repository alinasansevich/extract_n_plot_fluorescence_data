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
import matplotlib.pyplot as plt

# program starts here
# file_path = input("Enter the absolute file path\nof the directory where your files are located.\nExample: /home/alina/my_files\n\t:")
file_path = '/home/alina/Learning_to_Code/My_Projects/raw_readings/test_files' 
# file_path = '/home/alina/Learning_to_Code/My_Projects/raw_readings/other_files/Raw_Readings'
# these are the files to iterate over:
test_files = os.listdir(file_path)
test_files.sort()

# for i in range(len(test_files)):
#     test_files[i] = file_path + '/' + test_files[i]

all_data = {}

start = 46
stop = 62

for filename in test_files:
    try:
        raw_data =[]
        for i in range(start, stop):
            with open(file_path + '/' + filename) as f:
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


# # Plot with matplotlib.
data = [value for value in all_data.values()]
dates = [key for key in all_data.keys()]


# boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
# flierprops = dict(marker='o', markerfacecolor='green', markersize=12,
#                   linestyle='none')

flierprops = dict(marker='+', markersize=3)
fig = plt.figure(figsize=(40, 4))
ax = fig.add_subplot(111)

# ax1.figure(dpi=1200) 
ax.set_title("Fluorescence vs. date")
ax.boxplot(data, flierprops=flierprops)
ax.set_xlabel("Days")
ax.set_ylabel("Fluorescence")
ax.set_xticklabels(dates, rotation=30, fontsize=10)
plt.tight_layout()
plt.show()
# fig1.savefig('fluorescence_vs_date_27700.pdf')


# # using just plt is even worse, come back after learning matplotlib
# # plt.set_title("Fluorescence vs. date")
# plt.boxplot(data)
# # plt.set_xticklabels(dates, rotation=30, fontsize=10)
# plt.show()


# Plot with pygal.
# box_plot = pygal.Box(width=1000)
# box_plot.title = "Fluorescence vs. date"
# for key, value in all_data.items():
#     box_plot.add(key, value)
# box_plot.render_to_file('/home/alina/Learning_to_Code/My_Projects/raw_readings/fluorescence_vs_date_27700-hoy.svg')