import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(f"{os.path.realpath(os.path.dirname(__file__))}/epa-sea-level.csv")

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(x, y)
    x_range = np.arange(1880, 2051)
    plt.plot(x_range, x_range*slope + intercept)

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    slope, intercept, _, _, _ = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x_range = np.arange(2000, 2051)
    plt.plot(x_range, x_range*slope + intercept)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.xticks(np.arange(1850, 2076, 25))

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()