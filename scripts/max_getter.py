# -*- coding: utf-8 -*-
"""
==========
MAX GETTER
==========

should take a .csv file, with a row for each month, and calculate the max ozone for each day at each data collection site.

Created on Tue May 31 03:52:47 2022

@author: Ghost
"""

"""
1. Libraries
"""

import os
import time
import datetime
from calendar import monthrange
import math
import string
import numpy as np
import csv
import pandas as pd
import matplotlib as mpl
from mpl_toolkits import mplot3d
import ast


"""
2. Variable Declaration
"""
daily_somdf_headers = ["date", "month", "ozone", "site"]
daily_somdf = pd.DataFrame(columns = daily_somdf_headers)
some_fileread = False
daily_som_deprecated = False

month_year = ['June 2010', 'July 2010', 'August 2010', 'September 2010',
              'October 2010', 'November 2010', 'December 2010', 'January 2011',
              'February 2011', 'March 2011', 'April 2011', 'May 2011',
              'June 2011', 'July 2011', 'August 2011', 'September 2011',
              'October 2011', 'November 2011', 'December 2011', 'January 2012',
              'February 2012', 'March 2012', 'April 2012', 'May 2012',
              'June 2012', 'July 2012', 'August 2012', 'September 2012',
              'October 2012', 'November 2012', 'December 2012', 'January 2013',
              'February 2013', 'March 2013', 'April 2013', 'May 2013',
              'June 2013', 'July 2013', 'August 2013', 'September 2013',
              'October 2013', 'November 2013', 'December 2013', 'January 2014',
              'February 2014', 'March 2014', 'April 2014', 'May 2014',
              'June 2014', 'July 2014', 'August 2014', 'September 2014',
              'October 2014', 'November 2014', 'December 2014', 'January 2015',
              'February 2015', 'March 2015', 'April 2015', 'May 2015',
              'June 2015', 'July 2015', 'August 2015', 'September 2015',
              'October 2015', 'November 2015', 'December 2015', 'January 2016',
              'February 2016', 'March 2016', 'April 2016', 'May 2016',
              'June 2016', 'July 2016', 'August 2016', 'September 2016',
              'October 2016', 'November 2016', 'December 2016', 'January 2017',
              'February 2017', 'March 2017', 'April 2017', 'May 2017',
              'June 2017', 'July 2017', 'August 2017', 'September 2017',
              'October 2017', 'November 2017', 'December 2017', 'January 2018',
              'February 2018', 'March 2018', 'April 2018', 'May 2018',
              'June 2018', 'July 2018', 'August 2018', 'September 2018',
              'October 2018', 'November 2018', 'December 2018', 'January 2019',
              'February 2019', 'March 2019', 'April 2019', 'May 2019',
              'June 2019', 'July 2019', 'August 2019', 'September 2019']
months_numbers = [0,1,2,3,
         12,13,14,15,
         24,25,26,27,
         36,37,38,39,
         48,49,50,51,
         60,61,62,63,
         72,73,74,75, 
         84,85,86,87,
         96,97,98,99,
         108,109,110,111,112, 113]

threedee_df = []
finalspreadsheet_df = pd.DataFrame(columns = ["date", "month", "ozone", "site"])

"""
3. Function Definition
"""

"""
New function. We've found we need to use ast.literal_eval() on each of these matrix entries to get them to read as a list.
"""
def append_test():
    month = 0
    row = 1
    row_aslist = False
    month_sample_length = len(ast.literal_eval(daily_ozonedf[month][row]))
    # Currently 29 is a magic number. I think it needs to be 34, the number of rows in this table
    print(month_sample_length)
    while row < month_sample_length:
        row_aslist = ast.literal_eval(daily_ozonedf[month][row])
        threedee_df.append(row_aslist)
        row = row + 1
    
# Test function call
    
"""
row_aslist = ast.literal_eval(daily_ozonedf[0][0])
print(row_aslist)
print(len(row_aslist))
"""
def column_tryer(x):
    # x should be the column that we check all the values in for a month
    # i is the row within the month to be iterated through
    i = 0
    month = 0
    month_aslist = ast.literal_eval(daily_ozonedf[month][x])
    print(len(month_aslist))
    while i < len(month_aslist):
        threedee_df.append(month_aslist[i])
        i = i + 1

"""
Here we make a function that returns the number of days in each month, and the 
year.
"""
def month_days(i):
    # I don't understand why using 5 instead of 6 here works for both the year 
    # and the month when the calendar starts in June, but I'm just gonna leave
    # it.
    # i should start at 0 in the loop whenever this function is called
    year = 2010 + math.floor((5 + i) * 1/12)
    month = ((5 + i) % 12) + 1
    dayrange = monthrange(year, month)[1]
    return_list = [dayrange, i, year, month]

    return (return_list)


def month_lengthtest():
    i = 0
    while i < 113:
        print(month_days(i))
        i = i + 1

"""
Each x in this function is a month. This returns all of the data columns, plus 
the headers, for the month.

I didn't explain this well. Each x should be a new month. each c should be a 
new day. We want to modify the function to create an internal list per day and 
return the max each day. Right now this gives me a list for each site that 
extends through the sample. I need it to compare samples from different sites 
for the same day. May need to make a subroutine returning the number of sites 
for each day.

Okay, now it gives the daily maximum. I need this to work given a particular 
date in the SOM file, and I also need it to return the site as a separate 
argument. Forcing int in the print/try loop seems to have made something work 
correctly that I don't really understand. Look there first when debugging.

"""

"""
So then, if I'm trying to return the site at which the daily max occurs, we do 
something with the index corresponding to the site_row while shifting the 
column backwards to the one that says site.
"""

def df_maxer(x, c, t, m):
# i is something else. i is the row in terms of which monitoring site.    
# c should be a column constant, after the first few columns it denotes the day
# what is x? no, x is the row+month. 
# m is the current month.
    

    daily_max = []
    date = t - 3
    month_name = str(month_year[m])
    i = 1    
    while i < 34:

        try:
            evidence = ast.literal_eval(daily_ozonedf[i][x])
            daily_max.append(int(evidence[c]))
            i = i + 1
        except ValueError:
#            print("ValueError")
            i = i + 1
        except SyntaxError:
#            print("SyntaxError")
            i = i + 1

    try:
        max_ozone = (max(daily_max))
        max_index = daily_max.index(max_ozone) - 1
        month_name = str(month_year[m]) 
        max_name = daily_ozonedf[max_index][1]
        evidence = ast.literal_eval(max_name)
    except:
        print("hooty hoo")

    finally:
        site_name = str(evidence[1])

    
    return(date, month_name, max_ozone, site_name)
        
# Good, now this correctly prints the same column in each row meaning month
    

def daily_function():
    i = 1
    while i < 1221:
        current_date = daily_somdf[1][i]
        current_month = daily_somdf[3][i]
        print(datetime.datetime.strptime(current_date, "%Y-%m-%d"))
        print(current_month)
        i = i + 1
    return(False)
    
# Here is our function to get the list of maxes for the whole moonth using 
# daily_max function and return them as a list or something.
def month_looper(month, length, month_count, input_df):
# I think I need to dig into this function and get the program using DataFrames at a more core level
    i = 4
    while i < length:
#        print(df_maxer(month, i, i, month_count))
        date, month_name, max_ozone, site_name = (df_maxer(month, i , i, month_count))
#        print(date, month_name, max_ozone, site_name)
        item_dict = {'date': [date], 'month': [month_name], 'ozone': [max_ozone], 'site': [site_name]}
        new_items = pd.DataFrame(item_dict)
        input_df = pd.concat([input_df, new_items])
        print(input_df)
        i = i + 1
    return(input_df)
 
def column_tryloop(row, input_data, output_data):
    null_items = {'date': ['NA'], 'month' : ['NA'], 'ozone': ['NA'], 'site': ['NA']}
    null_row = pd.DataFrame(null_items)
    try:
        output_data_buffer = (month_looper(row, 35, row, output_data))
        output_data = pd.concat([output_data, output_data_buffer])
        # 34 is the highest list index that is in range for middle term of month_looper        
        print(output_data)
    except:
        output_data = pd.concat([output_data, null_row])
        print(row)
    finally:
        return(output_data)
 
def column_creator(output_filename, input_df):
    i = 0
    new_columns = pd.DataFrame(columns = ["date", "month", "ozone", "site"])
    rows_list = [new_columns]
    while i < 114: # at this point in time, i seems to function properly up to 
        if i in (months_numbers):
            x = column_tryloop(i, new_columns, input_df)
            rows_list.append(x)
            new_columns = pd.concat(rows_list)
            i = i + 1
        else:
            i = i + 1
        

    new_columns.to_csv(output_filename)
    print(len(new_columns))
    print(type(new_columns))
    return(new_columns)

       
"""
4. Main

"""
# Navigating to the right folder

os.chdir('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\')
         
with open('som_cluster_10yr_700hpa_00utc.csv') as som_file, open('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\cleaned_data.csv') as ozone_file:
              
    som_fileread = csv.reader(som_file)
    daily_som_deprecated = list(som_fileread)
    daily_somdf = pd.DataFrame(data = daily_som_deprecated)
    
    ozone_fileread = csv.reader(ozone_file)
    daily_ozone_deprecated = list(ozone_fileread)
    daily_ozone_deprecated.pop(0)
    daily_ozonedf = pd.DataFrame(data = daily_ozone_deprecated)


    
    
"""
5. Unit Tests
"""
print(column_creator('4column_fullDFtrialerror.csv', finalspreadsheet_df))
