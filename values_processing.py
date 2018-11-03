# Values processing
from collections import defaultdict


def append_student_to_value(values):
    values_with_student_number = []
    for i in range(len(values)):
        values_with_student_number.append((i, values[i]))
    return values_with_student_number


def put_values_to_clusters(values, labels):
    clusters_dict = defaultdict(list)
    for val, l in zip(values, labels):
        clusters_dict[l].append(val)
    return clusters_dict


def sort_clusters(values_in_clusters, labels_count):
    temp = []
    for i in range(labels_count):
        values_from_cluster = [int(tup[1]) for tup in values_in_clusters[i]]
        if max(values_from_cluster) > -1:
            temp.append((i, max(values_in_clusters[i])))
        else:
            temp.append((i, None))
    temp.sort(key=lambda tup: tup[1], reverse=True)
    sorted_values_in_clusters = {}
    for i, pos in zip(temp, range(labels_count)):
        sorted_values_in_clusters[pos] = values_in_clusters[i[0]]
    return sorted_values_in_clusters


def normalize(vector):
    return [(value - min(vector))/max(vector) for value in vector]


def sort_value_in_each_cluster(clusters):
    for item in clusters:
        all_tuples_in_cluster = clusters[item]
        tmp = all_tuples_in_cluster.sort(key=lambda x: int(x[1]))
    return clusters
