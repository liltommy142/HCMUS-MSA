# Implement some basic functions by using Python and NumPy:
# - Mean, Median, Max, Min, Range
# - Variance & Standard Deviation
# - Correlation, etc.

import numpy as np


def calculate_mean(data):
    return sum(data) / len(data)


def calculate_median(data):
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def calculate_max(data):
    return max(data)


def calculate_min(data):
    return min(data)


def calculate_range(data):
    return max(data) - min(data)


def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def calculate_std_deviation(data):
    variance = calculate_variance(data)
    return variance ** 0.5


def calculate_correlation(data1, data2):
    mean1 = calculate_mean(data1)
    mean2 = calculate_mean(data2)
    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2))
    denominator = (sum((x - mean1) ** 2 for x in data1) *
                   sum((y - mean2) ** 2 for y in data2)) ** 0.5
    return numerator / denominator


if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    data2 = [2, 3, 4, 5, 6]
    print("Mean:", calculate_mean(data1))
    print("Median:", calculate_median(data1))
    print("Max:", calculate_max(data1))
    print("Min:", calculate_min(data1))
    print("Range:", calculate_range(data1))
    print("Variance:", calculate_variance(data1))
    print("Standard Deviation:", calculate_std_deviation(data1))
    print("Correlation:", calculate_correlation(data1, data2))

# Input:
# data1 = [1, 2, 3, 4, 5]
# data2 = [2, 3, 4, 5, 6]

# Output:
# Mean: 3.0
# Median: 3
# Max: 5
# Min: 1
# Range: 4
# Variance: 2.0
# Standard Deviation: 1.4142135623730951
# Correlation: 1.0

# In this code, we have implemented some basic functions to calculate the mean, median, max, min, range, variance, standard deviation, and correlation of two datasets.
# We have used the following functions:

# calculate_mean(data)  – to calculate the mean of a dataset.
# calculate_median(data)  – to calculate the median of a dataset.
# calculate_max(data)  – to calculate the maximum value in a dataset.
# calculate_min(data)  – to calculate the minimum value in a dataset.
# calculate_range(data)  – to calculate the range of a dataset.
# calculate_variance(data)  – to calculate the variance of a dataset.
# calculate_std_deviation(data)  – to calculate the standard deviation of a dataset.
# calculate_correlation(data1, data2)  – to calculate the correlation between two datasets.

# We have tested these functions with two datasets  data1  and  data2  and printed the results.
# Conclusion
# In this article, we have discussed how to calculate the mean, median, max, min, range, variance, standard deviation, and correlation of datasets using Python and NumPy. We have also implemented these functions in Python and tested them with sample datasets.
# You can use these functions to calculate these statistical values for your datasets.


def test_numpy():
    X = [1, 2, 3, 4, 5]
    print("Mean X = ", np.mean(X))

    X = np.array([[1, 2], [3, 4]])
    print("Mean X = ", np.mean(X))
    print("Mean X with axis = 0: ", np.mean(X, axis=0))
    print("Mean X with axis = 1: ", np.mean(X, axis=1))
    a = np.zeros((2, 512 * 512), dtype=np.float32)
    a[0, :] = 1.0
    a[1, :] = 0.1
    print("a.shape: ", a.shape)
    print("mean a = ", np.mean(a))
    print("mean a = ", np.mean(a, dtype=np.float64))
    
    # Median
    X = np.array([2, 5, 3, 1, 7])
    Y = np.array([2, 1, 8, 5, 7, 9])
    print("Median X = ", np.median(X))
    print("Median Y = ", np.median(Y))
    arr = np.array([[7, 4, 2], [3, 9, 5]])
    print("median arr (axis = 0) = ", np.median(arr, axis=0))
    print("median arr (axis = 1) = ", np.median(arr, axis=1))
    
    # Variance & Standard Deviation
    X = [19, 33, 51, 22, 18, 13, 45, 24, 58, 11, 25, 27, 26, 29]
    print("Variance: ", np.var(X))
    print("Standard Deviation: ", np.std(X))
    
    # Variance & Standard Deviation with NaN
    A = np.array([1, np.nan, 3, 4])
    print("var = ", np.var(A))
    print("std = ", np.std(A))
    print("nan var = ", np.nanvar(A))
    print("nan std = ", np.nanstd(A))

    # Order statistics
    X = np.array([[14, 96],
    [46, 82],
    [80, 67],
    [77, 91],
    [99, 87]])
    
    print("X = ", X)
    print("Max: ", np.amax(X))
    print("Min: ", np.amin(X))
    print("Max (axis = 0): ", np.amax(X, axis=0))
    print("Min (axis = 1): ", np.amax(X, axis=1))
    
    # Order statistics with NaN
    X = np.array([[14, 96],
    [np.nan, 82],
    [80, 67],
    [77, np.nan],
    [99, 87]])
    print("X = ", X)
    print("Max: ", np.nanmax(X))
    print("Min: ", np.nanmin(X))

    # Range
    X = np.array([[14, 96],
    [46, 82],
    [80, 67],
    [77, 91],
    [99, 87]])
    print("x = ", X)
    print("Range = ", np.ptp(X))
    print("Range (axis = 0) = ", np.ptp(X, axis=0))
    print("Range (axis = 1) = ", np.ptp(X, axis=1))
    
test_numpy()
