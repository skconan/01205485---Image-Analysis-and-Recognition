import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
import random
import numpy as np
import time
def random_centroid(x, y):
    ix = random.randint(0,len(x)-1)
    iy = random.randint(0,len(y)-1)
    return x[ix], y[iy]


def euclidean_distance(p,q):
    # print(p,q)
    result = 0
    for a, b in zip(p, q):
        result += (a-b)**2
    return result ** 0.5

n_cluster = 2

X, y_true = make_blobs(n_samples=200, centers=n_cluster,
                       cluster_std=2, random_state=20)

plt.scatter(X[:, 0], X[:, 1], s=50, color='blue')

centroids = []
centroids.append(random_centroid(X[:, 0], X[:, 1]))
centroids.append(random_centroid(X[:, 0], X[:, 1]))

for c in centroids:
    plt.scatter(c[0], c[1], s=50, color="red", marker='v')

plt.show()

colour = ["green", "blue", "pink", "red"]
centroids_before = centroids.copy()
plt.ion()

while True:
    distance = []
    # find distance for each centroid
    for i in range(len(centroids)):
        distance.append([])
        for j in range(len(X)):
            euclidean_d = euclidean_distance(X[j],centroids[i])
            distance[i].append(euclidean_d)
    
    cluster = []
    for i in range(len(centroids)):
        cluster.append([])    
    
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
        

    for i in range(len(cluster)):
        plt.scatter(cluster[i][:, 0], cluster[i][:, 1], s=50, color=colour[i])

    for c in centroids:
        plt.scatter(c[0], c[1], s=50, color=colour[i+2], marker='v')
 
    if centroids == centroids_before:
        time.sleep(3)
        break
    centroids_before = centroids.copy()
    plt.pause(1)
    plt.clf()

