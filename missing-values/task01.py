import numpy as np

def mean_without_nan(values):
    values_sum = 0
    not_nan_count = 0

    for value in values:
        if not np.isnan(value):
            values_sum += value
            not_nan_count += 1

    return values_sum / not_nan_count


def impute_missing_values(values):
    values = values.copy()
    values_mean = mean_without_nan(values)

    for i in range(len(values)):
        if np.isnan(values[i]):
            values[i] = values_mean

    return values


test_values = [60, 68, 77, 67, np.nan, 69, np.nan, 70, 66, 70]
complete_values = impute_missing_values(test_values)
print(complete_values)
