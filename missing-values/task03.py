import numpy as np

def get_distance(value, neighbor):
    return abs(value - neighbor)


def get_neighbors_with_distances(complete_tuples, value):
    neighbors_distances = []
    for tuple in complete_tuples:
        neighbors_distances.append((tuple, get_distance(value, tuple[0])))
    return neighbors_distances


def second(tuple):
    return tuple[1]


def k_nearest_mean(complete_tuples, value, k):
    neighbors_distances = get_neighbors_with_distances(complete_tuples, value)
    neighbors_distances.sort(key=second) # Sorts tuples by their second values.
    neighbors_distances = neighbors_distances[:k]

    values_sum = 0
    for tuple, _ in neighbors_distances:
        values_sum += tuple[1]
    
    return values_sum / k


def add_missing_value(complete_tuples, known_value, k):
    computed_missing_value = k_nearest_mean(complete_tuples, known_value, k)
    complete_tuples.append((known_value, computed_missing_value))
    return complete_tuples


def filter_complete_tuples(data):
    complete_tuples = []
    for tuple in data:
        if not np.isnan(tuple[1]):
            complete_tuples.append(tuple)
    return complete_tuples


def impute_missing_values(data, k):
    complete_tuples = filter_complete_tuples(data)
    for known_value, possibly_missing in data:
        if np.isnan(possibly_missing):
            complete_tuples = add_missing_value(complete_tuples, known_value, k)
    return complete_tuples


test_values = [(166, 71), (176, np.nan), (183, np.nan), (169, 68), (191, 89), (180, 81), (171, 66), (179, 81), (178, 83), (173, np.nan), (184, 79), (191, 87), (166, 70), (165, np.nan), (178, 73), (179, 76), (170, 72), (178, np.nan), (182, 80), (188, 85)]
complete_values = impute_missing_values(test_values, 5)
print(complete_values)
