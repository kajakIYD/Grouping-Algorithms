import matplotlib.pyplot as plt


def plot(clusters_with_tuples_sorted, title, max_grade=5):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    plt.figure()
    plt.xlabel('Student')
    plt.ylabel('Result')
    handles = []
    labels = []
    for item, color, in zip(clusters_with_tuples_sorted, colors):
        for pair, count in zip(clusters_with_tuples_sorted[item], range(len(clusters_with_tuples_sorted[item]))):
            if count == 0:
                handles.append(plt.scatter(pair[0] + 1, pair[1], color=color))
                labels.append("Grade " + str(max_grade - item))
            else:
                plt.scatter(pair[0] + 1, pair[1], color=color)
    plt.legend(handles, labels, loc=0,
                ncol=1, fancybox=True, shadow=True, prop={'size': 6})
    plt.xticks(list(plt.xticks()[0]) + [1])
    plt.xlim(left=1)
    plt.title(title)
    plt.show()
