import pandas as pd
import matplotlib.pyplot as plt

# read csv file and load to data frame
df = pd.read_csv('data/covid-19-cases.csv')

# group by country column and sum over the different states/regions of each country
grouped = df.groupby('Country/Region')
df_countries = grouped.sum()


def make_plot(country):
    """make the bar plot of case numbers and change in numbers line plot."""

    # extract the series corresponding to the case numbers for country
    c_df = df_countries.loc[country, df_countries.columns[3:]]

    # convert index to a proper datetime object
    c_df.index = pd.to_datetime(c_df.index)

    # get the number of column
    n = len(c_df)

    # setting bar with corresponding values
    plt.bar(range(n), c_df.values)

    # setting x and y label
    plt.xlabel('Days')
    plt.ylabel('Confirmed cases, $N$')

    # add a title reporting the latest number of cases available
    title = '{}\n{} cases on {}'.format(country, c_df[-1],
                                        c_df.index[-1].strftime('%d %B %Y'))
    plt.suptitle(title)


# make plot for a corresponding country
make_plot('Vietnam')
plot = plt.show()
