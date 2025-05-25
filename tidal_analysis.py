#!/usr/bin/env python3

# importing the modules i need
import argparse
import pandas as pd
import numpy as np



def read_tidal_data(filename):

    """ 
    this function below will read the tidal data files, 
    making sure to skip the first 11 unnecessary 11 lines which don't contain useful data.
    also parsing date and time and cleaning missing values.
    it will return a DataFrame indexed by 'datetime' with 'Sea Level' column.
    
    """

    df = pd.read_csv(
        filename,
        skiprows=11,
        sep=r'\s+',
        header=None,
        engine='python',
        on_bad_lines='skip'
    )

    df = df[[1, 2, 3]]  # date, time, sea level
    df.columns = ['Date', 'Time', 'Sea Level']

    df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors='coerce')
    
    df.replace(
        to_replace=r'.*[MNT]$',
        value={'Sea Level': np.nan},
        regex=True,
        inplace=True   # 'inplace' tells pandas to edit the DataFrame directly,instead of returning a new modified copy.
    )
    
    df['Sea Level'] = pd.to_numeric(df['Sea Level'], errors='coerce')
    df = df.dropna(subset=['datetime'])

    df = df.set_index('datetime')
    
    return df[['Sea Level']]

  
   
def extract_section_remove_mean(start, end, data):
    
    """
    Extracts a time slice of the tidal data between 'start' and 'end' datetimes,
    removes missing values, and subtracts the mean sea level so the result is zero-centered.
    """
    
    section = data.loc[start:end]
    section = section.dropna(subset=['Sea Level'])
    section['Sea Level'] = section['Sea Level'] - section['Sea Level'].mean()
    return section

# Due to flagged/missing data in the files, the actual number of valid records was 1358 instead of 2064 between the given dates. 
# The function drops NaNs as required by the spec before computing the mean.


def join_data(data1, data2):
   
    """
    Joins two time-indexed tidal DataFrames into one, sorting by datetime.
    """
  
    combined = pd.concat([data1, data2])
    combined = combined.sort_index()
    return combined


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
    


