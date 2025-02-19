import pandas as pd
import matplotlib.pyplot as plt

# read csv and load to data frame
df = pd.read_csv('data/samples.csv')

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

# create a default plot with some chose info (Rank, P25th, Median, P75th)
def plot_default(data_frame):
    return data_frame.plot(x="Rank", y=["P25th", "Median", "P75th"])

# create a hist plot with median info (distributions and histograms)
def plot_median_hist(data_frame):
    return data_frame["Median"].plot(kind="hist")

# create a bar plot with median info (top 5)
def plot_median_top5(data_frame):
    return data_frame.sort_values(by="Median", ascending=False).head().plot(
        x="Major", y="Median", kind="bar", rot=5, fontsize=4)

# create a bar plot with median info (three bars per major)
def plot_three_bars(data_frame):
    return data_frame[data_frame["Median"] > 60000].sort_values("Median").plot(
        x="Major", y=["P25th", "Median", "P75th"], kind="bar")

# create a scatter plot with median info
def plot_scatter(data_frame):
    return data_frame.plot(x="Median", y="Unemployment_rate", kind="scatter")

# create a plot with grouping
def plot_grouping(data_frame):
    return data_frame.groupby("Major_category")["Total"].sum().sort_values().plot(kind="barh", fontsize=4)

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
def show_plot(plot):
    plt.show(plot)

# save the plot figure to file
def save_plot(plot, file_name):
    plot.figure.savefig("graph/"+file_name)


plot_default = df.plot(x="Rank", y=["P25th", "Median", "P75th"])
# show the plot to screen
plt.show()
# save the plot figure to file
plot_default.figure.savefig('graph/plot_default.png')


# create a hist plot with median info (distributions and histograms)
median_column = df["Median"]
plot_median_hist = median_column.plot(kind="hist")
plt.show()
plot_median_hist.figure.savefig('graph/plot_hist.png')


# create a bar plot with median info
# sort and get top 5 values
top_5 = df.sort_values(by="Median", ascending=False).head()
plot_median_top5 = top_5.plot(
    x="Major", y="Median", kind="bar", rot=5, fontsize=4)
plt.show()
plot_median_top5.figure.savefig('graph/plot_bar_top5.png')


# three bars per major
top_medians = df[df["Median"] > 60000].sort_values("Median")
plot_three_bars = top_medians.plot(
    x="Major", y=["P25th", "Median", "P75th"], kind="bar")
plt.show()
plot_three_bars.figure.savefig('graph/plot_three_bars.png')


# create a scatter plot with median info
plot_scatter = df.plot(x="Median", y="Unemployment_rate", kind="scatter")
plt.show()
plot_scatter.figure.savefig('graph/plot_scatter.png')


# create a plot with grouping
cat_totals = df.groupby("Major_category")["Total"].sum().sort_values()
plot_grouping = cat_totals.plot(kind="barh", fontsize=4)
plt.show()
plot_grouping.figure.savefig('graph/plot_grouping.png')


# create a pie plot
small_cat_totals = cat_totals[cat_totals < 100_000]
big_cat_totals = cat_totals[cat_totals > 100_000]
# adding a new item "Other" with the sum of the small categories
small_sums = pd.Series([small_cat_totals.sum()], index=["Other"])
big_cat_totals = big_cat_totals._append(small_sums)

plot_pie = big_cat_totals.plot(kind="pie", label="")
plt.show()
plot_pie.figure.savefig('graph/plot_pie.png')
