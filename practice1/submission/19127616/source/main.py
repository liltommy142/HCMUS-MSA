# Implement some basic functions by using Python and NumPy:
# - Mean, Median, Max, Min, Range
# - Variance & Standard Deviation
# - Correlation, etc.

import numpy as np

# Calculate the sum of a list of numbers
def sum(data):
    total = 0
    for x in data:
        total += x
    return total


# Calculate the length of a list of numbers
def len(data):
    count = 0
    for x in data:
        count += 1
    return count


# Calculate the mean of a list of numbers
def calculate_mean(data):
    return sum(data) / len(data)


# Calculate the mean of matrix by X axis
def calculate_mean_axis0(data):
    return [sum(row) / len(row) for row in data]


# Calculate the mean of matrix by Y axis
def calculate_mean_axis1(data):
    return [sum(column) / len(column) for column in zip(*data)]


# Print the mean of matrix by X axis
def print_mean_axis0(data):
    print(calculate_mean_axis0(data))


# Print the mean of matrix by Y axis
def print_mean_axis1(data):
    print(calculate_mean_axis1(data))


# Calculate the median of a list of numbers
def calculate_median(data):
    sorted_data = sorted(data)  # Sort the data
    print("sorted_data = ", sorted_data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        # If the length of the data is even return the average of the two middle elements
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        # If the length of the data is odd return the middle element
        return sorted_data[mid]


# Calculate the max of a list of numbers
def calculate_max(data):
    return np.amax(data)
    # np.amax: Return the maximum of an array or maximum along an axis.


# Calculate the min of a list of numbers
def calculate_min(data):
   return np.amin(data)
    # np.amin: Return the minimum of an array or minimum along an axis.

# Calculate the range of a list of numbers
def calculate_range(data):
    return calculate_max(data) - calculate_min(data)


# Calculate the range of matrix by axis
def calculate_range_by_axis(matrix, axis):
    return np.max(matrix, axis=axis) - np.min(matrix, axis=axis) # axis = 0 or 1
    # np.max & np.min: Return the maximum or minimum of an array or maximum along an axis.


# Calculate the variance of a list of numbers
def calculate_variance(data):
    mean = calculate_mean(data)
    # Calculate the sum of the squared differences between each element and the mean, then divide by the length of the data
    return sum((x - mean) ** 2 for x in data) / len(data)


# Calculate the standard deviation of a list of numbers
def calculate_std_deviation(data):
    variance = calculate_variance(data)
    return variance ** 0.5


# Calculate the covariance between two lists of numbers
def calculate_covariance(data1, data2):
    mean1 = calculate_mean(data1)
    mean2 = calculate_mean(data2)
    # covariance = sum((x - mean(x)) * (y - mean(y))) / n
    return sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2)) / len(data1)


# Calculate the correlation between two lists of numbers
def calculate_correlation(data1, data2):
    mean1 = calculate_mean(data1)
    mean2 = calculate_mean(data2)

    # Calculate the covariance between the two lists
    numerator = calculate_covariance(data1, data2)
    # Calculate the product of the standard deviations of the two lists
    denominator = (calculate_std_deviation(data1)
                   * calculate_std_deviation(data2))
    return numerator / denominator


if __name__ == '__main__':
    # Test mean
    X = np.array([[1, 2], [3, 4]])
    print("X = ", X)
    print("Mean X = ", calculate_mean(X))
    print("Mean X with axis = 0: ", calculate_mean_axis0(X))
    print("Mean X with axis = 1: ", calculate_mean_axis1(X))

    # Test median
    X = [2, 5, 3, 1, 7]
    Y = [2, 1, 8, 5, 7, 9]
    print("X = ", X)
    print("Y = ", Y)
    print("Median X = ", calculate_median(X))
    print("Median Y = ", calculate_median(Y))

    # Test max & min
    X = np.array([[14, 96],
                  [46, 82],
                  [80, 67],
                  [77, 91],
                  [99, 87]])
    print("X = ", X)
    print("Max: ", calculate_max(X))
    print("Min: ", calculate_min(X))

    # Test range
    X = np.array([[14, 96],
                  [46, 82],
                  [80, 67],
                  [77, 91],
                  [99, 87]])
    print("X = ", X)
    print("Range = ", calculate_range(X))
    
    print("Range (axis = 0) = ", np.ptp(X, axis=0))
    print("Range (axis = 1) = ", np.ptp(X, axis=1))
    
    print("Range (axis = 0) = ", calculate_range_by_axis(X, axis=0))
    print("Range (axis = 1) = ", calculate_range_by_axis(X, axis=1))
    
    # Test variance & standard deviation
    X = [19, 33, 51, 22, 18, 13, 45, 24, 58, 11, 25, 27, 26, 29]
    print("X = ", X)
    print("Variance: ", calculate_variance(X))
    print("Standard Deviation: ", calculate_std_deviation(X))

    # Test correlation
    data1 = [1, 2, 3, 4, 5]
    data2 = [2, 3, 4, 5, 6]
    print("Data1 = ", data1)
    print("Data2 = ", data2)
    print("Correlation: ", calculate_correlation(data1, data2))
    
    # Test covariance
    data1 = [1, 2, 3, 4, 5]
    data2 = [2, 3, 4, 5, 6]
    print("Data1 = ", data1)
    print("Data2 = ", data2)
    print("Covariance: ", calculate_covariance(data1, data2))
    