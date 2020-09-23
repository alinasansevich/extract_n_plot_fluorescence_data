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

import datetime
import pygal

#######
# bosquejo inicial:

# data = {}

# # using os module
# for file in directory:
#     reader = csv.reader()
#     # read until reader == ROX -- or go to line xxx
#     data[primeros8chardelfile] = [reader]
#     # y despues .append las demas lineas

# plot

# usar datetime para transformar cada key en un datetime object

# box-plot

# filename_1 = "20200102113551_00890018002017-00320181107-874282.csv"

######
# program starts here
file_path = '/home/alina/Learning_to_Code/My_Projects/raw_readings/test_files'

# these are the files to iterate over:
test_files = os.listdir(file_path)

all_data = {}

start = 46
stop = 62

for filename in test_files:
    raw_data =[]
    for i in range(start, stop):
        with open(filename) as f:
            row = next(itertools.islice(csv.reader(f), i, None))
            raw_data.append(row)
    
    file_date = filename[0:8]
    data_points_lists = []
    for item in raw_data:
        x = item[1:len(item)-1]   # I only need raw_data[item][1:25]
        data_points_lists.append(x)
    data_points = [data_point for inner_list in data_points_lists for data_point in inner_list]

    if file_date not in all_data.keys():
        all_data[file_date] = data_points
    else:
        for data_point in data_points:
            all_data[file_date].append(data_point)



