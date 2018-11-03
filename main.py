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
    values_raw = file_parsing.load_values(file_path=class_string)
    values = values_processing.append_student_to_value(values_raw)
    plt.figure(i)
    plt.xlabel('Result')
    plt.xlim(left=1)
    plt.ylabel('Student')
    X = np.array(values_raw)
    estimator = KMeans(n_clusters=5, random_state=42).fit(X.reshape(-1, 1))
    x = [tup[0] for tup in values]
    y = [tup[1] for tup in values]
    colors = values_processing.normalize(estimator.labels_)
    plt.scatter(np.asarray(x), np.asarray(y), c=colors)
    plt.show()
