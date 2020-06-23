import sys
import math
import numpy as np

# helper methods:
def cal_dist(d1, d2):
    return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2 + (d1[2] - d2[2]) ** 2)


# read in the input and initialize a distance matrix
earth = [0.0, 0.0, 0.0]
line = sys.stdin.readline()
zearth = list(line.strip().split(" "))
zearth = list(map(float, zearth))

line = sys.stdin.readline()
# iteration is the number of teleportation stations, including earth and zearth
loop = int(line.strip())
iteration = loop + 2

# N*N matrix used to store the distances between any two points, earth w/ index 0 , zearth w/index iteration-1
distant_matrix = np.zeros((iteration, iteration))

# A list that keeps track of all the coordinates
stations = [earth]

while loop > 0:
    loop -= 1
    line = sys.stdin.readline()
    # if line == '':
    #     break
    new_station = list(line.strip().split(" "))
    new_station = list(map(float, new_station))
    stations.append(new_station)
    for i in range(len(stations)):
        distantTo = cal_dist(stations[i], new_station)
        distant_matrix[i][len(stations) - 1] = distantTo
        distant_matrix[len(stations) - 1][i] = distantTo

# Add zearth to complete the distant_matrix
stations.append(zearth)
for i in range(len(stations)):
    distantTo = cal_dist(stations[i], zearth)
    distant_matrix[i][len(stations) - 1] = distantTo
    # distant_matrix[len(stations) - 1][i] = distantTo

# Implentation inspired by Floyd-Warshall's algorithm.
# For each iteration of k, we add a new station for consideration; basically, we go through column by column of the distant_matrix
# After each iteration, each whether we have found a better path with min max edge weight

for k in range(iteration):
    for j in range(iteration):
        for i in range(j):
            distant_matrix[i][j] = min(distant_matrix[i][j], max(distant_matrix[i][k], distant_matrix[k][j]))
            distant_matrix[j][i] = min(distant_matrix[i][j], max(distant_matrix[i][k], distant_matrix[k][j]))

output = round((distant_matrix[0][iteration - 1]), 2)
print ("{0:.2f}".format(output)) 