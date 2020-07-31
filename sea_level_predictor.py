import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"])

    x_extended = np.arange(1880, 2050)

    plt.plot(x_extended, intercept + slope*x_extended, "r")
    # Create second line of best fit
    dfNew = df.loc[(df["Year"] >= 2000)]

    slopeNew, interceptNew, r_valueNew, p_valueNew, std_errNew = linregress(
        dfNew["Year"], dfNew["CSIRO Adjusted Sea Level"])

    plt.plot(x_extended, interceptNew + slopeNew*x_extended, "r")
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
