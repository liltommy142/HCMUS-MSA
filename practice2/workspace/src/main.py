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


# create a default plot with some chose info
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
plot_median_top5 = top_5.plot(x="Major", y="Median", kind="bar", rot=5, fontsize=4)
plt.show()
plot_median_top5.figure.savefig('graph/plot_bar_top5.png')


# three bars per major
top_medians = df[df["Median"] > 60000].sort_values("Median")
plot_three_bars = top_medians.plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")
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
