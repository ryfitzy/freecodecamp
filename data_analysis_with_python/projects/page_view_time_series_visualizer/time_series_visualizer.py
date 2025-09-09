import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(f"{os.path.realpath(os.path.dirname(__file__))}/fcc-forum-pageviews.csv", parse_dates=['date'] ,index_col="date")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16,5))
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.plot(df.index.tolist(), df["value"], 'r')

    ax.set_xticks(ticks=['2016-07-01', '2017-01-01', '2017-07-01', '2018-01-01', '2018-07-01', '2019-01-01', '2019-07-01', '2020-01-01'], labels=['2016-07', '2017-01', '2017-07', '2018-01', '2018-07', '2019-01', '2019-07', '2020-01'])

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(pd.Grouper(freq='ME')).mean()

    # Draw bar plot
    fig, ax = plt.subplots()
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    ax.bar(np.arange(48, 60), df_bar[df_bar.index.year == 2019]['value'], width=1, label=months, color=colors)
    ax.bar(np.arange(32, 44), df_bar[df_bar.index.year == 2018]['value'], width=1, color=colors)
    ax.bar(np.arange(16, 28), df_bar[df_bar.index.year == 2017]['value'], width=1, color=colors)
    df_bar_2016 = [0,0,0,0] + df_bar[df_bar.index.year == 2016]['value'].tolist()
    ax.bar(np.arange(0, 12), df_bar_2016, width=1, color=colors)
    
    ax.set_xticks([5, 21, 37, 53], ['2016', '2017', '2018', '2019'])

    ax.legend(loc='upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,6))
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[0].set_ylim(0, 200000)
    axes[0].set_yticks(np.arange(0, 200001, 20000))
    axes[1].set_ylim(0, 200000)
    axes[1].set_yticks(np.arange(0, 200001, 20000))

    axes[0].set_xlabel("Year")
    axes[1].set_xlabel("Month")
    axes[0].set_ylabel("Page Views")
    axes[1].set_ylabel("Page Views")

    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], fliersize=1)
    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], fliersize=1, order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig