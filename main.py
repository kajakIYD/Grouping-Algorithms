# Grouping algorithms
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

import file_parsing
import values_processing


classes = ['a', 'b', 'c', 'd', 'e']
kmeans = []
for c, i in zip(classes, range(len(classes))):
    class_string = "Klasa 3" + c + ".txt"
    values_raw_unsorted = [int(item) for item in file_parsing.load_values(file_path=class_string)]
    values_raw = sorted(values_raw_unsorted)
    values = values_processing.append_student_to_value(values_raw)
    values_unsorted = values_processing.append_student_to_value(values_raw_unsorted)
    plt.figure(i)
    plt.xlabel('Student')
    plt.ylabel('Result')
    X = np.array(values_raw_unsorted)
    estimator = KMeans(n_clusters=5).fit(X.reshape(-1, 1))
    clusters = values_processing.put_values_to_clusters(values_unsorted, estimator.labels_)
    clusters_sorted = values_processing.sort_clusters(clusters, len(set(estimator.labels_)))
    clusters_with_tuples_sorted = values_processing.sort_value_in_each_cluster(clusters_sorted)
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    for item, color in zip(clusters_with_tuples_sorted, colors):
        for pair in clusters_with_tuples_sorted[item]:
            plt.scatter(pair[0]+1, pair[1], color=color)
    plt.xticks(list(plt.xticks()[0]) + [1])
    plt.xlim(left=1)
    plt.show()
    kmeans.append(estimator)