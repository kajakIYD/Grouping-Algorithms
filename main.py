# Grouping algorithms
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import SpectralClustering
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch


import file_parsing
import values_processing
import plotting


classes = ['a', 'b', 'c', 'd', 'e']
estimators = [KMeans(n_clusters=5), AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward'),
                  MiniBatchKMeans(n_clusters=5), SpectralClustering(n_clusters=5)]
kmeans = []
values_for_all_classes_unsorted = []
for c, i in zip(classes, range(len(classes))):
    class_string = "Klasa 3" + c + ".txt"
    values_raw_unsorted = [int(item) for item in file_parsing.load_values(file_path=class_string)]
    values_for_all_classes_unsorted.append(values_raw_unsorted)
    # values_raw = sorted(values_raw_unsorted)
    # values = values_processing.append_student_to_value(values_raw)
    values_unsorted = values_processing.append_student_to_value(values_raw_unsorted)
    X = np.array(values_raw_unsorted).reshape(-1, 1)
    for est in estimators:
        estimator = est.fit(X)
        clusters = values_processing.put_values_to_clusters(values_unsorted, estimator.labels_)
        clusters_sorted = values_processing.sort_clusters(clusters, len(set(estimator.labels_)))
        clusters_with_tuples_sorted = values_processing.sort_value_in_each_cluster(clusters_sorted)
        plotting.plot(clusters_with_tuples_sorted, str(repr(est)).split('(')[0] + " " + class_string)

# Whole students
values_for_all_classes_unsorted = [item for sublist in values_for_all_classes_unsorted for item in sublist]
# values_raw_for_all_classes = sorted(values_for_all_classes_unsorted)
values_unsorted = values_processing.append_student_to_value(values_for_all_classes_unsorted)
X = np.array(values_for_all_classes_unsorted).reshape(-1, 1)
estimators = [KMeans(n_clusters=5), AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward'),
              MiniBatchKMeans(n_clusters=5), SpectralClustering(n_clusters=5)]
for est in estimators:
    estimator = est.fit(X)
    clusters = values_processing.put_values_to_clusters(values_unsorted, estimator.labels_)
    clusters_sorted = values_processing.sort_clusters(clusters, len(set(estimator.labels_)))
    clusters_with_tuples_sorted = values_processing.sort_value_in_each_cluster(clusters_sorted)
    plotting.plot(clusters_with_tuples_sorted, str(repr(est)).split('(')[0] + " all students")