import numpy as np
import pandas as pd

def count_occurences(values):
    occurences = dict()

    for value in values:
        if np.isnan(value):
            continue

        if value in occurences.keys():
            occurences[value] += 1
        else:
            occurences[value] = 1

    return occurences


def find_most_frequent_value(values):
    counts = count_occurences(values)
    max_count = 0
    max_value = np.NaN

    for value, count in counts.items():
        if count > max_count:
            max_value = value
            max_count = count

    return max_value


def impute_missing_values(values):
    values = values.copy()
    mode = find_most_frequent_value(values)

    for i in range(len(values)):
        if np.isnan(values[i]):
            values[i] = mode

    return values

test_df = pd.read_csv("missing-values.csv")
test_df["weight"] = impute_missing_values(test_df["weight"])
test_df.to_csv("filled-values.csv", index=False)

