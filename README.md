# extract_n_plot_fluorescence_data

## Table of contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description
[(Back to top)](#table-of-contents)

This program extracts fluorescence data from structured .csv files and plots the values in box-plots, fluorescence vs. date.

## Installation
[(Back to top)](#table-of-contents)

This project uses [matplotlib](https://matplotlib.org/stable/users/installing.html) to create the plots. You'll need to install this library before running the program.

## Usage
[(Back to top)](#table-of-contents)

Place all the .csv files with the fluorescence data in a directory, and `extract_n_plot_fluo_data.py` in its parent directory.
On the terminal, navigate to the directory where you have `extract_n_plot_fluo_data.py` and then type or copy/paste the following line:

        `python3 extract_n_plot_fluo_data.py`

The program will prompt you to enter the filepath of the directory where your files are located. Example:

        `/home/alina/csv_files`

This plots the graph directly for the user to see, zoom and choose the file format to save. It saves by default to .pdf after the user closes the matplotlib pop-up window.

Examples of output plots are below:

![run3_1000](https://user-images.githubusercontent.com/58040292/114072305-bde6b900-9867-11eb-8b7e-bfa2d5e1927b.png)
##### Box-plot with values from 1000 .csv files.<br>





![run4_27700](https://user-images.githubusercontent.com/58040292/114072518-f9818300-9867-11eb-9fc9-0adb0419091b.png)
##### Box-plot with values from 27700 .csv files. The dates are still readable and all details can be clearly seen by zooming-in in the .png file.

***

## License
[(Back to top)](#table-of-contents)

This repository contains content developed by Alina Sansevich and is distributed under the MIT license.<br>
***
