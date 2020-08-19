import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
import random
import numpy as np
import time

# Random centroid from data
def random_centroid(x, y):
    # random index of x and y axis
    ix = random.randint(0,len(x)-1)
    iy = random.randint(0,len(y)-1)
    return x[ix], y[iy]


def euclidean_distance(p,q):
    # Find euclidean distance between p point and q point
    result = 0
    for a, b in zip(p, q):
        result += (a-b)**2
    return result ** 0.5

if __name__ == "__main__":
    # define number of cluster 
    n_cluster = 3

    # define color for each cluster
    colour = ["green", "blue", "pink", "black"]
    color_centroid = "red"

    # generate sample data
    X, y_true = make_blobs(n_samples=500, centers=n_cluster,
                        cluster_std=5, random_state=20)

    # plot data
    plt.scatter(X[:, 0], X[:, 1], s=50, color='blue')

    # intialize centroid for each cluster
    centroids = []
    for i in range(n_cluster):
        centroids.append(random_centroid(X[:, 0], X[:, 1]))

    # plot centroids
    for c in centroids:
        plt.scatter(c[0], c[1], s=50, color=color_centroid, marker='v')

    plt.show()

    # use plot ion (interactive mode on) for animation
    plt.ion()

    while True:
        # Assign centroid before = (current) centroid 
        # For compare with (new) centroid
        # if (new) centroid equal to previous_centroid, the algorithm done
        previous_centroid = centroids.copy()

        distance = []
        
        # find distance between all data and each centroid
        # distance i represent distance between data and centroid i
        for i in range(len(centroids)):
            distance.append([])
            for j in range(len(X)):
                euclidean_d = euclidean_distance(X[j],centroids[i])
                distance[i].append(euclidean_d)
        
        # create new cluster
        cluster = []
        for i in range(len(centroids)):
            cluster.append([])    
        
        # collect data to new cluster 
        for j in range(len(X)):
            index_cluster = 1000000
            min_d = 1000000
            point = None
            for i in range(len(centroids)):
                if distance[i][j] < min_d:
                    index_cluster = i
                    min_d = distance[i][j]
                    point = list(X[j])

            cluster[index_cluster].append(point)

        centroids = []
        for i in range(len(cluster)):
            if len(cluster) == 0:
                continue

            cluster[i] = np.array(cluster[i])
            centroids.append((cluster[i][:, 0].mean(), cluster[i][:, 1].mean()))
            
        # plot the result of each iterations
        for i in range(len(cluster)):
            plt.scatter(cluster[i][:, 0], cluster[i][:, 1], s=50, color=colour[i])

        for c in centroids:
            plt.scatter(c[0], c[1], s=50, color=color_centroid, marker='v')

        # compare new centroid with previous centroid
        if centroids == previous_centroid:
            time.sleep(3)
            break

        plt.pause(0.5)
        plt.clf()

