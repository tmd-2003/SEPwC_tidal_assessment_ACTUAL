#!/usr/bin/env python3

# importing the modules i need
import argparse
import pandas as pd
import numpy as np


#this reads one tidal data file, ignore headers and returns data w/ datetime + sea level
def read_tidal_data(filename):
    """ 
    reads tidal data file, skipping headers, parses data and time while cleaning missing/flagged values. 
    returns a dataframe with (datetime) and (sealevel) columns 
    --> sealevel is defined by ASLVZZ01 data
    """

    # Read the file, skipping first 9 header rows
    df = pd.read_csv(
        filename,
        skiprows=9,
        sep=r'\s+',  
        header=None,
        names=["Cycle", "Date", "Time", "SeaLevel", "Residual"],
        engine='python'
    )

    # Combine Date and Time into a single 'datetime' column
    df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors='coerce')

    # Here replaces any flagged values (ending in M, N or T) with NaN in SeaLevel column.
   df['SeaLevel'].replace(
    to_replace=r'.*[MNT]$', value=np.nan, regex=True, inplace=True
    )
   
    # Convert SeaLevel to float (any non-numeric will become NaN)
    df['SeaLevel'] = pd.to_numeric(df['SeaLevel'], errors='coerce')

    # Drop rows where datetime is NaT (just in case)
    df = df.dropna(subset=['datetime'])

    # Return only datetime and SeaLevel columns, reset index
    return df[['datetime', 'SeaLevel']].reset_index(drop=True)

    return 0
 
#this extracts only this year's data, removes mean   
def extract_single_year_remove_mean(year, data):
   

    return 

#basically like above but for a certain date rangee
def extract_section_remove_mean(start, end, data):


    return 

#apparently combines two data frames (stacks them) but need to make sure time collumns are aligned.
def join_data(data1, data2):

    return 


#linear regression ie. scipy.stats.linregress to calculate rate of sea level change
def sea_level_rise(data):

                                                     
    return 

# calculate amplitudes for M2, S2 (maybe using tital analysis library or soething called "Fourier Transform?")
def tidal_analysis(data, constituents, start_datetime):


    return 

#finds longest stretch of time without missing data
def get_longest_contiguous_data(data):


    return 

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                     prog="UK Tidal analysis",
                     description="Calculate tidal constiuents and RSL from tide gauge data",
                     epilog="Copyright 2024, Jon Hill"
                     )

    parser.add_argument("directory",
                    help="the directory containing txt files with data")
    parser.add_argument('-v', '--verbose',
                    action='store_true',
                    default=False,
                    help="Print progress")

    args = parser.parse_args()
    dirname = args.directory
    verbose = args.verbose
    


