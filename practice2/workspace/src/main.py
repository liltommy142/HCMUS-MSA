import pandas as pd
import matplotlib.pyplot as plt

# read csv and load to data frame
df = pd.read_csv("D:\Study\HCMUS-MSA\practice2\workspace\data\samples.csv")

# print the first five rows of data frame
print(df.head())

# "Median" is the median earnings of full-time, year-round workers
# "P25th" is the 25th percentile of earnings
# "P75th" is the 75th percentile of earnings
# "Rank" is the major’s rank by median earnings

# some optional parameters of plot
# "area" is for area plots
# "bar" is for vertical bar charts
# "barh" is for horizontal bar charts
# "box" is for box plots
# "hexbin" is for hexbin plots
# "hist" is for histograms
# "kde" is for kernel density estimate charts
# "density" is an alias for "kde"
# "line" is for line graphs
# "pie" is for pie charts
# "scatter" is for scatter plots

# read file and load to data frame (using Pandas)
def read_file(file_name):
    return pd.read_csv(file_name)

# visualize the data (using Matplotlib)
def visualize_data(data_frame):
    data_frame.plot()
    plt.show()

# create a default plot with some chosen info (Rank, P25th, Median, P75th)
def plot_default(data_frame):
    return data_frame.plot(x="Rank", y=["P25th", "Median", "P75th"])

# create a hist plot with median info (distributions and histograms)
def plot_median_hist(data_frame):
    return data_frame["Median"].plot(kind="hist")

# create a bar plot with median info (top 5)
def plot_median_top5(data_frame):
    return (
        data_frame.sort_values(by="Median", ascending=False)
        .head()
        .plot(x="Major", y="Median", kind="bar", rot=5, fontsize=4)
    )

# create a bar plot with median info (three bars per major)
def plot_three_bars(data_frame):
    return (
        data_frame[data_frame["Median"] > 60000]
        .sort_values("Median")
        .plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")
    )

# create a scatter plot with median info
def plot_scatter(data_frame):
    return data_frame.plot(x="Median", y="Unemployment_rate", kind="scatter")

# create a plot with grouping
def plot_grouping(data_frame):
    return (
        data_frame.groupby("Major_category")["Total"]
        .sum()
        .sort_values()
        .plot(kind="barh", fontsize=4)
    )

# create a pie plot
def plot_pie(data_frame):
    cat_totals = data_frame.groupby("Major_category")[
        "Total"].sum().sort_values()
    small_cat_totals = cat_totals[cat_totals < 100_000]
    big_cat_totals = cat_totals[cat_totals > 100_000]
    # adding a new item "Other" with the sum of the small categories
    small_sums = pd.Series([small_cat_totals.sum()], index=["Other"])
    big_cat_totals = big_cat_totals._append(small_sums)
    return big_cat_totals.plot(kind="pie", label="")

# show the plot to screen
def show_plot():
    plt.show()

# save the plot figure to file
def save_plot(plot, file_name):
    plot.figure.savefig("graph/" + file_name)

# main
if __name__ == "__main__":
    # Read the CSV file into a DataFrame
    df = read_file("D:\Study\HCMUS-MSA\practice2\workspace\data\samples.csv")
    
    # Print the first five rows of the DataFrame
    print(df.head())
    
    # Visualize the entire DataFrame
    visualize_data(df)

    # Create and show the default plot
    plot = plot_default(df)
    show_plot()
    save_plot(plot, "default_plot.png")

    # Create and show the histogram of median earnings
    plot = plot_median_hist(df)
    show_plot()
    save_plot(plot, "median_hist.png")

    # Create and show the bar plot of top 5 median earnings
    plot = plot_median_top5(df)
    show_plot()
    save_plot(plot, "median_top5.png")

    # Create and show the bar plot of median earnings above 60,000
    plot = plot_three_bars(df)
    show_plot()
    save_plot(plot, "three_bars.png")

    # Create and show the scatter plot of median earnings vs. unemployment rate
    plot = plot_scatter(df)
    show_plot()
    save_plot(plot, "scatter.png")

    # Create and show the bar plot grouped by major category
    plot = plot_grouping(df)
    show_plot()
    save_plot(plot, "grouping.png")

    # Create and show the pie chart of major categories
    plot = plot_pie(df)
    show_plot()
    save_plot(plot, "pie.png")
